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

from app_common.settings import PER_PAGE_FRONTEND
from app_frontend import app
from app_frontend.models import User, UserProfile, Order
from app_frontend.api.order import get_order_rows, get_order_row
from app_common.maps.status_pay import *
from app_common.maps.status_rec import *
from app_common.maps.status_delete import *

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

    # 支付状态
    status_pay = request.args.get('status_pay', 0, type=int)

    search_condition_order = [
        Order.apply_put_uid == uid,
        Order.status_rec == STATUS_REC_HOLDING,  # 默认未处理
        Order.status_delete == STATUS_DEL_NO,  # 默认未删除
    ]

    if status_pay in STATUS_PAY_DICT:
        search_condition_order.append(Order.status_pay == status_pay)

    pagination = Order.query. \
        filter(*search_condition_order). \
        outerjoin(UserProfile, Order.apply_get_uid == UserProfile.user_id). \
        add_entity(UserProfile). \
        order_by(Order.id.desc()). \
        paginate(page, PER_PAGE_FRONTEND, False)

    return render_template('order/put_list.html', title='order_put_list', pagination=pagination)


@bp_order.route('/get/list/')
@bp_order.route('/get/list/<int:page>/')
@login_required
def lists_get(page=1):
    """
    提现订单列表
    """
    uid = current_user.id

    # 收款状态
    status_rec = request.args.get('status_rec', 0, type=int)

    search_condition_order = [
        Order.apply_get_uid == uid,
        Order.status_rec == STATUS_REC_HOLDING,  # 默认未处理
        Order.status_delete == STATUS_DEL_NO,  # 默认未删除
    ]

    if status_rec in STATUS_REC_DICT:
        search_condition_order.append(Order.status_rec == status_rec)

    pagination = Order.query. \
        filter(*search_condition_order). \
        outerjoin(UserProfile, Order.apply_put_uid == UserProfile.user_id). \
        add_entity(UserProfile). \
        order_by(Order.id.desc()). \
        paginate(page, PER_PAGE_FRONTEND, False)

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


@bp_order.route('/pay/<int:order_id>/', methods=['GET', 'POST'])
@login_required
def pay(order_id):
    """
    订单支付
    """
    uid = current_user.id
    # 获取投资订单详情
    condition = {
        'id': order_id,
        'apply_put_uid': uid
    }
    order_info = get_order_row(**condition)
    return render_template('order/pay.html', title='order_pay', order_info=order_info)


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
