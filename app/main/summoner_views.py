import json
import decimal
from collections import OrderedDict
from flask import render_template, request,  redirect, url_for, make_response, current_app
from flask_security import login_required
from . import main
from ..filters import champion_img_filter
from ..service.summoner_service import query_all_summoners, query_one_summoner_by_name
from ..service.summoner_service import update_summoner_by_account_id, add_summoner_by_name
from ..service.game_service import query_statistics_champion_use, get_win_rate
from ..service.static_service import query_recent_version_list


@main.route('/', methods=['GET', 'POST'])
@login_required
def index():
    summoner_list = query_all_summoners()
    return render_template('index.html', summoner_list=summoner_list)


@main.route('/background', methods=['GET'])
@login_required
def background():
    return render_template('background.html')


@main.route('/get_summoner_detail/<name>', methods=["GET", "POST"])
@login_required
def get_summoner_detail(name):
    summoner = query_one_summoner_by_name(name)
    full_version_list = query_recent_version_list()
    version_list = list(OrderedDict.fromkeys(full_version_list))
    version_set = set(item.get_version() for item in full_version_list)
    win_rate_list = get_win_rate(
        summoner.account_id, '')
    return render_template('summoner_detail.html', summoner=summoner, version_list=version_list, win_rate_list=win_rate_list)


@main.route('/put_summoner_detail/<account_id>', methods=["GET"])
@login_required
def put_summoner_detail(account_id):
    summoner = update_summoner_by_account_id(account_id)
    return redirect(url_for('main.get_summoner_detail', name=summoner.name))


@main.route('/get_statistics_champion_use/<account_id>', methods=["GET"])
@login_required
def get_statistics_champion_use(account_id):
    lane = request.values['lane']
    png_output = query_statistics_champion_use(account_id, lane)
    response = make_response(png_output.getvalue())
    response.headers['Content-Type'] = 'image/png'
    return response


@main.route('/post_summoner', methods=["POST"])
@login_required
def post_summoner():
    summoner_name = request.values['summonerName']
    add_summoner_by_name(summoner_name)
    return redirect(url_for('main.index'))


class DecimalEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, decimal.Decimal):
            return '{:f}'.format(float(o))
        return super(DecimalEncoder, self).default(o)


@main.route('/post_filter_win_rate', methods=["POST"])
@login_required
def post_filter_win_rate():
    start_date = request.values['startDate']
    end_date = request.values['endDate']
    account_id = int(request.values['accountId'])
    champion_id = int(request.values['championId'])
    version = request.values['version']
    win_rate_list = get_win_rate(
        account_id, version, start_date, end_date, champion_id)
    for win_rate in win_rate_list:
        win_rate['championId'] = champion_img_filter(int(win_rate['championId']))
    return json.dumps(win_rate_list, cls=DecimalEncoder)
    
        
