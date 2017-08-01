#!/usr/bin/env python
# encoding: utf-8

"""
@author: zhanghe
@software: PyCharm
@file: bit_coin.py
@time: 2017/4/25 下午1:25
"""


from datetime import datetime
from flask import redirect
from flask import render_template, request, flash, g
from flask import url_for
from flask_login import current_user, login_required

from app_frontend import app
from app_frontend.models import User
from app_frontend.api.bit_coin import get_bit_coin_rows
from app_frontend.api.bit_coin_item import get_bit_coin_item_rows

PER_PAGE_FRONTEND = app.config['PER_PAGE_FRONTEND']

from flask import Blueprint


bp_bit_coin = Blueprint('bit_coin', __name__, url_prefix='/bit_coin')


@bp_bit_coin.route('/list/')
@bp_bit_coin.route('/list/<int:page>/')
@login_required
def lists(page=1):
    """
    数字货币列表
    """
    pagination = get_bit_coin_item_rows(page, PER_PAGE_FRONTEND, **{'user_id': current_user.id})
    return render_template('bit_coin/list.html', title='bit_coin_list', pagination=pagination)


@bp_bit_coin.route('/add/', methods=['GET', 'POST'])
@login_required
def add():
    """
    创建数字货币
    :return:
    """
    pass


@bp_bit_coin.route('/del/', methods=['GET', 'POST'])
@login_required
def delete():
    """
    删除数字货币
    :return:
    """
    pass


@bp_bit_coin.route('/stats/', methods=['GET', 'POST'])
@login_required
def stats():
    """
    数字货币统计
    :return:
    """
    pass
