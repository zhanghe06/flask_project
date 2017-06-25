#!/usr/bin/env python
# encoding: utf-8

"""
@author: zhanghe
@software: PyCharm
@file: message.py
@time: 2017/6/24 下午10:45
"""


from flask_login import current_user
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, PasswordField, BooleanField, DateField, DateTimeField, DecimalField, IntegerField, HiddenField
from wtforms.validators import DataRequired, Length, NumberRange, EqualTo, Email, ValidationError, IPAddress


class MessageAddForm(FlaskForm):
    """
    留言添加表单
    """
    user_id = StringField(u'留言给用户')
    content = TextAreaField(u'留言内容', validators=[
        DataRequired(message=u'留言内容不能为空'),
        Length(min=2, message=u'请输入有效的留言内容'),
        Length(max=512, message=u'留言内容超出长度限制'),
    ])
