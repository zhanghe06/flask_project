#!/usr/bin/env python
# encoding: utf-8

"""
@author: zhanghe
@software: PyCharm
@file: reg.py
@time: 2017/3/10 下午10:49
"""


from flask_wtf import FlaskForm as Form
from wtforms import StringField, PasswordField, BooleanField, DateField, DateTimeField, SelectField, HiddenField
from wtforms.validators import DataRequired, Length, NumberRange, EqualTo, Email, ValidationError, IPAddress, Regexp, AnyOf
from app_frontend.forms import SelectAreaCode

from app_frontend.api.user_auth import get_user_auth_row


try:
    from html import escape
except ImportError:
    from cgi import escape
import re
from app_common.maps import area_code_list

from app_common.maps.auth_type import *
# 认证类型（0未知，1邮箱，2手机，3qq，4微信，5微博）


def reg_account_repeat(form, field):
    """
    账号重复校验
    """
    condition = {
        'auth_type': AUTH_TYPE_ACCOUNT,
        'auth_key': field.data
    }
    row = get_user_auth_row(**condition)
    if row:
        raise ValidationError(u'注册账号重复')


def reg_email_repeat(form, field):
    """
    邮箱重复校验
    """
    condition = {
        'auth_type': AUTH_TYPE_EMAIL,
        'auth_key': field.data
    }
    row = get_user_auth_row(**condition)
    if row:
        raise ValidationError(u'注册邮箱重复')


class UserNameValidate(object):
    """
    用户名称校验
    """
    def __init__(self, message=None):
        self.message = message
        self._reg = re.compile(ur'^[a-zA-Z0-9\u4e00-\u9fa5\s]+$')

    def __call__(self, form, field):
        data = field.data
        if not self._reg.match(data):
            raise ValidationError(self.message or u"用户名称只能包含中文和英文")


class ChineseNameValidate(object):
    """
    中文姓名校验
    """
    def __init__(self, message=None):
        self.message = message
        self._reg = re.compile(ur'^[\u4e00-\u9fa5]+$')

    def __call__(self, form, field):
        data = field.data
        if not self._reg.match(data):
            raise ValidationError(self.message or u"请输入正确的中文姓名")


def reg_phone_repeat(form, field):
    """
    手机重复校验
    """
    condition = {
        'auth_type': AUTH_TYPE_PHONE,
        'auth_key': field.data
    }
    row = get_user_auth_row(**condition)
    if row:
        raise ValidationError(u'注册手机重复')


class RegForm(Form):
    """
    注册表单
    """
    account = StringField('Account', validators=[DataRequired(), reg_account_repeat])
    password = PasswordField('New Password', validators=[
        DataRequired(),
        Length(min=6, max=20),
        EqualTo('confirm', message='Passwords must match')
    ])
    confirm = PasswordField('Confirmation Password', validators=[
        DataRequired(),
        Length(min=6, max=20)
    ])
    user_pid = HiddenField('User Pid', default='0')
    accept_agreement = BooleanField('I accept the agreement', validators=[DataRequired()], default=False)


class RegPhoneForm(Form):
    """
    手机注册表单
    """
    area_code_choices = []
    for m, n in enumerate(area_code_list):
        area_code_choices.append((m, n))

    area_id = SelectAreaCode('Area Id', default='0', choices=area_code_choices, validators=[DataRequired()])
    phone = StringField('Phone', validators=[DataRequired(), Email(), reg_phone_repeat])
    captcha = StringField('Captcha', validators=[
        DataRequired(),
        Length(min=4, max=4, message='Captcha must match')
    ])
    sms = StringField('Sms', validators=[
        DataRequired(),
        Length(min=6, max=6, message='Sms out of range')
    ])
    password = PasswordField('New Password', validators=[
        DataRequired(),
        Length(min=6, max=20, message='Passwords out of range'),
        EqualTo('confirm', message='Passwords must match')
    ])
    confirm = PasswordField('Confirmation Password', validators=[
        DataRequired(),
        Length(min=6, max=20)
    ])
    user_pid = HiddenField('User Pid', default='0')
    accept_agreement = BooleanField('I accept the agreement', validators=[DataRequired()], default=False)


class RegEmailForm(Form):
    """
    邮箱注册表单
    """
    email = StringField('Email', validators=[DataRequired(), Email(), reg_email_repeat])
    password = PasswordField('New Password', validators=[
        DataRequired(),
        Length(min=6, max=20),
        EqualTo('confirm', message='Passwords must match')
    ])
    confirm = PasswordField('Confirmation Password', validators=[
        DataRequired(),
        Length(min=6, max=20)
    ])
    user_pid = HiddenField('User Pid', default='0')
    accept_agreement = BooleanField('I accept the agreement', validators=[DataRequired()], default=False)
