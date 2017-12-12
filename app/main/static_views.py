from flask import render_template, redirect, url_for
from flask_security import login_required
from . import main
from ..service.static_service import update_item_data, update_champion_data, update_summoner_spell_data


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
