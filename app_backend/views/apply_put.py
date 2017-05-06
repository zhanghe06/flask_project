#!/usr/bin/env python
# encoding: utf-8

"""
@author: zhanghe
@software: PyCharm
@file: apply_put.py
@time: 2017/4/13 下午9:32
"""


from datetime import datetime
import json

from flask import abort
from flask import redirect
from flask import render_template, request, flash, g
from flask import url_for
from flask_login import current_user, login_required

from app_backend import app
from app_backend.api.apply_get import get_apply_get_rows, get_apply_get_rows_by_ids, edit_apply_get

from app_backend.forms.admin import AdminProfileForm
from app_backend.forms.apply_get import ApplyGetSearchForm
from app_backend.models import User, ApplyGet, UserProfile, ApplyPut
from app_backend.api.apply_put import get_apply_put_rows, get_apply_put_row, get_apply_put_row_by_id, edit_apply_put, apply_put_match
from app_backend.api.order import get_order_row, get_order_rows, get_order_lists, add_order, get_put_match_order_rows
from app_backend.forms.apply_put import ApplyPutSearchForm
from app_common.settings import PER_PAGE_BACKEND
from app_common.maps.status_delete import *
from app_common.maps.status_order import *
from app_common.maps.status_pay import *
from app_common.maps.status_rec import *
from app_common.maps.status_audit import *

from flask import Blueprint


bp_apply_put = Blueprint('apply_put', __name__, url_prefix='/apply_put')


@bp_apply_put.route('/list/')
@bp_apply_put.route('/list/<int:page>/')
@login_required
def lists(page=1):
    """
    投资申请列表
    """
    form = ApplyPutSearchForm(request.form)

    apply_put_id = request.args.get('apply_put_id', '', type=int)
    user_id = request.args.get('user_id', '', type=int)
    type_apply = request.args.get('type_apply', '', type=str)
    money_apply = request.args.get('money_apply', '', type=str)
    status_apply = request.args.get('status_apply', '', type=str)
    status_order = request.args.get('status_order', '', type=str)
    status_delete = request.args.get('status_delete', '', type=str)
    start_time = request.args.get('start_time', '', type=str)
    end_time = request.args.get('end_time', '', type=str)
    op = request.args.get('op', 0, type=int)

    form.apply_put_id.data = apply_put_id
    form.user_id.data = user_id
    form.type_apply.data = type_apply
    form.money_apply.data = money_apply
    form.status_apply.data = status_apply
    form.status_order.data = status_order
    form.status_delete.data = status_delete
    form.start_time.data = start_time
    form.end_time.data = end_time

    search_condition_apply_put = [
        ApplyPut.status_delete == STATUS_DEL_NO,
    ]
    if apply_put_id:
        search_condition_apply_put.append(ApplyPut.id == apply_put_id)
    if user_id:
        search_condition_apply_put.append(ApplyPut.user_id == user_id)
    if status_apply:
        search_condition_apply_put.append(ApplyPut.status_apply == status_apply)
    if status_order:
        search_condition_apply_put.append(ApplyPut.status_order == status_order)
    if status_delete:
        search_condition_apply_put.append(ApplyPut.status_delete == status_delete)
    if start_time:
        search_condition_apply_put.append(ApplyPut.create_time >= start_time)
    if end_time:
        search_condition_apply_put.append(ApplyPut.create_time <= end_time)

    # pagination = get_apply_put_rows(page)
    pagination = ApplyPut.query. \
        filter(*search_condition_apply_put). \
        outerjoin(UserProfile, ApplyPut.user_id == UserProfile.user_id). \
        add_entity(UserProfile). \
        order_by(ApplyPut.id.desc()). \
        paginate(page, PER_PAGE_BACKEND, False)
    return render_template('apply_put/list.html', title='apply_put_list', pagination=pagination, form=form)


@bp_apply_put.route('/info/<int:apply_put_id>/')
@bp_apply_put.route('/info/<int:apply_put_id>/<int:page>/')
@login_required
def info(apply_put_id, page=1):
    """
    投资申请信息
    """
    apply_put_info = get_apply_put_row_by_id(apply_put_id)
    # 没有信息
    if not apply_put_info:
        return redirect('apply_put.lists')
    # 删除状态
    if apply_put_info.status_delete == int(STATUS_DEL_OK):
        return redirect('apply_put.lists')
    apply_get_list = []
    # 已经匹配, 显示匹配的信息
    if apply_put_info.status_order > int(STATUS_ORDER_HANDING):
        apply_get_list = get_put_match_order_rows(apply_put_id)

    form = ApplyGetSearchForm(request.form)

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

    search_condition_apply_get = [
        ApplyGet.status_delete == STATUS_DEL_NO,
        ApplyGet.status_order < STATUS_ORDER_COMPLETED,
        ApplyGet.user_id != apply_put_info.user_id
    ]
    if user_id:
        search_condition_apply_get.append(ApplyGet.user_id == user_id)
    if min_money:
        search_condition_apply_get.append(ApplyGet.money_apply >= min_money)
    if max_money:
        search_condition_apply_get.append(ApplyGet.money_apply <= max_money)
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

    return render_template(
        'apply_put/info.html',
        title='apply_put_info',
        apply_put_info=apply_put_info,
        apply_get_list=apply_get_list,
        pagination=pagination,
        form=form,
        STATUS_ORDER_HANDING=STATUS_ORDER_HANDING,
        STATUS_ORDER_COMPLETED=STATUS_ORDER_COMPLETED,
    )


@bp_apply_put.route('/ajax/match/', methods=['GET', 'POST'])
@login_required
def ajax_match():
    """
    投资申请匹配
    :return:
    """
    if request.method == 'POST' and request.is_xhr:
        form = request.form
        accept_split = form.get('accept_split', 0, type=int)
        apply_put_id = form.get('apply_put_id', 0, type=int)
        apply_get_ids = form.getlist('apply_get_id')

        try:
            result = apply_put_match(apply_put_id, apply_get_ids, accept_split)
            if result == 1:
                return json.dumps({'success': u'匹配成功'})
            if result == 0:
                return json.dumps({'error': u'匹配失败'})
        except Exception as e:
            return json.dumps({'error': e.message})
    abort(404)


@bp_apply_put.route('/add/', methods=['GET', 'POST'])
@login_required
def add():
    """
    创建投资申请
    :return:
    """
    return render_template('apply_put/add.html', title='apply_put_add')


@bp_apply_put.route('/del/', methods=['GET', 'POST'])
@login_required
def delete():
    """
    删除投资申请
    :return:
    """
    pass


@bp_apply_put.route('/stats/', methods=['GET', 'POST'])
@login_required
def stats():
    """
    投资申请统计
    :return:
    """
    return render_template('apply_put/stats.html', title='apply_put_stats')
