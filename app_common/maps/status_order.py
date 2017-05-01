#!/usr/bin/env python
# encoding: utf-8

"""
@author: zhanghe
@software: PyCharm
@file: status_order.py
@time: 2017/4/27 上午11:44
"""


# 订单状态:0:待匹配，1:部分匹配，2:完全匹配
STATUS_ORDER_HANDING = '0'
STATUS_ORDER_PROCESSING = '1'
STATUS_ORDER_COMPLETED = '2'

STATUS_ORDER_DICT = {
    0: u'待匹配',
    1: u'部分匹配',
    2: u'完全匹配',
}
