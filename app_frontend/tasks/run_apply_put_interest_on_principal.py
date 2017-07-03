#!/usr/bin/env python
# encoding: utf-8

"""
@author: zhanghe
@software: PyCharm
@file: run_apply_put_interest_on_principal.py
@time: 2017/5/22 下午3:10
"""


import json
import time
import traceback
from datetime import datetime
from decimal import Decimal

from app_common.maps.status_audit import *
from app_common.maps.type_payment import *
from app_common.maps.status_delete import *
from app_common.maps.status_flow import *
from app_common.maps.status_rec import *
from app_common.maps.status_order import *

from app_frontend.lib.rabbit_mq import RabbitDelayQueue

from app_frontend.api.bonus import get_bonus_row_by_id, add_bonus, edit_bonus
from app_frontend.api.bonus_item import add_bonus_item
from app_frontend.api.user_config import get_user_config_row_by_id
from app_frontend.api.user_profile import get_p_uid_list
from app_frontend.api.wallet import get_wallet_row_by_id, add_wallet, edit_wallet
from app_frontend.api.wallet_item import add_wallet_item
from app_frontend.api.apply_put import get_apply_put_row_by_id

from app_frontend.api.score_charity import increase_score_charity
from app_frontend.api.score_charity_item import add_score_charity_item

from app_frontend.api.score_digital import increase_score_digital
from app_frontend.api.score_digital_item import add_score_digital_item

from app_frontend.api.score_expense import increase_score_expense
from app_frontend.api.score_expense_item import add_score_expense_item

from app_frontend.api.apply_put import is_put
from app_frontend.api.user import lock
from app_frontend.api.order import get_order_lists
from app_frontend import app
from app_frontend.tools.config_manage import get_conf
from app_frontend.tools.exception import DropException

EXCHANGE_NAME = app.config['EXCHANGE_NAME']
APPLY_PUT_INTEREST_ON_PRINCIPAL_TTL = app.config['APPLY_PUT_INTEREST_ON_PRINCIPAL_TTL']


INTEREST_PUT = Decimal(get_conf('INTEREST_PUT'))               # 投资利息（日息）

INTEREST_PAY_AHEAD = Decimal(get_conf('INTEREST_PAY_AHEAD'))   # 提前支付奖金比例
INTEREST_PAY_DELAY = Decimal(get_conf('INTEREST_PAY_DELAY'))   # 延迟支付罚金比例

DIFF_TIME_PAY_AHEAD = int(get_conf('DIFF_TIME_PAY_AHEAD'))   # 提前支付奖金时间差
DIFF_TIME_PAY_DELAY = int(get_conf('DIFF_TIME_PAY_DELAY'))   # 延迟支付罚金时间差

INTEREST_REC_AHEAD = Decimal(get_conf('INTEREST_REC_AHEAD'))   # 提前确认奖金比例
INTEREST_REC_DELAY = Decimal(get_conf('INTEREST_REC_DELAY'))   # 延迟确认罚金比例

DIFF_TIME_REC_AHEAD = int(get_conf('DIFF_TIME_REC_AHEAD'))   # 提前支付奖金时间差
DIFF_TIME_REC_DELAY = int(get_conf('DIFF_TIME_REC_DELAY'))   # 延迟支付罚金时间差

BONUS_DIRECT = Decimal(get_conf('BONUS_DIRECT'))     # 直接推荐奖励

BONUS_LEVEL_FIRST = Decimal(get_conf('BONUS_LEVEL_FIRST'))     # 一级推荐奖励
BONUS_LEVEL_SECOND = Decimal(get_conf('BONUS_LEVEL_SECOND'))     # 二级推荐奖励
BONUS_LEVEL_THIRD = Decimal(get_conf('BONUS_LEVEL_THIRD'))     # 三级推荐奖励
BONUS_LEVEL = [BONUS_LEVEL_FIRST, BONUS_LEVEL_SECOND, BONUS_LEVEL_THIRD]     # 奖金等级


