#!/usr/bin/env python
# encoding: utf-8

"""
@author: zhanghe
@software: PyCharm
@file: order.py
@time: 2017/4/24 下午10:49
"""


from datetime import datetime
from flask import redirect
from flask import render_template, request, flash, g
from flask import url_for
from flask_login import current_user, login_required

from app_backend import app
from app_backend.forms.admin import AdminProfileForm
from app_backend.models import User
from app_backend.api.order import get_order_rows, get_order_row

from flask import Blueprint


bp_order = Blueprint('order', __name__, url_prefix='/order')


@bp_order.route('/list/')
@bp_order.route('/list/<int:page>/')
@login_required
def lists(page=1):
    """
    订单列表
    """
    pagination = get_order_rows(page)
    return render_template('order/list.html', title='order_list', pagination=pagination)


@bp_order.route('/add/', methods=['GET', 'POST'])
@login_required
def add():
    """
    创建订单
    :return:
    """
    pass


@bp_order.route('/del/', methods=['GET', 'POST'])
@login_required
def delete():
    """
    删除订单
    :return:
    """
    pass
