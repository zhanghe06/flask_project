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

from app_api.maps import area_code_list, role_admin_list
from app_backend.api.admin import get_admin_row
from app_backend.forms import SelectAreaCode, SelectBS


def reg_username_repeat(form, field):
    """
    登录账号重复校验
    """
    condition = {
        'username': field.data
    }
    row = get_admin_row(**condition)
    if row:
        raise ValidationError(u'登录账号重复')


class AdminProfileForm(Form):
    """
    管理员基本信息表单
    """
    username = StringField('User Name', validators=[DataRequired(), Length(min=2, max=20)])
    password = StringField('Password', validators=[DataRequired(), Length(min=6, max=20)])
    area_id = StringField('Area Id', validators=[DataRequired()])
    phone = StringField('Phone')
    role = StringField('Role')
    create_time = DateTimeField('Create Time')
    login_ip = StringField('Login Ip')
    login_time = DateTimeField('Login Time')


class AdminAddForm(Form):
    """
    管理员添加表单
    """
    username = StringField('User Name', validators=[DataRequired(), Length(min=2, max=20)])
    password = StringField('Password', validators=[DataRequired(), Length(min=6, max=20)])
    area_code_choices = []
    for m, n in enumerate(area_code_list):
        area_code_choices.append((m, n))
    area_id = SelectAreaCode('Area Id', default='0', choices=area_code_choices, validators=[DataRequired()])
    phone = StringField('Phone')
    role = SelectBS('Role', default='', choices=role_admin_list, validators=[DataRequired()])
    create_time = DateTimeField('Create Time')
    login_ip = StringField('Login Ip')
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

