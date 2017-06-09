#!/usr/bin/env python
# encoding: utf-8

"""
@author: zhanghe
@software: PyCharm
@file: apply.py
@time: 2017/4/29 下午1:11
"""


# [投资配置]
# 单次投资金额范围
APPLY_PUT_MIN_EACH = 2000  # 最小值
APPLY_PUT_MAX_EACH = 20000  # 最大值
APPLY_PUT_STEP = 1000  # 投资金额步长（基数）

# 单个用户投资限制
APPLY_PUT_USER_MAX_AMOUNT = 30000  # 单个用户投资最大交易中金额
APPLY_PUT_USER_MAX_COUNT = 1  # 单个用户投资最大交易中单数(0 表示不限制)

# 每日投资限制
APPLY_PUT_MAX_AMOUNT_DAILY = 1000000  # 最大金额
APPLY_PUT_MAX_COUNT_DAILY = 1000  # 最大数量(0 表示不限制)

# 每月投资限制
APPLY_PUT_MAX_AMOUNT_MONTHLY = 30000000  # 最大值
APPLY_PUT_MAX_COUNT_MONTHLY = 30000  # 最大数量(0 表示不限制)

# 投资时间配置
APPLY_PUT_TIME_START = '00:00:00'  # 每天投资申请开始时间
APPLY_PUT_TIME_END = '23:59:59'  # 每天投资申请结束时间

# 分红配置
APPLY_PUT_DAYS_BONUS = 15  # 分红计算天数
APPLY_PUT_DAYS_LOCK = 15  # 投资锁定天数、提现冻结天数

APPLY_PUT_INTEREST_ON_PRINCIPAL_TTL = 3600 * 24 * 15  # 投资申请后15天完成的订单执行回收本息


# [提现配置]
# 单次提现金额范围
APPLY_GET_MIN_EACH = 2000  # 最小值
APPLY_GET_MAX_EACH = 20000  # 最大值
APPLY_GET_STEP = 1000  # 投资金额步长（基数）

# 单个用户提现限制
APPLY_GET_USER_MAX_AMOUNT = 30000  # 单个用户提现最大交易中金额
APPLY_GET_USER_MAX_COUNT = 1  # 单个用户提现最大交易中单数(0 表示不限制)

# 每日提现限制
APPLY_GET_MAX_AMOUNT_DAILY = 1000000  # 最大金额
APPLY_GET_MAX_COUNT_DAILY = 1000  # 最大数量(0 表示不限制)

# 每月提现限制
APPLY_GET_MAX_AMOUNT_MONTHLY = 30000000  # 最大值
APPLY_GET_MAX_COUNT_MONTHLY = 30000  # 最大数量(0 表示不限制)

# 提现时间配置
APPLY_GET_TIME_START = '00:00:00'  # 每天提现申请开始时间
APPLY_GET_TIME_END = '23:59:59'  # 每天提现申请结束时间
