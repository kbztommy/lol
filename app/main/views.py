from flask import render_template, request, current_app
from flask_security import login_required
from . import main
from ..import db
from ..models import Summoner


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
