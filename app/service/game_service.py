import time
import datetime
from io import BytesIO
from flask import current_app
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
import matplotlib.pyplot as plt
from ..models import GameMatch, Game, GameParticipant, ParticipantItem, ParticipantPerk, ParticipantStatistics, GameTeam, LmsPlayer
from ..riot_api.game_api import get_matches_by_account_id, get_game
from ..extensions import db, scheduler
from ..filters import get_champion_id_map


def query_game_match_list(account_id):
    game_match_list = GameMatch.query.filter_by(
        account_id=account_id).order_by(GameMatch.match_timestamp.desc()).all()
    return game_match_list


def update_recent_game_detail():
    app = scheduler.app
    app.logger.debug('prepare update game detail')
    with app.app_context():
        game_id_list = __get_need_update_game_id_list()
        for game_id in game_id_list:
            app.logger.debug('%d had been update' % game_id)
            __add_game(game_id)
        update_count = query_not_yet_added_game_count()
        app.logger.debug('%d game(s) need to update' % update_count)
    app.logger.debug('end update game detail')


def add_recent_game_match(account_id):
    match_list_json = get_matches_by_account_id(account_id)
    matches = match_list_json.get('matches')
    try:
        if matches:
            for geme_match in matches:
                game_match_do = GameMatch(account_id, **geme_match)
                db.session.merge(game_match_do)
            db.session.commit()
    except:
        db.session.rollback()
        raise


def update_recent_game_match():
    app = scheduler.app
    app.logger.debug('prepare update lms player')
    with app.app_context():
        lms_player_list = LmsPlayer.query.all()
        for lms_player in lms_player_list:
            add_recent_game_match(lms_player.accountId)
    app.logger.debug('end update lms player')


def query_not_yet_added_game_count():
    not_yet_added_game_count = db.session.execute(
        'SELECT DISTINCT count(gm.game_id) FROM game_match gm WHERE NOT EXISTS (SELECT g.game_id FROM game g WHERE g.game_id = gm.game_id)')
    return not_yet_added_game_count.fetchone()[0]


def __get_need_update_game_id_list():
    game_id_list = []
    result = db.session.execute(
        'SELECT DISTINCT gm.game_id FROM game_match gm WHERE NOT EXISTS (SELECT g.game_id FROM game g WHERE g.game_id = gm.game_id) ORDER BY gm.game_id DESC LIMIT 10')
    for row in result:
        game_id_list.append(row['game_id'])
    return game_id_list


def __add_game(game_id):
    game_json = get_game(game_id)
    participant_identity_map = __get_participant_identity_map(
        game_json.get('participantIdentities'))
    participant_map = __get_participant_map(game_json.get('participants'))
    participant_do_list = __get_participant_list(
        game_id, participant_identity_map, participant_map)
    team_list = game_json.get('teams')
    game_do = Game(**game_json)

    try:
        db.session.merge(game_do)

        for team in team_list:
            bans = __get_bans(team)
            team_do = GameTeam(game_id, team, bans)
            db.session.merge(team_do)

        for participant_do in participant_do_list:
            db.session.merge(participant_do)
        db.session.commit()
    except:
        db.session.rollback()
        raise


def query_all_game_participant(game_id):
    game_participant_list = GameParticipant.query.filter_by(
        game_id=game_id).order_by(GameParticipant.participant_id).all()
    return game_participant_list


def query_statistics_champion_use(account_id, lane=''):
    now = int(time.time() * 1000)
    seven_day_ago = int(time.mktime(
        (datetime.datetime.now() - datetime.timedelta(days=7)).timetuple()) * 1000)
    champion_count_map = __query_recent_champion_count_map(
        account_id, seven_day_ago, now, lane)
    champions_code_map = get_champion_id_map()
    champions = list()
    for champion_id in champion_count_map:
        champions.append(champions_code_map[str(champion_id)])

    counts = champion_count_map.values()
    fig1, ax1 = plt.subplots()
    current_app.logger.debug(counts)
    current_app.logger.debug(champions)
    ax1.pie(counts, labels=champions, autopct='%1.1f%%')
    ax1.axis('equal')
    canvas = FigureCanvas(fig1)
    png_output = BytesIO()
    canvas.print_png(png_output)
    return png_output


def __get_bans(team):
    ban_list = team.get('bans')
    bans = list()
    if bans is None:
        return ''
    else:
        for ban in ban_list:
            bans.append(str(ban.get('championId')))
    return bans


def __query_recent_champion_count_map(account_id, start_time, end_time, lane=''):
    champion_count_map = dict()
    game_participant_do_list = list()

    if not lane:
        game_participant_do_list = db.session.query(GameParticipant).join(Game).filter(Game.game_creation >= start_time).filter(
            Game.game_creation <= end_time).filter(GameParticipant.account_id == account_id)
    else:
        game_participant_do_list = db.session.query(GameParticipant).join(Game).filter(Game.game_creation >= start_time).filter(
            Game.game_creation <= end_time).filter(GameParticipant.account_id == account_id).filter(GameParticipant.lane == lane)
    for game_participant_do in game_participant_do_list:
        champion_count_map[game_participant_do.champion_id] = champion_count_map.get(
            game_participant_do.champion_id, 0) + 1

    return champion_count_map


def __get_participant_list(game_id, participant_identity_map, participant_map):
    game_participant_do_list = []
    for participant_id, participant_identity in participant_identity_map.items():
        account_id = participant_identity.get('player').get('accountId')
        stats = participant_map.get(participant_id).get('stats')
        participant_item = ParticipantItem(game_id, account_id, stats)
        participant_perk = ParticipantPerk(game_id, account_id, stats)
        participant_perk_statistics = ParticipantStatistics(
            game_id, account_id, stats)
        game_participant_do = GameParticipant(game_id,
                                              participant_identity, participant_map.get(participant_id), participant_item, participant_perk, participant_perk_statistics)
        game_participant_do_list.append(game_participant_do)
    return game_participant_do_list


def __get_participant_identity_map(participantIdentities):
    participant_map = {}
    for participant_identity in participantIdentities:
        participant_map[participant_identity.get(
            'participantId')] = participant_identity
    return participant_map


def __get_participant_map(participants):
    participant_map = {}
    for participant in participants:
        participant_map[participant.get('participantId')] = participant
    return participant_map
