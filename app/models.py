from .extensions import db
from flask_security import UserMixin, RoleMixin
import time
from sqlalchemy import ForeignKey, PrimaryKeyConstraint, ForeignKeyConstraint
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.mysql import LONGTEXT
# Define models
roles_users = db.Table('roles_users',
                       db.Column('user_id', db.Integer(),
                                 db.ForeignKey('user.id')),
                       db.Column('role_id', db.Integer(), db.ForeignKey('role.id')))


class Role(db.Model, RoleMixin):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(80), unique=True)
    description = db.Column(db.String(255))


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(255), unique=True)
    password = db.Column(db.String(255))
    active = db.Column(db.Boolean())
    confirmed_at = db.Column(db.DateTime())
    roles = db.relationship('Role', secondary=roles_users,
                            backref=db.backref('users', lazy='dynamic'))


class Summoner(db.Model):
    __tablename__ = 'summoner'
    id = db.Column(db.BigInteger, primary_key=True)
    account_id = db.Column(db.BigInteger)
    name = db.Column(db.String(45))
    profile_icon_id = db.Column(db.INTEGER)
    revision_date = db.Column(db.BigInteger)
    summoner_level = db.Column(db.BigInteger)
    update_date = db.Column(db.BigInteger)

    def __init__(self, **kwargs):
        self.id = kwargs['id']
        self.account_id = kwargs['accountId']
        self.name = kwargs['name']
        self.profile_icon_id = kwargs['profileIconId']
        self.revision_date = kwargs['revisionDate']
        self.summoner_level = kwargs['summonerLevel']
        self.update_date = time.time() * 1000.0


class GameMatch(db.Model):
    __tablename__ = 'game_match'
    account_id = db.Column(db.BigInteger, primary_key=True)
    game_id = db.Column(db.BigInteger, primary_key=True)
    champion = db.Column(db.INTEGER)
    lane = db.Column(db.String(50))
    platform_id = db.Column(db.String(10))
    season = db.Column(db.INTEGER)
    queue = db.Column(db.INTEGER)
    role = db.Column(db.String(50))
    match_timestamp = db.Column(db.BigInteger)

    def __init__(self, account_id, **kwargs):
        self.account_id = account_id
        self.game_id = kwargs['gameId']
        self.champion = kwargs['champion']
        self.lane = kwargs['lane']
        self.platform_id = kwargs['platformId']
        self.season = kwargs['season']
        self.queue = kwargs['queue']
        self.role = kwargs['role']
        self.match_timestamp = kwargs['timestamp']


class ChampionCode(db.Model):
    __tablename__ = 'champion_code'
    champion_id = db.Column(db.INTEGER, primary_key=True)
    title = db.Column(db.String(100))
    key = db.Column(db.String(100))
    name = db.Column(db.String(100))

    def __init__(self, **kwargs):
        self.champion_id = kwargs['id']
        self.title = kwargs['title']
        self.key = kwargs['key']
        self.name = kwargs['name']


class Game(db.Model):
    __tablename__ = 'game'
    game_id = db.Column(db.BigInteger, primary_key=True)
    game_version = db.Column(db.String(45))
    season_id = db.Column(db.INTEGER)
    platform_id = db.Column(db.String(45))
    game_mode = db.Column(db.String(45))
    map_id = db.Column(db.INTEGER)
    game_type = db.Column(db.String(45))
    game_duration = db.Column(db.BigInteger)
    game_creation = db.Column(db.BigInteger)

    def __init__(self, **kwargs):
        self.game_id = kwargs.get('gameId')
        self.game_version = kwargs.get('gameVersion')
        self.season_id = kwargs.get('seasonId')
        self.platform_id = kwargs.get('platformId')
        self.game_mode = kwargs.get('gameMode')
        self.map_id = kwargs.get('mapId')
        self.game_type = kwargs.get('gameType')
        self.game_duration = kwargs.get('gameDuration')
        self.game_creation = kwargs.get('gameCreation')


