#!/usr/bin/env python
# encoding: utf-8

"""
@author: zhanghe
@software: PyCharm
@file: run_lock_order_not_pay.py
@time: 2017/5/17 上午9:00
"""


import json
import time
import traceback


from app_frontend.lib.rabbit_mq import RabbitDelayQueue

from app_frontend.api.order import get_order_row
from app_frontend.api.user import lock
from app_common.maps.status_pay import *
from app_common.maps.status_audit import *
from app_common.maps.status_delete import *
from app_frontend import app
EXCHANGE_NAME = app.config['EXCHANGE_NAME']
LOCK_ORDER_NOT_PAY_TTL = app.config['LOCK_ORDER_NOT_PAY_TTL']


def on_lock_order_not_pay(ch, method, properties, body):
    """
    回调处理 - 封号
    :return:
    """
    try:
        print " [x]  %s Get %r" % (time.strftime('%Y-%m-%d %H:%M:%S'), body,)
        msg = json.loads(body)
        user_id = msg['user_id']
        order_id = msg['order_id']
        create_time = msg['create_time']

        condition = {
            'id': order_id,
            'apply_put_uid': user_id,
            'status_audit': int(STATUS_AUDIT_SUCCESS),
            'status_delete': int(STATUS_DEL_NO)
        }
        order_info = get_order_row(**condition)
        if order_info and order_info.status_pay != int(STATUS_PAY_SUCCESS):
            # 订单审核，未付款，封号
            lock(user_id)

        ch.basic_ack(delivery_tag=method.delivery_tag)
    except Exception as e:
        print traceback.print_exc()
        raise e


def run():
    q = RabbitDelayQueue(exchange=EXCHANGE_NAME, queue_name='lock_order_not_pay', ttl=LOCK_ORDER_NOT_PAY_TTL)
    q.consume(on_lock_order_not_pay)


def test_put():
    """
    测试数据推入队列
    :return:
    """
    q = RabbitDelayQueue(exchange=EXCHANGE_NAME, queue_name='lock_order_not_pay', ttl=LOCK_ORDER_NOT_PAY_TTL)
    q.put({'user_id': 0, 'order_id': 0, 'create_time': time.strftime('%Y-%m-%d %H:%M:%S')})


if __name__ == '__main__':
    run()
    # test_put()

