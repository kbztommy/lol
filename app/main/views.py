from flask import render_template
from flask_security import login_required
from . import main
from ..import db
from ..models import Summoner


@main.route('/', methods=['GET', 'POST'])
@login_required
def index():
    summoner_list = Summoner.query.all()
    return render_template('index.html', summoner_list=summoner_list)
