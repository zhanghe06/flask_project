#!/usr/bin/env python
# encoding: utf-8

"""
@author: zhanghe
@software: PyCharm
@file: order.py
@time: 2017/3/30 下午6:05
"""


import json
from datetime import datetime
import traceback
from decimal import Decimal

from flask import abort
from flask import redirect
from flask import render_template, request, flash, g
from flask import url_for
from flask_login import current_user, login_required
import flask_excel as excel

from app_common.maps.status_active import STATUS_ACTIVE_NO
from app_frontend import app
from app_frontend.api.user_profile import get_p_uid_list, user_profile_is_complete
from app_frontend.models import User, UserProfile, Order
from app_frontend.api.order import get_order_rows, get_order_row, get_order_row_by_id, edit_order
from app_frontend.api.user_bank import get_user_bank_row_by_id, user_bank_is_complete
from app_frontend.api.order_bill import get_order_bill_lists, add_order_bill, get_order_bill_count
from app_frontend.api.wallet_item import add_wallet_item
from app_frontend.api.wallet import get_wallet_row_by_id, add_wallet, edit_wallet
from app_frontend.api.bonus_item import add_bonus_item
from app_frontend.api.bonus import get_bonus_row_by_id, add_bonus, edit_bonus
from app_frontend.api.user_config import get_user_config_row_by_id
from app_common.maps.status_pay import *
from app_common.maps.status_rec import *
from app_common.maps.status_delete import *
from app_common.maps.status_audit import *
from app_common.maps.type_payment import *
from app_frontend.database import db

from flask import Blueprint

from app_frontend.tools.config_manage import get_conf
from decimal import Decimal

PER_PAGE_FRONTEND = app.config['PER_PAGE_FRONTEND']

INTEREST_PUT = Decimal(get_conf('INTEREST_PUT'))               # 投资利息（日息）

INTEREST_PAY_AHEAD = Decimal(get_conf('INTEREST_PAY_AHEAD'))   # 提前支付奖金比例
INTEREST_PAY_DELAY = Decimal(get_conf('INTEREST_PAY_DELAY'))   # 延迟支付罚金比例

DIFF_TIME_PAY_AHEAD = int(get_conf('DIFF_TIME_PAY_AHEAD'))   # 提前支付奖金时间差
DIFF_TIME_PAY_DELAY = int(get_conf('DIFF_TIME_PAY_DELAY'))   # 延迟支付罚金时间差

INTEREST_REC_AHEAD = Decimal(get_conf('INTEREST_REC_AHEAD'))   # 提前确认奖金比例
INTEREST_REC_DELAY = Decimal(get_conf('INTEREST_REC_DELAY'))   # 延迟确认罚金比例

DIFF_TIME_REC_AHEAD = int(get_conf('DIFF_TIME_REC_AHEAD'))   # 提前支付奖金时间差
DIFF_TIME_REC_DELAY = int(get_conf('DIFF_TIME_REC_DELAY'))   # 延迟支付罚金时间差

BONUS_DIRECT = Decimal(get_conf('BONUS_DIRECT'))     # 直接推荐奖励

BONUS_LEVEL_FIRST = Decimal(get_conf('BONUS_LEVEL_FIRST'))     # 一级推荐奖励
BONUS_LEVEL_SECOND = Decimal(get_conf('BONUS_LEVEL_SECOND'))     # 二级推荐奖励
BONUS_LEVEL_THIRD = Decimal(get_conf('BONUS_LEVEL_THIRD'))     # 三级推荐奖励
BONUS_LEVEL = [BONUS_LEVEL_FIRST, BONUS_LEVEL_SECOND, BONUS_LEVEL_THIRD]     # 奖金等级

bp_order = Blueprint('order', __name__, url_prefix='/order')


