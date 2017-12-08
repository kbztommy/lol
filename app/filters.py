from datetime import datetime

from flask import current_app as app
from jinja2 import Markup
from .models import ChampionCode


__champion_id_map = dict()


def time_format_filter(t):
    if t is not None:
        return datetime.fromtimestamp(int(t / 1000))
    else:
        return 'no record found'


def champion_id_filter(champion_id):
    id_name_map = get_champion_id_map()
    return id_name_map[champion_id]


def __init_champion_id_map():
    app.logger.debug("init champion_id_map")
    champion_code_do_list = ChampionCode.query.all()
    for champion_code in champion_code_do_list:
        __champion_id_map[champion_code.champion_id] = champion_code.key


def get_champion_id_map():
    count = len(__champion_id_map)
    if count == 0:
        __init_champion_id_map()
    return __champion_id_map.copy()
