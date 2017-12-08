from flask import render_template, redirect, url_for
from flask_security import login_required
from . import main
from ..service.static_service import update_item_code

@main.route('/put_item_code', methods=['GET'])
@login_required
def put_item_code():
    update_item_code()
    return redirect(url_for('main.index'))
