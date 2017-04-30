#!/usr/bin/env python
# encoding: utf-8

"""
@author: zhanghe
@software: PyCharm
@file: apply_get.py
@time: 2017/4/13 下午9:32
"""


from datetime import datetime

from flask import abort
import json
from flask import redirect
from flask import render_template, request, flash, g
from flask import url_for
from flask_login import current_user, login_required

from app_backend import app
from app_backend.api.apply_put import get_apply_put_rows_by_ids, edit_apply_put
from app_backend.api.order import get_order_lists, add_order
from app_backend.api.ticket_get import add_ticket_get
from app_backend.api.ticket_put import add_ticket_put
from app_backend.forms.admin import AdminProfileForm
from app_backend.forms.apply_put import ApplyPutSearchForm
from app_backend.models import User, ApplyGet, UserProfile, ApplyPut
from app_backend.api.apply_get import get_apply_get_rows, get_apply_get_row, get_apply_get_row_by_id, \
    get_apply_get_rows_by_ids, edit_apply_get
from app_backend.forms.apply_get import ApplyGetSearchForm
from app_api.settings import PER_PAGE_BACKEND
from app_api.maps.status_delete import *
from app_api.maps.status_order import *
from app_api.maps.status_pay import *
from app_api.maps.status_rec import *
from app_api.maps.status_audit import *

from flask import Blueprint


bp_apply_get = Blueprint('apply_get', __name__, url_prefix='/apply_get')


@bp_apply_get.route('/list/')
@bp_apply_get.route('/list/<int:page>/')
@login_required
def lists(page=1):
    """
    提现申请列表
    """
    form = ApplyGetSearchForm(request.form)

    apply_get_id = request.args.get('apply_get_id', '', type=int)
    user_id = request.args.get('user_id', '', type=int)
    type_apply = request.args.get('type_apply', '', type=str)
    money_apply = request.args.get('money_apply', '', type=str)
    status_apply = request.args.get('status_apply', '', type=str)
    status_order = request.args.get('status_order', '', type=str)
    status_delete = request.args.get('status_delete', '', type=str)
    start_time = request.args.get('start_time', '', type=str)
    end_time = request.args.get('end_time', '', type=str)
    op = request.args.get('op', 0, type=int)

    form.apply_get_id.data = apply_get_id
    form.user_id.data = user_id
    form.type_apply.data = type_apply
    form.money_apply.data = money_apply
    form.status_apply.data = status_apply
    form.status_order.data = status_order
    form.status_delete.data = status_delete
    form.start_time.data = start_time
    form.end_time.data = end_time

    search_condition_apply_get = [
        ApplyGet.status_delete == STATUS_DEL_NO,
    ]
    if apply_get_id:
        search_condition_apply_get.append(ApplyGet.id == apply_get_id)
    if user_id:
        search_condition_apply_get.append(ApplyGet.user_id == user_id)
    if start_time:
        search_condition_apply_get.append(ApplyGet.create_time >= start_time)
    if end_time:
        search_condition_apply_get.append(ApplyGet.create_time <= end_time)

    # pagination = get_apply_get_rows(page)
    pagination = ApplyGet.query. \
        filter(*search_condition_apply_get). \
        outerjoin(UserProfile, ApplyGet.user_id == UserProfile.user_id). \
        add_entity(UserProfile). \
        order_by(ApplyGet.id.desc()). \
        paginate(page, PER_PAGE_BACKEND, False)
    return render_template('apply_get/list.html', title='apply_get_list', pagination=pagination, form=form)


@bp_apply_get.route('/info/<int:apply_get_id>/')
@bp_apply_get.route('/info/<int:apply_get_id>/<int:page>/')
@login_required
def info(apply_get_id, page=1):
    """
    提现申请信息
    """
    # apply_get_info = get_apply_get_row_by_id(apply_get_id)
    # return render_template('apply_get/info.html', title='apply_get_list', apply_get_info=apply_get_info)
    apply_get_info = get_apply_get_row_by_id(apply_get_id)
    # 没有信息
    if not apply_get_info:
        return redirect('apply_get.lists')
    # 删除状态
    if apply_get_info.status_delete == int(STATUS_DEL_OK):
        return redirect('apply_get.lists')
    apply_put_list = []
    # 已经匹配, 显示匹配的信息
    if apply_get_info.status_order > int(STATUS_ORDER_HANDING):
        condition = {
            'apply_get_id': apply_get_id,
            'status_delete': STATUS_DEL_NO
        }
        order_list = get_order_lists(**condition)
        apply_put_ids = [order_item.apply_put_id for order_item in order_list]
        apply_put_list = get_apply_put_rows_by_ids(apply_put_ids)

    form = ApplyPutSearchForm(request.form)

    user_id = request.args.get('user_id', '', type=int)
    type_apply = request.args.get('type_apply', '', type=str)
    money_apply = request.args.get('money_apply', '', type=str)
    status_apply = request.args.get('status_apply', '', type=str)
    status_order = request.args.get('status_order', '', type=str)
    status_delete = request.args.get('status_delete', '', type=str)
    min_money = request.args.get('min_money', '', type=str)
    max_money = request.args.get('max_money', '', type=str)
    start_time = request.args.get('start_time', '', type=str)
    end_time = request.args.get('end_time', '', type=str)
    op = request.args.get('op', 0, type=int)

    form.user_id.data = user_id
    form.type_apply.data = type_apply
    form.money_apply.data = money_apply
    form.status_apply.data = status_apply
    form.status_order.data = status_order
    form.status_delete.data = status_delete
    form.min_money.data = min_money
    form.max_money.data = max_money
    form.start_time.data = start_time
    form.end_time.data = end_time

    search_condition_apply_put = [
        ApplyPut.status_delete == STATUS_DEL_NO,
        ApplyPut.status_order < STATUS_ORDER_COMPLETED,
        ApplyPut.user_id != apply_get_id
    ]
    if user_id:
        search_condition_apply_put.append(ApplyPut.user_id == user_id)
    if min_money:
        search_condition_apply_put.append(ApplyPut.money_apply >= min_money)
    if max_money:
        search_condition_apply_put.append(ApplyPut.money_apply <= max_money)
    if start_time:
        search_condition_apply_put.append(ApplyPut.create_time >= start_time)
    if end_time:
        search_condition_apply_put.append(ApplyPut.create_time <= end_time)

    # pagination = get_apply_get_rows(page)
    pagination = ApplyPut.query. \
        filter(*search_condition_apply_put). \
        outerjoin(UserProfile, ApplyPut.user_id == UserProfile.user_id). \
        add_entity(UserProfile). \
        order_by(ApplyPut.id.desc()). \
        paginate(page, PER_PAGE_BACKEND, False)

    return render_template(
        'apply_get/info.html',
        title='apply_get_info',
        apply_get_info=apply_get_info,
        apply_put_list=apply_put_list,
        pagination=pagination,
        form=form,
        STATUS_ORDER_HANDING=STATUS_ORDER_HANDING,
        STATUS_ORDER_COMPLETED=STATUS_ORDER_COMPLETED,
    )


