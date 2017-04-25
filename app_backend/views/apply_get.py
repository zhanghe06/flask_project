#!/usr/bin/env python
# encoding: utf-8

"""
@author: zhanghe
@software: PyCharm
@file: apply_get.py
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
from app_backend.api.apply_get import get_apply_get_rows, get_apply_get_row
from app_backend.forms.apply_get import ApplyGetSearchForm

from flask import Blueprint


bp_apply_get = Blueprint('apply_get', __name__, url_prefix='/apply_get')


@bp_apply_get.route('/list/')
@bp_apply_get.route('/list/<int:page>/')
@login_required
def lists(page=1):
    """
    提现申请列表
    """
    form = ApplyGetSearchForm(request.form)

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

    pagination = get_apply_get_rows(page)
    return render_template('apply_get/list.html', title='apply_get_list', pagination=pagination, form=form)


@bp_apply_get.route('/add/', methods=['GET', 'POST'])
@login_required
def add():
    """
    创建提现申请
    :return:
    """
    pass


@bp_apply_get.route('/del/', methods=['GET', 'POST'])
@login_required
def delete():
    """
    删除提现申请
    :return:
    """
    pass


@bp_apply_get.route('/stats/', methods=['GET', 'POST'])
@login_required
def stats():
    """
    提现申请统计
    :return:
    """
    pass
