from app.riot_api.league_api import get_challenger_leagues
from app.models import League, LeagueItem
from app.extensions import db


def update_challenger_league():
    league_dto = get_challenger_leagues()
    league_do = League(**league_dto)
    league_item_list = league_dto.get('entries')

    try:
        db.session.merge(league_do)
        db.session.query(LeagueItem).filter(
            LeagueItem.league_id == league_do.league_id).delete()
        for league_item_dto in league_item_list:
            league_item = LeagueItem(league_dto, league_item_dto)
            db.session.merge(league_item)
        db.session.commit()
    except:
        db.session.rollback()
        raise


def query_all_challenger():
    league_item_list = LeagueItem.query.order_by(
        LeagueItem.league_points.desc()).all()
    return league_item_list
