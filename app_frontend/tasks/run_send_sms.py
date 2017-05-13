#!/usr/bin/env python
# encoding: utf-8

"""
@author: zhanghe
@software: PyCharm
@file: run_send_sms.py
@time: 2017/5/12 上午11:07
"""


import json
import traceback

from app_frontend.lib.rabbit_mq import RabbitQueue
from config import EXCHANGE_NAME


def on_send_sms(ch, method, properties, body):
    """
    回调处理 - 发送短信
    :return:
    """
    try:
        print " [x]  Get %r" % (body,)
        msg = json.loads(body)
        # todo
        ch.basic_ack(delivery_tag=method.delivery_tag)
    except Exception as e:
        print traceback.print_exc()
        raise e


def run():
    q = RabbitQueue(exchange=EXCHANGE_NAME, queue_name='send_sms')
    q.consume(on_send_sms)


def test_put():
    """
    测试数据推入队列
    :return:
    """
    q = RabbitQueue(exchange=EXCHANGE_NAME, queue_name='send_sms')
    q.put({'user_id': 0, 'reg_time': '1900-01-01 00:00:00'})


if __name__ == '__main__':
    run()
    # test_put()
