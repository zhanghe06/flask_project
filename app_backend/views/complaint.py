#!/usr/bin/env python
# encoding: utf-8

"""
@author: zhanghe
@software: PyCharm
@file: complaint.py
@time: 2017/4/30 下午10:31
"""


import json
from datetime import datetime

from flask import abort
from flask import redirect
from flask import render_template, request, flash, g
from flask import url_for
from flask_login import current_user, login_required
import flask_excel as excel
from sqlalchemy.orm import aliased

from app_backend import app
from app_backend.database import db
from app_backend.forms.admin import AdminProfileForm
from app_backend.models import User, UserProfile, Complaint
from app_backend.api.order import get_order_rows, get_order_row
from app_backend.forms.order import OrderSearchForm
from app_backend.api.complaint import edit_complaint, get_complaint_row_by_id

from app_backend.forms.complaint import ComplaintReplyForm

from flask import Blueprint

from app_backend.permissions import permission_msg
from app_common.maps.status_delete import STATUS_DEL_OK
from app_common.maps.status_reply import STATUS_REPLY_DICT, STATUS_REPLY_SUCCESS
from config import PER_PAGE_BACKEND

bp_complaint = Blueprint('complaint', __name__, url_prefix='/complaint')


@bp_complaint.route('/list/', methods=['GET', 'POST'])
@bp_complaint.route('/list/<int:page>/', methods=['GET', 'POST'])
@login_required
@permission_msg.require(http_exception=403)
def lists(page=1):
    """
    投诉列表
    :return:
    """
    condition = {
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
            paginate(page, PER_PAGE_BACKEND, False)
        db.session.commit()
        return render_template('complaint/list.html', title='complaint_list', pagination=pagination)
    except Exception as e:
        db.session.rollback()
        flash(e.message, category='warning')
        return redirect(url_for('index'))


@bp_complaint.route('/reply/<int:complaint_id>/', methods=['GET', 'POST'])
@login_required
@permission_msg.require(http_exception=403)
def reply(complaint_id):
    """
    投诉处理
    :param complaint_id:
    :return:
    """
    complaint_info = get_complaint_row_by_id(complaint_id)
    form = ComplaintReplyForm(request.form)
    if complaint_info:
        if request.method == 'GET':
            form.send_user_id.data = complaint_info.send_user_id
            form.receive_user_id.data = complaint_info.receive_user_id
            form.content.data = complaint_info.content
    if request.method == 'POST':
        if form.validate_on_submit():
            current_time = datetime.utcnow()
            complaint_data = {
                'content_reply': form.content_reply.data,
                'status_reply': STATUS_REPLY_SUCCESS,
                'reply_time': current_time,
                'update_time': current_time,
            }
            result = edit_complaint(complaint_id, complaint_data)
            if result:
                flash(u'处理投诉成功', 'success')
                return redirect(url_for('.lists', msg_type='send'))
            else:
                flash(u'处理投诉失败', 'warning')
        flash(u'处理投诉失败', 'warning')
    return render_template('complaint/reply.html', title='complaint_reply', form=form)


@bp_complaint.route('/ajax/del/', methods=['GET', 'POST'])
@login_required
@permission_msg.require(http_exception=403)
def ajax_delete():
    """
    删除投诉
    :return:
    """
    if request.method == 'GET' and request.is_xhr:
        msg_id = request.args.get('msg_id', 0, type=int)
        if not msg_id:
            return json.dumps({'error': u'删除失败'})
        current_time = datetime.utcnow()
        msg_data = {
            'status_delete': STATUS_DEL_OK,
            'delete_time': current_time,
            'update_time': current_time
        }
        result = edit_complaint(msg_id, msg_data)
        if result == 1:
            return json.dumps({'success': u'删除成功'})
        if result == 0:
            return json.dumps({'error': u'删除失败'})
    abort(404)