class ParticipantItem(db.Model):
    __tablename__ = 'participant_item'
    __table_args__ = (
        PrimaryKeyConstraint('game_id', 'account_id'), ForeignKeyConstraint(
            ['game_id', 'account_id'],
            ['game_participant.game_id', 'game_participant.account_id']
        ),
    )
    game_id = db.Column(db.BigInteger)
    account_id = db.Column(db.BigInteger)
    item0 = db.Column(db.INTEGER)
    item1 = db.Column(db.INTEGER)
    item2 = db.Column(db.INTEGER)
    item3 = db.Column(db.INTEGER)
    item4 = db.Column(db.INTEGER)
    item5 = db.Column(db.INTEGER)
    item6 = db.Column(db.INTEGER)

    def __init__(self, game_id, accountId, stats):
        self.game_id = game_id
        self.account_id = accountId
        self.item0 = stats.get('item0')
        self.item1 = stats.get('item1')
        self.item2 = stats.get('item2')
        self.item3 = stats.get('item3')
        self.item4 = stats.get('item4')
        self.item5 = stats.get('item5')
        self.item6 = stats.get('item6')


class ParticipantPerk(db.Model):
    __tablename__ = 'participant_perk'
    __table_args__ = (
        PrimaryKeyConstraint('game_id', 'account_id'), ForeignKeyConstraint(
            ['game_id', 'account_id'],
            ['game_participant.game_id', 'game_participant.account_id']
        ),
    )
    game_id = db.Column(db.BigInteger)
    account_id = db.Column(db.BigInteger)
    perkPrimaryStyle = db.Column(db.INTEGER)
    perkSubStyle = db.Column(db.INTEGER)
    perk0 = db.Column(db.INTEGER)
    perk1 = db.Column(db.INTEGER)
    perk2 = db.Column(db.INTEGER)
    perk3 = db.Column(db.INTEGER)
    perk4 = db.Column(db.INTEGER)
    perk5 = db.Column(db.INTEGER)
    perk0Var1 = db.Column(db.INTEGER)
    perk0Var2 = db.Column(db.INTEGER)
    perk0Var3 = db.Column(db.INTEGER)
    perk1Var1 = db.Column(db.INTEGER)
    perk1Var2 = db.Column(db.INTEGER)
    perk1Var3 = db.Column(db.INTEGER)
    perk2Var1 = db.Column(db.INTEGER)
    perk2Var2 = db.Column(db.INTEGER)
    perk2Var3 = db.Column(db.INTEGER)
    perk3Var1 = db.Column(db.INTEGER)
    perk3Var2 = db.Column(db.INTEGER)
    perk3Var3 = db.Column(db.INTEGER)
    perk4Var1 = db.Column(db.INTEGER)
    perk4Var2 = db.Column(db.INTEGER)
    perk4Var3 = db.Column(db.INTEGER)
    perk5Var1 = db.Column(db.INTEGER)
    perk5Var2 = db.Column(db.INTEGER)
    perk5Var3 = db.Column(db.INTEGER)

    def __init__(self, game_id, accountId, stats):
        self.game_id = game_id
        self.account_id = accountId
        self.perkPrimaryStyle = stats.get('perkPrimaryStyle')
        self.perkSubStyle = stats.get('perkSubStyle')
        self.perk0 = stats.get('perk0')
        self.perk1 = stats.get('perk1')
        self.perk2 = stats.get('perk2')
        self.perk3 = stats.get('perk3')
        self.perk4 = stats.get('perk4')
        self.perk5 = stats.get('perk5')
        self.perk0Var1 = stats.get('perk0Var1')
        self.perk0Var2 = stats.get('perk0Var2')
        self.perk0Var3 = stats.get('perk0Var3')
        self.perk1Var1 = stats.get('perk1Var1')
        self.perk1Var2 = stats.get('perk1Var2')
        self.perk1Var3 = stats.get('perk1Var3')
        self.perk2Var1 = stats.get('perk2Var1')
        self.perk2Var2 = stats.get('perk2Var2')
        self.perk2Var3 = stats.get('perk2Var3')
        self.perk3Var1 = stats.get('perk3Var1')
        self.perk3Var2 = stats.get('perk3Var2')
        self.perk3Var3 = stats.get('perk3Var3')
        self.perk4Var1 = stats.get('perk4Var1')
        self.perk4Var2 = stats.get('perk4Var2')
        self.perk4Var3 = stats.get('perk4Var3')
        self.perk5Var1 = stats.get('perk5Var1')
        self.perk5Var2 = stats.get('perk5Var2')
        self.perk5Var3 = stats.get('perk5Var3')


