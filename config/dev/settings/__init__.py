#!/usr/bin/env python
# encoding: utf-8

"""
@author: zhanghe
@software: PyCharm
@file: __init__.py.py
@time: 2017/4/27 下午6:45
"""


# 开关状态
ON = True
OFF = False


# 网站配置
PER_PAGE_FRONTEND = 12   # 分页显示数据条数 前台
PER_PAGE_BACKEND = 12   # 分页显示数据条数 后台

# 功能开关

SWITCH_EXPORT = OFF     # 导出
SWITCH_REG = ON     # 用户注册

SWITCH_LOGIN_ACCOUNT = ON     # 用户账号登录
SWITCH_LOGIN_PHONE = ON     # 用户手机登录
SWITCH_LOGIN_EMAIL = ON     # 用户邮箱登录

SWITCH_LOGIN_THREE_PART = OFF     # 第三方平台登录
