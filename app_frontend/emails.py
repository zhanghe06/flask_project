#!/usr/bin/env python
# encoding: utf-8

"""
@author: zhanghe
@software: PyCharm
@file: emails.py
@time: 16-3-11 下午2:35
"""


from app_frontend import app
from flask_mail import Mail, Message
mail = Mail(app)


def send_email(subject, sender, recipients, text_body=None, html_body=None):
    """
    发送邮件
    :param subject:
    :param sender:
    :param recipients:
    :param text_body:
    :param html_body:
    :return:
    """
    msg = Message(subject, sender=sender, recipients=recipients)
    msg.body = text_body
    msg.html = html_body
    mail.send(msg)


# 邮件服务调试
# 用 python 快速开启一个 SMTP 服务
"""
$ python -m smtpd -n -c DebuggingServer localhost:1025
假如想让程序运行于标准的 25 的端口上的话，必须使用 sudo 命令，因为只有 root 才能在 1-1024 端口上开启服务
$ sudo python -m smtpd -n -c DebuggingServer localhost:25
"""
