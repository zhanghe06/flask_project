#!/usr/bin/env python
# encoding: utf-8

"""
@author: zhanghe
@software: PyCharm
@file: apply_put.py
@time: 2017/4/13 下午9:31
"""


from decimal import Decimal
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, DateField, DateTimeField, DecimalField, IntegerField
from wtforms.validators import DataRequired, Length, NumberRange, EqualTo, Email, ValidationError, IPAddress

from flask_login import current_user
from app_frontend.api.apply_put import get_current_day_put_amount, get_current_month_put_amount, \
    get_put_processing_amount
from app_frontend.api.user_auth import get_user_auth_row
from app_frontend.forms import SelectBS, RadioInlineBS
from app_common.maps import type_apply_list, type_pay_list
from app_frontend.tools.config_manage import get_conf
from datetime import datetime


class ApplyPutMoneyValidate(object):
    """
    投资申请金额校验
    """
    def __init__(self, message=None):
        self.message = message

    def __call__(self, form, field):
        # 投资时间配置
        APPLY_PUT_TIME_START = get_conf('APPLY_PUT_TIME_START')  # 每天投资申请开始时间
        APPLY_PUT_TIME_END = get_conf('APPLY_PUT_TIME_END')  # 每天投资申请结束时间
        current_time = datetime.now().strftime('%H:%M:%S')
        if current_time < APPLY_PUT_TIME_START or current_time > APPLY_PUT_TIME_END:
            raise ValidationError(u'为了您的资金安全，请在%s~%s时间段投资' % (APPLY_PUT_TIME_START, APPLY_PUT_TIME_END))

        # 当天次数限制（一天只能投资一次）
        if get_current_day_put_amount(user_id=current_user.id) > 0:
            raise ValidationError(u'超出当天投资次数限制')

        # 单次投资金额范围
        APPLY_PUT_MIN_EACH = Decimal(get_conf('APPLY_PUT_MIN_EACH'))  # 最小值
        APPLY_PUT_MAX_EACH = Decimal(get_conf('APPLY_PUT_MAX_EACH'))  # 最大值
        APPLY_PUT_STEP = Decimal(get_conf('APPLY_PUT_STEP'))  # 投资金额步长（基数）

        if field.data < APPLY_PUT_MIN_EACH:
            raise ValidationError(u'投资金额最小为%s' % APPLY_PUT_MIN_EACH)
        if field.data > APPLY_PUT_MAX_EACH:
            raise ValidationError(u'投资金额最大为%s' % APPLY_PUT_MAX_EACH)
        if (field.data/APPLY_PUT_STEP)*APPLY_PUT_STEP != field.data:
            raise ValidationError(u'金额必须为%s的倍数' % APPLY_PUT_STEP)

        # 单个用户投资限制
        put_processing_amount = get_put_processing_amount(user_id=current_user.id)
        APPLY_PUT_USER_MAX_AMOUNT = Decimal(get_conf('APPLY_PUT_USER_MAX_AMOUNT'))  # 单个用户投资最大交易中金额
        if field.data + put_processing_amount > APPLY_PUT_USER_MAX_AMOUNT:
            raise ValidationError(u'超出投资待处理金额限制')

        # 每日投资限制
        current_day_put_amount = get_current_day_put_amount()
        if current_day_put_amount > Decimal(get_conf('APPLY_PUT_MAX_AMOUNT_DAILY')):
            raise ValidationError(u'超出当天投资最大金额限制')

        # 每月投资限制
        current_month_put_amount = get_current_month_put_amount()
        if current_month_put_amount > Decimal(get_conf('APPLY_PUT_MAX_AMOUNT_MONTHLY')):
            raise ValidationError(u'超出当月投资最大金额限制')


class ApplyPutAddForm(FlaskForm):
    """
    投资申请添加表单
    """
    type_pay_list.pop(0)
    type_pay = RadioInlineBS(u'支付方式',
                             choices=type_pay_list,
                             validators=[DataRequired(message=u'支付方式不能为空')]
                             )
    money_apply = IntegerField(u'申请金额', validators=[
        DataRequired(message=u'金额必须为整数'),
        NumberRange(min=100, message=u'金额必须为100的倍数'),
        ApplyPutMoneyValidate()
    ])


class ApplyPutEditForm(FlaskForm):
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
