#!/usr/bin/env python
# encoding: utf-8

"""
@author: zhanghe
@software: PyCharm
@file: count.py
@time: 16-1-27 下午3:03
"""


import redis


redis_client = redis.StrictRedis(host='localhost', port=6379, db=0)


class Count(object):
    """
    计数器
    """
    def __init__(self, stat_type):
        if stat_type not in ['view', 'star', 'flag']:
            raise TypeError(u'类型错误')
        pass


def test():
    count_obj = Count('view')


if __name__ == '__main__':
    test()