@bp_order.route('/put/list/')
@bp_order.route('/put/list/<int:page>/')
@login_required
def lists_put(page=1):
    """
    投资订单列表
    """
    user_id = current_user.id

    # 判断基本信息和银行信息是否完整
    if not user_profile_is_complete(user_id):
        flash(u'请先完善基本信息', 'warning')
        return redirect(url_for('user.profile'))
    if not user_bank_is_complete(user_id):
        flash(u'请先完善银行信息', 'warning')
        return redirect(url_for('user.bank'))
        # 判断是否激活
    if current_user.status_active == int(STATUS_ACTIVE_NO):
        flash(u'请先激活当前账号', 'warning')
        return redirect(url_for('user.profile'))

    # 支付状态（默认未处理）
    status_pay = request.args.get('status_pay', 0, type=int)

    search_condition_order = [
        Order.apply_put_uid == user_id,
        Order.status_delete == STATUS_DEL_NO,  # 默认未删除
    ]

    if status_pay in STATUS_PAY_DICT:
        search_condition_order.append(Order.status_pay == status_pay)

    try:
        pagination = Order.query. \
            filter(*search_condition_order). \
            outerjoin(UserProfile, Order.apply_get_uid == UserProfile.user_id). \
            add_entity(UserProfile). \
            order_by(Order.id.desc()). \
            paginate(page, PER_PAGE_FRONTEND, False)
        db.session.commit()
        return render_template('order/put_list.html', title='order_put_list', pagination=pagination)
    except Exception as e:
        db.session.rollback()
        flash(e.message, category='warning')
        return redirect(url_for('index'))


@bp_order.route('/get/list/')
@bp_order.route('/get/list/<int:page>/')
@login_required
def lists_get(page=1):
    """
    提现订单列表
    """
    user_id = current_user.id

    # 判断基本信息和银行信息是否完整
    if not user_profile_is_complete(user_id):
        flash(u'请先完善基本信息', 'warning')
        return redirect(url_for('user.profile'))
    if not user_bank_is_complete(user_id):
        flash(u'请先完善银行信息', 'warning')
        return redirect(url_for('user.bank'))
        # 判断是否激活
    if current_user.status_active == int(STATUS_ACTIVE_NO):
        flash(u'请先激活当前账号', 'warning')
        return redirect(url_for('user.profile'))

    # 收款状态（默认未处理）
    status_rec = request.args.get('status_rec', 0, type=int)

    search_condition_order = [
        Order.apply_get_uid == user_id,
        Order.status_delete == STATUS_DEL_NO,  # 默认未删除
    ]

    if status_rec in STATUS_REC_DICT:
        search_condition_order.append(Order.status_rec == status_rec)

    try:
        pagination = Order.query. \
            filter(*search_condition_order). \
            outerjoin(UserProfile, Order.apply_put_uid == UserProfile.user_id). \
            add_entity(UserProfile). \
            order_by(Order.id.desc()). \
            paginate(page, PER_PAGE_FRONTEND, False)
        db.session.commit()
        return render_template('order/get_list.html', title='order_get_list', pagination=pagination)
    except Exception as e:
        db.session.rollback()
        flash(e.message, category='warning')
        return redirect(url_for('index'))


@bp_order.route('/put/info/<int:order_id>/', methods=['GET', 'POST'])
@login_required
def info_put(order_id):
    """
    投资订单详情
    """
    uid = current_user.id
    # 获取投资订单详情
    condition = {
        'id': order_id,
        'apply_put_uid': uid
    }
    order_info = get_order_row(**condition)
    if not order_info:
        flash(u'订单查询失败', 'warning')
        return redirect(url_for('order.lists_put'))
    if order_info.status_delete == int(STATUS_DEL_OK):
        flash(u'订单已被删除', 'warning')
        return redirect(url_for('order.lists_put'))

    # 订单信息
    order_info = get_order_row_by_id(order_id)
    # 收款信息
    bank_info = get_user_bank_row_by_id(order_info.apply_get_uid)
    # 订单凭证
    order_bill_lists_condition = {
        'order_id': order_id,
        'status_delete': STATUS_DEL_NO
    }
    order_bill_lists = get_order_bill_lists(**order_bill_lists_condition)

    return render_template(
        'order/put_info.html',
        title='order_put_info',
        order_info=order_info,
        bank_info=bank_info,
        order_bill_lists=order_bill_lists
    )


