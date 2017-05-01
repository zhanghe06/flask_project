#!/usr/bin/env python
# encoding: utf-8

"""
@author: zhanghe
@software: PyCharm
@file: message.py
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
from app_frontend.api.message import get_message_rows, get_message_row
from app_common.maps.status_reply import STATUS_REPLY_DICT

from flask import Blueprint


bp_message = Blueprint('message', __name__, url_prefix='/message')


@bp_message.route('/send/list/')
@bp_message.route('/send/list/<int:page>/')
@login_required
def lists_send(page=1):
    """
    发送留言列表
    """
    uid = current_user.id
    condition = {
        'send_user_id': uid,
        'status_delete': 0
    }

    pagination = get_message_rows(page, **condition)
    return render_template('message/send_list.html', title='message_send_list', pagination=pagination)


@bp_message.route('/receive/list/')
@bp_message.route('/receive/list/<int:page>/')
@login_required
def lists_receive(page=1):
    """
    接收留言列表
    """
    uid = current_user.id
    condition = {
        'receive_user_id': uid,
        'status_delete': 0
    }

    pagination = get_message_rows(page, **condition)
    return render_template('message/receive_list.html', title='message_receive_list', pagination=pagination)


@bp_message.route('/add/', methods=['GET', 'POST'])
@login_required
def add():
    """
    创建留言
    :return:
    """
    pass


@bp_message.route('/del/', methods=['GET', 'POST'])
@login_required
def delete():
    """
    删除留言
    :return:
    """
    pass


@bp_message.route('/stats/', methods=['GET', 'POST'])
@login_required
def stats():
    """
    留言统计
    :return:
    """
    pass
