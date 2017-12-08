from flask import render_template, redirect, url_for
from flask_security import login_required
from . import main
from ..service.league_service import update_challenger_league, query_all_challenger


@main.route('/get_all_challenger', methods=['GET'])
@login_required
def get_all_challenger():
    challenger_list = query_all_challenger()
    return render_template('challenger_league.html', challenger_list=challenger_list)


@main.route('/post_challenger_league', methods=['POST'])
@login_required
def post_challenger_league():
    update_challenger_league()
    return '/get_all_challenger'
