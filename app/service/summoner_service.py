from ..extensions import db
from ..riot_api.summoner_api import get_summoner_by_account_id, get_summoner_by_summoner_name
from ..models import Summoner


def get_all_summoners():
    summoner_list = Summoner.query.all()
    return summoner_list


def get_one_summoner_by_name(summoner_name):
    summoner = Summoner.query.filter_by(name=summoner_name).first_or_404()
    return summoner

def update_summoner_by_account_id(account_id):
    summoner_dto = get_summoner_by_account_id(account_id)
    summoner = Summoner(**summoner_dto)
    db.session.merge(summoner)
    db.session.commit()
    return summoner

def add_summoner_by_name(summoner_name):
    summoner_dto = get_summoner_by_summoner_name(summoner_name)
    summoner = Summoner(**summoner_dto)
    db.session.add(summoner)
    db.session.commit()