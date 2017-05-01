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

from app_common.maps import area_code_list, role_admin_list
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


def password_edit_validator(form, field):
    """
    密码修改表单校验
    :param form:
    :param field:
    :return:
    """
    field_data_length = len(field.data) if field.data else 0
    if field_data_length > 0 and (field_data_length < 6 or field_data_length > 20):
        raise ValidationError(u'密码长度不符')


class AdminProfileForm(Form):
    """
    管理员基本信息表单
    """
    id = HiddenField('Id')
    username = StringField('User Name', validators=[DataRequired(), Length(min=2, max=20)])
    password = StringField('Password', validators=[password_edit_validator])
    area_code_choices = []
    for m, n in enumerate(area_code_list):
        area_code_choices.append((m, n))
    area_id = SelectAreaCode('Area Id', default='0', choices=area_code_choices, validators=[DataRequired()])
    phone = StringField('Phone')
    role = SelectBS('Role', default='', choices=role_admin_list, validators=[DataRequired()])
    login_ip = StringField('Login Ip')
    login_time = DateTimeField('Login Time')
    create_time = DateTimeField('Create Time')
    update_time = DateTimeField('Update Time')


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
    login_ip = StringField('Login Ip')
    login_time = DateTimeField('Login Time')


class AdminEditForm(Form):
    """
    管理员编辑表单
    """
    id = HiddenField('Id')
    username = StringField('User Name', validators=[DataRequired(), Length(min=2, max=20)])
    password = StringField('Password', validators=[password_edit_validator])
    area_code_choices = []
    for m, n in enumerate(area_code_list):
        area_code_choices.append((m, n))
    area_id = SelectAreaCode('Area Id', default='0', choices=area_code_choices, validators=[DataRequired()])
    phone = StringField('Phone')
    role = SelectBS('Role', default='', choices=role_admin_list, validators=[DataRequired()])
    login_ip = StringField('Login Ip')
    login_time = DateTimeField('Login Time')
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

