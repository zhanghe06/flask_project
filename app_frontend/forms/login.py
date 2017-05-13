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
from app_frontend.api.user_auth import get_user_auth_row
from app_frontend.forms import SelectAreaCode
from app_common.maps import area_code_list


class LoginForm(FlaskForm):
    """
    账号登录表单
    """
    account = StringField(u'登录账号', validators=[
        DataRequired(u'登录账号不能为空'),
        Length(min=2, max=20, message=u'登录账号长度不符'),
    ])
    password = PasswordField(u'登录密码', validators=[
        DataRequired(u'登录密码不能为空'),
        Length(min=6, max=20, message=u'登录密码长度不符'),
    ])
    remember = BooleanField(u'记住登录状态', default=False)


class LoginPhoneForm(FlaskForm):
    """
    手机登录表单
    """
    area_code_choices = []
    for m, n in enumerate(area_code_list):
        area_code_choices.append((m, n))

    area_id = SelectAreaCode(u'手机区号', default='0', choices=area_code_choices, validators=[DataRequired()])
    phone = StringField(u'登录手机', validators=[DataRequired(u'登录手机不能为空')])
    password = PasswordField(u'登录密码', validators=[
        DataRequired(u'登录密码不能为空'),
        Length(min=6, max=20, message=u'登录密码长度不符'),
    ])
    remember = BooleanField(u'记住登录状态', default=False)


class LoginEmailForm(FlaskForm):
    """
    邮箱登录表单
    """
    email = StringField(u'登录邮箱', validators=[
        DataRequired(u'登录邮箱不能为空'),
        Email(u'登录邮箱格式不符')
    ])
    password = PasswordField(u'登录密码', validators=[
        DataRequired(u'登录密码不能为空'),
        Length(min=6, max=20, message=u'登录密码长度不符'),
    ])
    remember = BooleanField(u'记住登录状态', default=False)
