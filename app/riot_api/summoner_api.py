from flask import current_app as app
import requests


def get_summoner_by_account_id(account_id):
    url = '{}/lol/summoner/v3/summoners/by-account/{}'.format(
        app.config['RIOT_URL'], account_id)
    r = requests.get(url, params={'api_key':  app.config['RIOT_API_KEY']})
    return r.json()


def get_summoner_by_summoner_name(summoner_name):
    url = '{}/lol/summoner/v3/summoners/by-name/{}'.format(
        app.config['RIOT_URL'], summoner_name)
    r = requests.get(url, params={'api_key': app.config['RIOT_API_KEY']})
    return r.json()
