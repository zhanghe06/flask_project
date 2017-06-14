#!/usr/bin/env python
# encoding: utf-8

"""
@author: zhanghe
@software: PyCharm
@file: settings.py
@time: 2017/6/4 上午11:53
"""


from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, DateField, DateTimeField, HiddenField, IntegerField, DecimalField
from wtforms.validators import DataRequired, Length, NumberRange, EqualTo, Email, ValidationError, IPAddress, AnyOf
from flask_login import current_user
from app_frontend.models import UserProfile
from app_backend.forms import SelectBS, CheckBoxBS
from app_common.maps import status_lock_list
from app_common.maps import status_active_list
from app_common.maps import area_code_list
from app_backend.api.user_auth import get_user_auth_row
from app_backend.forms import SelectAreaCode

from app_frontend.api.user_profile import get_user_profile_row
from app_frontend.forms import SelectAreaCode, CheckBoxBS


class SwitchForm(FlaskForm):
    """
    开关配置表单
    SWITCH_EXPORT = OFF         # 导出

    SWITCH_REG_ACCOUNT = ON     # 用户账号注册
    SWITCH_REG_PHONE = OFF      # 用户手机注册
    SWITCH_REG_EMAIL = OFF      # 用户邮箱注册

    SWITCH_REG_THREE_PART = OFF     # 第三方平台注册

    SWITCH_LOGIN_ACCOUNT = ON   # 用户账号登录
    SWITCH_LOGIN_PHONE = ON     # 用户手机登录
    SWITCH_LOGIN_EMAIL = ON     # 用户邮箱登录

    SWITCH_LOGIN_THREE_PART = OFF     # 第三方平台登录
    """
    SWITCH_EXPORT = CheckBoxBS(u'导出开关')

    SWITCH_REG_ACCOUNT = CheckBoxBS(u'用户账号注册')
    SWITCH_REG_PHONE = CheckBoxBS(u'用户手机注册')
    SWITCH_REG_EMAIL = CheckBoxBS(u'用户邮箱注册')
    SWITCH_REG_THREE_PART = CheckBoxBS(u'第三方平台注册')

    SWITCH_LOGIN_ACCOUNT = CheckBoxBS(u'用户账号登录')
    SWITCH_LOGIN_PHONE = CheckBoxBS(u'用户手机登录')
    SWITCH_LOGIN_EMAIL = CheckBoxBS(u'用户邮箱登录')
    SWITCH_LOGIN_THREE_PART = CheckBoxBS(u'第三方平台登录')


class UserForm(FlaskForm):
    """
    用户配置表单
    LOCK_REG_NOT_ACTIVE_TTL = 3600*24*3     # 注册后3天内未激活
    LOCK_ACTIVE_NOT_PUT_TTL = 3600*24*3     # 激活后3天内未排单
    LOCK_ORDER_NOT_PAY_TTL = 3600*48        # 匹配后超过48小时不打款
    LOCK_PAY_NOT_REC_TTL = 3600*48          # 收款后48小时不确认
    """
    LOCK_REG_NOT_ACTIVE_TTL = IntegerField(u'注册未激活时间', validators=[
        DataRequired(u'时间不能为空'),
        NumberRange(min=0, message=u'时间必须为正数')
    ])
    LOCK_ACTIVE_NOT_PUT_TTL = IntegerField(u'激活未排单时间', validators=[
        DataRequired(u'时间不能为空'),
        NumberRange(min=0, message=u'时间必须为正数')
    ])
    LOCK_ORDER_NOT_PAY_TTL = IntegerField(u'匹配未付款时间', validators=[
        DataRequired(u'时间不能为空'),
        NumberRange(min=0, message=u'时间必须为正数')
    ])
    LOCK_PAY_NOT_REC_TTL = IntegerField(u'收款未确认时间', validators=[
        DataRequired(u'时间不能为空'),
        NumberRange(min=0, message=u'时间必须为正数')
    ])