@bp_order.route('/get/info/<int:order_id>/', methods=['GET', 'POST'])
@login_required
def info_get(order_id):
    """
    提现订单详情
    """
    uid = current_user.id
    # 获取提现订单详情
    condition = {
        'id': order_id,
        'apply_get_uid': uid
    }
    order_info = get_order_row(**condition)
    if not order_info:
        flash(u'订单查询失败', 'warning')
        return redirect(url_for('order.lists_get'))
    if order_info.status_delete == int(STATUS_DEL_OK):
        flash(u'订单已被删除', 'warning')
        return redirect(url_for('order.lists_get'))

    # 订单信息
    order_info = get_order_row_by_id(order_id)
    # 收款信息
    bank_info = get_user_bank_row_by_id(order_info.apply_get_uid)
    # 订单凭证
    order_bill_lists_condition = {
        'order_id': order_id,
        'status_delete': STATUS_DEL_NO
    }
    order_bill_lists = get_order_bill_lists(**order_bill_lists_condition)

    return render_template(
        'order/get_info.html',
        title='order_get_info',
        order_info=order_info,
        bank_info=bank_info,
        order_bill_lists=order_bill_lists
    )


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
    if not order_info:
        flash(u'订单查询失败', 'warning')
        return redirect(url_for('order.lists_put'))
    if order_info.status_delete == int(STATUS_DEL_OK):
        flash(u'订单已被删除', 'warning')
        return redirect(url_for('order.lists_put'))
    if request.method == 'POST':
        pass

    # 订单信息
    order_info = get_order_row_by_id(order_id)
    # 收款信息
    bank_info = get_user_bank_row_by_id(order_info.apply_get_uid)
    # 订单凭证
    order_bill_lists_condition = {
        'order_id': order_id,
        'status_delete': STATUS_DEL_NO
    }
    order_bill_lists = get_order_bill_lists(**order_bill_lists_condition)

    return render_template(
        'order/pay.html',
        title='order_pay',
        order_info=order_info,
        bank_info=bank_info,
        order_bill_lists=order_bill_lists
    )


@bp_order.route('/pay_bill_uploads/<int:order_id>/', methods=['GET', 'POST'])
@login_required
def pay_bill_uploads(order_id):
    """
    支付凭证上传 多文件上传
    :param order_id:
    :return:
    """
    from app_common.tools.file import get_file_size
    from app_common.tools.file import create_file_name
    from app_common.tools.file import validate
    if request.method == 'POST':
        # 判断权限
        uid = current_user.id
        # 获取投资订单详情
        condition = {
            'id': order_id,
            'apply_put_uid': uid
        }
        order_info = get_order_row(**condition)
        if not order_info:
            flash(u'订单查询失败', 'warning')
            return redirect(url_for('order.lists_put'))
        if order_info.status_delete == int(STATUS_DEL_OK):
            flash(u'订单已被删除', 'warning')
            return redirect(url_for('order.lists_put'))

        files = []
        file_list = request.files.getlist('files[]')
        for file_item in file_list:
            file_name = create_file_name(file_item)
            file_info = {
                'name': file_name,
                'content_type': file_item.content_type,
                'size': get_file_size(file_item),
                'delete_type': 'POST'
            }
            try:
                # 校验上传文件
                validate(file_item)
                file_info['url'] = url_for('static', filename='uploads/%s' % file_name)
                file_info['thumbnail_url'] = url_for('static', filename='uploads/%s' % file_name)
                file_info['delete_url'] = url_for('file.delete')
                # 保存上传文件
                file_item.save(app.config['UPLOAD_FOLDER'] + file_name)
                # 添加订单付款凭证
                current_time = datetime.utcnow()
                order_bill_data = {
                    'order_id': order_id,
                    'bill_img': file_name,
                    'status_audit': STATUS_AUDIT_SUCCESS,
                    'audit_time': current_time,
                    'create_time': current_time,
                    'update_time': current_time,
                }
                add_order_bill(order_bill_data)
            except Exception as e:
                file_info['error'] = e.message

            files.append(file_info)
        # # 更新订单付款凭证
        # current_time = datetime.utcnow()
        # order_data = {
        #     'status_pay': STATUS_PAY_SUCCESS,
        #     'pay_time': current_time,
        #     'update_time': current_time
        # }
        # edit_order(order_id, order_data)
        return json.dumps({'files': files})
        # return redirect(url_for('order.info_put', order_id=order_id))