def _on_score(user_id, apply_put_id, interest, current_time):
    """
    处理积分
    :param user_id:
    :param apply_put_id:
    :param interest:
    :param current_time:
    :return:
    """
    # 1、慈善积分（3%）
    score_charity_amount = interest * Decimal('0.03')
    app.logger.info('score_charity_amount: +%s' % score_charity_amount)
    # 插入积分明细
    score_charity_item_data = {
        'user_id': user_id,
        'type': TYPE_PAYMENT_INCOME,
        'amount': score_charity_amount,
        'sc_id': apply_put_id,
        'note': '来自排单收益',
        'status_audit': STATUS_AUDIT_SUCCESS,
        'audit_time': current_time,
        'create_time': current_time,
        'update_time': current_time
    }
    add_score_charity_item(score_charity_item_data)
    # 更新积分总表
    current_score_charity_amount = increase_score_charity(user_id, score_charity_amount)
    app.logger.info('current_score_charity_amount: %s' % current_score_charity_amount)

    # 2、数字积分（7%）
    score_digital_amount = interest * Decimal('0.07')
    app.logger.info('score_digital_amount: +%s' % score_digital_amount)
    # 插入积分明细
    score_digital_item_data = {
        'user_id': user_id,
        'type': TYPE_PAYMENT_INCOME,
        'amount': score_digital_amount,
        'sc_id': apply_put_id,
        'note': '来自排单收益',
        'status_audit': STATUS_AUDIT_SUCCESS,
        'audit_time': current_time,
        'create_time': current_time,
        'update_time': current_time
    }
    add_score_digital_item(score_digital_item_data)
    # 更新积分总表
    current_score_digital_amount = increase_score_digital(user_id, score_digital_amount)
    app.logger.info('current_score_digital_amount: %s' % current_score_digital_amount)

    # 3、消费积分（10%）
    score_expense_amount = interest * Decimal('0.1')
    app.logger.info('score_expense_amount: +%s' % score_expense_amount)
    # 插入积分明细
    score_expense_item_data = {
        'user_id': user_id,
        'type': TYPE_PAYMENT_INCOME,
        'amount': score_expense_amount,
        'sc_id': apply_put_id,
        'note': '来自排单收益',
        'status_audit': STATUS_AUDIT_SUCCESS,
        'audit_time': current_time,
        'create_time': current_time,
        'update_time': current_time
    }
    add_score_expense_item(score_expense_item_data)
    # 更新积分总表
    current_score_expense_amount = increase_score_expense(user_id, score_expense_amount)
    app.logger.info('current_score_expense_amount: %s' % current_score_expense_amount)


def _on_wallet(user_id, apply_put_id, principal_interest, current_time):
    """
    处理钱包
    :param user_id:
    :param apply_put_id:
    :param principal_interest:
    :param current_time:
    :return:
    """
    # 添加钱包明细
    wallet_item_data = {
        'user_id': user_id,
        'type': TYPE_PAYMENT_INCOME,
        'sc_id': apply_put_id,
        'note': '来自排单收益',
        'amount': principal_interest,
        'status_audit': STATUS_AUDIT_SUCCESS,
        'audit_time': current_time,
        'create_time': current_time,
        'update_time': current_time
    }
    add_wallet_item(wallet_item_data)

    wallet_info = get_wallet_row_by_id(user_id)
    # 新增钱包记录，更新钱包余额
    if not wallet_info:
        app.logger.info('wallet_amount: 0')
        wallet_data = {
            'user_id': user_id,
            'amount_initial': 0,
            'amount_current': principal_interest,
            'amount_lock': 0,
            'create_time': current_time,
            'update_time': current_time,
        }
        add_wallet(wallet_data)
    # 更新钱包余额
    else:
        app.logger.info('wallet_amount: %s' % wallet_info.amount_current)
        wallet_data = {
            'user_id': user_id,
            'amount_current': wallet_info.amount_current + principal_interest,
            'update_time': current_time,
        }
        edit_wallet(user_id, wallet_data)
    wallet_info = get_wallet_row_by_id(user_id)
    current_wallet_amount = wallet_info.amount_current if wallet_info else 0
    app.logger.info('current_wallet_amount: %s' % current_wallet_amount)


def _on_bonus(user_id, apply_put_id, interest, current_time):
    """
    处理奖金
    :param user_id:
    :param apply_put_id:
    :param interest:
    :param current_time:
    :return:
    """
    p_uid_list = get_p_uid_list(user_id)
    c = 0
    for uid, bonus_rate in zip(p_uid_list, BONUS_LEVEL):
        # 获取用户团队奖励优先级配置
        user_config_row = get_user_config_row_by_id(uid)
        bonus_user_config = [Decimal(i) for i in user_config_row.team_bonus.split(',')] if user_config_row else []
        bonus_rate = bonus_user_config[c] if len(bonus_user_config) >= 3 else bonus_rate

        # 计算上级推广奖金
        bonus = interest * bonus_rate
        # 添加奖金明细
        bonus_item_data = {
            'user_id': uid,
            'type': TYPE_PAYMENT_INCOME,
            'sc_id': apply_put_id,
            'amount': bonus,
            'status_audit': STATUS_AUDIT_SUCCESS,
            'audit_time': current_time,
            'create_time': current_time,
            'update_time': current_time
        }
        add_bonus_item(bonus_item_data)

        bonus_info = get_bonus_row_by_id(uid)
        # 新增奖金记录，更新奖金余额
        if not bonus_info:
            app.logger.info('p_uid: %s, bonus_amount: %s, bonus_rate: %s' % (uid, 0, bonus_rate))
            bonus_data = {
                'user_id': uid,
                'amount': bonus,
                'create_time': current_time,
                'update_time': current_time,
            }
            add_bonus(bonus_data)
        # 更新奖金余额
        else:
            app.logger.info('p_uid: %s, bonus_amount: %s, bonus_rate: %s' % (uid, bonus_info.amount, bonus_rate))
            bonus_data = {
                'amount': bonus_info.amount + bonus,
                'update_time': current_time,
            }
            edit_bonus(uid, bonus_data)
        bonus_info = get_bonus_row_by_id(uid)
        current_bonus_amount = bonus_info.amount if bonus_info else 0
        app.logger.info('p_uid: %s, current_bonus_amount: %s' % (uid, current_bonus_amount))
        c += 1


