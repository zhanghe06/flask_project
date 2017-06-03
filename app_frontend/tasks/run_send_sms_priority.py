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
from app_frontend import sms_client
from app_frontend import app
EXCHANGE_NAME = app.config['EXCHANGE_NAME']


def on_send_sms_priority(ch, method, properties, body):
    """
    回调处理 - 发送短信(带优先级) 一般是带验证码短信，时效性要求高
    :return:
    """
    try:
        print " [x]  Get %r" % (body,)
        msg = json.loads(body)
        mobile = msg['mobile']
        sms_content = msg['sms_content']

        result = sms_client.send_international(mobile, sms_content)
        print result
        # 发送成功
        if result.get('success'):
            print u'发送成功 mobile:%s, content: %s' % (mobile, sms_content)
        # 发送失败
        else:
            print u'发送失败 mobile:%s, content: %s' % (mobile, sms_content)
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
    q.put({'mobile': '8613800001111', 'sms_content': '1111'}, 20)
    q.put({'mobile': '8613800002222', 'sms_content': '2222'}, 30)
    q.put({'mobile': '8613800003333', 'sms_content': '3333'}, 10)


if __name__ == '__main__':
    run()
    # test_put()
