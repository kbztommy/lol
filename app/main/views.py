from flask import render_template, request, current_app, redirect, url_for
from flask_security import login_required
from . import main
from ..models import Summoner
from .riot_api.summoner_api import get_summoner_by_account_id, get_summoner_by_summoner_name
from ..extensions import db


@main.route('/', methods=['GET', 'POST'])
@login_required
def index():
    summoner_list = Summoner.query.all()
    return render_template('index.html', summoner_list=summoner_list)


@main.route('/get_summoner', methods=["GET", "POST"])
@login_required
def get_summoner():
    current_app.logger.debug(request.form.get('name', 'form is empty'))
    current_app.logger.debug(request.args.get('name', 'args is empty'))
    current_app.logger.debug(request.values.get('name', 'values is empty'))
    summoner = Summoner.query.filter_by(name=request.values['name']).first()
    return "{} , {}".format(summoner.id, summoner.name)


@main.route('/get_summoner_detail/<name>', methods=["GET", "POST"])
@login_required
def get_summoner_detail(name):
    summoner = Summoner.query.filter_by(name=name).first()
    return render_template('get_summoner_detail.html', summoner=summoner)


@main.route('/put_summoner_detail/<account_id>', methods=["GET"])
@login_required
def put_summoner_detail(account_id):
    summoner_dto = get_summoner_by_account_id(account_id)
    summoner = Summoner(**summoner_dto)
    db.session.merge(summoner)
    db.session.commit()
    return render_template('get_summoner_detail.html', summoner=summoner)


@main.route('/post_summoner', methods=["POST"])
@login_required
def post_summoner():
    summoner_name = request.values['summonerName']
    summoner_dto = get_summoner_by_summoner_name(summoner_name)
    summoner = Summoner(**summoner_dto)
    db.session.add(summoner)
    db.session.commit()
    return redirect(url_for('main.index'))