@bp_order.route('/ajax_pay/', methods=['GET', 'POST'])
@login_required
def ajax_pay():
    """
    订单支付
    :return:
    """
    if request.method == 'POST' and request.is_xhr:
        form = request.form
        order_id = form.get('order_id', 0, type=int)
        status_pay = form.get('status_pay', 0, type=int)

        user_id = current_user.id

        try:
            # 参数校验
            if not order_id:
                raise Exception(u'参数错误，操作失败')
            if status_pay not in STATUS_PAY_DICT:
                raise Exception(u'参数错误，操作失败')

            # 检查付款凭证
            order_bill_condition = {
                'order_id': order_id,
                'status_delete': STATUS_DEL_NO
            }
            order_bill_count = get_order_bill_count(**order_bill_condition)
            if order_bill_count == 0:
                raise Exception(u'请先上传付款凭证')

            # 订单异常处理
            order_info = get_order_row_by_id(order_id)
            if not order_info:
                raise Exception(u'异常操作，此订单不存在')
            if order_info.apply_put_uid != current_user.id:
                raise Exception(u'异常操作，此订单无权限')
            if order_info.status_delete == int(STATUS_DEL_OK):
                raise Exception(u'异常操作，此订单已删除')
            if order_info.status_pay == status_pay:
                raise Exception(u'异常操作，此订单已支付')

            # 订单创建时间 与订单支付时间比较
            order_time = order_info.create_time
            current_time = datetime.utcnow()
            diff_time = (current_time - order_time).seconds
            # 判断是否满足奖励规则
            if diff_time < DIFF_TIME_PAY_AHEAD:
                interest = order_info.money * Decimal(INTEREST_PAY_AHEAD)
                # 添加奖励明细
                wallet_item_data = {
                    'user_id': user_id,
                    'type': TYPE_PAYMENT_INCOME,
                    'sc_id': order_id,
                    'amount': interest,
                    'status_audit': STATUS_AUDIT_SUCCESS,
                    'audit_time': current_time,
                    'create_time': current_time,
                    'update_time': current_time
                }
                add_wallet_item(wallet_item_data)

                wallet_info = get_wallet_row_by_id(user_id)
                # 新增钱包记录，更新钱包余额
                if not wallet_info:
                    wallet_data = {
                        'user_id': user_id,
                        'amount_initial': 0,
                        'amount_current': interest,
                        'amount_lock': 0,
                        'create_time': current_time,
                        'update_time': current_time,
                    }
                    add_wallet(wallet_data)
                # 更新钱包余额
                else:
                    wallet_data = {
                        'user_id': user_id,
                        'amount_current': wallet_info.amount_current + interest,
                        'update_time': current_time,
                    }
                    edit_wallet(user_id, wallet_data)

            # 判断是否满足惩罚规则
            if diff_time > DIFF_TIME_PAY_DELAY:
                interest = order_info.money * INTEREST_PAY_DELAY
                # 添加惩罚明细
                wallet_item_data = {
                    'user_id': user_id,
                    'type': TYPE_PAYMENT_EXPENSE,
                    'sc_id': order_id,
                    'amount': interest,
                    'status_audit': STATUS_AUDIT_SUCCESS,
                    'audit_time': current_time,
                    'create_time': current_time,
                    'update_time': current_time
                }
                add_wallet_item(wallet_item_data)

                wallet_info = get_wallet_row_by_id(user_id)
                # 新增钱包记录，更新钱包余额
                if not wallet_info:
                    wallet_data = {
                        'user_id': user_id,
                        'amount_initial': 0,
                        'amount_current': interest,
                        'amount_lock': 0,
                        'create_time': current_time,
                        'update_time': current_time,
                    }
                    add_wallet(wallet_data)
                # 更新钱包余额
                else:
                    wallet_data = {
                        'amount_current': wallet_info.amount_current + interest,
                        'update_time': current_time,
                    }
                    edit_wallet(user_id, wallet_data)

            # 更新支付状态
            current_time = datetime.utcnow()
            order_data = {
                'status_pay': status_pay,
                'pay_time': current_time,
                'update_time': current_time,
            }
            result = edit_order(order_id, order_data)
            if result:
                return json.dumps({'success': u'操作成功'})
            else:
                return json.dumps({'error': u'操作失败'})
        except Exception as e:
            print traceback.print_exc()
            return json.dumps({'error': e.message})
    abort(404)


