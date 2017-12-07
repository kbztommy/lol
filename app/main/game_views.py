from flask import render_template, request, current_app, redirect, url_for
from flask_security import login_required
from . import main
from ..models import GameMatch
from .riot_api.game_api import get_matches_by_account_id
from ..extensions import db


@main.route('/get_all_game_match/<account_id>', methods=['GET', 'POST'])
@login_required
def get_all_game_match(account_id):
    game_match_list = GameMatch.query.filter_by(account_id=account_id).order_by(GameMatch.game_id.desc()).all()
    return render_template('current_game_match_list.html', game_match_list=game_match_list)
