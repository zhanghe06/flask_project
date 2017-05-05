#!/usr/bin/env python
# encoding: utf-8

"""
@author: zhanghe
@software: PyCharm
@file: type_auth.py
@time: 2017/4/19 下午8:08
"""


# 认证类型（0未知，1邮箱，2手机，3qq，4微信，5微博）
TYPE_AUTH_ACCOUNT = '0'
TYPE_AUTH_EMAIL = '1'
TYPE_AUTH_PHONE = '2'
TYPE_AUTH_QQ = '3'
TYPE_AUTH_WECHAT = '4'
TYPE_AUTH_WEIBO = '5'

TYPE_AUTH_DICT = {
    0: u'未知',
    1: u'邮箱',
    2: u'手机',
    3: u'QQ',
    4: u'微信',
    5: u'微博',
}
