#!/usr/bin/env python
# encoding: utf-8

"""
@author: zhanghe
@software: PyCharm
@file: apply_put.py
@time: 2017/4/13 下午9:32
"""


from datetime import datetime
from flask import redirect
from flask import render_template, request, flash, g
from flask import url_for
from flask_login import current_user, login_required

from app_backend import app
from app_backend.forms.admin import AdminProfileForm
from app_backend.models import User
from app_backend.api.apply_put import get_apply_put_rows, get_apply_put_row

from flask import Blueprint


bp_apply_put = Blueprint('apply_put', __name__, url_prefix='/apply_put')


@bp_apply_put.route('/list/')
@bp_apply_put.route('/list/<int:page>/')
@login_required
def lists(page=1):
    """
    投资申请列表
    """
    pagination = get_apply_put_rows(page)
    return render_template('apply_put/list.html', title='apply_put_list', pagination=pagination)


@bp_apply_put.route('/add/', methods=['GET', 'POST'])
@login_required
def add():
    """
    创建投资申请
    :return:
    """
    pass


@bp_apply_put.route('/del/', methods=['GET', 'POST'])
@login_required
def delete():
    """
    删除投资申请
    :return:
    """
    pass

