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

from app_common.maps.type_scheduling import TYPE_SCHEDULING_USER, TYPE_SCHEDULING_GIVE
from app_frontend import app
from app_frontend.api.scheduling import get_scheduling_row_by_id
from app_frontend.api.scheduling_item import get_scheduling_item_item_rows

from flask import Blueprint

from app_frontend.database import db
from app_frontend.models import UserProfile, SchedulingItem

from config import PER_PAGE_FRONTEND

bp_scheduling = Blueprint('scheduling', __name__, url_prefix='/scheduling')


@bp_scheduling.route('/list/')
@bp_scheduling.route('/list/<int:page>/')
@login_required
def lists(page=1):
    """
    排单列表
    """
    user_id = current_user.id
    # （1：用户排单、2：系统发送）
    scheduling_type = request.args.get('scheduling_list', 0, int)

    # 多次连接同一张表，需要别名
    user_profile_put = aliased(UserProfile)
    user_profile_get = aliased(UserProfile)

    if scheduling_type == 1:
        condition = [
            SchedulingItem.type == TYPE_SCHEDULING_USER,
            SchedulingItem.sc_id == user_id
        ]
    elif scheduling_type == 2:
        condition = [
            SchedulingItem.type == TYPE_SCHEDULING_GIVE,
            SchedulingItem.sc_id == user_id
        ]
    else:
        condition = [SchedulingItem.sc_id == user_id]

    try:
        pagination = SchedulingItem.query. \
            outerjoin(user_profile_put, SchedulingItem.user_id == user_profile_put.user_id). \
            add_entity(user_profile_put). \
            outerjoin(user_profile_get, SchedulingItem.sc_id == user_profile_get.user_id). \
            add_entity(user_profile_get). \
            filter(*condition). \
            order_by(SchedulingItem.id.desc()). \
            paginate(page, PER_PAGE_FRONTEND, False)
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
    创建积分
    :return:
    """
    pass


@bp_scheduling.route('/del/', methods=['GET', 'POST'])
@login_required
def delete():
    """
    删除积分
    :return:
    """
    pass


@bp_scheduling.route('/stats/', methods=['GET', 'POST'])
@login_required
def stats():
    """
    积分统计
    :return:
    """
    pass
