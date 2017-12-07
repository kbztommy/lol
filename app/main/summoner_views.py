from flask import render_template, request,  redirect, url_for
from flask_security import login_required
from . import main
from ..service.summoner_service import get_all_summoners, get_one_summoner_by_name
from ..service.summoner_service import update_summoner_by_account_id, add_summoner_by_name


@main.route('/', methods=['GET', 'POST'])
@login_required
def index():
    summoner_list = get_all_summoners()
    return render_template('index.html', summoner_list=summoner_list)


@main.route('/get_summoner_detail/<name>', methods=["GET", "POST"])
@login_required
def get_summoner_detail(name):
    summoner = get_one_summoner_by_name(name)
    return render_template('summoner_detail.html', summoner=summoner)


@main.route('/put_summoner_detail/<account_id>', methods=["GET"])
@login_required
def put_summoner_detail(account_id):
    summoner = update_summoner_by_account_id(account_id)
    return render_template('summoner_detail.html', summoner=summoner)


@main.route('/post_summoner', methods=["POST"])
@login_required
def post_summoner():
    summoner_name = request.values['summonerName']
    add_summoner_by_name(summoner_name)
    return redirect(url_for('main.index'))
