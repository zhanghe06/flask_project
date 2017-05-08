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
from app_backend.api.user_auth import get_user_auth_row
from app_backend.forms import SelectBS, CheckBoxBS
from app_common.maps import status_lock_list
from app_common.maps import status_active_list
from app_common.maps import area_code_list
from app_backend.api.user_auth import get_user_auth_row
from app_backend.forms import SelectAreaCode


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
    user_id = HiddenField('User Id', validators=[DataRequired()])
    user_pid = StringField(u'推荐人ID', validators=[DataRequired()])
    nickname = StringField(u'用户名称')
    avatar_url = StringField(u'用户头像')
    email = StringField(u'电子邮箱')
    area_code_choices = []
    for m, n in enumerate(area_code_list):
        area_code_choices.append((m, n))
    area_id = SelectAreaCode(u'手机区号', default='0', choices=area_code_choices, validators=[DataRequired()])
    area_code = StringField('Area Code')
    phone = StringField(u'手机号码')
    birthday = DateField(u'出生日期')
    id_card = StringField(u'身份证号')
    create_time = DateTimeField(u'创建时间')
    update_time = DateTimeField(u'修改时间')


class UserAuthForm(Form):
    """
    用户登录认证信息表单
    """
    id = HiddenField('Id', validators=[DataRequired()])
    user_id = HiddenField('User Id', validators=[DataRequired()])
    type_auth = StringField(u'账号类型')
    auth_key = StringField(u'登录账号')
    auth_secret = StringField(u'登录密码')
    status_verified = CheckBoxBS(u'认证状态')
    create_time = DateTimeField(u'创建时间')
    update_time = DateTimeField(u'更新时间')


class UserBankForm(Form):
    """
    用户基本银行信息表单
    """
    user_id = HiddenField(u'用户ID', validators=[DataRequired()])
    account_name = StringField(u'账户姓名')
    bank_name = StringField(u'银行名称')
    bank_address = StringField(u'支行名称')
    bank_account = StringField(u'银行卡号')
    status_verified = CheckBoxBS(u'认证状态')
    status_delete = StringField(u'删除状态')
    create_time = DateTimeField(u'创建时间')
    update_time = DateTimeField(u'更新时间')


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
    user_id = StringField(u'用户ID')
    user_name = StringField(u'用户名称')
    start_time = StringField('Start Time')
    end_time = StringField('End Time')
    status_active = SelectBS('Status Active', default='', choices=status_active_list)
    status_lock = SelectBS('Status Lock', default='', choices=status_lock_list)
