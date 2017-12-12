from flask import current_app as app
import requests


def get_all_item_data():
    url = '{}/lol/static-data/v3/items'.format(
        app.config['RIOT_URL'])
    r = requests.get(
        url, params={'api_key': app.config['RIOT_API_KEY'], 'locale':  app.config['APP_LOCALE'], 'tags': 'all'})
    return r.json()


def get_champion_data():
    url = '{}/lol/static-data/v3/champions'.format(
        app.config['RIOT_URL'])
    r = requests.get(
        url, params={'api_key': app.config['RIOT_API_KEY'], 'locale': app.config['APP_LOCALE'], 'dataById': 'false', 'tags': 'all'})
    return r.json()


def get_summoner_spell_data_data():
    url = url = '{}/lol/static-data/v3/summoner-spells'.format(
        app.config['RIOT_URL'])
    r = requests.get(
        url, params={'api_key': app.config['RIOT_API_KEY'], 'locale': app.config['APP_LOCALE'], 'dataById': 'false', 'tags': 'all'})
    return r.json()