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

# 时间差
DIFF_TIME_PAY_AHEAD = 60*60*1   # 提前支付奖金时间差
DIFF_TIME_PAY_DELAY = 60*60*24  # 延迟支付罚金时间差


# 推广奖励

BONUS_DIRECT = 0.03  # 直接推荐奖励

BONUS_LEVEL_FIRST = 0.05        # 一级推荐奖励
BONUS_LEVEL_SECOND = 0.05       # 二级推荐奖励
BONUS_LEVEL_THIRD = 0.03        # 三级推荐奖励

BONUS_LEVEL = [BONUS_LEVEL_FIRST, BONUS_LEVEL_SECOND, BONUS_LEVEL_THIRD]
