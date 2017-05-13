#!/usr/bin/env python
# encoding: utf-8

"""
@author: zhanghe
@software: PyCharm
@file: order.py
@time: 2017/4/13 下午9:32
"""


from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, DateField, DateTimeField
from wtforms.validators import DataRequired, Length, NumberRange, EqualTo, Email, ValidationError, IPAddress
from app_backend.api.user_auth import get_user_auth_row
from app_backend.forms import SelectBS
from app_common.maps import status_audit_list
from app_common.maps import status_pay_list
from app_common.maps import status_rec_list


class OrderSearchForm(FlaskForm):
    """
    订单搜索表单
    """
    order_id = StringField(U'订单ID')
    apply_put_id = StringField(u'申请投资ID')      # 申请投资Id
    apply_get_id = StringField(u'申请提现ID')      # 申请提现Id
    apply_put_uid = StringField(u'申请投资用户ID')    # 申请投资用户Id
    apply_get_uid = StringField(u'申请提现用户ID')    # 申请提现用户Id
    status_audit = SelectBS('Status Audit', default='', choices=status_audit_list)      # 审核状态:0:待审核，1:审核通过，2:审核失败
    status_pay = SelectBS('Status Pay', default='', choices=status_pay_list)            # 支付状态:0:待支付，1:支付成功，2:支付失败
    status_rec = SelectBS('Status Rec', default='', choices=status_rec_list)            # 收款状态:0:待收款，1:收款成功，2:收款失败
    start_time = StringField('Start Time')
    end_time = StringField('End Time')
