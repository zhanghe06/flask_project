#!/usr/bin/env python
# encoding: utf-8

"""
@author: zhanghe
@software: PyCharm
@file: __init__.py.py
@time: 2017/3/10 下午10:56
"""


import os
from datetime import datetime
import json
import traceback

from flask import current_app, Response
from sqlalchemy.exc import OperationalError
from pika.exceptions import ConnectionClosed
from flask import send_from_directory
from flask_login import current_user
from flask_principal import identity_changed, Identity, AnonymousIdentity
from flask_principal import identity_loaded, RoleNeed, UserNeed

from flask import g, request, render_template, jsonify
from flask import session, redirect, url_for, flash
from flask_login import login_user
from flask_login import logout_user
from flask_login import current_user, login_required

from app_backend.lib.rabbit_mq import RabbitPriorityQueue
from app_common.maps import area_code_map
from app_backend import app, oauth_github, oauth_qq, oauth_weibo
from app_common.maps.type_auth import *
from app_common.maps.status_delete import *

from app_backend import app, login_manager

# cache = SimpleCache()  # 默认最大支持500个key, 超时时间5分钟, 参数可配置
from app_backend.api.admin import get_admin_row
# from app_backend.lib.sms_chuanglan_iso import SmsChuangLanIsoApi
from app_common.tools import md5, get_randint
from app_backend.tools.send_sms import UN, PW
from app_common.tools.ip import get_real_ip

from app_backend.permissions import admin_permission

SMS_CODE_LOGIN = app.config['SMS_CODE_LOGIN']
EXCHANGE_NAME = app.config['EXCHANGE_NAME']


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


@identity_loaded.connect_via(app)
def on_identity_loaded(sender, identity):
    # Set the identity user object
    identity.user = current_user

    # Add the UserNeed to the identity
    if hasattr(current_user, 'id'):
        identity.provides.add(UserNeed(current_user.id))

    # Assuming the User model has a list of roles, update the
    # identity with the roles that the user provides
    if hasattr(current_user, 'roles'):
        for role in current_user.roles:
            identity.provides.add(RoleNeed(role.name))


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
@login_required
def index():
    """
    后台首页
    """
    # return "Hello, World!"
    return render_template('index.html', title='home')


@app.route('/login/', methods=['GET', 'POST'])
def login():
    """
    后台登录页面
    """
    # print current_user.__dict__
    # return json.dumps(current_user.__dict__)
    if g.user is not None and g.user.is_authenticated:
        return redirect(url_for('index'))
    from app_backend.forms.login import LoginForm
    form = LoginForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            from app_backend.api.admin import get_admin_row
            condition = {
                'username': form.account.data,
                'password': md5(form.password.data)
            }
            admin_info = get_admin_row(**condition)
            if admin_info is None:
                flash(u'%s, 登录失败，账号密码错误' % form.account.data, 'warning')
                return render_template('login.html', title='login', form=form)
            if admin_info.status_delete == STATUS_DEL_OK:
                flash(u'%s, 登录失败，账号已被删除' % form.account.data, 'warning')
                return render_template('login.html', title='login', form=form)
            # session['logged_in'] = True
            # 用户通过验证后，记录登入IP
            from app_backend.api.admin import edit_admin
            ip_data = {
                'login_ip': get_real_ip(),
                'login_time': datetime.utcnow()
            }
            edit_admin(admin_info.id, ip_data)
            # 用 login_user 函数来登入他们
            from app_backend.api.admin import get_admin_row_by_id
            login_user(get_admin_row_by_id(admin_info.id), remember=form.remember.data)

            # 加载权限
            # Tell Flask-Principal the identity changed
            identity_changed.send(app, identity=Identity(admin_info.id, admin_info.role))

            flash(u'%s, 恭喜，登录成功' % form.account.data, 'success')
            return redirect(request.args.get('next') or url_for('index'))
        # flash(form.errors, 'warning')  # 调试打开
    return render_template('login.html', title='login', form=form)


@app.route('/logout/')
def logout():
    """
    退出登录
    """
    logout_user()
    session.pop('qq_token', None)
    session.pop('weibo_token', None)
    session.pop('github_token', None)

    # 退出权限
    # Remove session keys set by Flask-Principal
    for key in ('identity.name', 'identity.auth_type'):
        session.pop(key, None)

    # Tell Flask-Principal the user is anonymous
    identity_changed.send(app, identity=AnonymousIdentity())

    flash(u'成功退出登录', 'info')
    return redirect(url_for('index'))


@app.route('/ajax/get_sms_code/', methods=['GET', 'POST'])
def ajax_get_sms_code():
    """
    获取短信验证码
    :return:
    """
    try:
        # 获取短信验证码
        account = request.args.get('account', '', type=str)
        if not account:
            return json.dumps({'result': False, 'msg': u'账号为空，请重新填写'})
        account = request.args.get('account', '', type=str)
        admin_info = get_admin_row(username=account)
        if not admin_info:
            return json.dumps({'result': False, 'msg': u'账号不存在，请填写正确'})
        area_code = admin_info.area_code
        mobile = admin_info.phone
        if not area_code or not mobile:
            return json.dumps({'result': False, 'msg': u'手机号码错误，请在后台更新'})
        mobile_iso = '%s%s' % (area_code, mobile)

        sms_code = str(get_randint())
        code_key = '%s:%s' % ('sms_code', 'login')
        session[code_key] = sms_code

        sms_content = SMS_CODE_LOGIN % sms_code

        # sms_client = SmsChuangLanIsoApi(UN, PW)
        # result = sms_client.send_international(mobile_iso, msg)

        # 推送短信优先级队列
        q = RabbitPriorityQueue(exchange=EXCHANGE_NAME, queue_name='send_sms_p')
        q.put({'mobile': mobile_iso, 'sms_content': sms_content}, 20)

        return json.dumps({'result': True})
    except OperationalError:
        print traceback.print_exc()
        return json.dumps({'result': False, 'msg': u'数据库连接失败'})
    except ConnectionClosed:
        print traceback.print_exc()
        return json.dumps({'result': False, 'msg': u'短信队列连接失败'})
    except Exception as e:
        print traceback.print_exc()
        return json.dumps({'result': False, 'msg': u'服务器异常，短信获取失败；%s' % e.message})


@app.errorhandler(403)
def page_permission_denied(error):
    session['redirected_from'] = request.url
    return redirect(url_for('index'))


@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404


@app.errorhandler(500)
def internal_error(error):
    from app_backend.database import db
    db.session.rollback()
    return render_template('500.html'), 500


@app.route('/admin_permission/')
@admin_permission.require(http_exception=403)
def test_admin_permission():
    """
    管理员权限测试
    :return:
    """
    return Response('Only if you are admin')

