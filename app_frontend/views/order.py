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

from flask import abort
from flask import redirect
from flask import render_template, request, flash, g
from flask import url_for
from flask_login import current_user, login_required
import flask_excel as excel

from app_common.settings import PER_PAGE_FRONTEND
from app_frontend import app
from app_frontend.models import User, UserProfile, Order
from app_frontend.api.order import get_order_rows, get_order_row, get_order_row_by_id, edit_order
from app_frontend.api.user_bank import get_user_bank_row_by_id
from app_frontend.api.order_bill import get_order_bill_lists, add_order_bill, get_order_bill_count
from app_common.maps.status_pay import *
from app_common.maps.status_rec import *
from app_common.maps.status_delete import *
from app_common.maps.status_audit import *

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
        # 更新订单付款凭证
        current_time = datetime.utcnow()
        order_data = {
            'status_pay': STATUS_PAY_SUCCESS,
            'pay_time': current_time,
            'update_time': current_time
        }
        edit_order(order_id, order_data)
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
                raise Exception(u'异常操作，不能重复操作')

            # 更新支付状态
            current_time = datetime.utcnow()
            order_data = {
                'status_pay': status_pay,
                'pay_time': current_time,
                'update_time': current_time,
            }
            result = edit_order(order_id, order_data)
            if result == 1:
                return json.dumps({'success': u'操作成功'})
            if result == 0:
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
            if order_info.apply_get_uid != current_user.id:
                raise Exception(u'异常操作，此订单无权限')
            if order_info.status_delete == int(STATUS_DEL_OK):
                raise Exception(u'异常操作，此订单已删除')
            if order_info.status_pay != int(STATUS_PAY_SUCCESS):
                raise Exception(u'异常操作，此订单未支付')
            if order_info.status_rec == status_rec:
                raise Exception(u'异常操作，不能重复操作')

            # 更新确认状态
            current_time = datetime.utcnow()
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
