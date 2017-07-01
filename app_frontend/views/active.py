#!/usr/bin/env python
# encoding: utf-8

"""
@author: zhanghe
@software: PyCharm
@file: active.py
@time: 2017/5/31 下午11:06
"""


from datetime import datetime
from flask import redirect
from flask import render_template, request, flash, g
from flask import url_for
from flask_login import current_user, login_required
from sqlalchemy.orm import aliased

from app_frontend import app
from app_frontend.api.active import give_active
from app_frontend.api.user_profile import get_team_tree
from app_frontend.api.user_profile import get_user_id_by_name
from app_frontend.models import User, UserProfile, ActiveItem
from app_frontend.api.active_item import get_active_item_rows
from app_common.maps.type_active import *
from app_frontend.forms.active import ActiveAddForm
from app_frontend.database import db

from flask import Blueprint

PER_PAGE_FRONTEND = app.config['PER_PAGE_FRONTEND']


bp_active = Blueprint('active', __name__, url_prefix='/active')


@bp_active.route('/list/')
@bp_active.route('/list/<int:page>/')
@login_required
def lists(page=1):
    """
    激活列表
    """
    user_id = current_user.id

    # 赠送、接收 状态
    active_status = request.args.get('active_status', 0, type=int)

    # 多次连接同一张表，需要别名
    user_profile_put = aliased(UserProfile)
    user_profile_get = aliased(UserProfile)

    # 接收
    if active_status == 1:
        condition = {
            'sc_id': user_id,
        }
    # 赠送、激活
    else:
        condition = {
            'user_id': user_id
        }
    try:
        pagination = ActiveItem.query. \
            filter_by(**condition). \
            outerjoin(user_profile_put, ActiveItem.user_id == user_profile_put.user_id). \
            add_entity(user_profile_put). \
            outerjoin(user_profile_get, ActiveItem.sc_id == user_profile_get.user_id). \
            add_entity(user_profile_get). \
            order_by(ActiveItem.id.desc()). \
            paginate(page, PER_PAGE_FRONTEND, False)

        # pagination = get_active_item_rows(page, PER_PAGE_FRONTEND, **condition)
        db.session.commit()
        return render_template('active/list.html', title='active_list', pagination=pagination)
    except Exception as e:
        db.session.rollback()
        flash(e.message, category='warning')
        return redirect(url_for('index'))


@bp_active.route('/add/', methods=['GET', 'POST'])
@login_required
def add():
    """
    添加激活记录
    :return:
    """
    # 获取团队成员三级树形结构
    team_tree = get_team_tree(current_user.id)

    user_name = request.args.get('user_name', '')

    form = ActiveAddForm(request.form)

    # 初始化表单的值
    if user_name:
        form.user_name.data = user_name
    if not form.amount.data:
        form.amount.data = 1

    if request.method == 'POST':
        if form.validate_on_submit():
            # 赠送激活数量
            try:
                user_id = get_user_id_by_name(form.user_name.data)
                result = give_active(current_user.id, user_id, form.amount.data)
                if result:
                    flash(u'赠送激活数量操作成功', 'success')
                return redirect(url_for('.lists'))
            except Exception as e:
                flash(e.message or u'赠送激活数量操作失败', 'warning')
        # 闪现消息 success info warning danger
        # flash(form.errors, 'warning')  # 调试打开
    return render_template('active/add.html', title='active_add', form=form, team_tree=team_tree)


@bp_active.route('/del/', methods=['GET', 'POST'])
@login_required
def delete():
    """
    删除激活
    :return:
    """
    pass


@bp_active.route('/stats/', methods=['GET', 'POST'])
@login_required
def stats():
    """
    激活统计
    :return:
    """
    pass
