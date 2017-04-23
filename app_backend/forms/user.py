#!/usr/bin/env python
# encoding: utf-8

"""
@author: zhanghe
@software: PyCharm
@file: user.py
@time: 2017/3/17 下午11:49
"""


from flask_wtf import FlaskForm as Form
from wtforms import StringField, PasswordField, BooleanField, DateField, DateTimeField
from wtforms.validators import DataRequired, Length, NumberRange, EqualTo, Email, ValidationError, IPAddress
from app_backend.api.user_auth import get_user_auth_row


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
    nickname = StringField('Nick Name', validators=[DataRequired(), Length(min=2, max=20)])
    avatar_url = StringField('Avatar Url')
    email = StringField('Email', validators=[DataRequired()])
    phone = StringField('Phone')
    birthday = DateField('Birthday')
    create_time = DateTimeField('Create Time')
    update_time = DateTimeField('Update Time')
    login_ip = StringField('Login Ip', validators=[IPAddress()])
    login_time = DateTimeField('Login Time')


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


class UserSearchForm(Form):
    """
    用户搜索表单
    """
    user_id = StringField('User Id')
    user_name = StringField('User Name')
    start_time = StringField('Start Time')
    end_time = StringField('End Time')
