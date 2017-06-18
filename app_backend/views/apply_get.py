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
from flask import Blueprint
import json
from flask import redirect
from flask import render_template, request, flash, g
from flask import url_for
from flask_login import current_user, login_required

from app_backend import app
from app_backend.api.apply_put import get_apply_put_rows_by_ids, edit_apply_put
from app_backend.api.order import get_order_lists, add_order, get_get_match_order_rows

from app_backend.forms.admin import AdminProfileForm
from app_backend.forms.apply_put import ApplyPutSearchForm
from app_backend.models import User, ApplyGet, UserProfile, ApplyPut
from app_backend.api.apply_get import get_apply_get_rows, get_apply_get_row, get_apply_get_row_by_id, \
    get_apply_get_rows_by_ids, edit_apply_get, apply_get_match, apply_get_stats
from app_backend.forms.apply_get import ApplyGetSearchForm

from app_common.maps.status_delete import *
from app_common.maps.status_order import *
from app_common.maps.status_pay import *
from app_common.maps.status_rec import *
from app_common.maps.status_audit import *
from app_common.tools import json_default
from app_common.tools.date_time import time_local_to_utc
from app_backend.permissions import permission_order
from app_backend.database import db


PER_PAGE_BACKEND = app.config['PER_PAGE_BACKEND']

bp_apply_get = Blueprint('apply_get', __name__, url_prefix='/apply_get')


@bp_apply_get.route('/list/')
@bp_apply_get.route('/list/<int:page>/')
@login_required
@permission_order.require(http_exception=403)
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
    if status_apply:
        search_condition_apply_get.append(ApplyGet.status_apply == status_apply)
    if status_order:
        search_condition_apply_get.append(ApplyGet.status_order == status_order)
    if status_delete:
        search_condition_apply_get.append(ApplyGet.status_delete == status_delete)
    if start_time:
        search_condition_apply_get.append(ApplyGet.create_time >= time_local_to_utc(start_time))
    if end_time:
        search_condition_apply_get.append(ApplyGet.create_time <= time_local_to_utc(end_time))

    # pagination = get_apply_get_rows(page)
    try:
        pagination = ApplyGet.query. \
            filter(*search_condition_apply_get). \
            outerjoin(UserProfile, ApplyGet.user_id == UserProfile.user_id). \
            add_entity(UserProfile). \
            order_by(ApplyGet.id.desc()). \
            paginate(page, PER_PAGE_BACKEND, False)
        db.session.commit()
        return render_template('apply_get/list.html', title='apply_get_list', pagination=pagination, form=form)
    except Exception as e:
        db.session.rollback()
        flash(e.message, category='warning')
        return redirect(url_for('index'))


@bp_apply_get.route('/info/<int:apply_get_id>/')
@bp_apply_get.route('/info/<int:apply_get_id>/<int:page>/')
@login_required
@permission_order.require(http_exception=403)
def info(apply_get_id, page=1):
    """
    提现申请信息
    """
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
        apply_put_list = get_get_match_order_rows(apply_get_id)

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
        ApplyPut.user_id != apply_get_info.user_id
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
    try:
        pagination = ApplyPut.query. \
            filter(*search_condition_apply_put). \
            outerjoin(UserProfile, ApplyPut.user_id == UserProfile.user_id). \
            add_entity(UserProfile). \
            order_by(ApplyPut.id.desc()). \
            paginate(page, PER_PAGE_BACKEND, False)
        db.session.commit()
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
    except Exception as e:
        db.session.rollback()
        flash(e.message, category='warning')
        return redirect(url_for('index'))


@bp_apply_get.route('/ajax/match/', methods=['GET', 'POST'])
@login_required
@permission_order.require(http_exception=403)
def ajax_match():
    """
    提现申请匹配
    :return:
    """
    if request.method == 'POST' and request.is_xhr:
        form = request.form
        accept_split = form.get('accept_split', 0, type=int)
        apply_get_id = form.get('apply_get_id', 0, type=int)
        apply_put_ids = form.getlist('apply_put_id')

        try:
            result = apply_get_match(apply_get_id, apply_put_ids, accept_split)
            if result == 1:
                return json.dumps({'success': u'匹配成功'})
            if result == 0:
                return json.dumps({'error': u'匹配失败'})
        except Exception as e:
            return json.dumps({'error': e.message})
    abort(404)


@bp_apply_get.route('/add/', methods=['GET', 'POST'])
@login_required
@permission_order.require(http_exception=403)
def add():
    """
    创建提现申请
    :return:
    """
    return render_template('apply_get/add.html', title='apply_get_add')


@bp_apply_get.route('/del/', methods=['GET', 'POST'])
@login_required
@permission_order.require(http_exception=403)
def delete():
    """
    删除提现申请
    :return:
    """
    pass


# @bp_apply_get.route('/stats/', methods=['GET', 'POST'])
# @login_required
# def stats():
#     """
#     提现申请统计
#     :return:
#     """
#     return render_template('apply_get/stats.html', title='apply_get_stats')


@bp_apply_get.route('/ajax_stats/', methods=['GET', 'POST'])
@login_required
def ajax_stats():
    """
    提现申请统计
    :return:
    """
    time_based = request.args.get('time_based', 'hour')
    result_apply_get = apply_get_stats(time_based)

    line_chart_data = {
        'labels': [label for label, _ in result_apply_get],
        'datasets': [
            {
                'label': u'提现申请',
                'backgroundColor': 'rgba(220,220,220,0.5)',
                'borderColor': 'rgba(220,220,220,1)',
                'pointBackgroundColor': 'rgba(220,220,220,1)',
                'pointBorderColor': '#fff',
                'pointBorderWidth': 2,
                'data': [data for _, data in result_apply_get]
            }
        ]
    }
    return json.dumps(line_chart_data, default=json_default)
