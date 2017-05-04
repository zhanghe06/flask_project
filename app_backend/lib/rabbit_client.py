#!/usr/bin/env python
# encoding: utf-8

"""
@author: zhanghe
@software: PyCharm
@file: rabbit_client.py
@time: 2017/4/1 上午9:55
"""


import pika
import json
import traceback


from app.config import RABBIT_MQ

_client_conn = {'conn': None}


def get_conn():
    """
    获取连接
    :return:
    """
    if not _client_conn.get('conn'):
        conn_mq = pika.BlockingConnection(
            pika.ConnectionParameters(
                host=RABBIT_MQ.get('host', '127.0.0.1'),
                port=RABBIT_MQ.get('port', 5672),
                virtual_host=RABBIT_MQ.get('virtual_host', '/'),
                heartbeat_interval=RABBIT_MQ.get('heartbeat_interval', 0),
                retry_delay=RABBIT_MQ.get('retry_delay', 3)
            )
        )
        _client_conn['conn'] = conn_mq
        return conn_mq
    else:
        return _client_conn['conn']


class RabbitQueue(object):
    """
    队列
    """
    def __init__(self, exchange, queue_name, exchange_type='direct', durable=True, **arguments):
        self.exchange = exchange
        self.queue_name = queue_name
        self.exchange_type = exchange_type
        self.durable = durable
        self.arguments = arguments
        print u'实例化附加参数:', arguments
        self.conn = get_conn()
        self.channel = self.conn.channel()
        self.declare()

    def close_conn(self):
        """
        关闭连接
        :return:
        """
        if _client_conn.get('conn'):
            self.conn.close()
            _client_conn.pop('conn')

    def declare(self):
        """
        声明队列
        """
        self.channel.exchange_declare(exchange=self.exchange, exchange_type=self.exchange_type, durable=self.durable)
        self.channel.queue_declare(queue=self.queue_name, durable=self.durable, arguments=self.arguments)
        self.channel.queue_bind(exchange=self.exchange,
                                queue=self.queue_name,
                                routing_key=self.queue_name)
        self.channel.basic_qos(prefetch_count=1)

    def put(self, message):
        """
        推送队列消息
        :param message:
        :return:
        """
        if isinstance(message, dict):
            message = json.dumps(message)
        self.channel.basic_publish(exchange=self.exchange,
                                   routing_key=self.queue_name,
                                   body=message,
                                   properties=pika.BasicProperties(
                                       delivery_mode=2 if self.durable else 1,  # make message persistent
                                   ))
        print " [x] Sent %r" % (message,)

    def get(self):
        """
        获取队列消息
        :return:
        """
        # data = self.channel.basic_get(self.queue_name)
        # print data
        method_frame, header_frame, body = self.channel.basic_get(self.queue_name)
        if method_frame:
            print " [x]  Get %r" % (body,)
            print method_frame, header_frame, body
            self.channel.basic_ack(method_frame.delivery_tag)
        else:
            print('No message returned')

    def get_block(self):
        """
        获取队列消息(阻塞)
        direct 模式下多进程消费，进程轮流获取单个消息
        :return:
        """
        def callback(ch, method, properties, body):
            try:
                print " [x]  Get %r" % (body,)
                # raise Exception('test')
                ch.basic_ack(delivery_tag=method.delivery_tag)
            except Exception as e:
                print traceback.print_exc()
                raise e

        self.consume(callback)

    def consume(self, callback):
        """
        消费
        """
        # 处理队列
        self.channel.basic_consume(consumer_callback=callback, queue=self.queue_name)
        try:
            self.channel.start_consuming()
        except KeyboardInterrupt:
            self.channel.stop_consuming()
        self.close_conn()


class RabbitPubSub(object):
    """
    订阅
    """
    def __init__(self, exchange, exchange_type='fanout', durable=True, **arguments):
        self.exchange = exchange
        self.exchange_type = exchange_type
        self.durable = durable
        self.arguments = arguments
        print u'实例化附加参数:', arguments
        self.conn = get_conn()
        self.channel = self.conn.channel()
        self.channel.exchange_declare(exchange=self.exchange, exchange_type=self.exchange_type, durable=self.durable)

    def close_conn(self):
        """
        关闭连接
        :return:
        """
        if _client_conn.get('conn'):
            self.conn.close()
            _client_conn.pop('conn')

    def pub(self, message):
        """
        推送队列消息
        :param message:
        :return:
        """
        if isinstance(message, dict):
            message = json.dumps(message)
        self.channel.basic_publish(exchange=self.exchange,
                                   body=message,
                                   routing_key='',
                                   properties=pika.BasicProperties(
                                       delivery_mode=2 if self.durable else 1,  # make message persistent
                                   ))
        print " [x] Pub %r" % (message,)

    def sub(self):
        """
        订阅队列消息
        exchange_type='fanout'
        fanout 模式下多进程消费，进程同时同步获取消息
        :return:
        """
        result = self.channel.queue_declare(exclusive=True)
        queue_name = result.method.queue

        self.channel.queue_bind(exchange=self.exchange, queue=queue_name)

        print ' [*] Waiting for logs. To exit press CTRL+C'

        def callback(ch, method, properties, body):
            print " [x] Sub %r" % (body,)

        self.channel.basic_consume(callback,
                                   queue=queue_name,
                                   no_ack=True
                                   )

        self.channel.start_consuming()


