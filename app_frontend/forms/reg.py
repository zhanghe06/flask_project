#!/usr/bin/env python
# encoding: utf-8

"""
@author: zhanghe
@software: PyCharm
@file: reg.py
@time: 2017/3/10 下午10:49
"""


from flask import session
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
from app_common.maps import area_code_list, area_code_map

from app_common.maps.type_auth import *
# 认证类型（0未知，1邮箱，2手机，3qq，4微信，5微博）


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

        code_key = '%s:%s' % ('sms_code', 'reg')
        # print session.get(code_key), type(session.get(code_key)), data, type(data)
        if session.get(code_key) != data:
            raise ValidationError(self.message or u"短信验证码校验错误")


class RegAccountRepeatValidate(object):
    """
    注册账号重复校验
    """
    def __init__(self, message=None):
        self.message = message

    def __call__(self, form, field):
        condition = {
            'type_auth': TYPE_AUTH_ACCOUNT,
            'auth_key': field.data
        }
        row = get_user_auth_row(**condition)
        if row:
            raise ValidationError(self.message or u'注册账号重复')


class RegEmailRepeatValidate(object):
    """
    注册邮箱重复校验
    """
    def __init__(self, message=None):
        self.message = message

    def __call__(self, form, field):
        condition = {
            'type_auth': TYPE_AUTH_EMAIL,
            'auth_key': field.data
        }
        row = get_user_auth_row(**condition)
        if row:
            raise ValidationError(self.message or u'注册邮箱重复')


class RegPhoneRepeatValidate(object):
    """
    注册手机重复校验
    """
    def __init__(self, message=None):
        self.message = message

    def __call__(self, form, field):
        # 手机号码国际化
        area_id = form['area_id'].data
        area_code = area_code_map.get(area_id, '86')
        mobile_iso = '%s%s' % (area_code, field.data)

        condition = {
            'type_auth': TYPE_AUTH_PHONE,
            'auth_key': mobile_iso
        }
        row = get_user_auth_row(**condition)

        if row:
            raise ValidationError(self.message or u'注册手机重复')


class RegForm(Form):
    """
    注册表单
    """
    account = StringField(u'登陆账号', validators=[DataRequired(), RegAccountRepeatValidate()])
    password = PasswordField(u'登录密码', validators=[
        DataRequired(message=u'密码不能为空'),
        Length(min=6, max=20, message=u'密码长度不符'),
        EqualTo('confirm', message=u'两次输入的密码不一致')
    ])
    confirm = PasswordField(u'确认密码', validators=[
        DataRequired(message=u'密码不能为空'),
        Length(min=6, max=20, message=u'密码长度不符'),
    ])
    user_pid = HiddenField('User Pid', default='0')
    accept_agreement = BooleanField('I accept the agreement', validators=[
        DataRequired(message=u'请阅读并同意注册协议')
    ], default=True)


class RegPhoneForm(Form):
    """
    手机注册表单
    """
    area_code_choices = []
    for m, n in enumerate(area_code_list):
        area_code_choices.append((m, n))

    area_id = SelectAreaCode(u'手机区号', default='0', choices=area_code_choices, validators=[DataRequired()])
    phone = StringField(u'手机号码', validators=[
        DataRequired(u'手机号码不能为空'),
        RegPhoneRepeatValidate(u'手机已被注册')
    ])
    captcha = StringField(u'图形验证码', validators=[
        DataRequired(),
        Length(min=4, max=4, message=u'图形验证码长度不符')
    ])
    sms = StringField(u'短信验证码', validators=[
        DataRequired(u'短信验证码不能为空'),
        Length(min=6, max=6, message=u'短信验证码长度不符'),
        SmsCodeValidate()
    ])
    password = PasswordField(u'登陆密码', validators=[
        DataRequired(u'密码不能为空'),
        Length(min=6, max=20, message=u'密码长度不符'),
        EqualTo('confirm', message=u'两次输入的密码不一致')
    ])
    confirm = PasswordField(u'确认密码', validators=[
        DataRequired(u'密码不能为空'),
        Length(min=6, max=20, message=u'密码长度不符')
    ])
    user_pid = HiddenField('User Pid', default='0')
    accept_agreement = BooleanField(u'我已阅读并同意注册协议', validators=[DataRequired(u'请阅读并同意注册协议')], default=True)


class RegEmailForm(Form):
    """
    邮箱注册表单
    """
    email = StringField(u'登陆邮箱', validators=[
        DataRequired(u'登陆邮箱不能为空'),
        Email(u'邮箱格式不对'),
        RegEmailRepeatValidate(u'邮箱已被注册')
    ])
    password = PasswordField(u'登陆密码', validators=[
        DataRequired(u'密码不能为空'),
        Length(min=6, max=20, message=u'密码长度不符'),
        EqualTo('confirm', message=u'两次输入的密码不一致')
    ])
    confirm = PasswordField(u'确认密码', validators=[
        DataRequired(u'密码不能为空'),
        Length(min=6, max=20, message=u'密码长度不符')
    ])
    user_pid = HiddenField('User Pid', default='0')
    accept_agreement = BooleanField(u'我已阅读并同意注册协议', validators=[DataRequired(u'请阅读并同意注册协议')], default=True)
