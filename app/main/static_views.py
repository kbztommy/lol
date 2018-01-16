import json
from flask import redirect, url_for
from flask_security import login_required
from app.main import main
from app.service.static_service import update_item_data, update_champion_data
from app.service.static_service import update_summoner_spell_data, insert_version_list
from app.filters import get_champion_id_map, champion_img_filter


@main.route('/put_item_code', methods=['GET'])
@login_required
def put_item_code():
    update_item_data()
    return redirect(url_for('main.index'))


@main.route('/put_champion_code', methods=['GET'])
@login_required
def put_champion_code():
    update_champion_data()
    return redirect(url_for('main.index'))


@main.route('/put_summoner_spell_code', methods=['GET'])
@login_required
def put_summoner_spell_code():
    update_summoner_spell_data()
    return redirect(url_for('main.index'))


@main.route('/put_version_list', methods=['GET'])
@login_required
def put_version_list():
    insert_version_list()
    return redirect(url_for('main.index'))


@main.route('/get_all_champion_img', methods=['GET', 'POST'])
@login_required
def get_all_champion_img():
    champion_img_dict = dict()
    champion_dict = get_champion_id_map()
    for champion_id in champion_dict.keys():
        champion_img_dict[champion_id] = champion_img_filter(champion_id)
    return json.dumps(champion_img_dict)
