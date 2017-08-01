#!/usr/bin/env python
# encoding: utf-8

"""
@author: zhanghe
@software: PyCharm
@file: complaint.py
@time: 2017/4/29 下午2:28
"""


from datetime import datetime
from flask import redirect
from flask import render_template, request, flash, g
from flask import url_for
from flask_login import current_user, login_required
import flask_excel as excel
from sqlalchemy.orm import aliased

from app_frontend import app
from app_frontend.database import db
from app_frontend.forms.complaint import ComplaintAddForm
from app_frontend.models import User, UserProfile, Complaint
from app_frontend.api.complaint import get_complaint_rows, get_complaint_row, add_complaint
from app_common.maps.status_reply import STATUS_REPLY_DICT


from flask import Blueprint

PER_PAGE_FRONTEND = app.config['PER_PAGE_FRONTEND']

bp_complaint = Blueprint('complaint', __name__, url_prefix='/complaint')


@bp_complaint.route('/list/')
@bp_complaint.route('/list/<int:page>/')
@login_required
def lists(page=1):
    """
    投诉列表
    """
    user_id = current_user.id
    condition = {
        'send_user_id': user_id,
        'status_reply': 0,  # 默认未处理
        'status_delete': 0
    }
    # 回复状态
    status_reply = request.args.get('status_reply', 0, type=int)
    if status_reply in STATUS_REPLY_DICT:
        condition['status_reply'] = status_reply

    # pagination = get_complaint_rows(page, **condition)
    # return render_template('complaint/list.html', title='complaint_list', pagination=pagination)

    # 多次连接同一张表，需要别名
    user_profile_put = aliased(UserProfile)
    user_profile_get = aliased(UserProfile)
    try:
        pagination = Complaint.query. \
            filter_by(**condition). \
            outerjoin(user_profile_put, Complaint.send_user_id == user_profile_put.user_id). \
            add_entity(user_profile_put). \
            outerjoin(user_profile_get, Complaint.receive_user_id == user_profile_get.user_id). \
            add_entity(user_profile_get). \
            order_by(Complaint.id.desc()). \
            paginate(page, PER_PAGE_FRONTEND, False)
        db.session.commit()
        return render_template('complaint/list.html', title='complaint_list', pagination=pagination)
    except Exception as e:
        db.session.rollback()
        flash(e.message, category='warning')
        return redirect(url_for('index'))


@bp_complaint.route('/add/', methods=['GET', 'POST'])
@login_required
def add():
    """
    创建投诉
    :return:
    """
    form = ComplaintAddForm(request.form)
    user_id = request.args.get('user_id')
    form.user_id.data = user_id
    if request.method == 'POST':
        if form.validate_on_submit():
            current_time = datetime.utcnow()
            complaint_data = {
                'send_user_id': current_user.id,
                'receive_user_id': user_id,
                'content': form.content.data,
                'create_time': current_time,
                'update_time': current_time,
            }
            result = add_complaint(complaint_data)
            if result:
                flash(u'投诉成功', 'success')
                return redirect(url_for('.lists', msg_type='send'))
            else:
                flash(u'投诉失败', 'warning')
        flash(u'投诉失败', 'warning')
    return render_template('complaint/add.html', title='complaint_add', form=form)


@bp_complaint.route('/del/', methods=['GET', 'POST'])
@login_required
def delete():
    """
    删除投诉
    :return:
    """
    pass


@bp_complaint.route('/stats/', methods=['GET', 'POST'])
@login_required
def stats():
    """
    投诉统计
    :return:
    """
    pass
