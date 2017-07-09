#!/usr/bin/env python
# encoding: utf-8

"""
@author: zhanghe
@software: PyCharm
@file: apply_get.py
@time: 2017/4/13 下午9:31
"""


from datetime import datetime

from decimal import Decimal
from flask_login import current_user
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, DateField, DateTimeField, DecimalField, IntegerField
from wtforms.validators import DataRequired, Length, NumberRange, EqualTo, Email, ValidationError, IPAddress

from app_frontend import app
from app_frontend.api.apply_get import get_current_month_get_amount, get_current_day_get_amount, \
    get_get_processing_amount, get_get_processing_count
from app_frontend.api.user_auth import get_user_auth_row
from app_frontend.api.wallet import get_wallet_row_by_id
from app_frontend.api.bit_coin import get_bit_coin_row_by_id
from app_frontend.forms import SelectBS, RadioInlineBS
from app_common.maps import type_apply_list, type_pay_list, type_withdraw_list
from app_common.maps.type_withdraw import *
from app_frontend.tools.config_manage import get_conf


class ApplyGetMoneyValidate(object):
    """
    提现申请金额校验
    """
    def __init__(self, message=None):
        self.message = message

    def __call__(self, form, field):
        # 提现时间配置
        APPLY_GET_TIME_START = get_conf('APPLY_GET_TIME_START')  # 每天提现申请开始时间
        APPLY_GET_TIME_END = get_conf('APPLY_GET_TIME_END')  # 每天提现申请结束时间
        current_time = datetime.now().strftime('%H:%M:%S')
        if current_time < APPLY_GET_TIME_START or current_time > APPLY_GET_TIME_END:
            raise ValidationError(u'为了您的资金安全，请在%s~%s时间段提现' % (APPLY_GET_TIME_START, APPLY_GET_TIME_END))

        # # 当天次数限制（一天只能提现一次）
        # if not app.config.get('TEST') and get_current_day_get_amount(user_id=current_user.id) > 0:
        #     raise ValidationError(u'超出当天提现次数限制')

        # 单次提现金额范围
        APPLY_GET_MIN_EACH = Decimal(get_conf('APPLY_GET_MIN_EACH'))  # 最小值
        APPLY_GET_MAX_EACH = Decimal(get_conf('APPLY_GET_MAX_EACH'))  # 最大值
        APPLY_GET_STEP = Decimal(get_conf('APPLY_GET_STEP'))  # 提现金额步长（基数）

        if field.data < APPLY_GET_MIN_EACH:
            raise ValidationError(u'提现金额最小为%s' % APPLY_GET_MIN_EACH)
        if field.data > APPLY_GET_MAX_EACH:
            raise ValidationError(u'提现金额最大为%s' % APPLY_GET_MAX_EACH)
        if (field.data / APPLY_GET_STEP) * APPLY_GET_STEP != field.data:
            raise ValidationError(u'金额必须为%s的倍数' % APPLY_GET_STEP)

        # 单个用户提现限制
        # 金额限制
        get_processing_amount = get_get_processing_amount(user_id=current_user.id)
        # 单个用户提现最大交易中金额
        APPLY_GET_USER_MAX_AMOUNT = Decimal(get_conf('APPLY_GET_USER_MAX_AMOUNT'))
        if field.data + get_processing_amount >= APPLY_GET_USER_MAX_AMOUNT:
            raise ValidationError(u'超出提现处理中金额限制')

        # 单数限制（处理中的申请单数）
        # 单个用户提现最大交易中单数(0 表示不限制)
        APPLY_GET_USER_MAX_COUNT = Decimal(get_conf('APPLY_GET_USER_MAX_COUNT'))
        if APPLY_GET_USER_MAX_COUNT > 0:
            get_processing_count = get_get_processing_count(user_id=current_user.id)
            if get_processing_count >= APPLY_GET_USER_MAX_COUNT:
                raise ValidationError(u'超出提现处理中数量限制')

        # 每日提现限制
        current_day_get_amount = get_current_day_get_amount()
        if current_day_get_amount > Decimal(get_conf('APPLY_GET_MAX_AMOUNT_DAILY')):
            raise ValidationError(u'超出当天提现最大金额限制')

        # 每月提现限制
        current_month_get_amount = get_current_month_get_amount()
        if current_month_get_amount > Decimal(get_conf('APPLY_GET_MAX_AMOUNT_MONTHLY')):
            raise ValidationError(u'超出当月提现最大金额限制')
        
        # 钱包余额不够
        if form.type_withdraw.data == TYPE_WITHDRAW_WALLET:
            wallet_info = get_wallet_row_by_id(current_user.id)
            if not wallet_info or wallet_info.amount_current < field.data:
                raise ValidationError(u'钱包余额不够')
        # 数字货币余额不够
        if form.type_withdraw.data == TYPE_WITHDRAW_BIT_COIN:
            bit_coin_info = get_bit_coin_row_by_id(current_user.id)
            if not bit_coin_info or bit_coin_info.amount < field.data:
                raise ValidationError(u'数字货币余额不够')


class ApplyGetAddForm(FlaskForm):
    """
    提现申请添加表单
    """
    # type_pay_list.pop(0)
    type_pay = RadioInlineBS(u'收款方式',
                             choices=type_pay_list,
                             validators=[DataRequired(message=u'收款方式不能为空')]
                             )

    type_withdraw_list.pop(0)
    type_withdraw = RadioInlineBS(u'提现类型',
                                  choices=type_withdraw_list,
                                  validators=[DataRequired(message=u'提现类型不能为空')]
                                  )
    money_apply = IntegerField(u'申请金额', validators=[
        DataRequired(message=u'金额必须为整数'),
        NumberRange(min=100, message=u'金额必须为100的倍数'),
        ApplyGetMoneyValidate()
    ])


class ApplyGetEditForm(FlaskForm):
    """
    提现申请编辑表单
    """
    apply_put_id = StringField('Apply Put Id')
    money_apply = StringField('Money Apply')
    status_apply = StringField('Status Apply')
    status_order = StringField('Status Order')
    status_delete = StringField('Status Delete')
    create_time = DateTimeField('Create Time')
    update_time = DateTimeField('Update Time')
