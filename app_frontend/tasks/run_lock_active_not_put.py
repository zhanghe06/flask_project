#!/usr/bin/env python
# encoding: utf-8

"""
@author: zhanghe
@software: PyCharm
@file: run_lock_active_not_put.py
@time: 2017/5/17 上午8:58
"""


import json
import time
import traceback


from app_frontend.lib.rabbit_mq import RabbitDelayQueue

from app_frontend.api.apply_put import is_put
from app_frontend.api.user import lock
from app_frontend import app
EXCHANGE_NAME = app.config['EXCHANGE_NAME']
LOCK_ACTIVE_NOT_PUT_TTL = app.config['LOCK_ACTIVE_NOT_PUT_TTL']


def on_lock_active_not_put(ch, method, properties, body):
    """
    回调处理 - 封号
    :return:
    """
    try:
        print " [x]  %s Get %r" % (time.strftime('%Y-%m-%d %H:%M:%S'), body,)
        msg = json.loads(body)
        user_id = msg['user_id']
        # 检查是否投资
        if not is_put(user_id):
            lock(user_id)
        ch.basic_ack(delivery_tag=method.delivery_tag)
    except Exception as e:
        print traceback.print_exc()
        raise e


def run():
    q = RabbitDelayQueue(
        exchange=EXCHANGE_NAME,
        queue_name='lock_active_not_put',
        ttl=LOCK_ACTIVE_NOT_PUT_TTL
    )
    q.consume(on_lock_active_not_put)


def test_put():
    """
    测试数据推入队列
    触发条件：用户成功激活
    :return:
    """
    q = RabbitDelayQueue(
        exchange=EXCHANGE_NAME,
        queue_name='lock_active_not_put',
        ttl=LOCK_ACTIVE_NOT_PUT_TTL
    )
    q.put({'user_id': 0, 'active_time': time.strftime('%Y-%m-%d %H:%M:%S')})


if __name__ == '__main__':
    run()
    # test_put()

