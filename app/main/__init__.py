from flask import Blueprint

main = Blueprint('main', __name__)

from . import summoner_views, errors, game_views, league_views, static_views
