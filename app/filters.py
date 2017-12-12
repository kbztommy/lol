from datetime import datetime
import json
from flask import current_app as app
from .models import ItemCode, StaticData


__champion_id_map = dict()
__item_id_map = dict()
__summoner_spell_id_map = dict()


def time_format_filter(t):
    if t is not None:
        return datetime.fromtimestamp(int(t / 1000))
    else:
        return 'no record found'


def champion_id_filter(champion_id):
    id_name_map = get_champion_id_map(False)
    return id_name_map.get(str(champion_id), champion_id)


def champion_img_filter(champion_id):
    id_name_map = get_champion_id_map(False)
    champion_name = id_name_map[str(champion_id)]
    img_url = 'http://ddragon.leagueoflegends.com/cdn/%s/img/champion/%s.png' % (
        app.config['GAME_VERSION'], champion_name)
    return img_url


def item_id_filter(item_id):
    id_name_map = get_item_id_map(False)
    return id_name_map.get(str(item_id), (item_id, ''))[0]


def item_img_filter(item_id):
    id_name_map = get_item_id_map(False)
    return id_name_map.get(str(item_id), (item_id, ''))[1]


def summoner_spell_id_filter(summoner_spell_id):
    id_name_map = get_summoner_spell_id_map(False)
    return id_name_map.get(summoner_spell_id, (summoner_spell_id, ''))[0]


def summoner_spell_img_filter(summoner_spell_id):
    id_name_map = get_summoner_spell_id_map(False)
    return id_name_map.get(summoner_spell_id, (summoner_spell_id, ''))[1]


def get_champion_id_map(copy=True):
    count = len(__champion_id_map)
    if count == 0:
        __init_champion_id_map()
    if copy:
        return __champion_id_map.copy()
    else:
        return __champion_id_map


def get_summoner_spell_id_map(copy=True):
    count = len(__summoner_spell_id_map)
    if count == 0:
        __init_summoner_spell_id_map()
    if copy:
        return __summoner_spell_id_map.copy()
    else:
        return __summoner_spell_id_map


def get_item_id_map(copy=True):
    count = len(__item_id_map)
    if count == 0:
        __init_item_id_map()
    if copy:
        return __item_id_map.copy()
    else:
        return __item_id_map


def __init_champion_id_map():
    app.logger.debug("init champion_id_map")
    static_data = StaticData.query.filter_by(
        type='champion', version=app.config['GAME_VERSION']).first()
    __champion_id_map.update(json.loads(static_data.data).get('keys'))


def __init_item_id_map():
    app.logger.debug("init item_id_map")
    query_type = 'item'
    version = app.config['GAME_VERSION']
    static_data = StaticData.query.filter_by(
        type=query_type, version=version).first()
    data = json.loads(static_data.data).get('data')
    for item_code in data:
        img = 'http://ddragon.leagueoflegends.com/cdn/%s/img/%s/' % (version, query_type) + \
            data[item_code]['image']['full']
        __item_id_map[item_code] = (data[item_code]['name'], img)


def __init_summoner_spell_id_map():
    app.logger.debug("init summoner_spell_id_map")
    query_type = 'summoner'
    version = app.config['GAME_VERSION']
    static_data = StaticData.query.filter_by(
        type=query_type, version=version).first()
    data = json.loads(static_data.data).get('data')
    for summoner_spell_code in data:
        img = 'http://ddragon.leagueoflegends.com/cdn/%s/img/spell/' % (version) + \
            data[summoner_spell_code]['image']['full']
        __summoner_spell_id_map[data[summoner_spell_code]['id']] = (
            data[summoner_spell_code]['name'], img)
