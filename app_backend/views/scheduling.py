#!/usr/bin/env python
# encoding: utf-8

"""
@author: zhanghe
@software: PyCharm
@file: scheduling.py
@time: 2017/6/29 下午8:45
"""


from datetime import datetime
from flask import redirect
from flask import render_template, request, flash, g
from flask import url_for
from flask_login import current_user, login_required
from sqlalchemy.orm import aliased

from app_backend import app
from app_backend.api.scheduling import give_scheduling
from app_backend.models import User, UserProfile, SchedulingItem
from app_backend.api.active_item import get_active_item_rows
from app_common.maps.type_scheduling import *
from app_backend.forms.scheduling import SchedulingAddForm
from app_backend.database import db

PER_PAGE_BACKEND = app.config['PER_PAGE_BACKEND']

from flask import Blueprint


bp_scheduling = Blueprint('scheduling', __name__, url_prefix='/scheduling')


@bp_scheduling.route('/list/')
@bp_scheduling.route('/list/<int:page>/')
@login_required
def lists(page=1):
    """
    排单列表
    """
    # （1：用户排单、2：系统发送）
    scheduling_type = request.args.get('scheduling_list', 0, int)

    # 多次连接同一张表，需要别名
    user_profile_put = aliased(UserProfile)
    user_profile_get = aliased(UserProfile)

    if scheduling_type == 1:
        condition = [
            SchedulingItem.type == TYPE_SCHEDULING_USER
        ]
    elif scheduling_type == 2:
        condition = [
            SchedulingItem.type == TYPE_SCHEDULING_GIVE
        ]
    else:
        condition = []

    try:
        pagination = SchedulingItem.query. \
            outerjoin(user_profile_put, SchedulingItem.user_id == user_profile_put.user_id). \
            add_entity(user_profile_put). \
            outerjoin(user_profile_get, SchedulingItem.sc_id == user_profile_get.user_id). \
            add_entity(user_profile_get). \
            filter(*condition). \
            order_by(SchedulingItem.id.desc()). \
            paginate(page, PER_PAGE_BACKEND, False)
        db.session.commit()
        return render_template('scheduling/list.html', title='scheduling_list', pagination=pagination)
    except Exception as e:
        db.session.rollback()
        flash(e.message, category='warning')
        return redirect(url_for('index'))


@bp_scheduling.route('/add/', methods=['GET', 'POST'])
@login_required
def add():
    """
    添加排单记录
    :return:
    """
    user_id = request.args.get('user_id', '', type=int)

    form = SchedulingAddForm(request.form)

    # 初始化表单的值
    if user_id:
        form.user_id.data = user_id
    if not form.amount.data:
        form.amount.data = 1

    if request.method == 'POST':
        if form.validate_on_submit():
            # 赠送排单数量
            try:
                result = give_scheduling(form.user_id.data, form.amount.data)
                if result:
                    flash(u'赠送排单数量操作成功', 'success')
                return redirect(url_for('.lists'))
            except Exception as e:
                flash(e.message or u'赠送排单数量操作失败', 'warning')
        # 闪现消息 success info warning danger
        # flash(form.errors, 'warning')  # 调试打开
    return render_template('scheduling/add.html', title='scheduling_add', form=form)


@bp_scheduling.route('/del/', methods=['GET', 'POST'])
@login_required
def delete():
    """
    删除排单
    :return:
    """
    pass


@bp_scheduling.route('/stats/', methods=['GET', 'POST'])
@login_required
def stats():
    """
    排单统计
    :return:
    """
    pass
