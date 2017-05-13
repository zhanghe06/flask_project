#!/usr/bin/env python
# encoding: utf-8

"""
@author: zhanghe
@software: PyCharm
@file: run_send_sms_priority.py
@time: 2017/5/12 上午11:07
"""


import json
import traceback

from app_frontend.lib.rabbit_mq import RabbitPriorityQueue
from config import EXCHANGE_NAME


def on_send_sms_priority(ch, method, properties, body):
    """
    回调处理 - 发送短信(带优先级)
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
    q = RabbitPriorityQueue(exchange=EXCHANGE_NAME, queue_name='send_sms_p')
    q.consume(on_send_sms_priority)


def test_put():
    """
    测试数据推入队列
    因为消费进程没有延时，所以先执行推送，再开启消费，能看到优先级效果
    :return:
    """
    q = RabbitPriorityQueue(exchange=EXCHANGE_NAME, queue_name='send_sms_p')
    q.put({'user_id': 1, 'reg_time': '1900-01-01 00:00:00'}, 20)
    q.put({'user_id': 2, 'reg_time': '1900-01-01 00:00:00'}, 30)
    q.put({'user_id': 3, 'reg_time': '1900-01-01 00:00:00'}, 10)


if __name__ == '__main__':
    run()
    # test_put()
