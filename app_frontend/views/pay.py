#!/usr/bin/env python
# encoding: utf-8

"""
@author: zhanghe
@software: PyCharm
@file: pay.py
@time: 2017/3/18 上午12:29
"""


from datetime import datetime
from flask import redirect
from flask import render_template, request, flash, g
from flask import url_for
from flask_login import current_user, login_required

from app_frontend import app
from app_frontend.models import User
from app_frontend.api.apply_get import get_apply_get_rows, get_apply_get_row, add_apply_get
from app_frontend.api.apply_put import get_apply_put_rows, get_apply_put_row, add_apply_put
from app_frontend.api.order import get_order_row_by_id
from app_common.maps.status_order import *
from app_common.maps.type_apply import *
from app_common.maps.status_apply import *
from app_common.maps.status_delete import *
from app_frontend.forms.apply_get import ApplyGetAddForm
from app_frontend.forms.apply_put import ApplyPutAddForm
from flask import Blueprint


bp_pay = Blueprint('pay', __name__, url_prefix='/pay')


@bp_pay.route('/bit_coin/')
@login_required
def bit_coin():
    """
    支付 - 数字货币
    """
    order_id = request.args.get('order_id', 0, type=int)
    # 订单信息
    order_row = get_order_row_by_id(order_id)
    # 数字货币信息


    uid = current_user.id
    condition = {
        'user_id': uid,
        'status_order': 0,
        'status_delete': 0
    }
    # 订单状态

    if status_order in STATUS_ORDER_DICT:
        condition['status_order'] = status_order

    pagination = get_apply_put_rows(page, **condition)
    return render_template('pay/bit_coin.html', title='pay_bit_coin', pagination=pagination)



# 第三方支付（支付宝）
@app.route('/pay/alipay/')
def pay_alipay():
    return 'alipay'


# 第三方支付（微信）
@app.route('/pay/wechat/')
def pay_wechat():
    return 'wechat'
