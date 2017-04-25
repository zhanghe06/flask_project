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
import flask_excel as excel

from app_backend import app
from app_backend.forms.admin import AdminProfileForm
from app_backend.models import User, UserProfile
from app_backend.api.order import get_order_rows, get_order_row
from app_backend.forms.order import OrderSearchForm

from flask import Blueprint


bp_order = Blueprint('order', __name__, url_prefix='/order')


@bp_order.route('/list/')
@bp_order.route('/list/<int:page>/')
@login_required
def lists(page=1):
    """
    订单列表
    """
    form = OrderSearchForm(request.form)

    order_id = request.args.get('order_id', '', type=int)
    apply_put_id = request.args.get('apply_put_id', '', type=int)
    apply_get_id = request.args.get('apply_get_id', '', type=int)
    apply_put_uid = request.args.get('apply_put_uid', '', type=int)
    apply_get_uid = request.args.get('apply_get_uid', '', type=int)
    ticket_put_id = request.args.get('ticket_put_id', '', type=int)
    ticket_get_id = request.args.get('ticket_get_id', '', type=int)
    status_audit = request.args.get('status_audit', '', type=str)
    status_pay = request.args.get('status_pay', '', type=str)
    status_rec = request.args.get('status_rec', '', type=str)
    start_time = request.args.get('start_time', '', type=str)
    end_time = request.args.get('end_time', '', type=str)
    op = request.args.get('op', 0, type=int)

    form.order_id.data = order_id
    form.apply_put_id.data = apply_put_id
    form.apply_get_id.data = apply_get_id
    form.apply_put_uid.data = apply_put_uid
    form.apply_get_uid.data = apply_get_uid
    form.ticket_put_id.data = ticket_put_id
    form.ticket_get_id.data = ticket_get_id
    form.status_audit.data = status_audit
    form.status_pay.data = status_pay
    form.status_rec.data = status_rec
    form.start_time.data = start_time
    form.end_time.data = end_time

    pagination = get_order_rows(page)
    return render_template('order/list.html', title='order_list', pagination=pagination, form=form)


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
