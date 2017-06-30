#!/usr/bin/env python
# encoding: utf-8

"""
@author: zhanghe
@software: PyCharm
@file: apply.py
@time: 2017/4/27 上午9:34
"""


from datetime import datetime

from decimal import Decimal
from flask import redirect
from flask import render_template, request, flash, g
from flask import url_for
from flask_login import current_user, login_required

from app_frontend import app
from app_frontend.lib.rabbit_mq import RabbitDelayQueue
from app_frontend.models import User, ApplyGet, ApplyPut
from app_frontend.api.apply_get import get_apply_get_rows, get_apply_get_row, add_apply_get, user_apply_get
from app_frontend.api.apply_put import get_apply_put_rows, get_apply_put_row, add_apply_put
from app_frontend.api.user_bank import user_bank_is_complete
from app_frontend.api.user_profile import user_profile_is_complete, get_team_tree
from app_frontend.api.scheduling import get_scheduling_row_by_id, edit_scheduling
from app_frontend.api.scheduling_item import add_scheduling_item
from app_common.maps.status_order import *
from app_common.maps.type_apply import *
from app_common.maps.status_apply import *
from app_common.maps.status_delete import *
from app_common.maps.status_active import *
from app_common.maps.status_audit import *
from app_frontend.forms.apply_get import ApplyGetAddForm
from app_frontend.forms.apply_put import ApplyPutAddForm
from flask import Blueprint

from app_frontend.tools.config_manage import get_conf

EXCHANGE_NAME = app.config['EXCHANGE_NAME']
PER_PAGE_FRONTEND = app.config['PER_PAGE_FRONTEND']
APPLY_PUT_INTEREST_ON_PRINCIPAL_TTL = app.config['APPLY_PUT_INTEREST_ON_PRINCIPAL_TTL']


bp_apply = Blueprint('apply', __name__, url_prefix='/apply')


@bp_apply.route('/put/list/')
@bp_apply.route('/put/list/<int:page>/')
@login_required
def lists_put(page=1):
    """
    投资申请列表
    """
    user_id = current_user.id

    # 判断基本信息和银行信息是否完整
    if not user_profile_is_complete(user_id):
        flash(u'请先完善基本信息', 'warning')
        return redirect(url_for('user.profile'))
    if not user_profile_is_complete(user_id):
        flash(u'请先完善银行信息', 'warning')
        return redirect(url_for('user.bank'))
        # 判断是否激活
    if current_user.status_active == int(STATUS_ACTIVE_NO):
        flash(u'请先激活当前账号', 'warning')
        return redirect(url_for('user.profile'))

    condition = [
        ApplyPut.user_id == user_id,
        ApplyPut.status_delete == int(STATUS_DEL_NO)
    ]
    # 订单状态
    status_order = request.args.get('status_order', 0, type=int)
    if status_order == int(STATUS_ORDER_COMPLETED):
        condition.append(ApplyPut.status_order == int(STATUS_ORDER_COMPLETED))
    else:
        condition.append(ApplyPut.status_order < int(STATUS_ORDER_COMPLETED))

    pagination = get_apply_put_rows(page, PER_PAGE_FRONTEND, *condition)
    return render_template('apply/put_list.html', title='apply_put_list', pagination=pagination)


