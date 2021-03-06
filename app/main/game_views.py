from flask import render_template, redirect, url_for
from flask_security import login_required
from app.main import main
from app.service.game_service import query_game_match_list, update_recent_game_detail
from app.service.game_service import query_all_game_participant, add_recent_game_match


@main.route('/get_all_game_match/<account_id>', methods=['GET', 'POST'])
@login_required
def get_all_game_match(account_id):
    game_match_list = query_game_match_list(account_id)
    return render_template('current_game_match_list.html', game_match_list=game_match_list)


@main.route('/post_recent_game_match/<account_id>', methods=['GET', 'POST'])
@login_required
def post_recent_game_match(account_id):
    add_recent_game_match(account_id)
    return redirect(url_for('main.get_all_game_match', account_id=account_id))


@main.route('/put_recent_game_detail', methods=['GET', 'POST'])
@login_required
def put_recent_game_detail():
    update_recent_game_detail()
    return redirect(url_for('main.index'))


@main.route('/get_game_detail/<game_id>', methods=['GET'])
@login_required
def get_game_detail(game_id):
    game_detail_list = query_all_game_participant(game_id)
    return render_template('game_detail.html', game_detail_list=game_detail_list)
