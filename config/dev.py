#!/usr/bin/env python
# encoding: utf-8

"""
@author: zhanghe
@software: PyCharm
@file: dev.py
@time: 16-3-10 下午5:10
"""


import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__)+'/../')

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(BASE_DIR, 'flask.db')
SQLALCHEMY_TRACK_MODIFICATIONS = False

CSRF_ENABLED = True
SECRET_KEY = '\x03\xabjR\xbbg\x82\x0b{\x96f\xca\xa8\xbdM\xb0x\xdbK%\xf2\x07\r\x8c'

# 开发环境邮箱配置
MAIL_SERVER = 'smtp.163.com',
MAIL_PORT = 25,
MAIL_USERNAME = 'xxxxxx@163.com',
MAIL_PASSWORD = 'xxxxxx',
MAIL_DEFAULT_SENDER = (u'系统邮箱', 'zhang_he06@163.com')
# 后台管理人员邮件列表
ADMINS = ['455091702@qq.com']

if __name__ == '__main__':
    import os
    import binascii

    sk = os.urandom(24)
    print sk
    print binascii.b2a_hex(sk)
