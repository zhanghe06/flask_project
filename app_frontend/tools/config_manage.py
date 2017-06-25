#!/usr/bin/env python
# encoding: utf-8

"""
@author: zhanghe
@software: PyCharm
@file: config_manage.py
@time: 2017/6/4 上午11:00
"""


import redis
import json
import time
from app_frontend import app
redis_client = redis.Redis(**app.config['REDIS'])


def get_conf(conf_name):
    """
    获取配置
    :param conf_name:
    :return:
    """
    conf_key = 'conf:%s' % conf_name
    conf_value = redis_client.get(conf_key)
    return conf_value or app.config.get(conf_name)


def set_conf(conf_name, conf_value):
    """
    设置配置
    :param conf_name:
    :param conf_value:
    :return:
    """
    conf_key = 'conf:%s' % conf_name
    return redis_client.set(conf_key, conf_value)


def clean_conf():
    """
    清除配置
    :return:
    """
    conf_key = 'conf:*'
    conf_keys = redis_client.keys(conf_key)
    return redis_client.delete(*conf_keys)


if __name__ == '__main__':
    print get_conf('INTEREST_PUT'), type(get_conf('INTEREST_PUT'))
    # print set_conf('APPLY_PUT_MIN_EACH', 4000)
    print clean_conf()
