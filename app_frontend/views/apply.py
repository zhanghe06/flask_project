#!/usr/bin/env python
# encoding: utf-8

"""
@author: zhanghe
@software: PyCharm
@file: apply.py
@time: 2017/4/27 上午9:34
"""


from datetime import datetime
from flask import redirect
from flask import render_template, request, flash, g
from flask import url_for
from flask_login import current_user, login_required

from app_frontend import app
from app_frontend.models import User
from app_frontend.api.apply_get import get_apply_get_rows, get_apply_get_row, add_apply_get, user_apply_get
from app_frontend.api.apply_put import get_apply_put_rows, get_apply_put_row, add_apply_put
from app_frontend.api.user_bank import user_bank_is_complete
from app_frontend.api.user_profile import user_profile_is_complete
from app_common.maps.status_order import *
from app_common.maps.type_apply import *
from app_common.maps.status_apply import *
from app_common.maps.status_delete import *
from app_frontend.forms.apply_get import ApplyGetAddForm
from app_frontend.forms.apply_put import ApplyPutAddForm
from flask import Blueprint


bp_apply = Blueprint('apply', __name__, url_prefix='/apply')


@bp_apply.route('/put/list/')
@bp_apply.route('/put/list/<int:page>/')
@login_required
def lists_put(page=1):
    """
    投资申请列表
    """
    uid = current_user.id
    condition = {
        'user_id': uid,
        'status_order': 0,
        'status_delete': 0
    }
    # 订单状态
    status_order = request.args.get('status_order', 0, type=int)
    if status_order in STATUS_ORDER_DICT:
        condition['status_order'] = status_order

    pagination = get_apply_put_rows(page, **condition)
    return render_template('apply/put_list.html', title='apply_put_list', pagination=pagination)


@bp_apply.route('/get/list/')
@bp_apply.route('/get/list/<int:page>/')
@login_required
def lists_get(page=1):
    """
    提现申请列表
    """
    uid = current_user.id
    condition = {
        'user_id': uid,
        'status_order': 0,
        'status_delete': 0
    }
    # 订单状态
    status_order = request.args.get('status_order', 0, type=int)
    if status_order in STATUS_ORDER_DICT:
        condition['status_order'] = status_order

    pagination = get_apply_get_rows(page, **condition)
    return render_template('apply/get_list.html', title='apply_get_list', pagination=pagination)


@bp_apply.route('/put/add/', methods=['GET', 'POST'])
@login_required
def add_put():
    """
    创建投资申请
    :return:
    """
    user_id = current_user.id
    # 判断基本信息和银行信息是否完整
    if not user_profile_is_complete(user_id):
        flash(u'请先完善基本信息', 'warning')
        return redirect(url_for('user.profile'))
    if not user_profile_is_complete(user_id):
        flash(u'请先完善银行信息', 'warning')
        return redirect(url_for('user.bank'))
    form = ApplyPutAddForm(request.form)
    if request.method == 'POST':
        if form.validate_on_submit():
            current_time = datetime.utcnow()
            apply_put_info = {
                'user_id': user_id,
                'type_apply': TYPE_APPLY_USER,
                'type_pay': form.type_pay.data,
                'money_apply': form.money_apply.data,
                'status_apply': STATUS_APPLY_SUCCESS,
                'status_order': STATUS_ORDER_HANDING,
                'status_delete': STATUS_DEL_NO,
                'create_time': current_time,
                'update_time': current_time,
            }
            result = add_apply_put(apply_put_info)
            if result:
                flash(u'申请成功', 'success')
            else:
                flash(u'申请失败', 'warning')
            return redirect(url_for('apply.lists_put'))
    return render_template('apply/put_add.html', title='apply_put_add', form=form)


@bp_apply.route('/get/add/', methods=['GET', 'POST'])
@login_required
def add_get():
    """
    创建提现申请
    :return:
    """
    user_id = current_user.id
    # 判断基本信息和银行信息是否完整
    if not user_profile_is_complete(user_id):
        flash(u'请先完善基本信息', 'warning')
        return redirect(url_for('user.profile'))
    if not user_profile_is_complete(user_id):
        flash(u'请先完善银行信息', 'warning')
        return redirect(url_for('user.bank'))
    form = ApplyGetAddForm(request.form)
    if request.method == 'POST':
        if form.validate_on_submit():
            type_pay = form.type_pay.data
            type_withdraw = form.type_withdraw.data
            money_apply = form.money_apply.data
            try:
                result = user_apply_get(user_id, type_pay, type_withdraw, money_apply)
                if result:
                    flash(u'申请成功', 'success')
                    return redirect(url_for('apply.lists_get'))
            except Exception as e:
                flash(u'申请失败, 原因：%s' % e.message, 'warning')
    return render_template('apply/get_add.html', title='apply_get_add', form=form)


@bp_apply.route('/put/del/', methods=['GET', 'POST'])
@login_required
def delete_put():
    """
    删除投资申请
    :return:
    """
    pass


@bp_apply.route('/get/del/', methods=['GET', 'POST'])
@login_required
def delete_get():
    """
    删除提现申请
    :return:
    """
    pass


@bp_apply.route('/put/stats/', methods=['GET', 'POST'])
@login_required
def stats_put():
    """
    投资申请统计
    :return:
    """
    pass


@bp_apply.route('/get/stats/', methods=['GET', 'POST'])
@login_required
def stats_get():
    """
    提现申请统计
    :return:
    """
    pass
