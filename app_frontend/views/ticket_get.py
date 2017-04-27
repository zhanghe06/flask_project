#!/usr/bin/env python
# encoding: utf-8

"""
@author: zhanghe
@software: PyCharm
@file: ticket_get.py
@time: 2017/4/18 上午9:46
"""


from datetime import datetime
from flask import redirect
from flask import render_template, request, flash, g
from flask import url_for
from flask_login import current_user, login_required

from app_frontend import app
from app_frontend.models import User
from app_frontend.api.ticket_get import get_ticket_get_rows, get_ticket_get_row

from flask import Blueprint


bp_ticket_get = Blueprint('ticket_get', __name__, url_prefix='/ticket_get')


@bp_ticket_get.route('/list/')
@bp_ticket_get.route('/list/<int:page>/')
@login_required
def lists(page=1):
    """
    收款单列表
    """
    uid = current_user.id
    pagination = get_ticket_get_rows(page, **{'user_id': uid, 'status_delete': 0})
    return render_template('ticket_get/list.html', title='ticket_get_list', pagination=pagination)


@bp_ticket_get.route('/add/', methods=['GET', 'POST'])
@login_required
def add():
    """
    创建收款单
    :return:
    """
    pass


@bp_ticket_get.route('/del/', methods=['GET', 'POST'])
@login_required
def delete():
    """
    删除收款单
    :return:
    """
    pass
