#!/usr/bin/env python
# encoding: utf-8

"""
@author: zhanghe
@software: PyCharm
@file: reg.py
@time: 2017/3/10 下午10:49
"""


from flask_wtf import FlaskForm as Form
from wtforms import StringField, PasswordField, BooleanField, DateField, DateTimeField, SelectField
from wtforms.validators import DataRequired, Length, NumberRange, EqualTo, Email, ValidationError, IPAddress, Regexp, AnyOf
from wtforms.widgets import HTMLString

from app_frontend.api.user_auth import get_user_auth_row
from wtforms.widgets import html_params
from wtforms.compat import text_type, iteritems
try:
    from html import escape
except ImportError:
    from cgi import escape
import re
from app_api.maps import area_code_list

from app_api.maps.auth_type import *
# 认证类型（0未知，1邮箱，2手机，3qq，4微信，5微博）


def select_multi_checkbox(field, ul_class='', **kwargs):
    """
    多选框控件
    :param field:
    :param ul_class:
    :param kwargs:
    :return:
    """
    kwargs.setdefault('type', 'checkbox')
    field_id = kwargs.pop('id', field.id)
    html = [u'<ul %s>' % html_params(id=field_id, class_=ul_class)]
    for value, label, checked in field.iter_choices():
        choice_id = u'%s-%s' % (field_id, value)
        options = dict(kwargs, name=field.name, value=value, id=choice_id)
        if checked:
            options['checked'] = 'checked'
        html.append(u'<li><input %s /> ' % html_params(**options))
        html.append(u'<label for="%s">%s</label></li>' % (field_id, label))
    html.append(u'</ul>')
    return u''.join(html)


class SelectBSWidget(object):
    """
    自定义选择组件
    """
    def __call__(self, field, **kwargs):
        params = {
            'id': field.id,
            'name': field.id,
            'class': 'selectpicker show-tick',
            'data-live-search': 'true',
            'title': 'Choose one of the following...',
            'data-header': 'Select a condiment',
        }
        html = ['<select %s>' % html_params(**params)]
        for _, area_data in field.choices:
            for area_name, area_list in area_data.items():
                html.append('\t<optgroup label="%s">' % area_name)
                for country_data in area_list:
                    html.append('\t\t<option value="%s" data-subtext="%s(%s)">[%s] %s</option>' % (country_data['id'], country_data['name_c'], country_data['name_e'], country_data['short_code'], country_data['phone_pre']))
                html.append('\t</optgroup>')
        html.append('</select>')
        return HTMLString('\n'.join(html))


class SelectBS(SelectField):
    """
    自定义选择表单控件
    """
    widget = SelectBSWidget()

    def pre_validate(self, form):
        """
        校验表单传值是否合法
        """
        is_find = False
        for _, area_data in self.choices:
            for area_list in area_data.values():
                if self.data in [str(i['id']) for i in area_list]:
                    is_find = True
                    break
            if is_find:
                break
        else:
            raise ValueError(self.gettext('Not a valid choice'))


def reg_account_repeat(form, field):
    """
    账号重复校验
    """
    condition = {
        'auth_type': AUTH_TYPE_ACCOUNT,
        'auth_key': field.data
    }
    row = get_user_auth_row(**condition)
    if row:
        raise ValidationError(u'注册账号重复')


def reg_email_repeat(form, field):
    """
    邮箱重复校验
    """
    condition = {
        'auth_type': AUTH_TYPE_EMAIL,
        'auth_key': field.data
    }
    row = get_user_auth_row(**condition)
    if row:
        raise ValidationError(u'注册邮箱重复')


class UserNameValidate(object):
    """
    用户名称校验
    """
    def __init__(self, message=None):
        self.message = message
        self._reg = re.compile(ur'^[a-zA-Z0-9\u4e00-\u9fa5\s]+$')

    def __call__(self, form, field):
        data = field.data
        if not self._reg.match(data):
            raise ValidationError(self.message or u"用户名称只能包含中文和英文")


class ChineseNameValidate(object):
    """
    中文姓名校验
    """
    def __init__(self, message=None):
        self.message = message
        self._reg = re.compile(ur'^[\u4e00-\u9fa5]+$')

    def __call__(self, form, field):
        data = field.data
        if not self._reg.match(data):
            raise ValidationError(self.message or u"请输入正确的中文姓名")


def reg_phone_repeat(form, field):
    """
    手机重复校验
    """
    condition = {
        'auth_type': AUTH_TYPE_PHONE,
        'auth_key': field.data
    }
    row = get_user_auth_row(**condition)
    if row:
        raise ValidationError(u'注册手机重复')


class RegForm(Form):
    """
    注册表单
    """
    account = StringField('Account', validators=[DataRequired(), Email(), reg_account_repeat])
    password = PasswordField('New Password', validators=[
        DataRequired(),
        Length(min=6, max=40),
        EqualTo('confirm', message='Passwords must match')
    ])
    confirm = PasswordField('Confirmation Password', validators=[
        DataRequired(),
        Length(min=6, max=40)
    ])
    accept_agreement = BooleanField('I accept the agreement', validators=[DataRequired()], default=False)


class RegPhoneForm(Form):
    """
    手机注册表单
    """
    area_code_choices = []
    for m, n in enumerate(area_code_list):
        area_code_choices.append((m, n))

    area_code = SelectBS('Area Code', default='0', choices=area_code_choices, validators=[DataRequired()])
    phone = StringField('Phone', validators=[DataRequired(), Email(), reg_phone_repeat])
    captcha = StringField('Captcha', validators=[
        DataRequired(),
        Length(min=4, max=4, message='Captcha must match')
    ])
    sms = StringField('Sms', validators=[
        DataRequired(),
        Length(min=6, max=6, message='Sms out of range')
    ])
    password = PasswordField('New Password', validators=[
        DataRequired(),
        Length(min=6, max=40, message='Passwords out of range'),
        EqualTo('confirm', message='Passwords must match')
    ])
    confirm = PasswordField('Confirmation Password', validators=[
        DataRequired(),
        Length(min=6, max=40)
    ])
    accept_agreement = BooleanField('I accept the agreement', validators=[DataRequired()], default=False)


class RegEmailForm(Form):
    """
    邮箱注册表单
    """
    email = StringField('Email', validators=[DataRequired(), Email(), reg_email_repeat])
    password = PasswordField('New Password', validators=[
        DataRequired(),
        Length(min=6, max=40),
        EqualTo('confirm', message='Passwords must match')
    ])
    confirm = PasswordField('Confirmation Password', validators=[
        DataRequired(),
        Length(min=6, max=40)
    ])
    accept_agreement = BooleanField('I accept the agreement', validators=[DataRequired()], default=False)
