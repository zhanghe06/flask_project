#!/usr/bin/env python
# encoding: utf-8

"""
@author: zhanghe
@software: PyCharm
@file: order.py
@time: 2017/4/29 下午1:12
"""


# 订单限制
ORDER_MAX_AMOUNT = 10000  # 订单最大金额
ORDER_MAX_COUNT = 100  # 订单最大数量

# 系统自动确认收款
PAY_AUTO_REC_TTL = 60*60*48  # 系统在订单支付成功后超过48小时未确认收款，自动确认收款

# 推广奖励

BONUS_DIRECT = 0.03  # 直接推荐奖励

BONUS_LEVEL_FIRST = 0.05        # 一级推荐奖励
BONUS_LEVEL_SECOND = 0.05       # 二级推荐奖励
BONUS_LEVEL_THIRD = 0.03        # 三级推荐奖励

BONUS_LEVEL = [BONUS_LEVEL_FIRST, BONUS_LEVEL_SECOND, BONUS_LEVEL_THIRD]
