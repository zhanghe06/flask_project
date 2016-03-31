#!/usr/bin/env python
# encoding: utf-8

"""
@author: zhanghe
@software: PyCharm
@file: local.py
@time: 16-3-10 下午5:10
"""


import os
basedir = os.path.abspath(os.path.dirname(__file__))

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, '../flask.db')
SQLALCHEMY_TRACK_MODIFICATIONS = False

CSRF_ENABLED = True
SECRET_KEY = '\x03\xabjR\xbbg\x82\x0b{\x96f\xca\xa8\xbdM\xb0x\xdbK%\xf2\x07\r\x8c'

# 本地调试邮箱配置
# $ sudo python -m smtpd -n -c DebuggingServer localhost:25
MAIL_SERVER = 'localhost',
MAIL_PORT = 25,
MAIL_USERNAME = None,
MAIL_PASSWORD = None,
MAIL_DEFAULT_SENDER = ('no-reply', 'no-reply@localhost')
# 后台管理人员邮件列表
ADMINS = ['455091702@qq.com']

# 第三方开放授权登陆

GITHUB_OAUTH = {
    'consumer_key': '0ccd9367a1f81288b127',
    'consumer_secret': '711b6afcc938d760e9e57215dfbdcb115150ddc6',
    'request_token_params': {'scope': 'user:email'},
    'base_url': 'https://api.github.com/',
    'request_token_url': None,
    'access_token_method': 'POST',
    'access_token_url': 'https://github.com/login/oauth/access_token',
    'authorize_url': 'https://github.com/login/oauth/authorize'
}

QQ_OAUTH = {
    'consumer_key': '101187283',  # QQ_APP_ID
    'consumer_secret': '993983549da49e384d03adfead8b2489',  # QQ_APP_KEY
    'base_url': 'https://graph.qq.com',
    'request_token_url': None,
    'request_token_params': {'scope': 'get_user_info'},
    'access_token_url': '/oauth2.0/token',
    'authorize_url': '/oauth2.0/authorize',
}

WEIBO_OAUTH = {
    'consumer_key': '909122383',
    'consumer_secret': '2cdc60e5e9e14398c1cbdf309f2ebd3a',
    'request_token_params': {'scope': 'email,statuses_to_me_read'},
    'base_url': 'https://api.weibo.com/2/',
    'authorize_url': 'https://api.weibo.com/oauth2/authorize',
    'request_token_url': None,
    'access_token_method': 'POST',
    'access_token_url': 'https://api.weibo.com/oauth2/access_token',
    # since weibo's response is a shit, we need to force parse the content
    'content_type': 'application/json',
}

if __name__ == '__main__':
    import os
    import binascii

    sk = os.urandom(24)
    print sk
    print binascii.b2a_hex(sk)