def on_apply_put_interest_on_principal(ch, method, properties, body):
    """
    回调处理 - 投资申请本息回收
    :return:
    """
    try:
        print " [x]  %s Get %r" % (time.strftime('%Y-%m-%d %H:%M:%S'), body,)
        msg = json.loads(body)
        user_id = msg['user_id']
        apply_put_id = msg['apply_put_id']

        # 判断排单状态
        apply_put_info = get_apply_put_row_by_id(apply_put_id)
        if not apply_put_info or apply_put_info.status_order != int(STATUS_ORDER_COMPLETED):
            raise DropException('Drop apply_put_interest_on_principal uid:%s, apply_put_id: %s' % (user_id, apply_put_id))

        # 获取申请投资排单的所有匹配订单
        order_rows = get_order_lists(**{'apply_put_id': apply_put_id})
        for order_info in order_rows:
            # 检查订单, 只处理收款确认成功的订单
            if not order_info or order_info.status_rec != int(STATUS_REC_SUCCESS):
                continue
            current_time = datetime.utcnow()

            # 计算投资用户利息
            interest = order_info.money * INTEREST_PUT * 15  # 默认计息日 15 天

            # 处理积分 收益 20% 进入积分钱包（慈善3 数字7 消费10）
            _on_score(user_id, apply_put_id, interest, current_time)

            # 处理钱包 扣除积分之后的本息和加入钱包
            principal_interest = order_info.money + interest * Decimal('0.8')
            _on_wallet(user_id, apply_put_id, principal_interest, current_time)

            # 处理奖金 计算投资方上级推广利息（三级）
            _on_bonus(user_id, apply_put_id, interest, current_time)

        ch.basic_ack(delivery_tag=method.delivery_tag)
    except DropException:
        # 消息丢弃
        print traceback.print_exc()
        ch.basic_ack(delivery_tag=method.delivery_tag)
    except Exception as e:
        print traceback.print_exc()
        raise e


def run():
    q = RabbitDelayQueue(
        exchange=EXCHANGE_NAME,
        queue_name='apply_put_interest_on_principal',
        ttl=APPLY_PUT_INTEREST_ON_PRINCIPAL_TTL
    )
    q.consume(on_apply_put_interest_on_principal)


def test_put():
    """
    测试数据推入队列
    触发条件：投资成功申请
    :return:
    """
    q = RabbitDelayQueue(
        exchange=EXCHANGE_NAME,
        queue_name='apply_put_interest_on_principal',
        ttl=APPLY_PUT_INTEREST_ON_PRINCIPAL_TTL
    )
    msg = {
        'user_id': 0,
        'apply_put_id': 0,
        'apply_time': time.strftime('%Y-%m-%d %H:%M:%S')
    }
    q.put(msg)
    q.close_conn()


def test_callback():
    """
    测试回调
    :return:
    """
    user_id = 15
    apply_put_id = 10

    # 获取申请投资排单的所有匹配订单
    order_rows = get_order_lists(**{'apply_put_id': apply_put_id})
    print order_rows
    for order_info in order_rows:
        # 检查订单, 只处理收款确认成功的订单
        if not order_info or order_info.status_rec != int(STATUS_REC_SUCCESS):
            continue
        current_time = datetime.utcnow()

        # 计算投资用户利息
        interest = order_info.money * INTEREST_PUT * 15  # 默认计息日 15 天
        app.logger.info('interest: %s' % interest)

        # 处理积分 收益 20% 进入积分钱包（慈善3 数字7 消费10）
        _on_score(user_id, apply_put_id, interest, current_time)

        # 处理钱包 扣除积分之后的本息和加入钱包
        principal_interest = order_info.money + interest * Decimal('0.8')
        _on_wallet(user_id, apply_put_id, principal_interest, current_time)

        # 处理奖金 计算投资方上级推广利息（三级）
        _on_bonus(user_id, apply_put_id, interest, current_time)


if __name__ == '__main__':
    run()
    # test_put()
    # test_callback()
