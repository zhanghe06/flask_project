#!/usr/bin/env python
# encoding: utf-8

"""
@author: zhanghe
@software: PyCharm
@file: order.py
@time: 2017/4/29 下午1:12
"""


# 订单限制
ORDER_MAX_AMOUNT = 10000
ORDER_MAX_COUNT = 100


# 利息配置
INTEREST_PUT = 0.01  # 投资利息（日息）
INTEREST_PAY_AHEAD = 0.02  # 提前支付奖金比例
INTEREST_PAY_DELAY = 0.02  # 延迟支付罚金比例
