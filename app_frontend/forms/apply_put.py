#!/usr/bin/env python
# encoding: utf-8

"""
@author: zhanghe
@software: PyCharm
@file: apply_put.py
@time: 2017/4/13 下午9:31
"""


from flask_wtf import FlaskForm as Form
from wtforms import StringField, PasswordField, BooleanField, DateField, DateTimeField, DecimalField, IntegerField
from wtforms.validators import DataRequired, Length, NumberRange, EqualTo, Email, ValidationError, IPAddress
from app_frontend.api.user_auth import get_user_auth_row
from app_frontend.forms import SelectBS
from app_api.maps import type_apply_list


class ApplyPutAddForm(Form):
    """
    投资申请添加表单
    """
    money_apply = IntegerField('Money Apply', validators=[
        DataRequired(message=u'金额必须为整数'),
        NumberRange(min=0, message=u'金额必须为整数')
    ])


class ApplyPutEditForm(Form):
    """
    投资申请编辑表单
    """
    apply_get_id = StringField('Apply Get Id')
    money_apply = StringField('Money Apply')
    status_apply = StringField('Status Apply')
    status_order = StringField('Status Order')
    status_delete = StringField('Status Delete')
    create_time = DateTimeField('Create Time')
    update_time = DateTimeField('Update Time')
