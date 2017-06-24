#!/usr/bin/env python
# encoding: utf-8

"""
@author: zhanghe
@software: PyCharm
@file: message.py
@time: 2017/5/1 上午2:17
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
from app_backend.forms.admin import AdminProfileForm
from app_backend.models import User, UserProfile, Message
from app_backend.api.message import edit_message

from flask import Blueprint
from app_backend.database import db
from app_common.maps.status_delete import STATUS_DEL_OK
from config import PER_PAGE_BACKEND

from app_backend.permissions import permission_msg


bp_message = Blueprint('message', __name__, url_prefix='/message')


@bp_message.route('/list/', methods=['GET', 'POST'])
@bp_message.route('/list/<int:page>/', methods=['GET', 'POST'])
@login_required
@permission_msg.require(http_exception=403)
def lists(page=1):
    """
    留言列表
    """
    # 多次连接同一张表，需要别名
    user_profile_put = aliased(UserProfile)
    user_profile_get = aliased(UserProfile)

    condition = {
        'status_delete': 0
    }
    try:
        pagination = Message.query. \
            filter_by(**condition). \
            outerjoin(user_profile_put, Message.send_user_id == user_profile_put.user_id). \
            add_entity(user_profile_put). \
            outerjoin(user_profile_get, Message.receive_user_id == user_profile_get.user_id). \
            add_entity(user_profile_get). \
            order_by(Message.id.desc()). \
            paginate(page, PER_PAGE_BACKEND, False)
        db.session.commit()
        return render_template('message/list.html', title='message_list', pagination=pagination)
    except Exception as e:
        db.session.rollback()
        flash(e.message, category='warning')
        return redirect(url_for('index'))


@bp_message.route('/ajax/del/', methods=['GET', 'POST'])
@login_required
@permission_msg.require(http_exception=403)
def ajax_delete():
    """
    删除用户
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
        result = edit_message(msg_id, msg_data)
        if result == 1:
            return json.dumps({'success': u'删除成功'})
        if result == 0:
            return json.dumps({'error': u'删除失败'})
    abort(404)
