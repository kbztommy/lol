from .extensions import db
from flask_security import UserMixin, RoleMixin
import time
from sqlalchemy import ForeignKey, PrimaryKeyConstraint, ForeignKeyConstraint
from sqlalchemy.orm import relationship
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
    platform_id = db.Column(db.String(45))
    game_mode = db.Column(db.String(45))
    map_id = db.Column(db.INTEGER)
    game_type = db.Column(db.String(45))
    game_duration = db.Column(db.BigInteger)
    game_creation = db.Column(db.BigInteger)

    def __init__(self, **kwargs):
        self.game_id = kwargs.get('gameId')
        self.game_version = kwargs.get('gameVersion')
        self.platform_id = kwargs.get('platformId')
        self.game_mode = kwargs.get('gameMode')
        self.map_id = kwargs.get('mapId')
        self.game_type = kwargs.get('gameType')
        self.game_duration = kwargs.get('gameDuration')
        self.game_creation = kwargs.get('gameCreation')


class GameParticipant(db.Model):
    __tablename__ = 'game_participant'
    game_id = db.Column(db.BigInteger)
    account_id = db.Column(db.BigInteger)
    summoner_name = db.Column(db.String(100))
    participant_id = db.Column(db.INTEGER)
    team_id = db.Column(db.INTEGER)
    win = db.Column(db.Boolean)
    champion_id = db.Column(db.INTEGER)
    spell1_id = db.Column(db.INTEGER)
    spell2_id = db.Column(db.INTEGER)
    kills = db.Column(db.INTEGER)
    deaths = db.Column(db.INTEGER)
    assists = db.Column(db.INTEGER)
    wardsKilled = db.Column(db.INTEGER)
    wardsPlaced = db.Column(db.INTEGER)
    sightWardsBoughtInGame = db.Column(db.INTEGER)
    visionScore = db.Column(db.INTEGER)
    timeCCingOthers = db.Column(db.BigInteger)
    item0 = db.Column(db.INTEGER)
    item1 = db.Column(db.INTEGER)
    item2 = db.Column(db.INTEGER)
    item3 = db.Column(db.INTEGER)
    item4 = db.Column(db.INTEGER)
    item5 = db.Column(db.INTEGER)
    item6 = db.Column(db.INTEGER)
    game_match = relationship("GameMatch")

    __table_args__ = (
        PrimaryKeyConstraint('game_id', 'account_id'), ForeignKeyConstraint(
            ['game_id', 'account_id'],
            ['game_match.game_id', 'game_match.account_id']
        ),
    )

    def __init__(self, game_id, participant_identity, participant):
        stats = participant.get('stats')
        self.game_id = game_id
        self.account_id = participant_identity.get('player').get('accountId')
        self.summoner_name = participant_identity.get(
            'player').get('summonerName')
        self.participant_id = participant_identity.get('participantId')
        self.team_id = participant.get('teamId')
        self.win = stats.get('win')
        self.champion_id = participant.get('championId')
        self.spell1_id = participant.get('spell1Id')
        self.spell2_id = participant.get('spell2Id')
        self.kills = stats.get('kills')
        self.deaths = stats.get('deaths')
        self.assists = stats.get('assists')
        self.wardsKilled = stats.get('wardsKilled')
        self.wardsPlaced = stats.get('wardsPlaced')
        self.sightWardsBoughtInGame = stats.get('sightWardsBoughtInGame')
        self.visionScore = stats.get('visionScore')
        self.timeCCingOthers = stats.get('timeCCingOthers')
        self.item0 = stats.get('item0')
        self.item1 = stats.get('item1')
        self.item2 = stats.get('item2')
        self.item3 = stats.get('item3')
        self.item4 = stats.get('item4')
        self.item5 = stats.get('item5')
        self.item6 = stats.get('item6')
