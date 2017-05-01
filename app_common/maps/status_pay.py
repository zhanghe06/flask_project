#!/usr/bin/env python
# encoding: utf-8

"""
@author: zhanghe
@software: PyCharm
@file: status_pay.py
@time: 2017/4/27 下午1:46
"""


# 支付状态:0:待支付，1:支付成功，2:支付失败
STATUS_PAY_HOLDING = '0'
STATUS_PAY_SUCCESS = '1'
STATUS_PAY_FAILURE = '2'

STATUS_PAY_DICT = {
    0: u'待支付',
    1: u'支付成功',
    2: u'支付失败',
}
