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

from app_frontend import app
from app_frontend.api.user_profile import get_team_tree
from app_frontend.models import User
from app_frontend.api.wallet import get_wallet_rows
from app_frontend.api.wallet_item import get_wallet_item_rows

from flask import Blueprint

PER_PAGE_FRONTEND = app.config['PER_PAGE_FRONTEND']

bp_wallet = Blueprint('wallet', __name__, url_prefix='/wallet')


@bp_wallet.route('/list/')
@bp_wallet.route('/list/<int:page>/')
@login_required
def lists(page=1):
    """
    钱包列表
    """
    # 获取团队成员三级树形结构
    team_tree = get_team_tree(current_user.id)
    pagination = get_wallet_item_rows(page, PER_PAGE_FRONTEND, **{'user_id': current_user.id})
    return render_template('wallet/list.html', title='wallet_list', pagination=pagination, team_tree=team_tree)


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
