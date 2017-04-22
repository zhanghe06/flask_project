#!/usr/bin/env python
# encoding: utf-8

"""
@author: zhanghe
@software: PyCharm
@file: admin.py
@time: 2017/4/22 下午5:02
"""


from datetime import datetime
from flask import redirect
from flask import render_template, request, flash, g
from flask import url_for
from flask_login import current_user, login_required

from app_backend import app
from app_backend.forms.admin import AdminProfileForm
from app_backend.models import User
from app_backend.api.admin import get_admin_rows, get_admin_row

from flask import Blueprint


bp_admin = Blueprint('admin', __name__, url_prefix='/admin')


@bp_admin.route('/profile/')
@login_required
def profile():
    """
    当前登录管理员信息
    :return:
    """
    login_user_id = g.user.get_id()
    return login_user_id
    # get_admin_row()


def add():
    pass


@bp_admin.route('/list/')
@bp_admin.route('/list/<int:page>/')
@login_required
def lists(page=1):
    """
    会员列表
    """
    pagination = get_admin_rows(page)
    return render_template('admin/list.html', title='admin_list', pagination=pagination)

