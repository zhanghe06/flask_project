#!/usr/bin/env python
# encoding: utf-8

"""
@author: zhanghe
@software: PyCharm
@file: login.py
@time: 2017/3/10 下午10:49
"""


import re
from flask import session
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, DateField, DateTimeField
from wtforms.validators import DataRequired, Length, NumberRange, EqualTo, Email, ValidationError, IPAddress
from app_backend.api.user_auth import get_user_auth_row


class SmsCodeValidate(object):
    """
    短信验证码校验
    """
    def __init__(self, message=None):
        self.message = message

        self._reg = re.compile(ur'^\d{6}$')

    def __call__(self, form, field):
        data = field.data
        if not self._reg.match(data):
            raise ValidationError(self.message or u"短信验证码格式错误")

        code_key = '%s:%s' % ('sms_code', 'login')
        # print session.get(code_key), type(session.get(code_key)), data, type(data)
        if session.get(code_key) != data:
            raise ValidationError(self.message or u"短信验证码校验错误")


class LoginForm(FlaskForm):
    """
    账号登录表单
    """
    account = StringField(u'登录账号', validators=[
        DataRequired(u'登录账号不能为空'),
        Length(min=2, max=20, message=u'登录账号长度不符')
    ])
    password = PasswordField(u'登录密码', validators=[
        DataRequired(u'密码不能为空'),
        Length(min=6, max=20, message=u'密码长度不符')
    ])
    sms = StringField(u'短信验证码', validators=[
        DataRequired(u'短信验证码不能为空'),
        Length(min=6, max=6, message=u'短信验证码长度不符'),
        SmsCodeValidate()
    ])
    remember = BooleanField('Remember Me', default=False)
