#!/usr/bin/env python
# encoding: utf-8

"""
@author: zhanghe
@software: PyCharm
@file: session_manage.py
@time: 2017/4/9 上午11:16
"""


import redis
import json
from config import REDIS


redis_client = redis.Redis(**REDIS)


def get_session(session_id):
    session_key = 'session:%s' % session_id
    print json.loads(redis_client.get(session_key))


if __name__ == '__main__':
    get_session('f093df3e-5f8b-432a-ab56-99e3975225f4')
