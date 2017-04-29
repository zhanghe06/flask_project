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
from app_backend.forms.apply_put import ApplyPutSearchForm

from flask import Blueprint


bp_apply_put = Blueprint('apply_put', __name__, url_prefix='/apply_put')


@bp_apply_put.route('/list/')
@bp_apply_put.route('/list/<int:page>/')
@login_required
def lists(page=1):
    """
    投资申请列表
    """
    form = ApplyPutSearchForm(request.form)

    user_id = request.args.get('user_id', '', type=int)
    type_apply = request.args.get('type_apply', '', type=str)
    money_apply = request.args.get('money_apply', '', type=str)
    status_apply = request.args.get('status_apply', '', type=str)
    status_order = request.args.get('status_order', '', type=str)
    status_delete = request.args.get('status_delete', '', type=str)
    start_time = request.args.get('start_time', '', type=str)
    end_time = request.args.get('end_time', '', type=str)
    op = request.args.get('op', 0, type=int)

    form.user_id.data = user_id
    form.type_apply.data = type_apply
    form.money_apply.data = money_apply
    form.status_apply.data = status_apply
    form.status_order.data = status_order
    form.status_delete.data = status_delete
    form.start_time.data = start_time
    form.end_time.data = end_time

    pagination = get_apply_put_rows(page)
    return render_template('apply_put/list.html', title='apply_put_list', pagination=pagination, form=form)


@bp_apply_put.route('/add/', methods=['GET', 'POST'])
@login_required
def add():
    """
    创建投资申请
    :return:
    """
    return render_template('apply_put/add.html', title='apply_put_add')


@bp_apply_put.route('/del/', methods=['GET', 'POST'])
@login_required
def delete():
    """
    删除投资申请
    :return:
    """
    pass


@bp_apply_put.route('/stats/', methods=['GET', 'POST'])
@login_required
def stats():
    """
    投资申请统计
    :return:
    """
    pass
