#!/usr/bin/env python
# encoding: utf-8

"""
@author: zhanghe
@software: PyCharm
@file: user.py
@time: 2017/4/29 下午1:12
"""


# 用户配置

# 自动封号
LOCK_REG_NOT_ACTIVE_TTL = 3600*24*3     # 注册后3天内未激活
LOCK_ACTIVE_NOT_PUT_TTL = 3600*24*3     # 激活后3天内未排单
LOCK_ORDER_NOT_PAY_TTL = 3600*36        # 匹配后超过36小时不打款
LOCK_PAY_NOT_REC_TTL = 3600*36          # 收款后36小时不确认

