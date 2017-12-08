import json
import requests
from flask import current_app as app


def get_challenger_leagues():
    url = '{}/lol/league/v3/challengerleagues/by-queue/{}'.format(
        app.config['RIOT_URL'], 'RANKED_SOLO_5x5')
    r = requests.get(url, params={'api_key': app.config['RIOT_API_KEY']})
    return r.json()
