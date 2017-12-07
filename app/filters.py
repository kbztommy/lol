from jinja2 import Markup
from datetime import datetime
from .models import ChampionCode
from flask import current_app as app

champion_id_map = dict()


def time_format_filter(t):
    if t is not None:
        return datetime.fromtimestamp(int(t / 1000))
    else:
        return 'no record found'


def champion_id_filter(champion_id):
    count = len(champion_id_map)
    if count == 0:
        app.logger.debug("init champion_id_map")
        champion_code_do_list = ChampionCode.query.all()
        for champion_code in champion_code_do_list:
            champion_id_map[champion_code.champion_id] = champion_code.key
    return champion_id_map[champion_id]