class OrderForm(FlaskForm):
    """
    订单配置
    # 订单限制
    ORDER_MAX_AMOUNT = 10000  # 订单最大金额
    ORDER_MAX_COUNT = 100  # 订单最大数量

    # 推广奖励

    BONUS_DIRECT = 0.03  # 直接推荐奖励

    BONUS_LEVEL_FIRST = 0.05        # 一级推荐奖励
    BONUS_LEVEL_SECOND = 0.05       # 二级推荐奖励
    BONUS_LEVEL_THIRD = 0.03        # 三级推荐奖励
    """
    # 订单限制
    ORDER_MAX_AMOUNT = IntegerField(u'订单最大金额', validators=[
        DataRequired(u'金额不能为空'),
        NumberRange(min=0, message=u'金额必须为正数')
    ])
    ORDER_MAX_COUNT = IntegerField(u'订单最大数量', validators=[
        DataRequired(u'数量不能为空'),
        NumberRange(min=0, message=u'数量必须为正数')
    ])

    # 推广奖励
    BONUS_DIRECT = DecimalField(u'直接推荐奖励', validators=[
        DataRequired(u'利息不能为空'),
        NumberRange(min=0, message=u'利息必须为正数')
    ])
    BONUS_LEVEL_FIRST = DecimalField(u'一级推荐奖励', validators=[
        DataRequired(u'利息不能为空'),
        NumberRange(min=0, max=1, message=u'奖励利息范围：0-1')
    ])
    BONUS_LEVEL_SECOND = DecimalField(u'二级推荐奖励', validators=[
        DataRequired(u'利息不能为空'),
        NumberRange(min=0, max=1, message=u'奖励利息范围：0-1')
    ])
    BONUS_LEVEL_THIRD = DecimalField(u'三级推荐奖励', validators=[
        DataRequired(u'利息不能为空'),
        NumberRange(min=0, max=1, message=u'奖励利息范围：0-1')
    ])


class ApplyPutForm(FlaskForm):
    """
    投资配置
    # 单次投资金额范围
    APPLY_PUT_MIN_EACH = 2000               # 最小值
    APPLY_PUT_MAX_EACH = 20000              # 最大值
    APPLY_PUT_STEP = 1000                   # 投资金额步长（基数）

    # 单个用户投资限制
    APPLY_PUT_USER_MAX_AMOUNT = 30000       # 单个用户投资最大交易中金额
    APPLY_PUT_USER_MAX_COUNT = 1            # 单个用户投资最大交易中单数(0 表示不限制)

    # 每日投资限制
    APPLY_PUT_MAX_AMOUNT_DAILY = 1000000    # 最大金额
    APPLY_PUT_MAX_COUNT_DAILY = 0           # 最大数量(0 表示不限制)

    # 每月投资限制
    APPLY_PUT_MAX_AMOUNT_MONTHLY = 30000000 # 最大值
    APPLY_PUT_MAX_COUNT_MONTHLY = 0         # 最大数量(0 表示不限制)

    # 投资时间配置
    APPLY_PUT_TIME_START = '00:00:00'       # 每天投资申请开始时间
    APPLY_PUT_TIME_END = '59:00:00'         # 每天投资申请结束时间

    # 分红配置
    APPLY_PUT_DAYS_BONUS = 15               # 分红计算天数
    APPLY_PUT_DAYS_LOCK = 15                # 投资锁定天数、提现冻结天数

    APPLY_PUT_INTEREST_ON_PRINCIPAL_TTL = 3600*24*15     # 投资申请后15天完成的订单执行回收本息
    """
    # 单次投资金额范围
    APPLY_PUT_MIN_EACH = IntegerField(u'单次投资最小金额', validators=[
        DataRequired(u'金额不能为空'),
        NumberRange(min=0, message=u'金额必须为正数')
    ])
    APPLY_PUT_MAX_EACH = IntegerField(u'单次投资最大金额', validators=[
        DataRequired(u'金额不能为空'),
        NumberRange(min=0, message=u'金额必须为正数')
    ])
    APPLY_PUT_STEP = IntegerField(u'投资金额调整基数', validators=[
        DataRequired(u'金额不能为空'),
        NumberRange(min=0, message=u'金额必须为正数')
    ])

    # 单个用户投资限制
    APPLY_PUT_USER_MAX_AMOUNT = IntegerField(u'单个用户投资最大金额', validators=[
        DataRequired(u'金额不能为空'),
        NumberRange(min=0, message=u'金额必须为正数')
    ])
    APPLY_PUT_USER_MAX_COUNT = IntegerField(u'单个用户投资最大单数', validators=[
        DataRequired(u'数量不能为空'),
        NumberRange(min=0, message=u'数量必须为正数')
    ])

    # 每日投资限制
    APPLY_PUT_MAX_AMOUNT_DAILY = IntegerField(u'每日投资最大金额', validators=[
        DataRequired(u'金额不能为空'),
        NumberRange(min=0, message=u'金额必须为正数')
    ])
    APPLY_PUT_MAX_COUNT_DAILY = IntegerField(u'每日投资最大单数', validators=[
        DataRequired(u'数量不能为空'),
        NumberRange(min=0, message=u'数量必须为正数')
    ])

    # 每月投资限制
    APPLY_PUT_MAX_AMOUNT_MONTHLY = IntegerField(u'每月投资最大金额', validators=[
        DataRequired(u'金额不能为空'),
        NumberRange(min=0, message=u'金额必须为正数')
    ])
    APPLY_PUT_MAX_COUNT_MONTHLY = IntegerField(u'每月投资最大单数', validators=[
        DataRequired(u'数量不能为空'),
        NumberRange(min=0, message=u'数量必须为正数')
    ])

    # 投资时间配置
    APPLY_PUT_TIME_START = StringField(u'每天投资申请开始时间', validators=[
        DataRequired(u'时间不能为空')
    ])
    APPLY_PUT_TIME_END = StringField(u'每天投资申请结束时间', validators=[
        DataRequired(u'时间不能为空')
    ])