class GameParticipant(db.Model):
    __tablename__ = 'game_participant'
    game_id = db.Column(db.BigInteger)
    account_id = db.Column(db.BigInteger)
    summoner_name = db.Column(db.String(100))
    participant_id = db.Column(db.INTEGER)
    team_id = db.Column(db.INTEGER)
    win = db.Column(db.Boolean)
    champion_id = db.Column(db.INTEGER)
    champ_level = db.Column(db.INTEGER)
    lane = db.Column(db.String)
    role = db.Column(db.String)
    spell1_id = db.Column(db.INTEGER)
    spell2_id = db.Column(db.INTEGER)
    kills = db.Column(db.INTEGER)
    deaths = db.Column(db.INTEGER)
    assists = db.Column(db.INTEGER)
    # wardsKilled = db.Column(db.INTEGER)
    # wardsPlaced = db.Column(db.INTEGER)
    # sightWardsBoughtInGame = db.Column(db.INTEGER)
    # visionScore = db.Column(db.INTEGER)
    # timeCCingOthers = db.Column(db.BigInteger)
    game = relationship("Game", uselist=False)
    item = relationship("ParticipantItem", uselist=False)
    perk = relationship("ParticipantPerk", uselist=False)

    __table_args__ = (
        PrimaryKeyConstraint('game_id', 'account_id'),
        ForeignKeyConstraint(
            ['game_id'], ['game.game_id']
        ),
    )

    def __init__(self, game_id, participant_identity, participant, item, perk):
        stats = participant.get('stats')
        timeline = participant.get('timeline')
        self.game_id = game_id
        self.account_id = participant_identity.get('player').get('accountId')
        self.summoner_name = participant_identity.get(
            'player').get('summonerName')
        self.participant_id = participant_identity.get('participantId')
        self.team_id = participant.get('teamId')
        self.win = stats.get('win')
        self.champion_id = participant.get('championId')
        self.champ_level = stats.get('champLevel')
        self.lane = timeline.get('lane')
        self.role = timeline.get('role')
        self.spell1_id = participant.get('spell1Id')
        self.spell2_id = participant.get('spell2Id')
        self.kills = stats.get('kills')
        self.deaths = stats.get('deaths')
        self.assists = stats.get('assists')
        # self.wardsKilled = stats.get('wardsKilled')
        # self.wardsPlaced = stats.get('wardsPlaced')
        # self.sightWardsBoughtInGame = stats.get('sightWardsBoughtInGame')
        # self.visionScore = stats.get('visionScore')
        # self.timeCCingOthers = stats.get('timeCCingOthers')
        self.item = item
        self.perk = perk


class League(db.Model):
    __tablename__ = 'league'
    league_id = db.Column(db.String(100), primary_key=True)
    tier = db.Column(db.String(50))
    queue = db.Column(db.String(50))
    name = db.Column(db.String(50))

    def __init__(self, **kwargs):
        self.league_id = kwargs.get('leagueId')
        self.tier = kwargs.get('tier')
        self.queue = kwargs.get('queue')
        self.name = kwargs.get('name')


class LeagueItem(db.Model):
    __tablename__ = 'league_item'
    league_id = db.Column(db.String(100), primary_key=True)
    player_or_team_id = db.Column(db.BigInteger, primary_key=True)
    player_or_team_name = db.Column(db.String(100))
    league_points = db.Column(db.INTEGER)
    rank = db.Column(db.String(45))
    wins = db.Column(db.INTEGER)
    losses = db.Column(db.INTEGER)
    hot_streak = db.Column(db.Boolean)
    veteran = db.Column(db.Boolean)
    fresh_blood = db.Column(db.Boolean)
    inactive = db.Column(db.Boolean)

    def __init__(self, league, league_item):
        self.league_id = league.get('leagueId')
        self.player_or_team_id = league_item.get('playerOrTeamId')
        self.player_or_team_name = league_item.get('playerOrTeamName')
        self.league_points = league_item.get('leaguePoints')
        self.rank = league_item.get('rank')
        self.wins = league_item.get('wins')
        self.losses = league_item.get('losses')
        self.hot_streak = league_item.get('hotStreak')
        self.veteran = league_item.get('veteran')
        self.fresh_blood = league_item.get('freshBlood')
        self.inactive = league_item.get('inactive')


class ItemCode(db.Model):
    __tablename__ = 'item_code'
    item_id = db.Column(db.INTEGER, primary_key=True)
    name = db.Column(db.String(100))
    plaintext = db.Column(db.String(200))

    def __init__(self, **kwargs):
        self.item_id = kwargs.get('id')
        self.name = kwargs.get('name')
        self.plaintext = kwargs.get('plaintext')


class StaticData(db.Model):
    __tablename__ = 'static_data'
    version = db.Column(db.String(50), primary_key=True)
    type = db.Column(db.String(50), primary_key=True)
    locale = db.Column(db.String(50))
    data = db.Column(db.CLOB)
