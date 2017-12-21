from flask import current_app as app
import requests


def get_matches_by_account_id(account_id):
    url = '{}/lol/match/v3/matchlists/by-account/{}'.format(
        app.config['RIOT_URL'], account_id)
    r = requests.get(
        url, params={'api_key': app.config['RIOT_API_KEY']})
    return r.json()


def get_game_detail(game_id):
    url = '{}/lol/match/v3/matches/{}'.format(app.config['RIOT_URL'], game_id)
    r = requests.get(url, params={'api_key': app.config['RIOT_API_KEY']})
    return r.json()


def get_game(game_id):
    url = '{}/lol/match/v3/matches/{}'.format(app.config['RIOT_URL'], game_id)
    r = requests.get(url, params={'api_key': app.config['RIOT_API_KEY']})
    return r.json()
