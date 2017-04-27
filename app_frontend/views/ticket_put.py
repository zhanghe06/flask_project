#!/usr/bin/env python
# encoding: utf-8

"""
@author: zhanghe
@software: PyCharm
@file: ticket_put.py
@time: 2017/4/18 上午9:46
"""


from datetime import datetime
from flask import redirect
from flask import render_template, request, flash, g
from flask import url_for
from flask_login import current_user, login_required

from app_frontend import app
from app_frontend.models import User
from app_frontend.api.ticket_put import get_ticket_put_rows, get_ticket_put_row

from flask import Blueprint


bp_ticket_put = Blueprint('ticket_put', __name__, url_prefix='/ticket_put')


@bp_ticket_put.route('/list/')
@bp_ticket_put.route('/list/<int:page>/')
@login_required
def lists(page=1):
    """
    付款单列表
    """
    uid = current_user.id
    pagination = get_ticket_put_rows(page, **{'user_id': uid, 'status_delete': 0})
    return render_template('ticket_put/list.html', title='ticket_put_list', pagination=pagination)


@bp_ticket_put.route('/add/', methods=['GET', 'POST'])
@login_required
def add():
    """
    创建付款单
    :return:
    """
    pass


@bp_ticket_put.route('/del/', methods=['GET', 'POST'])
@login_required
def delete():
    """
    删除付款单
    :return:
    """
    pass


