#!/usr/bin/env python
# encoding: utf-8

"""
@author: zhanghe
@software: PyCharm
@file: token.py
@time: 16-4-4 下午9:31
"""


import redis
import hashlib
from base64 import urlsafe_b64encode, urlsafe_b64decode
from datetime import timedelta


redis_client = redis.StrictRedis(host='localhost', port=6379, db=0)


class Token(object):
    """
    token（数据结构：字符串）
    应用场景：
    1）用户id为key, 存储token为值
    2）用户id为key, 存储验证码为值
    """
    # 定义支持的实体类型
    entity_name_list = ['reg', 'login']
    # 设置 key 生命周期
    ttl = timedelta(seconds=60)
    # 设置签名密钥
    _sign_key = '05bed70ae968e133a86e3ce388f4509838bd7cbf753f01c3'

    def __init__(self, entity_name, prefix='token'):
        if entity_name not in self.entity_name_list:
            raise TypeError(u'类型错误')
        self.entity_name = entity_name
        self.prefix = prefix

    @staticmethod
    def generate_sign_key():
        """
        生成签名密钥
        05bed70ae968e133a86e3ce388f4509838bd7cbf753f01c3
        """
        import os
        import binascii
        sk = os.urandom(24)
        # print sk
        # print binascii.b2a_hex(sk)
        return binascii.b2a_hex(sk)

    def create_token(self):
        """
        生成 token (基于 uuid)
        """
        from uuid import uuid1
        from itsdangerous import TimestampSigner
        s = TimestampSigner(self._sign_key)
        return s.sign(str(uuid1()))

    def check_token(self, token_sign):
        """
        校验 token, 返回解密后的 token
        """
        from itsdangerous import TimestampSigner, SignatureExpired, BadTimeSignature
        s = TimestampSigner(self._sign_key)
        try:
            token = s.unsign(token_sign, max_age=60)  # 60秒过期
            return {'success': token}
        except SignatureExpired as e:
            # 处理签名超时
            return {'error': e.message}
        except BadTimeSignature as e:
            # 处理签名错误
            return {'error': e.message}

    def add_item(self, key_id, item):
        """
        添加 item
        :param key_id:
        :param item:
        :return:0/1
        """
        key = "%s:%s:%s" % (self.prefix, self.entity_name, key_id)
        return redis_client.set(key, item, ex=self.ttl)

    def get_item(self, key_id):
        """
        获取 item
        :param key_id:
        :return:None/String
        """
        key = "%s:%s:%s" % (self.prefix, self.entity_name, key_id)
        return redis_client.get(key)

    def del_item(self, key_id):
        """
        删除 item
        :param key_id:
        :return:0/1
        """
        key = "%s:%s:%s" % (self.prefix, self.entity_name, key_id)
        return redis_client.delete(key)


def test_token():
    """
    测试
    127.0.0.1:6379> get "token:reg:0020"
    "9B6E"
    """
    token_reg = Token('reg')
    # print token_reg.add_item('0020', '9B6E')
    print token_reg.get_item('0020')
    print token_reg.del_item('0021')
    # print token_reg.del_item('0020')

if __name__ == '__main__':
    test_token()
    # print urlsafe_b64encode('05bed70ae968e133a86e3ce388f4509838bd7cbf753f01c3')
