#!/usr/bin/env python
# encoding: utf-8

"""
@author: zhanghe
@software: PyCharm
@file: apply_get.py
@time: 2017/4/13 下午9:31
"""


from flask_wtf import FlaskForm as Form
from wtforms import StringField, PasswordField, BooleanField, DateField, DateTimeField
from wtforms.validators import DataRequired, Length, NumberRange, EqualTo, Email, ValidationError, IPAddress
from app_backend.api.user_auth import get_user_auth_row
from app_backend.forms import SelectBS
from app_common.maps import type_apply_list
from app_common.maps import status_apply_list
from app_common.maps import status_order_list
from app_common.maps import status_delete_list


class ApplyGetSearchForm(Form):
    """
    提现申请搜索表单
    """
    apply_get_id = StringField('Apply Get Id')
    user_id = StringField('User Id')
    type_apply = SelectBS('Type Apply', default='', choices=type_apply_list)
    money_apply = StringField('Type Apply')
    status_apply = SelectBS('Type Apply', default='', choices=status_apply_list)
    status_order = SelectBS('Status Order', default='', choices=status_order_list)
    status_delete = SelectBS('Status Delete', default='', choices=status_delete_list)
    min_money = StringField(u'最小金额')
    max_money = StringField(u'最大金额')
    start_time = StringField(u'开始时间')
    end_time = StringField(u'结束时间')
