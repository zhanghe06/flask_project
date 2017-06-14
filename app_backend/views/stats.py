#!/usr/bin/env python
# encoding: utf-8

"""
@author: zhanghe
@software: PyCharm
@file: stats.py
@time: 2017/6/10 下午1:29
"""



import json
from datetime import datetime

from flask import Blueprint
from flask import abort
from flask import redirect
from flask import render_template, request, flash
from flask import url_for
from flask_login import current_user, login_required

from app_backend.permissions import permission_stats

bp_stats = Blueprint('stats', __name__, url_prefix='/stats')


@bp_stats.route('/user/', methods=['GET', 'POST'])
@login_required
@permission_stats.require(http_exception=403)
def user():
    """
    用户统计
    按日、周、月统计注册量
    :return:
    """
    time_based = request.args.get('time_based', 'hour')
    if time_based not in ['hour', 'date', 'month']:
        time_based = 'hour'
    return render_template('stats/user.html', title='user_stats', time_based=time_based)


@bp_stats.route('/apply_put/', methods=['GET', 'POST'])
@login_required
@permission_stats.require(http_exception=403)
def apply_put():
    """
    投资统计
    按日、周、月统计注册量
    :return:
    """
    time_based = request.args.get('time_based', 'hour')
    if time_based not in ['hour', 'date', 'month']:
        time_based = 'hour'
    return render_template('stats/apply_put.html', title='apply_put_stats', time_based=time_based)


@bp_stats.route('/apply_get/', methods=['GET', 'POST'])
@login_required
@permission_stats.require(http_exception=403)
def apply_get():
    """
    提现统计
    按日、周、月统计注册量
    :return:
    """
    time_based = request.args.get('time_based', 'hour')
    if time_based not in ['hour', 'date', 'month']:
        time_based = 'hour'
    return render_template('stats/apply_get.html', title='apply_get_stats', time_based=time_based)


@bp_stats.route('/order/', methods=['GET', 'POST'])
@login_required
@permission_stats.require(http_exception=403)
def order():
    """
    订单统计
    按日、周、月统计注册量
    :return:
    """
    time_based = request.args.get('time_based', 'hour')
    if time_based not in ['hour', 'date', 'month']:
        time_based = 'hour'
    return render_template('stats/order.html', title='order_stats', time_based=time_based)
