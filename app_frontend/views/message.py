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
from sqlalchemy.orm import aliased

from app_frontend import app
from app_frontend.models import User, UserProfile, Message
from app_frontend.api.message import get_message_rows, get_message_row, add_message
from app_common.maps.status_reply import STATUS_REPLY_DICT

from app_frontend.forms.message import MessageAddForm

from flask import Blueprint

from app_frontend.database import db

PER_PAGE_FRONTEND = app.config['PER_PAGE_FRONTEND']

bp_message = Blueprint('message', __name__, url_prefix='/message')


@bp_message.route('/list/')
@bp_message.route('/list/<int:page>/')
@login_required
def lists(page=1):
    """
    留言列表
    """
    user_id = current_user.id
    msg_type = request.args.get('msg_type', 'rec')

    # 多次连接同一张表，需要别名
    user_profile_put = aliased(UserProfile)
    user_profile_get = aliased(UserProfile)

    # 发送
    if msg_type == 'send':
        condition = {
            'send_user_id': user_id,
            'status_delete': 0
        }
    # 接收
    else:
        condition = {
            'receive_user_id': user_id,
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
            paginate(page, PER_PAGE_FRONTEND, False)
        db.session.commit()
        return render_template('message/list.html', title='message_list', pagination=pagination)
    except Exception as e:
        db.session.rollback()
        flash(e.message, category='warning')
        return redirect(url_for('index'))


@bp_message.route('/add/', methods=['GET', 'POST'])
@login_required
def add():
    """
    创建留言
    :return:
    """
    form = MessageAddForm(request.form)
    user_id = request.args.get('user_id')
    form.user_id.data = user_id
    if request.method == 'POST':
        if form.validate_on_submit():
            current_time = datetime.utcnow()
            msg_data = {
                'send_user_id': current_user.id,
                'receive_user_id': form.user_id.data,
                'content': form.content.data,
                'create_time': current_time,
                'update_time': current_time,
            }
            result = add_message(msg_data)
            if result:
                flash(u'留言成功', 'success')
                return redirect(url_for('.lists', msg_type='send'))
            else:
                flash(u'留言失败', 'warning')
        flash(u'留言失败', 'warning')
    return render_template('message/add.html', title='message_add', form=form)


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
