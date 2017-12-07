from .extensions import db
from flask_security import UserMixin, RoleMixin
import time

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