class ApplyGetForm(FlaskForm):
    """
    提现配置

    # 单次提现金额范围
    APPLY_GET_MIN_EACH = 2000               # 最小值
    APPLY_GET_MAX_EACH = 20000              # 最大值
    APPLY_GET_STEP = 1000                   # 投资金额步长（基数）

    # 单个用户提现限制
    APPLY_GET_USER_MAX_AMOUNT = 30000       # 单个用户提现最大交易中金额
    APPLY_GET_USER_MAX_COUNT = 1            # 单个用户提现最大交易中单数(0 表示不限制)

    # 每日提现限制
    APPLY_GET_MAX_AMOUNT_DAILY = 1000000    # 最大金额
    APPLY_GET_MAX_COUNT_DAILY = 0           # 最大数量(0 表示不限制)

    # 每月提现限制
    APPLY_GET_MAX_AMOUNT_MONTHLY = 30000000 # 最大值
    APPLY_GET_MAX_COUNT_MONTHLY = 0         # 最大数量(0 表示不限制)

    # 提现时间配置
    APPLY_GET_TIME_START = '00:00:00'       # 每天提现申请开始时间
    APPLY_GET_TIME_END = '59:00:00'         # 每天提现申请结束时间
    """
    # 单次投资金额范围
    APPLY_GET_MIN_EACH = IntegerField(u'单次提现最小金额', validators=[
        DataRequired(u'金额不能为空'),
        NumberRange(min=0, message=u'金额必须为正数')
    ])
    APPLY_GET_MAX_EACH = IntegerField(u'单次提现最大金额', validators=[
        DataRequired(u'金额不能为空'),
        NumberRange(min=0, message=u'金额必须为正数')
    ])
    APPLY_GET_STEP = IntegerField(u'提现金额调整基数', validators=[
        DataRequired(u'金额不能为空'),
        NumberRange(min=0, message=u'金额必须为正数')
    ])

    # 单个用户提现限制
    APPLY_GET_USER_MAX_AMOUNT = IntegerField(u'单个用户提现最大金额', validators=[
        DataRequired(u'金额不能为空'),
        NumberRange(min=0, message=u'金额必须为正数')
    ])
    APPLY_GET_USER_MAX_COUNT = IntegerField(u'单个用户提现最大单数', validators=[
        DataRequired(u'数量不能为空'),
        NumberRange(min=0, message=u'数量必须为正数')
    ])

    # 每日提现限制
    APPLY_GET_MAX_AMOUNT_DAILY = IntegerField(u'每日提现最大金额', validators=[
        DataRequired(u'金额不能为空'),
        NumberRange(min=0, message=u'金额必须为正数')
    ])
    APPLY_GET_MAX_COUNT_DAILY = IntegerField(u'每日提现最大单数', validators=[
        DataRequired(u'数量不能为空'),
        NumberRange(min=0, message=u'数量必须为正数')
    ])

    # 每月提现限制
    APPLY_GET_MAX_AMOUNT_MONTHLY = IntegerField(u'每月提现最大金额', validators=[
        DataRequired(u'金额不能为空'),
        NumberRange(min=0, message=u'金额必须为正数')
    ])
    APPLY_GET_MAX_COUNT_MONTHLY = IntegerField(u'每月提现最大单数', validators=[
        DataRequired(u'数量不能为空'),
        NumberRange(min=0, message=u'数量必须为正数')
    ])

    # 提现时间配置
    APPLY_GET_TIME_START = StringField(u'每天提现申请开始时间', validators=[
        DataRequired(u'时间不能为空')
    ])
    APPLY_GET_TIME_END = StringField(u'每天提现申请结束时间', validators=[
        DataRequired(u'时间不能为空')
    ])


