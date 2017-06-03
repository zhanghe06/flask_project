#!/usr/bin/env python
# encoding: utf-8

"""
@author: zhanghe
@software: PyCharm
@file: interest.py
@time: 2017/6/4 下午11:03
"""


# 利息配置
INTEREST_PUT = 0.01  # 投资利息（日息）

# 支付奖惩比例
INTEREST_PAY_AHEAD = 0.02  # 提前支付奖金比例
INTEREST_PAY_DELAY = 0.02  # 延迟支付罚金比例

# 支付时间差
DIFF_TIME_PAY_AHEAD = 60*60*1   # 提前支付奖金时间差
DIFF_TIME_PAY_DELAY = 60*60*24  # 延迟支付罚金时间差

# 确认奖惩比例
INTEREST_REC_AHEAD = 0.02  # 提前确认奖金比例
INTEREST_REC_DELAY = 0.02  # 延迟确认罚金比例

# 确认时间差
DIFF_TIME_REC_AHEAD = 60*60*1   # 提前确认奖金时间差
DIFF_TIME_REC_DELAY = 60*60*24  # 延迟确认罚金时间差
