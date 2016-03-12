#!/usr/bin/env python
# encoding: utf-8

"""
@author: zhanghe
@software: PyCharm
@file: server.py
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

if __name__ == '__main__':
    import os
    import binascii

    sk = os.urandom(24)
    print sk
    print binascii.b2a_hex(sk)
