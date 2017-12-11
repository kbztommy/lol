import os
from flask import current_app as app
from json import dumps, loads
from ..riot_api.static_api import get_all_item_code, get_champion_data
from ..models import StaticData
from ..extensions import db


def update_item_code():
    item_data = get_all_item_code()

    write_static_data_file(item_data)
    insert_static_data(item_data)


def update_champion_code():
    champions_data = get_champion_data()

    write_static_data_file(champions_data)
    insert_static_data(champions_data)


def write_static_data_file(data):
    version = data.get('version')
    type = data.get('type')
    version_path = os.path.join(
        app.config['APP_STATIC_PATH'], version)
    file_path = os.path.join(version_path, type + '.txt')

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
