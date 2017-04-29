#!/usr/bin/env python
# encoding: utf-8

"""
@author: zhanghe
@software: PyCharm
@file: auth_type.py
@time: 2017/4/19 下午8:08
"""


# 认证类型（0未知，1邮箱，2手机，3qq，4微信，5微博）
AUTH_TYPE_ACCOUNT = '0'
AUTH_TYPE_EMAIL = '1'
AUTH_TYPE_PHONE = '2'
AUTH_TYPE_QQ = '3'
AUTH_TYPE_WECHAT = '4'
AUTH_TYPE_WEIBO = '5'

AUTH_TYPE_DICT = {
    0: u'未知',
    1: u'邮箱',
    2: u'手机',
    3: u'QQ',
    4: u'微信',
    5: u'微博',
}
