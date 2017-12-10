from ..riot_api.static_api import get_all_item_code, get_all_champion_code
from ..models import ItemCode,ChampionCode
from ..extensions import db


def update_item_code():
    item_data = get_all_item_code()
    item_map = item_data.get('data')

    try:
        for _, item in item_map.items():
            db.session.merge(ItemCode(**item))
        db.session.commit()
    except:
        db.session.rollback()
        raise


def update_champion_code():
    champions_data = get_all_champion_code()
    champion_map = champions_data.get('data')

    try:
        for _, champion in champion_map.items():
            db.session.merge(ChampionCode(**champion))
        db.session.commit()
    except:
        db.session.rollback()
        raise
