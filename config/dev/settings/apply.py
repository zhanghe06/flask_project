#!/usr/bin/env python
# encoding: utf-8

"""
@author: zhanghe
@software: PyCharm
@file: apply.py
@time: 2017/4/29 下午1:11
"""


# 单次投资金额范围
APPLY_PUT_MIN_EACH = 2000        # 最小值
APPLY_PUT_MAX_EACH = 20000       # 最大值
APPLY_PUT_STEP = 1000       # 投资金额步长（基数）

# 单次提现金额范围
APPLY_GET_MIN_EACH = 2000        # 最小值
APPLY_GET_MAX_EACH = 50000       # 最大值
APPLY_GET_STEP = 500       # 提现金额步长（基数）

# 每日投资限额
APPLY_PUT_MAX_DAILY = 100000        # 最大值

# 每日提现限额
APPLY_GET_MAX_DAILY = 100000        # 最大值

# 每月投资限额
APPLY_PUT_MAX_MONTHLY = 100000        # 最大值

# 每月提现限额
APPLY_GET_MAX_MONTHLY = 100000        # 最大值


APPLY_PUT_DAYS_BONUS = 15   # 分红计算天数
APPLY_PUT_DAYS_LOCK = 15    # 投资锁定天数、提现冻结天数

APPLY_PUT_USER_MAX_COUNT = 1        # 单个用户投资最大交易中单数(0 表示不限制)

APPLY_PUT_TIME_START = '00:00:00'       # 每天投资申请开始时间
APPLY_PUT_TIME_END = '59:00:00'         # 每天投资申请结束时间

APPLY_GET_TIME_START = '00:00:00'       # 每天提现申请开始时间
APPLY_GET_TIME_END = '59:00:00'         # 每天提现申请结束时间


APPLY_PUT_MAX_AMOUNT = 10000            # 投资总额
APPLY_PUT_MAX_COUNT = 100               # 投资总数

