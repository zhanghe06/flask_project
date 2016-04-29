#!/usr/bin/env python
# encoding: utf-8

"""
@author: zhanghe
@software: PyCharm
@file: forms.py
@time: 16-1-7 下午1:11
"""


from flask.ext.wtf import Form
from wtforms import StringField, PasswordField, BooleanField, DateField, DateTimeField
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


class BlogAddForm(Form):
    """
    Blog 添加表单
    """
    author = StringField('Author', validators=[DataRequired()])
    title = StringField('Title', validators=[DataRequired(), Length(max=40)])
    pub_date = DateField('Pub Date', validators=[DataRequired()])


class BlogEditForm(Form):
    """
    Blog 编辑表单
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


class UserForm(Form):
    """
    用户表单
    """
    nickname = StringField('Nick Name', validators=[DataRequired(), Length(min=2, max=20)])
    avatar_url = StringField('Avatar Url')
    email = StringField('Email', validators=[DataRequired()])
    phone = StringField('Phone')
    birthday = DateField('Birthday')
    create_time = DateTimeField('Create Time')
    update_time = DateTimeField('Update Time')
    last_ip = StringField('Last Ip')


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
