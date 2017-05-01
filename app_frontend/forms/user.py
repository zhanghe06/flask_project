#!/usr/bin/env python
# encoding: utf-8

"""
@author: zhanghe
@software: PyCharm
@file: user.py
@time: 2017/3/17 下午11:49
"""


from flask_wtf import FlaskForm as Form
from wtforms import StringField, PasswordField, BooleanField, DateField, DateTimeField, HiddenField
from wtforms.validators import DataRequired, Length, NumberRange, EqualTo, Email, ValidationError, IPAddress

from app_common.maps import area_code_list
from app_frontend.api.user_auth import get_user_auth_row
from app_frontend.forms import SelectAreaCode


def reg_email_repeat(form, field):
    """
    邮箱重复校验
    """
    condition = {
        'auth_type': 'email',
        'auth_key': field.data
    }
    row = get_user_auth_row(**condition)
    if row:
        raise ValidationError(u'注册邮箱重复')


class UserProfileForm(Form):
    """
    用户基本信息表单
    """
    user_pid = StringField('User Pid', validators=[DataRequired()])
    nickname = StringField('Nick Name')
    avatar_url = StringField('Avatar Url')
    email = StringField('Email')
    area_code_choices = []
    for m, n in enumerate(area_code_list):
        area_code_choices.append((m, n))
    area_id = SelectAreaCode('Area Id', default='0', choices=area_code_choices, validators=[DataRequired()])
    area_code = StringField('Area Code')
    phone = StringField('Phone')
    birthday = DateField('Birthday')
    id_card = StringField('ID Card')
    create_time = DateTimeField('Create Time')
    update_time = DateTimeField('Update Time')


class UserAuthForm(Form):
    """
    用户登录认证信息表单
    """
    id = HiddenField('Id', validators=[DataRequired()])
    auth_type = StringField('Auth Type')
    auth_key = StringField('Auth Key')
    auth_secret = StringField('Auth Secret')
    status_verified = StringField('Status Verified')
    create_time = DateTimeField('Create Time')
    update_time = DateTimeField('Update Time')


class UserBankForm(Form):
    """
    用户基本银行信息表单
    """
    account_name = StringField('Account Name')
    bank_name = StringField('Bank Name')
    bank_address = StringField('Bank Address')
    bank_account = StringField('Bank Account')
    status_verified = StringField('Status Verified')
    status_delete = StringField('Status Delete')
    create_time = DateTimeField('Create Time')
    update_time = DateTimeField('Update Time')


class EditPassword(Form):
    """
    修改用户密码
    """
    password = PasswordField('New Password', validators=[
        DataRequired(),
        Length(min=6, max=40),
        EqualTo('confirm', message='Passwords must match')
    ])
    confirm = PasswordField('Repeat Password', validators=[
        DataRequired(),
        Length(min=6, max=40)
    ])

