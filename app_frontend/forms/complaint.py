#!/usr/bin/env python
# encoding: utf-8

"""
@author: zhanghe
@software: PyCharm
@file: complaint.py
@time: 2017/6/24 下午11:13
"""


from flask_login import current_user
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, PasswordField, BooleanField, DateField, DateTimeField, DecimalField, IntegerField, HiddenField
from wtforms.validators import DataRequired, Length, NumberRange, EqualTo, Email, ValidationError, IPAddress


class ComplaintAddForm(FlaskForm):
    """
    投诉添加表单
    """
    user_id = StringField(u'被投诉用户')
    content = TextAreaField(u'投诉内容', validators=[
        DataRequired(message=u'投诉内容不能为空'),
        Length(min=2, message=u'请输入有效的投诉内容'),
        Length(max=512, message=u'投诉内容超出长度限制'),
    ])