class RabbitDelayQueue(object):
    """
    延时队列
    q_d_client = RabbitDelayQueue('amq.direct', q_name, ttl=3600*24)
    """
    def __init__(self, exchange, queue_name, exchange_type='direct', durable=True, **arguments):
        self.exchange = exchange
        self.queue_name = queue_name
        self.delay_queue_name = '%s_delay' % queue_name
        self.exchange_type = exchange_type
        self.durable = durable
        self.arguments = arguments
        print u'实例化附加参数:', arguments
        self.conn = get_conn()
        self.channel = self.conn.channel()
        self.channel.confirm_delivery()
        self.channel.queue_declare(queue=queue_name, durable=durable)

        # We need to bind this channel to an exchange, that will be used to transfer
        # messages from our delay queue.
        self.channel.queue_bind(exchange=self.exchange,
                                queue=queue_name)

        # 延时队列定义
        self.delay_channel = self.conn.channel()
        self.delay_channel.confirm_delivery()

        # This is where we declare the delay, and routing for our delay channel.
        self.delay_channel.queue_declare(queue=self.delay_queue_name, durable=durable, arguments={
            'x-message-ttl': arguments.get('ttl', 5)*1000,  # Delay until the message is transferred in milliseconds.
            'x-dead-letter-exchange': self.exchange,  # Exchange used to transfer the message from A to B.
            'x-dead-letter-routing-key': self.queue_name  # Name of the queue we want the message transferred to.
        })

    def close_conn(self):
        """
        关闭连接
        :return:
        """
        if _client_conn.get('conn'):
            self.conn.close()
            _client_conn.pop('conn')

    def put(self, message):
        """
        推送队列消息
        :param message:
        :return:
        """
        if isinstance(message, dict):
            message = json.dumps(message)
        self.delay_channel.basic_publish(exchange='',
                                         routing_key=self.delay_queue_name,
                                         body=message,
                                         properties=pika.BasicProperties(
                                             delivery_mode=2 if self.durable else 1,  # make message persistent
                                         ))
        print " [x] Sent %r" % (message,)

    def get(self):
        """
        获取队列消息
        :return:
        """
        # data = self.channel.basic_get(self.queue_name)
        # print data
        method_frame, header_frame, body = self.channel.basic_get(self.queue_name)
        if method_frame:
            print " [x]  Get %r" % (body,)
            print method_frame, header_frame, body
            self.channel.basic_ack(method_frame.delivery_tag)
        else:
            print('No message returned')

    def get_block(self):
        """
        获取队列消息(阻塞)
        direct 模式下多进程消费，进程轮流获取单个消息
        :return:
        """
        def callback(ch, method, properties, body):
            try:
                print " [x]  Get %r" % (body,)
                # raise Exception('test')
                ch.basic_ack(delivery_tag=method.delivery_tag)
            except Exception as e:
                print traceback.print_exc()
                raise e

        self.consume(callback)

    def consume(self, callback):
        """
        消费
        """
        # 处理队列
        self.channel.basic_consume(consumer_callback=callback, queue=self.queue_name)
        try:
            self.channel.start_consuming()
        except KeyboardInterrupt:
            self.channel.stop_consuming()
        self.close_conn()


def test_queue():
    """
    队列测试
    参数：方法 队列名称 消息
    :return:
    """
    import sys
    print sys.argv
    if len(sys.argv) < 3:
        print u'参数：方法 队列名称 消息'
        print u'python app/tools/rabbit_client.py put q_task 123456'
        print u'python app/tools/rabbit_client.py get q_task'
        return
    method, q_name, msg = sys.argv[1], sys.argv[2], ''.join(sys.argv[3:4])
    q_client = RabbitQueue('e_test', q_name)
    print u'连接id:%s' % id(q_client.conn)
    # 获取消息
    if method == 'get':
        q_client.get()
    # 推送消息
    if method == 'put':
        q_client.put(msg)
    # 阻塞获取消息
    if method == 'get_block':
        q_client.get_block()
    q_client.close_conn()


def test_pub_sub():
    """
    队列pub/sub
    参数：方法 队列名称 消息
    :return:
    """
    import sys
    print sys.argv
    if len(sys.argv) < 3:
        print u'参数：方法 队列名称 消息'
        print u'python app/tools/rabbit_client.py pub q_task 123456'
        print u'python app/tools/rabbit_client.py sub q_task'
        return
    method, q_name, msg = sys.argv[1], sys.argv[2], ''.join(sys.argv[3:4])
    q_client = RabbitPubSub(q_name)
    print u'连接id:%s' % id(q_client.conn)
    # 获取消息
    if method == 'sub':
        q_client.sub()
    # 推送消息
    if method == 'pub':
        q_client.pub(msg)
    q_client.close_conn()


def test_delay_queue():
    """
    延时队列测试
    参数：方法 队列名称 消息
    :return:
    """
    import sys
    print sys.argv
    if len(sys.argv) < 3:
        print u'参数：方法 队列名称 消息'
        print u'python app/tools/rabbit_client.py put q_delay_task 123456'
        print u'python app/tools/rabbit_client.py get q_delay_task'
        return
    method, q_name, msg = sys.argv[1], sys.argv[2], ''.join(sys.argv[3:4])
    q_client = RabbitDelayQueue('amq.direct', q_name)
    print u'连接id:%s' % id(q_client.conn)
    # 获取消息
    if method == 'get':
        q_client.get()
    # 推送消息
    if method == 'put':
        q_client.put(msg)
    # 阻塞获取消息
    if method == 'get_block':
        q_client.get_block()
    q_client.close_conn()


if __name__ == '__main__':
    # test_queue()
    # test_pub_sub()
    test_delay_queue()