@bp_order.route('/ajax_rec/', methods=['GET', 'POST'])
@login_required
def ajax_rec():
    """
    订单收款
    :return:
    """
    if request.method == 'POST' and request.is_xhr:
        form = request.form
        order_id = form.get('order_id', 0, type=int)
        status_rec = form.get('status_rec', 0, type=int)

        user_id = current_user.id

        try:
            # 参数校验
            if not order_id:
                raise Exception(u'参数错误，收款确认操作失败')
            if status_rec not in STATUS_REC_DICT:
                raise Exception(u'参数错误，收款确认操作失败')

            # 订单异常处理
            order_info = get_order_row_by_id(order_id)
            if not order_info:
                raise Exception(u'异常操作，此订单不存在')
            if order_info.apply_get_uid != user_id:
                raise Exception(u'异常操作，此订单无权限')
            if order_info.status_delete == int(STATUS_DEL_OK):
                raise Exception(u'异常操作，此订单已删除')
            if order_info.status_pay != int(STATUS_PAY_SUCCESS):
                raise Exception(u'异常操作，此订单未支付')
            if order_info.status_rec == status_rec:
                raise Exception(u'异常操作，此订单已完成')

            # TODO 事务 用户订单确认
            # 订单支付时间 与订单确认时间比较
            order_pay_time = order_info.pay_time
            current_time = datetime.utcnow()
            diff_time = (current_time - order_pay_time).seconds
            # 判断是否满足奖励规则
            if diff_time < DIFF_TIME_PAY_AHEAD:
                interest = order_info.money * Decimal(INTEREST_PAY_AHEAD)
                # 添加奖励明细
                wallet_item_data = {
                    'user_id': user_id,
                    'type': TYPE_PAYMENT_INCOME,
                    'sc_id': order_id,
                    'amount': interest,
                    'status_audit': STATUS_AUDIT_SUCCESS,
                    'audit_time': current_time,
                    'create_time': current_time,
                    'update_time': current_time
                }
                add_wallet_item(wallet_item_data)

                wallet_info = get_wallet_row_by_id(user_id)
                # 新增钱包记录，更新钱包余额
                if not wallet_info:
                    wallet_data = {
                        'user_id': user_id,
                        'amount_initial': 0,
                        'amount_current': interest,
                        'amount_lock': 0,
                        'create_time': current_time,
                        'update_time': current_time,
                    }
                    add_wallet(wallet_data)
                # 更新钱包余额
                else:
                    wallet_data = {
                        'user_id': user_id,
                        'amount_current': wallet_info.amount_current + interest,
                        'update_time': current_time,
                    }
                    edit_wallet(user_id, wallet_data)

            # 判断是否满足惩罚规则
            if diff_time > DIFF_TIME_PAY_DELAY:
                interest = order_info.money * INTEREST_PAY_DELAY
                # 添加惩罚明细
                wallet_item_data = {
                    'user_id': user_id,
                    'type': TYPE_PAYMENT_EXPENSE,
                    'sc_id': order_id,
                    'amount': interest,
                    'status_audit': STATUS_AUDIT_SUCCESS,
                    'audit_time': current_time,
                    'create_time': current_time,
                    'update_time': current_time
                }
                add_wallet_item(wallet_item_data)

                wallet_info = get_wallet_row_by_id(user_id)
                # 新增钱包记录，更新钱包余额
                if not wallet_info:
                    wallet_data = {
                        'user_id': user_id,
                        'amount_initial': 0,
                        'amount_current': interest,
                        'amount_lock': 0,
                        'create_time': current_time,
                        'update_time': current_time,
                    }
                    add_wallet(wallet_data)
                # 更新钱包余额
                else:
                    wallet_data = {
                        'amount_current': wallet_info.amount_current + interest,
                        'update_time': current_time,
                    }
                    edit_wallet(user_id, wallet_data)

            # 更新确认状态
            order_data = {
                'status_rec': status_rec,
                'rec_time': current_time,
                'update_time': current_time,
            }
            result = edit_order(order_id, order_data)

            if result == 1:
                return json.dumps({'success': u'收款确认操作成功'})
            if result == 0:
                return json.dumps({'error': u'收款确认操作失败'})
        except Exception as e:
            print traceback.print_exc()
            return json.dumps({'error': e.message})
    abort(404)


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