class InterestForm(FlaskForm):
    """
    利息配置

    INTEREST_PUT = 0.01  # 投资利息（日息）

    # 支付奖惩比例
    INTEREST_PAY_AHEAD = 0.02  # 提前支付奖金比例
    INTEREST_PAY_DELAY = 0.02  # 延迟支付罚金比例

    # 支付时间差
    DIFF_TIME_PAY_AHEAD = 60*60*1   # 提前支付奖金时间差
    DIFF_TIME_PAY_DELAY = 60*60*24  # 延迟支付罚金时间差

    # 确认奖惩比例
    INTEREST_REC_AHEAD = 0.02  # 提前确认奖金比例
    INTEREST_REC_DELAY = 0.02  # 延迟确认罚金比例

    # 确认时间差
    DIFF_TIME_REC_AHEAD = 60*60*1   # 提前确认奖金时间差
    DIFF_TIME_REC_DELAY = 60*60*24  # 延迟确认罚金时间差
    """
    # 利息配置
    INTEREST_PUT = DecimalField(u'投资利息（日息）', validators=[
        DataRequired(u'利息不能为空'),
        NumberRange(min=0, message=u'利息必须为正数')
    ])

    # 支付奖惩比例
    INTEREST_PAY_AHEAD = DecimalField(u'提前支付奖金比例', validators=[
        DataRequired(u'奖金比例不能为空'),
        NumberRange(min=0, message=u'奖金比例必须为正数')
    ])
    INTEREST_PAY_DELAY = DecimalField(u'延迟支付罚金比例', validators=[
        DataRequired(u'罚金比例不能为空'),
        NumberRange(min=0, message=u'罚金比例必须为正数')
    ])

    # 支付时间差
    DIFF_TIME_PAY_AHEAD = IntegerField(u'提前支付奖金时间', validators=[
        DataRequired(u'时间不能为空'),
        NumberRange(min=0, message=u'时间必须为正数')
    ])
    DIFF_TIME_PAY_DELAY = IntegerField(u'延迟支付罚金时间', validators=[
        DataRequired(u'时间不能为空'),
        NumberRange(min=0, message=u'时间必须为正数')
    ])

    # 确认奖惩比例
    INTEREST_REC_AHEAD = DecimalField(u'提前确认奖金比例', validators=[
        DataRequired(u'奖金比例不能为空'),
        NumberRange(min=0, message=u'奖金比例必须为正数')
    ])
    INTEREST_REC_DELAY = DecimalField(u'延迟确认罚金比例', validators=[
        DataRequired(u'罚金比例不能为空'),
        NumberRange(min=0, message=u'罚金比例必须为正数')
    ])

    # 确认时间差
    DIFF_TIME_REC_AHEAD = IntegerField(u'提前确认奖金时间', validators=[
        DataRequired(u'时间不能为空'),
        NumberRange(min=0, message=u'时间必须为正数')
    ])
    DIFF_TIME_REC_DELAY = IntegerField(u'延迟确认罚金时间', validators=[
        DataRequired(u'时间不能为空'),
        NumberRange(min=0, message=u'时间必须为正数')
    ])
