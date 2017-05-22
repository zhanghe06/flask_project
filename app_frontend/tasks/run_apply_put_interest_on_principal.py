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


from app_frontend.lib.rabbit_mq import RabbitDelayQueue

from app_frontend.api.apply_put import is_put
from app_frontend.api.user import lock
from app_frontend import app
EXCHANGE_NAME = app.config['EXCHANGE_NAME']
APPLY_PUT_INTEREST_ON_PRINCIPAL_TTL = app.config['APPLY_PUT_INTEREST_ON_PRINCIPAL_TTL']


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
        # todo 检查是否完成订单
        # 执行投资申请本息回收
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
    :return:
    """
    q = RabbitDelayQueue(
        exchange=EXCHANGE_NAME,
        queue_name='apply_put_interest_on_principal',
        ttl=APPLY_PUT_INTEREST_ON_PRINCIPAL_TTL
    )
    q.put({'user_id': 0, 'apply_put_id': 0, 'apply_time': time.strftime('%Y-%m-%d %H:%M:%S')})


if __name__ == '__main__':
    run()
    # test_put()
