#!/usr/bin/env python
# encoding: utf-8

"""
@author: zhanghe
@software: PyCharm
@file: settings.py
@time: 2017/4/30 下午9:11
"""


import json
from decimal import Decimal
from datetime import datetime

from flask import abort
from flask import redirect
from flask import render_template, request, flash, g
from flask import url_for
from flask_login import current_user, login_required

from app_backend import app
from app_backend.api.score import get_score_rows

from app_backend.forms.settings import SwitchForm, UserForm, OrderForm, ApplyPutForm, ApplyGetForm, InterestForm
from app_backend.tools.config_manage import get_conf, set_conf

from app_backend.tools.config_manage import clean_conf
from flask import Blueprint


bp_settings = Blueprint('settings', __name__, url_prefix='/settings')


@bp_settings.route('/ajax_clean/', methods=['GET', 'POST'])
@login_required
def ajax_clean():
    if request.method == 'GET' and request.is_xhr:
        result = clean_conf()
        if result:
            return json.dumps({'success': u'还原配置成功'})
        else:
            return json.dumps({'error': u'还原配置失败'})
    abort(404)


@bp_settings.route('/switch/', methods=['GET', 'POST'])
@login_required
def switch():
    """
    开关配置
    SWITCH_EXPORT = OFF         # 导出

    SWITCH_REG_ACCOUNT = ON     # 用户账号注册
    SWITCH_REG_PHONE = OFF      # 用户手机注册
    SWITCH_REG_EMAIL = OFF      # 用户邮箱注册

    SWITCH_REG_THREE_PART = OFF     # 第三方平台注册

    SWITCH_LOGIN_ACCOUNT = ON   # 用户账号登录
    SWITCH_LOGIN_PHONE = ON     # 用户手机登录
    SWITCH_LOGIN_EMAIL = ON     # 用户邮箱登录

    SWITCH_LOGIN_THREE_PART = OFF     # 第三方平台登录
    :return:
    """
    form = SwitchForm(request.form)
    if request.method == 'GET':
        load_dict = {
            'ON': True,
            'OFF': False,
            True: True,
            False: False
        }
        form.SWITCH_EXPORT.data = load_dict.get(get_conf('SWITCH_EXPORT'))

        form.SWITCH_REG_ACCOUNT.data = load_dict.get(get_conf('SWITCH_REG_ACCOUNT'))
        form.SWITCH_REG_PHONE.data = load_dict.get(get_conf('SWITCH_REG_PHONE'))
        form.SWITCH_REG_EMAIL.data = load_dict.get(get_conf('SWITCH_REG_EMAIL'))
        form.SWITCH_REG_THREE_PART.data = load_dict.get(get_conf('SWITCH_REG_THREE_PART'))

        form.SWITCH_LOGIN_ACCOUNT.data = load_dict.get(get_conf('SWITCH_LOGIN_ACCOUNT'))
        form.SWITCH_LOGIN_PHONE.data = load_dict.get(get_conf('SWITCH_LOGIN_PHONE'))
        form.SWITCH_LOGIN_EMAIL.data = load_dict.get(get_conf('SWITCH_LOGIN_EMAIL'))
        form.SWITCH_LOGIN_THREE_PART.data = load_dict.get(get_conf('SWITCH_LOGIN_THREE_PART'))

    if request.method == 'POST':
        dump_dict = {
            True: 'ON',
            False: 'OFF'
        }
        if form.validate_on_submit():
            set_conf('SWITCH_EXPORT', dump_dict.get(form.SWITCH_EXPORT.data))

            set_conf('SWITCH_REG_ACCOUNT', dump_dict.get(form.SWITCH_REG_ACCOUNT.data))
            set_conf('SWITCH_REG_PHONE', dump_dict.get(form.SWITCH_REG_PHONE.data))
            set_conf('SWITCH_REG_EMAIL', dump_dict.get(form.SWITCH_REG_EMAIL.data))
            set_conf('SWITCH_REG_THREE_PART', dump_dict.get(form.SWITCH_REG_THREE_PART.data))

            set_conf('SWITCH_LOGIN_ACCOUNT', dump_dict.get(form.SWITCH_LOGIN_ACCOUNT.data))
            set_conf('SWITCH_LOGIN_PHONE', dump_dict.get(form.SWITCH_LOGIN_PHONE.data))
            set_conf('SWITCH_LOGIN_EMAIL', dump_dict.get(form.SWITCH_LOGIN_EMAIL.data))
            set_conf('SWITCH_LOGIN_THREE_PART', dump_dict.get(form.SWITCH_LOGIN_THREE_PART.data))

            flash(u'修改成功', 'success')
        else:
            flash(u'修改失败', 'warning')
    return render_template('settings/switch.html', title='settings_switch', form=form)


