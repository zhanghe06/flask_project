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

from app_frontend import app
from app_frontend.models import User, UserProfile
from app_frontend.api.complaint import get_complaint_rows, get_complaint_row
from app_common.maps.status_reply import STATUS_REPLY_DICT


from flask import Blueprint


bp_complaint = Blueprint('complaint', __name__, url_prefix='/complaint')


@bp_complaint.route('/list/')
@bp_complaint.route('/list/<int:page>/')
@login_required
def lists(page=1):
    """
    投诉列表
    """
    uid = current_user.id
    condition = {
        'send_user_id': uid,
        'status_reply': 0,  # 默认未处理
        'status_delete': 0
    }
    # 回复状态
    status_reply = request.args.get('status_reply', 0, type=int)
    if status_reply in STATUS_REPLY_DICT:
        condition['status_reply'] = status_reply

    pagination = get_complaint_rows(page, **condition)
    return render_template('complaint/list.html', title='complaint_list', pagination=pagination)


@bp_complaint.route('/add/', methods=['GET', 'POST'])
@login_required
def add():
    """
    创建投诉
    :return:
    """
    pass


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
