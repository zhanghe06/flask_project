#!/usr/bin/env python
# encoding: utf-8

"""
@author: zhanghe
@software: PyCharm
@file: login.py
@time: 2017/3/10 下午10:49
"""


from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, DateField, DateTimeField
from wtforms.validators import DataRequired, Length, NumberRange, EqualTo, Email, ValidationError, IPAddress
from app_backend.api.user_auth import get_user_auth_row


class LoginForm(FlaskForm):
    """
    账号登录表单
    """
    account = StringField('Account', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    sms = StringField('Sms', validators=[
        DataRequired(),
        Length(min=6, max=6, message='Sms out of range')
    ])
    remember = BooleanField('Remember Me', default=False)