@bp_settings.route('/user/', methods=['GET', 'POST'])
@login_required
def user():
    """
    会员配置
    LOCK_REG_NOT_ACTIVE_TTL = 3600*24*3     # 注册后3天内未激活
    LOCK_ACTIVE_NOT_PUT_TTL = 3600*24*3     # 激活后3天内未排单
    LOCK_ORDER_NOT_PAY_TTL = 3600*48        # 匹配后超过48小时不打款
    LOCK_PAY_NOT_REC_TTL = 3600*48          # 收款后48小时不确认
    :return:
    """
    form = UserForm(request.form)
    if request.method == 'GET':
        form.LOCK_REG_NOT_ACTIVE_TTL.data = get_conf('LOCK_REG_NOT_ACTIVE_TTL')
        form.LOCK_ACTIVE_NOT_PUT_TTL.data = get_conf('LOCK_ACTIVE_NOT_PUT_TTL')
        form.LOCK_ORDER_NOT_PAY_TTL.data = get_conf('LOCK_ORDER_NOT_PAY_TTL')
        form.LOCK_PAY_NOT_REC_TTL.data = get_conf('LOCK_PAY_NOT_REC_TTL')

    if request.method == 'POST':
        if form.validate_on_submit():
            set_conf('LOCK_REG_NOT_ACTIVE_TTL', form.LOCK_REG_NOT_ACTIVE_TTL.data)
            set_conf('LOCK_ACTIVE_NOT_PUT_TTL', form.LOCK_ACTIVE_NOT_PUT_TTL.data)
            set_conf('LOCK_ORDER_NOT_PAY_TTL', form.LOCK_ORDER_NOT_PAY_TTL.data)
            set_conf('LOCK_PAY_NOT_REC_TTL', form.LOCK_PAY_NOT_REC_TTL.data)
            flash(u'修改成功', 'success')
        else:
            flash(u'修改失败', 'warning')
    return render_template('settings/user.html', title='settings_user', form=form)


