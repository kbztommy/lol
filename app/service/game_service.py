from ..models import GameMatch, Game, GameParticipant
from ..riot_api.game_api import get_matches_by_account_id, get_game, get_matches_by_account_id
from flask import current_app
from ..extensions import db


def get_game_match_list(account_id):
    game_match_list = GameMatch.query.filter_by(
        account_id=account_id).order_by(GameMatch.game_id.desc()).all()
    return game_match_list


def update_recent_game_detail():
    game_id_list = __get_need_update_game_id_list()
    for game_id in game_id_list:
        current_app.logger.debug("%d had been update" % game_id)
        __add_game(game_id)


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


def __get_need_update_game_id_list():
    game_id_list = []
    result = db.session.execute(
        'SELECT DISTINCT gm.game_id FROM game_match gm WHERE NOT EXISTS (SELECT g.game_id FROM game g WHERE g.game_id = gm.game_id) ORDER BY gm.game_id LIMIT 10')
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
    game_do = Game(**game_json)

    try:
        db.session.merge(game_do)
        for participant_do in participant_do_list:
            db.session.merge(participant_do)
        db.session.commit()
    except:
        db.session.rollback()
        raise


def __get_participant_list(game_id, participant_identity_map, participant_map):
    game_participant_do_list = []
    for participant_id, participant_identity in participant_identity_map.items():
        game_participant_do = GameParticipant(game_id,
                                              participant_identity, participant_map.get(participant_id))
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