@bp_apply.route('/get/list/')
@bp_apply.route('/get/list/<int:page>/')
@login_required
def lists_get(page=1):
    """
    提现申请列表
    """
    user_id = current_user.id

    # 判断基本信息和银行信息是否完整
    if not user_profile_is_complete(user_id):
        flash(u'请先完善基本信息', 'warning')
        return redirect(url_for('user.profile'))
    if not user_profile_is_complete(user_id):
        flash(u'请先完善银行信息', 'warning')
        return redirect(url_for('user.bank'))
        # 判断是否激活
    if current_user.status_active == int(STATUS_ACTIVE_NO):
        flash(u'请先激活当前账号', 'warning')
        return redirect(url_for('user.profile'))

    condition = [
        ApplyGet.user_id == user_id,
        ApplyGet.status_delete == int(STATUS_DEL_NO)
    ]
    # 订单状态
    status_order = request.args.get('status_order', 0, type=int)
    if status_order == int(STATUS_ORDER_COMPLETED):
        condition.append(ApplyGet.status_order == int(STATUS_ORDER_COMPLETED))
    else:
        condition.append(ApplyGet.status_order < int(STATUS_ORDER_COMPLETED))

    pagination = get_apply_get_rows(page, PER_PAGE_FRONTEND, *condition)
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
        # 判断是否激活
    if current_user.status_active == int(STATUS_ACTIVE_NO):
        flash(u'请先激活当前账号', 'warning')
        return redirect(url_for('user.profile'))

    # 获取团队成员三级树形结构
    team_tree = get_team_tree(current_user.id)

    # 单次投资金额范围
    APPLY_PUT_MIN_EACH = Decimal(get_conf('APPLY_PUT_MIN_EACH'))  # 最小值
    APPLY_PUT_MAX_EACH = Decimal(get_conf('APPLY_PUT_MAX_EACH'))  # 最大值
    APPLY_PUT_STEP = Decimal(get_conf('APPLY_PUT_STEP'))  # 投资金额步长（基数）

    form = ApplyPutAddForm(request.form)
    if request.method == 'POST':
        if form.validate_on_submit():
            current_time = datetime.utcnow()

            # 新增投资申请明细
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
            apply_put_id = add_apply_put(apply_put_info)

            # 扣除排单币总表数量
            scheduling_info = get_scheduling_row_by_id(user_id)

            amount = scheduling_info.amount if scheduling_info else 0

            scheduling_data = {
                'amount': amount - 1,
                'create_time': current_time,
                'update_time': current_time
            }
            edit_scheduling(user_id, scheduling_data)

            # 新增排单币明细
            scheduling_item_data = {
                'user_id': user_id,
                'type': user_id,
                'amount': 1,
                'sc_id': user_id,
                'note': u'投资申请编号：%s' % apply_put_id,
                'status_audit': STATUS_AUDIT_SUCCESS,
                'audit_time': current_time,
                'create_time': current_time,
                'update_time': current_time
            }
            add_scheduling_item(scheduling_item_data)

            if apply_put_id:
                # 加入投资申请本息回收队列
                q = RabbitDelayQueue(
                    exchange=EXCHANGE_NAME,
                    queue_name='apply_put_interest_on_principal',
                    ttl=APPLY_PUT_INTEREST_ON_PRINCIPAL_TTL
                )
                msg = {
                    'user_id': user_id,
                    'apply_put_id': apply_put_id,
                    'apply_time': current_time.strftime('%Y-%m-%d %H:%M:%S')
                }
                q.put(msg)
                q.close_conn()
                flash(u'申请成功', 'success')
            else:
                flash(u'申请失败', 'warning')
            return redirect(url_for('apply.lists_put'))
    return render_template(
        'apply/put_add.html',
        title='apply_put_add',
        form=form,
        APPLY_PUT_MIN_EACH=str(APPLY_PUT_MIN_EACH),
        APPLY_PUT_MAX_EACH=str(APPLY_PUT_MAX_EACH),
        APPLY_PUT_STEP=str(APPLY_PUT_STEP),
        team_tree=team_tree
    )


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
        # 判断是否激活
    if current_user.status_active == int(STATUS_ACTIVE_NO):
        flash(u'请先激活当前账号', 'warning')
        return redirect(url_for('user.profile'))

    # 获取团队成员三级树形结构
    team_tree = get_team_tree(current_user.id)

    # 单次提现金额范围
    APPLY_GET_MIN_EACH = Decimal(get_conf('APPLY_GET_MIN_EACH'))  # 最小值
    APPLY_GET_MAX_EACH = Decimal(get_conf('APPLY_GET_MAX_EACH'))  # 最大值
    APPLY_GET_STEP = Decimal(get_conf('APPLY_GET_STEP'))  # 投资金额步长（基数）

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
    return render_template(
        'apply/get_add.html',
        title='apply_get_add',
        form=form,
        APPLY_GET_MIN_EACH=str(APPLY_GET_MIN_EACH),
        APPLY_GET_MAX_EACH=str(APPLY_GET_MAX_EACH),
        APPLY_GET_STEP=str(APPLY_GET_STEP),
        team_tree=team_tree
    )


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
