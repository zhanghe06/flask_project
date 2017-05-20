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
from app_frontend import sms_client
from app_frontend import app
EXCHANGE_NAME = app.config['EXCHANGE_NAME']


def on_send_sms(ch, method, properties, body):
    """
    回调处理 - 发送短信  一般是非验证码短信，通知类的信息
    :return:
    """
    try:
        print " [x]  Get %r" % (body,)
        msg = json.loads(body)
        user_id = msg['user_id']
        mobile = msg['mobile']
        sms_content = msg['sms_content']

        result = sms_client.send_international(mobile, sms_content)
        print result
        # 发送成功
        if result.get('success'):
            print u'发送成功 uid:%s, mobile:%s, content: %s' % (user_id, mobile, sms_content)
        # 发送失败
        else:
            print u'发送失败 uid:%s, mobile:%s, content: %s' % (user_id, mobile, sms_content)
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
    q.put({'user_id': 1, 'mobile': '8613800001111', 'sms_content': '1111'})


if __name__ == '__main__':
    run()
    # test_put()
