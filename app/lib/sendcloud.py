#!/usr/bin/env python
# encoding: utf-8

"""
@author: zhanghe
@software: PyCharm
@file: sendcloud.py
@time: 16-5-2 下午12:30
"""


import requests
import json


class SendCloud(object):
    """
    SendCloud 邮件发送平台
    以下方法采用 API v2 (区别：请求地址，参数命名规则)
    link: http://sendcloud.sohu.com/doc/email_v2/
    仅列出常用接口，实际使用中定制
    """
    def __init__(self, app=None):
        """
        初始化应用
        """
        self.app = app
        if app is not None:
            self._api_key = app.config.get('SENDCLOUD_API_KEY', '')
            self._api_user = app.config.get('SENDCLOUD_API_USER', '')

    def userinfo_get(self):
        """
        用户信息 查询
        """
        api_url = 'http://api.sendcloud.net/apiv2/userinfo/get'
        params = {
            'apiUser': self._api_user,
            'apiKey': self._api_key
        }
        return requests.get(api_url, params=params).json()

    def mail_send(self, mail_from, mail_to, mail_subject, mail_html):
        """
        普通发送
        """
        api_url = 'http://api.sendcloud.net/apiv2/mail/send'
        params = {
            'apiUser': self._api_user,      # API_USER
            'apiKey': self._api_key,        # API_KEY
            'from': mail_from,              # 发件人地址
            'to': mail_to,                  # 收件人地址. 多个地址使用';'分隔
            'subject': mail_subject,        # 邮件标题
            'html': mail_html,              # 邮件的内容. 邮件格式为 text/html
        }
        return requests.post(api_url, data=params).json()

    def mail_sendtemplate(self, mail_from, xsmtpapi, mail_subject, template_name):
        """
        模板发送 不用地址列表
        xsmtpapi = {
            'to': ['test1@ifaxin.com', 'test2@ifaxin.com'],
            'sub': {
                '%name%': ['user1', 'user2'],
                '%money%': ['1000', '2000'],
            }
        }
        """
        api_url = 'http://api.sendcloud.net/apiv2/mail/sendtemplate'
        params = {
            'apiUser': self._api_user,              # API_USER
            'apiKey': self._api_key,                # API_KEY
            'from': mail_from,                      # 发件人地址
            'xsmtpapi': json.dumps(xsmtpapi),       # SMTP 扩展字段
            'subject': mail_subject,                # 邮件标题
            'templateInvokeName': template_name,    # 邮件模板调用名称
        }
        return requests.post(api_url, data=params).json()

    def label_list(self, query, start=0, limit=100):
        """
        邮件标签 查询 ( 批量查询 )
        """
        api_url = 'http://api.sendcloud.net/apiv2/label/list'
        params = {
            'apiUser': self._api_user,
            'apiKey': self._api_key,
            'query': query,
            'start': start,
            'limit': limit
        }
        return requests.get(api_url, params=params).json()

    def addresslist_list(self, address, start=0, limit=100):
        """
        查询地址列表 ( 批量查询 )
        """
        api_url = 'http://api.sendcloud.net/apiv2/addresslist/list'
        params = {
            'apiUser': self._api_user,
            'apiKey': self._api_key,
            'address': address,
            'start': start,
            'limit': limit
        }
        return requests.get(api_url, params=params).json()


if __name__ == '__main__':
    pass
