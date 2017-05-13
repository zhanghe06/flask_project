#!/usr/bin/env python
# encoding: utf-8

"""
@author: zhanghe
@software: PyCharm
@file: run_lock_reg_not_active.py
@time: 2017/5/12 上午11:07
"""


import json
import time
import traceback


from app_frontend.lib.rabbit_mq import RabbitDelayQueue
from config import EXCHANGE_NAME


def on_lock_reg_not_active(ch, method, properties, body):
    """
    回调处理 - 封号
    :return:
    """
    try:
        print " [x]  %s Get %r" % (time.strftime('%Y-%m-%d %H:%M:%S'), body,)
        msg = json.loads(body)
        # todo
        ch.basic_ack(delivery_tag=method.delivery_tag)
    except Exception as e:
        print traceback.print_exc()
        raise e


def run():
    q = RabbitDelayQueue(exchange=EXCHANGE_NAME, queue_name='lock_reg_not_active', ttl=5)
    q.consume(on_lock_reg_not_active)


def test_put():
    """
    测试数据推入队列
    :return:
    """
    q = RabbitDelayQueue(exchange=EXCHANGE_NAME, queue_name='lock_reg_not_active', ttl=5)
    q.put({'user_id': 0, 'reg_time': time.strftime('%Y-%m-%d %H:%M:%S')})


if __name__ == '__main__':
    run()
    # test_put()