@bp_apply_get.route('/ajax/match/', methods=['GET', 'POST'])
@login_required
def ajax_match():
    """
    提现申请匹配
    :return:
    """
    if request.method == 'POST' and request.is_xhr:
        form = request.form
        apply_get_id = form.get('apply_get_id', 0, type=int)
        apply_put_ids = form.getlist('apply_put_id')
        apply_get_info = get_apply_get_row_by_id(apply_get_id)
        # 判断是否已经匹配
        if apply_get_info.status_order == STATUS_ORDER_COMPLETED:
            return json.dumps({'error': u'不能重复匹配'})
        apply_put_list = get_apply_put_rows_by_ids(apply_put_ids)
        # 判断是否同一个人
        apply_put_user_ids = [apply_put_item.user_id for apply_put_item in apply_put_list]
        if apply_get_info.user_id in apply_put_user_ids:
            return json.dumps({'error': u'不能匹配给自己'})
        # 判断金额
        apply_put_amount = sum([apply_put_item.money_apply for apply_put_item in apply_put_list])
        if apply_get_info.money_apply != apply_put_amount:
            return json.dumps({'error': u'金额不匹配'})

        # 循环投资申请，生成对应的付款单和收款单，同时生成订单
        for apply_put_item in apply_put_list:

            current_time = datetime.utcnow()
            # 创建投资付款单
            ticket_put_info = {
                'user_id': apply_put_item.user_id,
                'apply_put_id': apply_put_item.id,
                'money': apply_put_item.money_apply,
                'create_time': current_time,
                'update_time': current_time,
            }
            ticket_put_id = add_ticket_put(ticket_put_info)
            # 创建提现收款单(根据投资申请金额拆分)
            ticket_get_info = {
                'user_id': apply_get_info.user_id,
                'apply_get_id': apply_get_id,
                'money': apply_put_item.money_apply,
                'create_time': current_time,
                'update_time': current_time,
            }
            ticket_get_id = add_ticket_get(ticket_get_info)

            order_info = {
                'apply_put_id': apply_put_item.id,
                'apply_get_id': apply_get_id,
                'apply_put_uid': apply_put_item.user_id,
                'apply_get_uid': apply_get_info.user_id,
                'ticket_put_id': ticket_put_id,
                'ticket_get_id': ticket_get_id,
                'money': apply_put_item.money_apply,
                'status_audit': STATUS_AUDIT_SUCCESS,
                'audit_time': current_time,
                'create_time': current_time,
                'update_time': current_time,
            }
            order_id = add_order(order_info)

            # 更新提现申请状态
            apply_put_update_info = {
                'status_order': STATUS_ORDER_COMPLETED,
                'update_time': current_time,
            }
            edit_apply_put(apply_put_item.id, apply_put_update_info)
        # 更新投资申请状态
        current_time = datetime.utcnow()
        apply_get_update_info = {
            'status_order': STATUS_ORDER_COMPLETED,
            'update_time': current_time,
        }
        result = edit_apply_get(apply_get_id, apply_get_update_info)

        if result == 1:
            return json.dumps({'success': u'匹配成功'})
        if result == 0:
            return json.dumps({'error': u'匹配失败'})
    abort(404)


@bp_apply_get.route('/add/', methods=['GET', 'POST'])
@login_required
def add():
    """
    创建提现申请
    :return:
    """
    return render_template('apply_get/add.html', title='apply_get_add')


@bp_apply_get.route('/del/', methods=['GET', 'POST'])
@login_required
def delete():
    """
    删除提现申请
    :return:
    """
    pass


@bp_apply_get.route('/stats/', methods=['GET', 'POST'])
@login_required
def stats():
    """
    提现申请统计
    :return:
    """
    return render_template('apply_get/stats.html', title='apply_get_stats')
