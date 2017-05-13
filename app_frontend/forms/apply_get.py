#!/usr/bin/env python
# encoding: utf-8

"""
@author: zhanghe
@software: PyCharm
@file: apply_get.py
@time: 2017/4/13 下午9:31
"""


from flask_login import current_user
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, DateField, DateTimeField, DecimalField, IntegerField
from wtforms.validators import DataRequired, Length, NumberRange, EqualTo, Email, ValidationError, IPAddress
from app_frontend.api.user_auth import get_user_auth_row
from app_frontend.api.wallet import get_wallet_row_by_id
from app_frontend.api.bit_coin import get_bit_coin_row_by_id
from app_frontend.forms import SelectBS, RadioInlineBS
from app_common.maps import type_apply_list, type_pay_list, type_withdraw_list
from app_common.maps.type_withdraw import *


class ApplyGetMoneyValidate(object):
    """
    提现申请金额校验
    """
    def __init__(self, message=None):
        self.message = message

    def __call__(self, form, field):
        # 金额必须为100的倍数
        if (field.data/100)*100 != field.data:
            raise ValidationError(u'金额必须为100的倍数')
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
