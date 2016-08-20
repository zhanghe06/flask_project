#!/usr/bin/env python
# encoding: utf-8

"""
@author: zhanghe
@software: PyCharm
@file: session.py
@time: 16-8-3 下午5:56
"""


import redis
import json
from datetime import timedelta
from itsdangerous import TimestampSigner, SignatureExpired, BadTimeSignature


redis_client = redis.StrictRedis(host='localhost', port=6379, db=0)


class Session(object):
    """
    基于redis的会话管理 数据结构：字符串（用户信息序列化）
    """
    # 定义支持的实体类型
    entity_name_list = ['web', 'app']
    # 设置 key 生命周期
    time_out = 7200
    ttl = timedelta(seconds=time_out)
    # 设置签名密钥
    _sign_key = '121e65bfbc1012625643b21b0a5cecdd'

    def __init__(self, entity_name, prefix='session'):
        if entity_name not in self.entity_name_list:
            raise TypeError(u'类型错误')
        self.entity_name = entity_name
        self.prefix = prefix

    @staticmethod
    def generate_sign_key(length=32):
        """
        生成签名密钥
        121e65bfbc1012625643b21b0a5cecdd
        """
        import os
        import binascii
        sk = os.urandom(length/2)
        # print sk
        # print binascii.b2a_hex(sk)
        return binascii.b2a_hex(sk)

    def sign(self, session_id):
        """
        签名 session_id
        :param session_id:
        :return:
        """
        s = TimestampSigner(self._sign_key)
        return s.sign(session_id)

    def un_sign(self, sign_session_id):
        """
        校验签名 session_id
        :param sign_session_id:
        :return:
        """
        s = TimestampSigner(self._sign_key)
        try:
            session_id = s.unsign(sign_session_id, max_age=self.time_out)
            return session_id
        except SignatureExpired as e:
            # 处理签名超时
            raise Exception(e.message)
        except BadTimeSignature as e:
            # 处理签名错误
            raise Exception(e.message)

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


def test_session():
    """
    测试
    a1282b2e1e2791b639f99417e7bbfe74
    sdf54657dry0wetwete34.CoNfJA.LafZyL4wc77gmry9P7PPjgLGMlw
    sdf54657dry0wetwete34
    True
    {"province": "\u4e0a\u6d77", "openid": "o9XD1weif6-0g_5MvZa7Bx6OkwxA", "headimgurl": "http://wx.qlogo.cn/mmopen/ALImIJLVKZtPiaaVkcKFR58xpgibiaxabiaStZYcwVNIfz4Tl8VkqzqpV5fKiaibbRGfkY2lDR9SlibQvVm2ClHD6AIhBYQeuy32qaj/0", "language": "zh_CN", "city": "\u95f8\u5317", "privilege": [], "country": "\u4e2d\u56fd", "nickname": "\u788eping\u5b50", "sex": 1}
    碎ping子
    """
    session_app = Session('app')
    print session_app.generate_sign_key()
    session_id = 'sdf54657dry0wetwete34'
    session_id_sign = session_app.sign(session_id)
    print session_id_sign
    print session_app.un_sign(session_id_sign)
    user_info = {
        "province": "上海",
        "openid": "o9XD1weif6-0g_5MvZa7Bx6OkwxA",
        "headimgurl": "http://wx.qlogo.cn/mmopen/ALImIJLVKZtPiaaVkcKFR58xpgibiaxabiaStZYcwVNIfz4Tl8VkqzqpV5fKiaibbRGfkY2lDR9SlibQvVm2ClHD6AIhBYQeuy32qaj/0",
        "language": "zh_CN",
        "city": "闸北",
        "privilege": [],
        "country": "中国",
        "nickname": "碎ping子",
        "sex": 1
    }
    user_info_str = json.dumps(user_info)
    print session_app.add_item(session_id, user_info_str)
    user_info_str = session_app.get_item(session_id)
    print user_info_str
    print json.loads(user_info_str).get('nickname')


if __name__ == '__main__':
    test_session()
