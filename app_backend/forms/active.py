#!/usr/bin/env python
# encoding: utf-8

"""
@author: zhanghe
@software: PyCharm
@file: active.py
@time: 2017/6/1 下午2:42
"""


from flask_login import current_user
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, DateField, DateTimeField, DecimalField, IntegerField
from wtforms.validators import DataRequired, Length, NumberRange, EqualTo, Email, ValidationError, IPAddress

from app_common.maps.status_delete import *
from app_common.maps.type_auth import *
from app_backend.api.user import get_user_row_by_id
from app_backend.api.user_auth import get_user_auth_row
from app_backend.api.user_profile import get_user_profile_row_by_id


class UserRightValidate(object):
    """
    用户权限校验
    """
    def __init__(self, message=None):
        self.message = message

    def __call__(self, form, field):
        # 用户异常处理
        user_info = get_user_row_by_id(field.data)

        if not user_info:
            raise ValidationError(u'异常操作，此用户不存在')
        if user_info.status_delete == int(STATUS_DEL_OK):
            raise ValidationError(u'异常操作，此用户已删除')

        user_profile_info = get_user_profile_row_by_id(field.data)
        if not user_profile_info:
            raise ValidationError(u'异常操作，此用户不存在')


class ActiveAddForm(FlaskForm):
    """
    激活添加表单
    """
    user_id = StringField(u'赠送用户ID', validators=[
        DataRequired(message=u'赠送用户ID不能为空'),
        UserRightValidate()
    ])
    amount = IntegerField(u'赠送数量', validators=[
        DataRequired(message=u'赠送数量必须为整数'),
        NumberRange(min=1, message=u'赠送数量必须为整数')
    ])


