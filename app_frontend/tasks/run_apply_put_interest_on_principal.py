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
from app_frontend.api.bonus import get_bonus_row_by_id, add_bonus, edit_bonus
from app_frontend.api.bonus_item import add_bonus_item
from app_frontend.api.user_config import get_user_config_row_by_id
from app_frontend.api.user_profile import get_p_uid_list
from app_frontend.api.wallet import get_wallet_row_by_id, add_wallet, edit_wallet
from app_frontend.api.wallet_item import add_wallet_item
from app_frontend.lib.rabbit_mq import RabbitDelayQueue

from app_frontend.api.apply_put import is_put
from app_frontend.api.user import lock
from app_frontend.api.order import get_order_rows
from app_frontend import app
from app_frontend.tools.config_manage import get_conf

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

        # 获取申请投资排单的所有匹配订单
        order_rows = get_order_rows(**{'apply_put_id': apply_put_id})
        for order_info in order_rows:
            # 检查订单, 只处理收款确认成功的订单
            if not order_info or order_info.status_rec != int(STATUS_REC_SUCCESS):
                continue
            current_time = datetime.utcnow()

            # 一、执行投资申请本息回收
            # 计算投资用户利息
            interest = order_info.money * INTEREST_PUT * 15  # 默认计息日 15 天
            # TODO 20% 按比例转入积分

            principal_interest = order_info.money + interest  # 本息

            # 添加钱包明细
            wallet_item_data = {
                'user_id': user_id,
                'type': TYPE_PAYMENT_INCOME,
                'sc_id': order_info.id,
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
                wallet_data = {
                    'user_id': user_id,
                    'amount_current': wallet_info.amount_current + principal_interest,
                    'update_time': current_time,
                }
                edit_wallet(user_id, wallet_data)

            # 二、投资方计算上级推广利息（三级）
            p_uid_list = get_p_uid_list(order_info.apply_put_uid)
            # print '=' * 200, p_uid_list, BONUS_LEVEL

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
                    'sc_id': order_info.id,
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
                    bonus_data = {
                        'user_id': uid,
                        'amount': bonus,
                        'create_time': current_time,
                        'update_time': current_time,
                    }
                    add_bonus(bonus_data)
                # 更新奖金余额
                else:
                    bonus_data = {
                        'amount': bonus,
                        'update_time': current_time,
                    }
                    edit_bonus(uid, bonus_data)
                c += 1

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


if __name__ == '__main__':
    run()
    # test_put()
