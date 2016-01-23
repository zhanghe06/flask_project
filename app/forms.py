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
from wtforms.validators import DataRequired, Length, NumberRange, EqualTo, Email


class RegForm(Form):
    """
    注册表单
    """
    email = StringField('Account(Email)', validators=[DataRequired(), Email()])
    password = PasswordField('New Password', validators=[
        DataRequired(),
        Length(min=6, max=40),
        EqualTo('confirm', message='Passwords must match')
    ])
    confirm = PasswordField('Repeat Password', validators=[
        DataRequired(),
        Length(min=6, max=40)
    ])
    accept_agreement = BooleanField('I accept the agreement', validators=[DataRequired()], default=False)


class LoginForm(Form):
    """
    登陆表单
    """
    email = StringField('Account(Email)', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me', default=False)


class BlogForm(Form):
    """
    Blog 表单
    """
    author = StringField('Author', validators=[DataRequired()])
    title = StringField('Title', validators=[DataRequired(), Length(max=40)])
    pub_date = DateField('Pub Date', validators=[DataRequired()])


class AuthorForm(Form):
    """
    作者表单
    """
    name = StringField('Name', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired()])
