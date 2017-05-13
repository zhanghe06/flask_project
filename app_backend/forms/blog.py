#!/usr/bin/env python
# encoding: utf-8

"""
@author: zhanghe
@software: PyCharm
@file: blog.py
@time: 2017/3/10 下午11:00
"""


from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, DateField, DateTimeField
from wtforms.validators import DataRequired, Length, NumberRange, EqualTo, Email, ValidationError, IPAddress


class BlogAddForm(FlaskForm):
    """
    Blog 添加表单
    """
    author = StringField('Author', validators=[DataRequired()])
    title = StringField('Title', validators=[DataRequired(), Length(max=40)])
    pub_date = DateField('Pub Date', validators=[DataRequired()])


class BlogEditForm(FlaskForm):
    """
    Blog 编辑表单
    """
    author = StringField('Author', validators=[DataRequired()])
    title = StringField('Title', validators=[DataRequired(), Length(max=40)])
    pub_date = DateField('Pub Date', validators=[DataRequired()])
