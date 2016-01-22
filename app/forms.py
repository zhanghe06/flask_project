#!/usr/bin/env python
# encoding: utf-8

"""
@author: zhanghe
@software: PyCharm
@file: forms.py
@time: 16-1-7 下午1:11
"""


from flask.ext.wtf import Form
from wtforms import StringField, PasswordField, BooleanField, DateField
from wtforms.validators import DataRequired


class LoginForm(Form):
    """
    登陆表单
    """
    username = StringField('username', validators=[DataRequired()])
    password = PasswordField('password', validators=[DataRequired()])
    remember = BooleanField('remember', default=False)


class BlogForm(Form):
    """
    Blog 表单
    """
    author = StringField('author', validators=[DataRequired()])
    title = StringField('title', validators=[DataRequired()])
    pub_date = DateField('pub_date', validators=[DataRequired()])


class AuthorForm(Form):
    """
    作者表单
    """
    name = StringField('name', validators=[DataRequired()])
    email = StringField('email', validators=[DataRequired()])
