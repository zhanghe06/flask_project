#!/usr/bin/env python
# encoding: utf-8

"""
@author: zhanghe
@software: PyCharm
@file: auth.py
@time: 2017/3/10 下午11:44
"""

import json

from flask import g, request, render_template, jsonify
from flask import session, redirect, url_for, flash
from flask_login import login_user
from flask_login import logout_user

from app_frontend import app, oauth_github, oauth_qq, oauth_weibo

from flask import Blueprint


bp_auth = Blueprint('auth', __name__, url_prefix='/auth')


@bp_auth.route('/login/', methods=['GET', 'POST'])
def login():
    """
    登录
    """
    if g.user is not None and g.user.is_authenticated:
        return redirect(url_for('index'))
    from app_frontend.forms.login import LoginForm
    form = LoginForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            from app_frontend.api.user_auth import get_user_auth_row
            condition = {
                'auth_type': 'email',
                'auth_key': form.email.data,
                'auth_secret': form.password.data
            }
            user_auth_info = get_user_auth_row(**condition)
            if user_auth_info is None:
                flash(u'%s, You were logged failed' % form.email.data, 'warning')
                return render_template('auth/login.html', title='login', form=form)
            if user_auth_info.verified == 0:
                flash(u'%s, Please verify email address in mailbox' % form.email.data, 'warning')
                return render_template('auth/login.html', title='login', form=form)
            # session['logged_in'] = True
            # 用户通过验证后，记录登入IP
            from app_frontend.api.user import edit_user
            edit_user(user_auth_info.user_id, {'last_ip': request.headers.get('X-Forwarded-For', request.remote_addr)})
            # 用 login_user 函数来登入他们
            from app_frontend.api.user import get_user_row_by_id
            login_user(get_user_row_by_id(user_auth_info.user_id))
            flash(u'%s, You were logged in' % form.email.data, 'success')
            return redirect(request.args.get('next') or url_for('index'))
        flash(form.errors, 'warning')  # 调试打开
    return render_template('auth/login.html', title='login', form=form)


# @app.route('/logout')
# def logout():
#     session.pop('logged_in', None)
#     flash(u'You were logged out')
#     return redirect(url_for('index'))

@bp_auth.route('/logout/')
def logout():
    """
    退出登录
    """
    logout_user()
    session.pop('qq_token', None)
    session.pop('weibo_token', None)
    session.pop('github_token', None)
    flash(u'You were logged out', 'info')
    return redirect(url_for('index'))


# # 第三方登陆（QQ）
def json_to_dict(x):
    """
    OAuthResponse class can't not parse the JSON data with content-type
    text/html, so we need reload the JSON data manually
    :param x:
    :return:
    """
    if x.find('callback') > -1:
        pos_lb = x.find('{')
        pos_rb = x.find('}')
        x = x[pos_lb:pos_rb + 1]
    try:
        return json.loads(x, encoding='utf-8')
    except:
        return x


def update_qq_api_request_data(data={}):
    """
    Update some required parameters for OAuth2.0 API calls
    :param data:
    :return:
    """
    defaults = {
        'openid': session.get('qq_openid'),
        'access_token': session.get('qq_token')[0],
        'oauth_consumer_key': app.config['consumer_key'],
    }
    defaults.update(data)
    return defaults


@bp_auth.route('/user_info')
def get_user_info():
    if 'qq_token' in session:
        data = update_qq_api_request_data()
        resp = oauth_qq.get('/user/get_user_info', data=data)
        return jsonify(status=resp.status, data=resp.data)
    return redirect(url_for('login_qq'))


@bp_auth.route('/login/qq/')
def login_qq():
    return oauth_qq.authorize(callback=url_for('auth.authorized_qq', _external=True))


@bp_auth.route('/login/authorized/qq/')
def authorized_qq():
    resp = oauth_qq.authorized_response()
    if resp is None:
        return 'Access denied: reason=%s error=%s' % (
            request.args['error_reason'],
            request.args['error_description']
        )
    session['qq_token'] = (resp['access_token'], '')

    # Get openid via access_token, openid and access_token are needed for API calls
    resp = oauth_qq.get('/oauth2.0/me', {'access_token': session['qq_token'][0]})
    resp = json_to_dict(resp.data)
    if isinstance(resp, dict):
        session['qq_openid'] = resp.get('openid')

    return redirect(url_for('get_user_info'))


@oauth_qq.tokengetter
def get_qq_oauth_token():
    return session.get('qq_token')


# 第三方登陆（WeiBo）
# @app.route('/')
# def index():
#     if 'oauth_token' in session:
#         access_token = session['oauth_token'][0]
#         resp = weibo.get('statuses/home_timeline.json')
#         return jsonify(resp.data)
#     return redirect(url_for('auth.login'))


@bp_auth.route('/login/weibo/')
def login_weibo():
    return oauth_weibo.authorize(callback=url_for('auth.authorized_weibo',
                                                  next=request.args.get('next') or request.referrer or None,
                                                  _external=True))


@bp_auth.route('/login/authorized/weibo/')
def authorized_weibo():
    resp = oauth_weibo.authorized_response()
    if resp is None:
        return 'Access denied: reason=%s error=%s' % (
            request.args['error_reason'],
            request.args['error_description']
        )
    session['oauth_token'] = (resp['access_token'], '')
    return redirect(url_for('index'))


@oauth_weibo.tokengetter
def get_weibo_oauth_token():
    return session.get('oauth_token')


def change_weibo_header(uri, headers, body):
    """Since weibo is a rubbish server, it does not follow the standard,
    we need to change the authorization header for it."""
    auth = headers.get('Authorization')
    if auth:
        auth = auth.replace('Bearer', 'OAuth2')
        headers['Authorization'] = auth
    return uri, headers, body


oauth_weibo.pre_request = change_weibo_header


# 第三方登陆（GitHub）
@bp_auth.route('/login/github/')
def login_github():
    return oauth_github.authorize(callback=url_for('auth.authorized_github', _external=True))


@bp_auth.route('/login/authorized/github/')
def authorized_github():
    resp = oauth_github.authorized_response()
    if resp is None:
        return 'Access denied: reason=%s error=%s' % (
            request.args['error'],
            request.args['error_description']
        )
    session['github_token'] = (resp['access_token'], '')
    me = oauth_github.get('user')
    return jsonify(me.data)


@oauth_github.tokengetter
def get_github_oauth_token():
    return session.get('github_token')
