#!/usr/bin/env python
# encoding: utf-8

"""
@author: zhanghe
@software: PyCharm
@file: user.py
@time: 2017/3/17 下午11:47
"""


from datetime import datetime
from flask import redirect
from flask import render_template, request, flash
from flask import url_for
from flask_login import current_user, login_required

from app_backend import app
from app_backend.forms.user import UserProfileForm
from app_backend.models import User
from app_backend.api.user import get_user_rows, get_user_detail_rows

from flask import Blueprint


bp_user = Blueprint('user', __name__, url_prefix='/user')


@bp_user.route('/list/')
@bp_user.route('/list/<int:page>/')
@login_required
def lists(page=1):
    """
    会员列表
    """
    pagination = get_user_detail_rows(page)
    return render_template('user/list.html', title='user_list', pagination=pagination)


@bp_user.route('/edit/profile/<int:user_id>/', methods=['GET', 'POST'])
@login_required
def edit_profile(user_id):
    """
    用户基本信息编辑
    """
    form = UserProfileForm(request.form)
    if request.method == 'GET':
        from app_backend.api.user import get_user_row_by_id
        user_info = get_user_row_by_id(user_id)
        if user_info:
            form.author.data = user_info.author
            form.title.data = user_info.title
            form.pub_date.data = user_info.pub_date
        else:
            return redirect(url_for('index'))
    if request.method == 'POST':
        if form.validate_on_submit():
            blog_info = {
                'author': form.author.data,
                'title': form.title.data,
                'pub_date': form.pub_date.data,
                'edit_time': datetime.utcnow(),
            }
            from app_frontend.api.blog import edit_blog
            result = edit_blog(blog_id, blog_info)
            if result == 1:
                flash(u'Edit Success', 'success')
                return redirect(request.args.get('next') or url_for('blog.index'))
            if result == 0:
                flash(u'Edit Failed', 'warning')
        flash(form.errors, 'warning')  # 调试打开
    flash(u'Hello, %s' % current_user.email, 'info')  # 测试打开
    return render_template('blog/edit.html', title='blog_edit', blog_id=blog_id, form=form)


@bp_user.route('/setting/', methods=['GET', 'POST'])
@login_required
def setting():
    """
    设置
    """
    # return "Hello, World!\nSetting!"
    form = UserProfileForm(request.form)
    if request.method == 'GET':
        from app_backend.api.user import get_user_row_by_id
        user_info = get_user_row_by_id(current_user.id)
        if user_info:
            form.nickname.data = user_info.nickname
            form.avatar_url.data = user_info.avatar_url
            form.email.data = user_info.email
            form.phone.data = user_info.phone
            form.birthday.data = user_info.birthday
            form.create_time.data = user_info.create_time
            form.update_time.data = user_info.update_time
            form.login_ip.data = user_info.last_ip
    if request.method == 'POST':
        if form.validate_on_submit():
            # todo 判断邮箱是否重复
            from app_backend.api.user import edit_user
            from datetime import datetime
            user_info = {
                'nickname': form.nickname.data,
                'avatar_url': form.avatar_url.data,
                'email': form.email.data,
                'phone': form.phone.data,
                'birthday': form.birthday.data,
                'update_time': datetime.utcnow(),
                'last_ip': request.headers.get('X-Forwarded-For', request.remote_addr),
            }
            result = edit_user(current_user.id, user_info)
            if result == 1:
                flash(u'Edit Success', 'success')
            if result == 0:
                flash(u'Edit Failed', 'warning')
        flash(form.errors, 'warning')  # 调试打开
    flash(u'Hello, %s' % current_user.email, 'info')  # 测试打开
    return render_template('./setting.html', title='setting', form=form)

