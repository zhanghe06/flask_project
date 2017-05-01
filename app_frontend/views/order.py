#!/usr/bin/env python
# encoding: utf-8

"""
@author: zhanghe
@software: PyCharm
@file: order.py
@time: 2017/3/30 下午6:05
"""


from datetime import datetime
from flask import redirect
from flask import render_template, request, flash, g
from flask import url_for
from flask_login import current_user, login_required
import flask_excel as excel

from app_frontend import app
from app_frontend.models import User, UserProfile
from app_frontend.api.order import get_order_rows, get_order_row
from app_common.maps.status_pay import STATUS_PAY_DICT
from app_common.maps.status_rec import STATUS_REC_DICT

from flask import Blueprint


bp_order = Blueprint('order', __name__, url_prefix='/order')


@bp_order.route('/put/list/')
@bp_order.route('/put/list/<int:page>/')
@login_required
def lists_put(page=1):
    """
    投资订单列表
    """
    uid = current_user.id
    condition = {
        'apply_put_uid': uid,
        'status_rec': 0,        # 默认未处理
        'status_delete': 0
    }
    # 支付状态
    status_pay = request.args.get('status_pay', 0, type=int)
    if status_pay in STATUS_PAY_DICT:
        condition['status_pay'] = status_pay

    pagination = get_order_rows(page, **condition)
    return render_template('order/put_list.html', title='order_put_list', pagination=pagination)


@bp_order.route('/get/list/')
@bp_order.route('/get/list/<int:page>/')
@login_required
def lists_get(page=1):
    """
    提现订单列表
    """
    uid = current_user.id
    condition = {
        'apply_get_uid': uid,
        'status_rec': 0,        # 默认未处理
        'status_delete': 0
    }
    # 收款状态
    status_rec = request.args.get('status_rec', 0, type=int)
    if status_rec in STATUS_REC_DICT:
        condition['status_rec'] = status_rec

    pagination = get_order_rows(page, **condition)
    return render_template('order/get_list.html', title='order_get_list', pagination=pagination)


@bp_order.route('/put/info/<int:order_id>/', methods=['GET', 'POST'])
@login_required
def info_put(order_id):
    """
    投资订单详情
    """
    uid = current_user.id
    condition = {
        'id': order_id,
        'apply_put_uid': uid
    }
    order_info = get_order_row(**condition)
    return render_template('order/put_info.html', title='order_put_info', order_info=order_info)


@bp_order.route('/get/info/<int:order_id>/', methods=['GET', 'POST'])
@login_required
def info_get(order_id):
    """
    提现订单详情
    """
    uid = current_user.id
    condition = {
        'id': order_id,
        'apply_get_uid': uid
    }
    order_info = get_order_row(**condition)
    return render_template('order/get_info.html', title='order_get_info', order_info=order_info)


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


@bp_order.route('/stats/', methods=['GET', 'POST'])
@login_required
def stats():
    """
    订单统计
    :return:
    """
    pass
