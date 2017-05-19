#!/usr/bin/env python
# encoding: utf-8

"""
@author: zhanghe
@software: PyCharm
@file: run_lock_pay_not_rec.py
@time: 2017/5/17 上午9:02
"""


import json
import time
import traceback


from app_frontend.lib.rabbit_mq import RabbitDelayQueue
from config import EXCHANGE_NAME
from app_common.settings.user import LOCK_PAY_NOT_REC_TTL
from app_frontend.api.order import get_order_row
from app_frontend.api.user import lock
from app_common.maps.status_pay import *
from app_common.maps.status_rec import *
from app_common.maps.status_audit import *
from app_common.maps.status_delete import *


def on_lock_pay_not_rec(ch, method, properties, body):
    """
    回调处理 - 封号
    :return:
    """
    try:
        print " [x]  %s Get %r" % (time.strftime('%Y-%m-%d %H:%M:%S'), body,)
        msg = json.loads(body)
        user_id = msg['user_id']
        order_id = msg['order_id']

        condition = {
            'id': order_id,
            'apply_get_uid': user_id,
            'status_pay': int(STATUS_PAY_SUCCESS),
            'status_audit': int(STATUS_AUDIT_SUCCESS),
            'status_delete': int(STATUS_DEL_NO)
        }
        order_info = get_order_row(**condition)
        if order_info and order_info.status_rec != int(STATUS_REC_SUCCESS):
            # 支付成功，未确认收款，封号
            lock(user_id)
        ch.basic_ack(delivery_tag=method.delivery_tag)
    except Exception as e:
        print traceback.print_exc()
        raise e


def run():
    q = RabbitDelayQueue(exchange=EXCHANGE_NAME, queue_name='lock_pay_not_rec', ttl=LOCK_PAY_NOT_REC_TTL)
    q.consume(on_lock_pay_not_rec)


def test_put():
    """
    测试数据推入队列
    :return:
    """
    q = RabbitDelayQueue(exchange=EXCHANGE_NAME, queue_name='lock_pay_not_rec', ttl=LOCK_PAY_NOT_REC_TTL)
    q.put({'user_id': 0, 'order_id': 0, 'pay_time': time.strftime('%Y-%m-%d %H:%M:%S')})


if __name__ == '__main__':
    run()
    # test_put()


