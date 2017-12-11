from datetime import datetime
import json
from flask import current_app as app
from .models import ItemCode, StaticData


__champion_id_map = dict()
__item_id_map = dict()


def time_format_filter(t):
    if t is not None:
        return datetime.fromtimestamp(int(t / 1000))
    else:
        return 'no record found'


def champion_id_filter(champion_id):
    id_name_map = get_champion_id_map()
    return id_name_map.get(str(champion_id), champion_id)


def item_id_filter(item_id):
    id_name_map = get_item_id_map()
    return id_name_map.get(str(item_id), (item_id, ''))[0]


def item_img_filter(item_id):
    id_name_map = get_item_id_map()
    return id_name_map.get(str(item_id), (item_id, ''))[1]


def __init_champion_id_map():
    app.logger.debug("init champion_id_map")
    static_data = StaticData.query.filter_by(
        type='champion', version=app.config['GAME_VERSION']).first()
    __champion_id_map.update(json.loads(static_data.data).get('keys'))


def __init_item_id_map():
    app.logger.debug("init item_id_map")
    static_data = StaticData.query.filter_by(
        type='item', version=app.config['GAME_VERSION']).first()
    data = json.loads(static_data.data).get('data')
    for item_code in data:
        img = 'http://ddragon.leagueoflegends.com/cdn/6.24.1/img/item/' + \
            data[item_code]['image']['full']
        app.logger.debug(img)
        __item_id_map[item_code] = (data[item_code]['name'], img)
    app.logger.debug(__item_id_map)


def get_champion_id_map():
    count = len(__champion_id_map)
    if count == 0:
        __init_champion_id_map()
    return __champion_id_map.copy()


def get_item_id_map():
    count = len(__item_id_map)
    if count == 0:
        __init_item_id_map()
    return __item_id_map.copy()
