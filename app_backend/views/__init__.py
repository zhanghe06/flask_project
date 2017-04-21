#!/usr/bin/env python
# encoding: utf-8

"""
@author: zhanghe
@software: PyCharm
@file: __init__.py.py
@time: 2017/3/10 下午10:56
"""


import os

from flask import send_from_directory
from flask_login import current_user

from flask import g, request, render_template, jsonify
from flask import session, redirect, url_for, flash
from flask_login import login_user
from flask_login import logout_user

from app_backend import app, oauth_github, oauth_qq, oauth_weibo
from app_api.maps.auth_type import *

from app_backend import app, login_manager

# cache = SimpleCache()  # 默认最大支持500个key, 超时时间5分钟, 参数可配置


@login_manager.user_loader
def load_user(user_id):
    """
    如果 user_id 无效，它应该返回 None （ 而不是抛出异常 ）。
    :param user_id:
    :return:
    """
    from app_backend.login import LoginUser
    return LoginUser.query.get(int(user_id))


@app.before_request
def before_request():
    """
    当前用户信息
    """
    g.user = current_user


@app.route('/favicon.ico')
def favicon():
    """
    首页ico图标
    """
    from app_backend import app
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'img/favicon.ico', mimetype='image/vnd.microsoft.icon')


@app.route('/')
@app.route('/index/')
def index():
    """
    后台首页
    """
    # return "Hello, World!"
    return render_template('index.html', title='home')


@app.route('/login/')
def login():
    """
    后台登录页面
    """
    if g.user is not None and g.user.is_authenticated:
        return redirect(url_for('index'))
    from app_backend.forms.login import LoginForm
    form = LoginForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            from app_backend.api.admin import get_user_auth_row
            condition = {
                'auth_type': AUTH_TYPE_ACCOUNT,
                'auth_key': form.account.data,
                'auth_secret': form.password.data
            }
            user_auth_info = get_user_auth_row(**condition)
            if user_auth_info is None:
                flash(u'%s, You were logged failed' % form.account.data, 'warning')
                return render_template('login.html', title='login', form=form)
            if user_auth_info.verified == 0:
                flash(u'%s, Please verify email address in mailbox' % form.account.data, 'warning')
                return render_template('login.html', title='login', form=form)
            # session['logged_in'] = True
            # 用户通过验证后，记录登入IP
            from app_backend.api.user import edit_user
            edit_user(user_auth_info.user_id, {'last_ip': request.headers.get('X-Forwarded-For', request.remote_addr)})
            # 用 login_user 函数来登入他们
            from app_backend.api.user import get_user_row_by_id
            login_user(get_user_row_by_id(user_auth_info.user_id))
            flash(u'%s, You were logged in' % form.account.data, 'success')
            return redirect(request.args.get('next') or url_for('index'))
        flash(form.errors, 'warning')  # 调试打开
    return render_template('login.html', title='login', form=form)


@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404


@app.errorhandler(500)
def internal_error(error):
    from app_backend.database import db
    db.session.rollback()
    return render_template('500.html'), 500

