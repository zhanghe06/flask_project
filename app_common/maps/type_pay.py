#!/usr/bin/env python
# encoding: utf-8

"""
@author: zhanghe
@software: PyCharm
@file: type_pay.py
@time: 2017/5/10 下午9:59
"""


# 支付/收款方式:0:不限，1:银行转账，2:数字货币，3:支付宝，4:微信
TYPE_PAY = '0'
TYPE_PAY_WALLET = '1'
TYPE_PAY_BIT_COIN = '2'
TYPE_PAY_ALI_PAY = '3'
TYPE_PAY_WE_CHAT = '4'

TYPE_PAY_DICT = {
    0: u'不限',
    1: u'钱包余额',
    2: u'数字货币',
    3: u'支付宝',
    4: u'微信',
}
