#!/usr/bin/env python
# encoding: utf-8

"""
@author: zhanghe
@software: PyCharm
@file: __init__.py.py
@time: 2017/3/10 下午10:56
"""


import os

from flask import render_template, request, redirect
from flask import send_from_directory, g, flash, url_for
from flask_login import current_user
from itsdangerous import URLSafeSerializer, BadSignature

from app_frontend import app, login_manager

# cache = SimpleCache()  # 默认最大支持500个key, 超时时间5分钟, 参数可配置


@login_manager.user_loader
def load_user(user_id):
    """
    如果 user_id 无效，它应该返回 None （ 而不是抛出异常 ）。
    :param user_id:
    :return:
    """
    from app_frontend.login import LoginUser
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
    from app_frontend import app
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'img/favicon.ico', mimetype='image/vnd.microsoft.icon')


@app.route('/index/')
@app.route('/')
def index():
    """
    网站首页
    """
    # return "Hello, World!"
    # 判断是否推广链接
    i = request.args.get('i', '')
    if i:
        try:
            s = URLSafeSerializer(app.config.get('USER_INVITE_LINK_SIGN_KEY', ''))
            link_param = s.loads(i)
            # 如果未登陆，或登陆用户打开的不是自己的推广链接
            if not current_user.get_id() or current_user.get_id() != link_param.get('user_id'):
                # 跳转注册页面
                return redirect(url_for('auth.phone'))
        except BadSignature as e:
            flash(u'Invite Link Failed, %s' % e.message, 'warning')
        except Exception as e:
            flash(e.message, 'warning')
    return render_template('index.html', title='home')


@app.route('/about/')
def about():
    """
    关于网站
    """
    # return "Hello, World!\nAbout!"
    return render_template('about.html', title='about')


@app.route('/contact/')
def contact():
    """
    联系方式
    """
    # return "Hello, World!\nContact!"
    return render_template('contact.html', title='contact')


@app.route('/search/', methods=['GET', 'POST'])
def search():
    """
    搜索
    """
    return 'search result!'


@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404


@app.errorhandler(500)
def internal_error(error):
    from app_frontend.database import db
    db.session.rollback()
    return render_template('500.html'), 500

