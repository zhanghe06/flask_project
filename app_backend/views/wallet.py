#!/usr/bin/env python
# encoding: utf-8

"""
@author: zhanghe
@software: PyCharm
@file: wallet.py
@time: 2017/4/25 下午1:25
"""


from datetime import datetime
from flask import redirect
from flask import render_template, request, flash, g
from flask import url_for
from flask_login import current_user, login_required

from app_backend import app
from app_backend.forms.admin import AdminProfileForm
from app_backend.models import User
from app_backend.api.wallet import get_wallet_rows

from flask import Blueprint


bp_wallet = Blueprint('wallet', __name__, url_prefix='/wallet')


@bp_wallet.route('/list/')
@bp_wallet.route('/list/<int:page>/')
@login_required
def lists(page=1):
    """
    钱包列表
    """

    pagination = get_wallet_rows(page)
    return render_template('wallet/list.html', title='wallet_list', pagination=pagination)


@bp_wallet.route('/add/', methods=['GET', 'POST'])
@login_required
def add():
    """
    创建钱包
    :return:
    """
    pass


@bp_wallet.route('/del/', methods=['GET', 'POST'])
@login_required
def delete():
    """
    删除钱包
    :return:
    """
    pass


@bp_wallet.route('/stats/', methods=['GET', 'POST'])
@login_required
def stats():
    """
    钱包统计
    :return:
    """
    pass
