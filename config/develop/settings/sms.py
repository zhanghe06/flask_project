#!/usr/bin/env python
# encoding: utf-8

"""
@author: zhanghe
@software: PyCharm
@file: sms_msg.py
@time: 2017/4/21 下午4:57
"""


# 短信验证码
SMS_CODE_REG = u'【网站签名】%s，是您注册的验证码'
SMS_CODE_LOGIN = u'【网站签名】%s，是您登录的验证码'
SMS_CODE_RESET = u'【网站签名】%s，是您重置密码的验证码'

# 订单通知
NOTICE_ORDER_CREATE = u'【网站签名】您的订单已经创建成功'
NOTICE_ORDER_CANCEL = u'【网站签名】您的订单已经取消成功'
NOTICE_ORDER_PAYED = u'【网站签名】您的订单已经支付成功'
NOTICE_ORDER_CONFIRM = u'【网站签名】您的订单已经确认完成'

# 事件通知
NOTICE_EVENT_ACTIVE = u'【网站签名】您的账号已经激活成功'
NOTICE_EVENT_LOCK = u'【网站签名】您的账号当前已经锁定'
NOTICE_EVENT_UNLOCK = u'【网站签名】您的账号已经解除锁定'
