#!/usr/bin/env python
# encoding: utf-8

"""
@author: zhanghe
@software: PyCharm
@file: cart.py
@time: 16-1-27 上午10:27
"""


import requests


# 服务地址
host = "sms.253.com"

# 端口号
port = 80

# 版本号
version = "v1.1"

# 查账户信息的URI
balance_get_uri = "/msg/balance"

# 智能匹配模版短信接口的URI
sms_send_uri = "/msg/send"

# 创蓝账号
un = "xxxx"

# 创蓝密码
pw = "xxxx"


def get_user_balance():
    """
    取账户余额
    """
    url = 'http://%s%s' % (host, balance_get_uri)
    params = {
        'un': un,  # 账号
        'pw': pw,  # 密码
    }
    return requests.get(url, params).json()


def send_sms(msg, phone):
    """
    接口发短信
    """
    url = 'http://%s%s' % (host, sms_send_uri)
    params = {
        'un': un,           # 账号
        'pw': pw,           # 密码
        'msg': msg,         # 消息
        'phone': phone,     # 手机
        'rd': 1,            # 是否需要状态报告
    }
    headers = {"Content-type": "application/x-www-form-urlencoded", "Accept": "text/plain"}
    return requests.post(url, data=params, headers=headers, timeout=30).json()


if __name__ == '__main__':
    user_phone = "188xxxxxxxx"
    user_msg = "【您的签名】您的验证码是1234"

    # 查账户余额
    print(get_user_balance())

    # 调用智能匹配模版接口发短信
    print(send_sms(user_msg, user_phone))
