#!/usr/bin/env python
# encoding: utf-8

"""
@author: zhanghe
@software: PyCharm
@file: settings.py
@time: 2017/4/30 下午9:11
"""


from datetime import datetime
from flask import redirect
from flask import render_template, request, flash, g
from flask import url_for
from flask_login import current_user, login_required

from app_backend import app
from app_backend.api.score import get_score_rows

from flask import Blueprint


bp_settings = Blueprint('settings', __name__, url_prefix='/settings')


@bp_settings.route('/user/', methods=['GET', 'POST'])
@login_required
def user():
    """
    会员配置
    :return:
    """
    return render_template('settings/user.html', title='settings_user')


@bp_settings.route('/order/', methods=['GET', 'POST'])
@login_required
def order():
    """
    订单配置
    :return:
    """
    return render_template('settings/order.html', title='settings_order')


@bp_settings.route('/wallet/', methods=['GET', 'POST'])
@login_required
def wallet():
    """
    钱包配置
    :return:
    """
    return render_template('settings/wallet.html', title='settings_wallet')


@bp_settings.route('/score/', methods=['GET', 'POST'])
@login_required
def score():
    """
    积分配置
    :return:
    """
    return render_template('settings/score.html', title='settings_score')


@bp_settings.route('/bonus/', methods=['GET', 'POST'])
@login_required
def bonus():
    """
    奖金配置
    :return:
    """
    return render_template('settings/bonus.html', title='settings_bonus')


@bp_settings.route('/interest/', methods=['GET', 'POST'])
@login_required
def interest():
    """
    利息配置
        提前打款 op=pay_early
        延迟打款 op=pay_delay
        提前收货 op=rec_early
        延迟收货 op=rec_delay
    :return:
    """
    return render_template('settings/interest.html', title='settings_interest')
