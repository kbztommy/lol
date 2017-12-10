from flask import current_app as app
import requests


def get_all_item_code():
    url = '{}/lol/static-data/v3/items'.format(
        app.config['RIOT_URL'])
    r = requests.get(
        url, params={'api_key': app.config['RIOT_API_KEY'], 'locale':  app.config['APP_LOCALE']})
    return r.json()


def get_all_champion_code():
    url = '{}/lol/static-data/v3/champions'.format(
        app.config['RIOT_URL'])
    r = requests.get(
        url, params={'api_key': app.config['RIOT_API_KEY'], 'locale': app.config['APP_LOCALE'], 'dataById': 'true'})
    return r.json()