@bp_settings.route('/order/', methods=['GET', 'POST'])
@login_required
def order():
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
    :return:
    """
    form = OrderForm(request.form)
    if request.method == 'GET':
        # 订单限制
        form.ORDER_MAX_AMOUNT.data = get_conf('ORDER_MAX_AMOUNT')
        form.ORDER_MAX_COUNT.data = get_conf('ORDER_MAX_COUNT')

        # 推广奖励
        form.BONUS_DIRECT.data = Decimal(get_conf('BONUS_DIRECT'))

        form.BONUS_LEVEL_FIRST.data = Decimal(get_conf('BONUS_LEVEL_FIRST'))
        form.BONUS_LEVEL_SECOND.data = Decimal(get_conf('BONUS_LEVEL_SECOND'))
        form.BONUS_LEVEL_THIRD.data = Decimal(get_conf('BONUS_LEVEL_THIRD'))

    if request.method == 'POST':
        if form.validate_on_submit():
            # 订单限制
            set_conf('ORDER_MAX_AMOUNT', form.ORDER_MAX_AMOUNT.data)
            set_conf('ORDER_MAX_COUNT', form.ORDER_MAX_COUNT.data)

            # 推广奖励
            set_conf('BONUS_DIRECT', form.BONUS_DIRECT.data)

            set_conf('BONUS_LEVEL_FIRST', form.BONUS_LEVEL_FIRST.data)
            set_conf('BONUS_LEVEL_SECOND', form.BONUS_LEVEL_SECOND.data)
            set_conf('BONUS_LEVEL_THIRD', form.BONUS_LEVEL_THIRD.data)

            flash(u'修改成功', 'success')
        else:
            flash(u'修改失败', 'warning')
    return render_template('settings/order.html', title='settings_order', form=form)


@bp_settings.route('/apply_put/', methods=['GET', 'POST'])
@login_required
def apply_put():
    """
    投资申请配置

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
    :return:
    """
    form = ApplyPutForm(request.form)
    if request.method == 'GET':
        # 单次投资金额范围
        form.APPLY_PUT_MIN_EACH.data = get_conf('APPLY_PUT_MIN_EACH')
        form.APPLY_PUT_MAX_EACH.data = get_conf('APPLY_PUT_MAX_EACH')
        form.APPLY_PUT_STEP.data = get_conf('APPLY_PUT_STEP')

        # 单个用户投资限制
        form.APPLY_PUT_USER_MAX_AMOUNT.data = get_conf('APPLY_PUT_USER_MAX_AMOUNT')
        form.APPLY_PUT_USER_MAX_COUNT.data = get_conf('APPLY_PUT_USER_MAX_COUNT')

        # 每日投资限额
        form.APPLY_PUT_MAX_AMOUNT_DAILY.data = get_conf('APPLY_PUT_MAX_AMOUNT_DAILY')
        form.APPLY_PUT_MAX_COUNT_DAILY.data = get_conf('APPLY_PUT_MAX_COUNT_DAILY')

        # 每月投资限额
        form.APPLY_PUT_MAX_AMOUNT_MONTHLY.data = get_conf('APPLY_PUT_MAX_AMOUNT_MONTHLY')
        form.APPLY_PUT_MAX_COUNT_MONTHLY.data = get_conf('APPLY_PUT_MAX_COUNT_MONTHLY')

        # 投资时间配置
        form.APPLY_PUT_TIME_START.data = get_conf('APPLY_PUT_TIME_START')
        form.APPLY_PUT_TIME_END.data = get_conf('APPLY_PUT_TIME_END')

    if request.method == 'POST':
        if form.validate_on_submit():
            # 单次投资金额范围
            set_conf('APPLY_PUT_MIN_EACH', form.APPLY_PUT_MIN_EACH.data)
            set_conf('APPLY_PUT_MAX_EACH', form.APPLY_PUT_MAX_EACH.data)
            set_conf('APPLY_PUT_STEP', form.APPLY_PUT_STEP.data)

            # 单个用户投资限制
            set_conf('APPLY_PUT_USER_MAX_AMOUNT', form.APPLY_PUT_USER_MAX_AMOUNT.data)
            set_conf('APPLY_PUT_USER_MAX_COUNT', form.APPLY_PUT_USER_MAX_COUNT.data)

            # 每日投资限额
            set_conf('APPLY_PUT_MAX_AMOUNT_DAILY', form.APPLY_PUT_MAX_AMOUNT_DAILY.data)
            set_conf('APPLY_PUT_MAX_COUNT_DAILY', form.APPLY_PUT_MAX_COUNT_DAILY.data)

            # 每月投资限额
            set_conf('APPLY_PUT_MAX_AMOUNT_MONTHLY', form.APPLY_PUT_MAX_AMOUNT_MONTHLY.data)
            set_conf('APPLY_PUT_MAX_COUNT_MONTHLY', form.APPLY_PUT_MAX_COUNT_MONTHLY.data)

            # 投资时间配置
            set_conf('APPLY_PUT_TIME_START', form.APPLY_PUT_TIME_START.data)
            set_conf('APPLY_PUT_TIME_END', form.APPLY_PUT_TIME_END.data)

            flash(u'修改成功', 'success')
        else:
            flash(u'修改失败', 'warning')
    return render_template('settings/apply_put.html', title='apply_put', form=form)


@bp_settings.route('/apply_get/', methods=['GET', 'POST'])
@login_required
def apply_get():
    """
    提现申请配置

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

    :return:
    """
    form = ApplyGetForm(request.form)
    if request.method == 'GET':
        # 单次提现金额范围
        form.APPLY_GET_MIN_EACH.data = get_conf('APPLY_GET_MIN_EACH')
        form.APPLY_GET_MAX_EACH.data = get_conf('APPLY_GET_MAX_EACH')
        form.APPLY_GET_STEP.data = get_conf('APPLY_GET_STEP')

        # 单个用户提现限制
        form.APPLY_GET_USER_MAX_AMOUNT.data = get_conf('APPLY_GET_USER_MAX_AMOUNT')
        form.APPLY_GET_USER_MAX_COUNT.data = get_conf('APPLY_GET_USER_MAX_COUNT')

        # 每日提现限额
        form.APPLY_GET_MAX_AMOUNT_DAILY.data = get_conf('APPLY_GET_MAX_AMOUNT_DAILY')
        form.APPLY_GET_MAX_COUNT_DAILY.data = get_conf('APPLY_GET_MAX_COUNT_DAILY')

        # 每月提现限额
        form.APPLY_GET_MAX_AMOUNT_MONTHLY.data = get_conf('APPLY_GET_MAX_AMOUNT_MONTHLY')
        form.APPLY_GET_MAX_COUNT_MONTHLY.data = get_conf('APPLY_GET_MAX_COUNT_MONTHLY')

        # 提现时间配置
        form.APPLY_GET_TIME_START.data = get_conf('APPLY_GET_TIME_START')
        form.APPLY_GET_TIME_END.data = get_conf('APPLY_GET_TIME_END')

    if request.method == 'POST':
        if form.validate_on_submit():
            # 单次提现金额范围
            set_conf('APPLY_GET_MIN_EACH', form.APPLY_GET_MIN_EACH.data)
            set_conf('APPLY_GET_MAX_EACH', form.APPLY_GET_MAX_EACH.data)
            set_conf('APPLY_GET_STEP', form.APPLY_GET_STEP.data)

            # 单个用户提现限制
            set_conf('APPLY_GET_USER_MAX_AMOUNT', form.APPLY_GET_USER_MAX_AMOUNT.data)
            set_conf('APPLY_GET_USER_MAX_COUNT', form.APPLY_GET_USER_MAX_COUNT.data)

            # 每日提现限额
            set_conf('APPLY_GET_MAX_AMOUNT_DAILY', form.APPLY_GET_MAX_AMOUNT_DAILY.data)
            set_conf('APPLY_GET_MAX_COUNT_DAILY', form.APPLY_GET_MAX_COUNT_DAILY.data)

            # 每月提现限额
            set_conf('APPLY_GET_MAX_AMOUNT_MONTHLY', form.APPLY_GET_MAX_AMOUNT_MONTHLY.data)
            set_conf('APPLY_GET_MAX_COUNT_MONTHLY', form.APPLY_GET_MAX_COUNT_MONTHLY.data)

            # 提现时间配置
            set_conf('APPLY_GET_TIME_START', form.APPLY_GET_TIME_START.data)
            set_conf('APPLY_GET_TIME_END', form.APPLY_GET_TIME_END.data)

            flash(u'修改成功', 'success')
        else:
            flash(u'修改失败', 'warning')
    return render_template('settings/apply_get.html', title='apply_get', form=form)


@bp_settings.route('/wallet/', methods=['GET', 'POST'])
@login_required
def wallet():
    """
    钱包配置
    :return:
    """
    return render_template('settings/wallet.html', title='settings_wallet')


@bp_settings.route('/score/', methods=['GET', 'POST'])
@login_required
def score():
    """
    积分配置
    :return:
    """
    return render_template('settings/score.html', title='settings_score')


@bp_settings.route('/bonus/', methods=['GET', 'POST'])
@login_required
def bonus():
    """
    奖金配置
    :return:
    """
    return render_template('settings/bonus.html', title='settings_bonus')


@bp_settings.route('/interest/', methods=['GET', 'POST'])
@login_required
def interest():
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
    :return:
    """
    form = InterestForm(request.form)
    if request.method == 'GET':
        # 利息配置
        form.INTEREST_PUT.data = Decimal(get_conf('INTEREST_PUT'))

        # 支付奖惩比例
        form.INTEREST_PAY_AHEAD.data = Decimal(get_conf('INTEREST_PAY_AHEAD'))
        form.INTEREST_PAY_DELAY.data = Decimal(get_conf('INTEREST_PAY_DELAY'))

        # 支付时间差
        form.DIFF_TIME_PAY_AHEAD.data = get_conf('DIFF_TIME_PAY_AHEAD')
        form.DIFF_TIME_PAY_DELAY.data = get_conf('DIFF_TIME_PAY_DELAY')

        # 确认奖惩比例
        form.INTEREST_REC_AHEAD.data = Decimal(get_conf('INTEREST_REC_AHEAD'))
        form.INTEREST_REC_DELAY.data = Decimal(get_conf('INTEREST_REC_DELAY'))

        # 确认时间差
        form.DIFF_TIME_REC_AHEAD.data = get_conf('DIFF_TIME_REC_AHEAD')
        form.DIFF_TIME_REC_DELAY.data = get_conf('DIFF_TIME_REC_DELAY')

    if request.method == 'POST':
        if form.validate_on_submit():
            # 利息配置
            set_conf('INTEREST_PUT', form.INTEREST_PUT.data)

            # 支付奖惩比例
            set_conf('INTEREST_PAY_AHEAD', form.INTEREST_PAY_AHEAD.data)
            set_conf('INTEREST_PAY_DELAY', form.INTEREST_PAY_DELAY.data)

            # 支付时间差
            set_conf('DIFF_TIME_PAY_AHEAD', form.DIFF_TIME_PAY_AHEAD.data)
            set_conf('DIFF_TIME_PAY_DELAY', form.DIFF_TIME_PAY_DELAY.data)

            # 确认奖惩比例
            set_conf('INTEREST_REC_AHEAD', form.INTEREST_REC_AHEAD.data)
            set_conf('INTEREST_REC_DELAY', form.INTEREST_REC_DELAY.data)

            # 确认时间差
            set_conf('DIFF_TIME_REC_AHEAD', form.DIFF_TIME_REC_AHEAD.data)
            set_conf('DIFF_TIME_REC_DELAY', form.DIFF_TIME_REC_DELAY.data)

            flash(u'修改成功', 'success')
        else:
            flash(u'修改失败', 'warning')
    return render_template('settings/interest.html', title='settings_interest', form=form)
