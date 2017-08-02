#!/usr/bin/env python
# encoding: utf-8

"""
@author: zhanghe
@software: PyCharm
@file: order.py
@time: 2017/4/24 下午10:49
"""


import json

from flask import abort
from sqlalchemy.orm import aliased
from datetime import datetime
from flask import redirect
from flask import render_template, request, flash, g
from flask import url_for
from flask_login import current_user, login_required
import flask_excel as excel

from app_backend import app
from app_backend.forms.admin import AdminProfileForm
from app_backend.models import User, UserProfile, Order
from app_backend.api.order import get_order_rows, get_order_row, order_stats, edit_order, get_order_row_by_id
from app_backend.api.apply_put import edit_apply_put, get_apply_put_row_by_id
from app_backend.api.apply_get import edit_apply_get, get_apply_get_row_by_id
from app_backend.forms.order import OrderSearchForm
from app_common.maps.status_order import STATUS_ORDER_HANDING, STATUS_ORDER_PROCESSING

from flask import Blueprint

from app_common.maps.status_delete import STATUS_DEL_NO, STATUS_DEL_OK
from app_common.tools import json_default
from app_common.tools.date_time import time_local_to_utc

from app_backend.permissions import permission_order
from app_backend.database import db

PER_PAGE_BACKEND = app.config['PER_PAGE_BACKEND']

bp_order = Blueprint('order', __name__, url_prefix='/order')


@bp_order.route('/list/')
@bp_order.route('/list/<int:page>/')
@login_required
@permission_order.require(http_exception=403)
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
    form.status_audit.data = status_audit
    form.status_pay.data = status_pay
    form.status_rec.data = status_rec
    form.start_time.data = start_time
    form.end_time.data = end_time

    # 搜索条件
    search_condition_order = [
        Order.status_delete == STATUS_DEL_NO,
    ]

    if order_id:
        search_condition_order.append(Order.id == order_id)
    if apply_put_id:
        search_condition_order.append(Order.apply_put_id == apply_put_id)
    if apply_get_id:
        search_condition_order.append(Order.apply_get_id == apply_get_id)
    if apply_put_uid:
        search_condition_order.append(Order.apply_put_uid == apply_put_uid)
    if apply_get_uid:
        search_condition_order.append(Order.apply_get_uid == apply_get_uid)
    if status_audit:
        search_condition_order.append(Order.status_audit == status_audit)
    if status_pay:
        search_condition_order.append(Order.status_pay == status_pay)
    if status_rec:
        search_condition_order.append(Order.status_rec == status_rec)
    if start_time:
        search_condition_order.append(Order.create_time >= time_local_to_utc(start_time))
    if end_time:
        search_condition_order.append(Order.create_time <= time_local_to_utc(end_time))

    # 多次连接同一张表，需要别名
    user_profile_put = aliased(UserProfile)
    user_profile_get = aliased(UserProfile)

    try:
        pagination = Order.query. \
            filter(*search_condition_order). \
            outerjoin(user_profile_put, Order.apply_put_uid == user_profile_put.user_id). \
            add_entity(user_profile_put). \
            outerjoin(user_profile_get, Order.apply_get_uid == user_profile_get.user_id). \
            add_entity(user_profile_get). \
            order_by(Order.id.desc()). \
            paginate(page, PER_PAGE_BACKEND, False)
        db.session.commit()
        return render_template('order/list.html', title='order_list', pagination=pagination, form=form)
    except Exception as e:
        db.session.rollback()
        flash(e.message, category='warning')
        return redirect(url_for('index'))


@bp_order.route('/add/', methods=['GET', 'POST'])
@login_required
@permission_order.require(http_exception=403)
def add():
    """
    创建订单
    :return:
    """
    pass


@bp_order.route('/del/', methods=['GET', 'POST'])
@login_required
@permission_order.require(http_exception=403)
def delete():
    """
    删除订单
    :return:
    """
    pass


@bp_order.route('/stats/', methods=['GET', 'POST'])
@login_required
@permission_order.require(http_exception=403)
def stats():
    """
    订单统计
    :return:
    """
    return render_template('order/stats.html', title='order_stats')


@bp_order.route('/ajax_stats/', methods=['GET', 'POST'])
@login_required
def ajax_stats():
    """
    订单金额统计
    :return:
    """
    time_based = request.args.get('time_based', 'hour')
    result_order = order_stats(time_based)

    line_chart_data = {
        'labels': [label for label, _ in result_order],
        'datasets': [
            {
                'label': u'订单金额',
                'backgroundColor': 'rgba(220,220,220,0.5)',
                'borderColor': 'rgba(220,220,220,1)',
                'pointBackgroundColor': 'rgba(220,220,220,1)',
                'pointBorderColor': '#fff',
                'pointBorderWidth': 2,
                'data': [data for _, data in result_order]
            }
        ]
    }
    return json.dumps(line_chart_data, default=json_default)


@bp_order.route('/ajax/audit/', methods=['GET', 'POST'])
@login_required
@permission_order.require(http_exception=403)
def ajax_audit():
    """
    订单审核
    :return:
    """
    if 1:
        return json.dumps({'success': u'审核成功'})
    else:
        return json.dumps({'error': u'审核失败'})


@bp_order.route('/ajax/del/', methods=['GET', 'POST'])
@login_required
@permission_order.require(http_exception=403)
def ajax_delete():
    """
    删除订单
    :return:
    """
    if request.method == 'GET' and request.is_xhr:
        order_id = request.args.get('order_id', 0, type=int)
        if not order_id:
            return json.dumps({'error': u'参数错误，删除失败'})
        order_info = get_order_row_by_id(order_id)
        if not order_info:
            return json.dumps({'error': u'订单不存在，删除失败'})
        if order_info.status_delete == int(STATUS_DEL_OK):
            return json.dumps({'error': u'订单已删除，不能重复删除'})
        current_time = datetime.utcnow()
        # 修改订单删除状态
        order_data = {
            'status_delete': STATUS_DEL_OK,
            'delete_time': current_time,
            'update_time': current_time
        }
        result = edit_order(order_id, order_data)

        # 还原提现申请订单金额
        apply_get_info = get_apply_get_row_by_id(order_info.apply_get_id)

        last_money = apply_get_info.money_order - order_info.money
        status_order = STATUS_ORDER_PROCESSING if last_money > 0 else STATUS_ORDER_HANDING

        apply_get_data = {
            'money_order': last_money,
            'status_order': status_order,
            'update_time': current_time
        }

        edit_apply_get(order_info.apply_get_id, apply_get_data)

        # 还原投资申请订单金额
        apply_put_info = get_apply_put_row_by_id(order_info.apply_put_id)

        last_money = apply_put_info.money_order - order_info.money
        status_order = STATUS_ORDER_PROCESSING if last_money > 0 else STATUS_ORDER_HANDING

        apply_put_data = {
            'money_order': last_money,
            'status_order': status_order,
            'update_time': current_time
        }

        edit_apply_put(order_info.apply_put_id, apply_put_data)

        if result:
            return json.dumps({'success': u'删除成功'})
        else:
            return json.dumps({'error': u'删除失败'})
    abort(404)
