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

from app_frontend.api.user import lock, is_active, get_user_row_by_id
from app_common.maps.status_active import *
from app_frontend import app

from app_frontend.tools.exception import DropException


EXCHANGE_NAME = app.config['EXCHANGE_NAME']
LOCK_REG_NOT_ACTIVE_TTL = app.config['LOCK_REG_NOT_ACTIVE_TTL']


def on_lock_reg_not_active(ch, method, properties, body):
    """
    回调处理 - 封号
    :return:
    """
    try:
        print " [x]  %s Get %r" % (time.strftime('%Y-%m-%d %H:%M:%S'), body,)
        msg = json.loads(body)
        user_id = msg['user_id']
        # 检查用户是否存在
        if not get_user_row_by_id(user_id):
            raise DropException(u'用户[user_id: %s]不存在' % user_id)
        # 检查是否激活
        if is_active(user_id) == int(STATUS_ACTIVE_NO):
            lock(user_id)
        ch.basic_ack(delivery_tag=method.delivery_tag)
    except DropException:
        print traceback.print_exc()
        ch.basic_ack(delivery_tag=method.delivery_tag)
    except Exception as e:
        print traceback.print_exc()
        raise e


def run():
    q = RabbitDelayQueue(
        exchange=EXCHANGE_NAME,
        queue_name='lock_reg_not_active',
        ttl=LOCK_REG_NOT_ACTIVE_TTL
    )
    q.consume(on_lock_reg_not_active)


def test_put():
    """
    测试数据推入队列
    触发条件：用户成功注册
    :return:
    """
    q = RabbitDelayQueue(
        exchange=EXCHANGE_NAME,
        queue_name='lock_reg_not_active',
        ttl=LOCK_REG_NOT_ACTIVE_TTL
    )
    msg = {
        'user_id': 0,
        'reg_time': time.strftime('%Y-%m-%d %H:%M:%S')
    }
    q.put(msg)
    q.close_conn()


if __name__ == '__main__':
    run()
    # test_put()
