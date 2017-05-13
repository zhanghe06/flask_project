#!/usr/bin/env python
# encoding: utf-8

"""
@author: zhanghe
@software: PyCharm
@file: user.py
@time: 2017/3/17 下午11:49
"""


from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, DateField, DateTimeField, HiddenField
from wtforms.validators import DataRequired, Length, NumberRange, EqualTo, Email, ValidationError, IPAddress

from app_common.maps import area_code_list
from app_frontend.api.user_auth import get_user_auth_row
from app_frontend.api.user_profile import get_user_profile_row
from app_frontend.forms import SelectAreaCode, CheckBoxBS


def reg_email_repeat(form, field):
    """
    邮箱重复校验
    """
    condition = {
        'type_auth': 'email',
        'auth_key': field.data
    }
    row = get_user_auth_row(**condition)
    if row:
        raise ValidationError(u'注册邮箱重复')


class PhoneFormatValidate(object):
    """
    手机号码格式校验
    """
    def __init__(self, message=None):
        self.message = message

    def __call__(self, form, field):
        phone_len = len(field.data)
        if phone_len < 6 or phone_len > 11:
            raise ValidationError(u'手机号码长度不符')
        # 中国手机号码格式校验
        if form.area_id.data == '0' and phone_len != 11:
            raise ValidationError(u'手机号码长度不符')
        if field.data.startswith('0'):
            raise ValidationError(u'手机号码格式不符')


class PhoneRepeatValidate(object):
    """
    手机重复校验
    """
    def __init__(self, message=None):
        self.message = message

    def __call__(self, form, field):
        condition = {
            'area_id': form.area_id.data,
            'phone': field.data
        }
        row = get_user_profile_row(**condition)

        if row:
            raise ValidationError(self.message or u'手机号码重复')


class UserProfileForm(FlaskForm):
    """
    用户基本信息表单
    """
    user_pid = StringField(u'推荐人')
    nickname = StringField(u'用户名称')
    avatar_url = StringField(u'用户头像')
    email = StringField(u'电子邮箱')
    area_code_choices = []
    for m, n in enumerate(area_code_list):
        area_code_choices.append((m, n))
    area_id = SelectAreaCode(u'手机区号', default='0', choices=area_code_choices, validators=[DataRequired()])
    area_code = StringField('Area Code')
    phone = StringField(u'手机号码', validators=[
        DataRequired(u'手机号码不能为空'),
        PhoneFormatValidate(),
        PhoneRepeatValidate()
    ])
    birthday = DateField(u'出生日期')
    id_card = StringField(u'身份证号', validators=[
        DataRequired(u'身份证号不能为空'),
        Length(min=18, max=18, message=u'身份证号长度不符')
    ])
    create_time = DateTimeField(u'创建时间')
    update_time = DateTimeField(u'修改时间')


class UserAuthForm(FlaskForm):
    """
    用户登录认证信息表单
    """
    id = HiddenField('Id', validators=[DataRequired()])
    type_auth = StringField(u'账号类型')
    auth_key = StringField(u'登录账号')
    auth_secret = StringField(u'登录密码')
    status_verified = CheckBoxBS(u'认证状态')
    create_time = DateTimeField(u'创建时间')
    update_time = DateTimeField(u'更新时间')


class UserBankForm(FlaskForm):
    """
    用户基本银行信息表单
    """
    account_name = StringField(u'账户姓名', validators=[
        DataRequired(u'账户姓名不能为空'),
        Length(min=2, max=4, message=u'账户姓名长度不符'),
    ])
    bank_name = StringField(u'银行名称', validators=[DataRequired(u'银行名称不能为空')])
    bank_address = StringField(u'支行名称', validators=[DataRequired(u'支行名称不能为空')])
    bank_account = StringField(u'银行卡号', validators=[DataRequired(u'银行卡号不能为空')])
    status_verified = CheckBoxBS(u'认证状态')
    status_delete = StringField(u'删除状态')
    create_time = DateTimeField(u'创建时间')
    update_time = DateTimeField(u'更新时间')


class EditPassword(FlaskForm):
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

