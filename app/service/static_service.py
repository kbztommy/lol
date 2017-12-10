from ..riot_api.static_api import get_all_item_code, get_all_champion_code
from ..models import ItemCode, ChampionCode
from ..extensions import db
import os
from flask import current_app as app
from json import dumps


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
    version = champions_data.get('version')  
    static_file_path = os.path.join(
        app.config['APP_STATIC_PATH'], 'champion_%s_file.txt' % version)

    if not os.path.exists(static_file_path):
        with open(static_file_path, 'w') as file:            
            file.write(dumps(champions_data))

    try:
        for _, champion in champion_map.items():
            db.session.merge(ChampionCode(**champion))
            db.session.commit()
    except:
        db.session.rollback()
        raise
