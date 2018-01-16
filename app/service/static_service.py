import os
from json import dumps
from flask import current_app as app
from app.riot_api.static_api import get_all_item_data, get_champion_data
from app.riot_api.static_api import get_summoner_spell_data_data, get_version_list_data
from app.models import StaticData, LOLVERSION
from app.extensions import db


def update_item_data():
    item_data = get_all_item_data()
    write_static_data_file(item_data)
    insert_static_data(item_data)


def update_champion_data():
    champions_data = get_champion_data()
    write_static_data_file(champions_data)
    insert_static_data(champions_data)


def update_summoner_spell_data():
    champions_data = get_summoner_spell_data_data()
    write_static_data_file(champions_data)
    insert_static_data(champions_data)


def write_static_data_file(data):
    version = data.get('version')
    query_type = data.get('type')
    version_path = os.path.join(
        app.config['APP_STATIC_PATH'], version)
    file_path = os.path.join(version_path, query_type + '.txt')

    if not os.path.exists(version_path):
        os.makedirs(version_path)

    if not os.path.exists(file_path):
        with open(file_path, 'w') as file:
            file.write(dumps(data))


def insert_static_data(data):
    try:
        static_data = StaticData()
        static_data.version = data.get('version')
        static_data.type = data.get('type')
        static_data.locale = app.config['APP_LOCALE']
        static_data.data = dumps(data).encode()
        db.session.merge(static_data)
        db.session.commit()
    except:
        db.session.rollback()
        raise


def insert_version_list():
    try:
        version_list = get_version_list_data()
        for version_str in version_list:
            version = LOLVERSION(version_str)
            db.session.merge(version)
            db.session.commit()
    except:
        db.session.rollback()
        raise


def query_recent_version_list():
    version_list = LOLVERSION.query.order_by(LOLVERSION.version1.desc()).order_by(
        LOLVERSION.version2.desc()).order_by(LOLVERSION.version3.desc()).limit(10).all()
    return version_list
