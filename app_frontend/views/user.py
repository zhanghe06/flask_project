#!/usr/bin/env python
# encoding: utf-8

"""
@author: zhanghe
@software: PyCharm
@file: user.py
@time: 2017/3/17 下午11:47
"""
import json
import traceback

from flask import abort
from flask import render_template, request, flash, redirect, url_for
from flask_login import current_user, login_required

from app_common.maps import area_code_map
from app_common.maps.status_delete import *
from app_common.maps.status_active import *
from app_common.settings import PER_PAGE_FRONTEND
from app_common.tools import md5
from app_frontend import app
from app_frontend.forms.user import UserProfileForm, UserAuthForm, UserBankForm
from app_frontend.api.user_profile import get_user_profile_row_by_id, edit_user_profile
from app_frontend.api.user_bank import get_user_bank_row_by_id, add_user_bank, edit_user_bank
from app_frontend.api.user_auth import get_user_auth_row_by_id, get_user_auth_row, edit_user_auth
from app_frontend.api.user import edit_user, get_user_team_rows, get_user_row_by_id
from app_common.maps.type_auth import *
from datetime import datetime
from flask import Blueprint


bp_user = Blueprint('user', __name__, url_prefix='/user')


@bp_user.route('/auth/', methods=['GET', 'POST'])
@login_required
def auth():
    """
    用户登录认证信息
    """
    form = UserAuthForm(request.form)
    if request.method == 'GET':
        condition = {
            'user_id': current_user.id,
            'type_auth': TYPE_AUTH_ACCOUNT,
        }
        user_auth_info = get_user_auth_row(**condition)
        if user_auth_info:
            form.id.data = user_auth_info.id
            form.type_auth.data = user_auth_info.type_auth
            form.auth_key.data = user_auth_info.auth_key
            form.auth_secret.data = ''
            form.status_verified.data = user_auth_info.status_verified
            form.create_time.data = user_auth_info.create_time
            form.update_time.data = user_auth_info.update_time
    if request.method == 'POST':
        if form.validate_on_submit():
            # 权限校验
            condition = {
                'id': form.id.data,
                'user_id': current_user.id,
                'type_auth': TYPE_AUTH_ACCOUNT,
            }
            op_right = get_user_auth_row(**condition)
            if not op_right:
                flash(u'Edit Failed', 'warning')
                return redirect(url_for('index'))

            current_time = datetime.utcnow()
            user_auth_data = {
                # 'type_auth': AUTH_TYPE_ACCOUNT,
                'auth_key': form.auth_key.data,
                # 'status_verified': form.status_verified.data,
                'update_time': current_time,
            }
            if form.auth_secret.data:
                user_auth_data['auth_secret'] = md5(form.auth_secret.data)
            result = edit_user_auth(form.id.data, user_auth_data)
            if result == 1:
                flash(u'Edit Success', 'success')
            if result == 0:
                flash(u'Edit Failed', 'warning')
        # flash(form.errors, 'warning')  # 调试打开

    # flash(u'Hello, %s' % current_user.id, 'info')  # 测试打开
    return render_template('user/auth.html', title='auth', form=form)


@bp_user.route('/bank/', methods=['GET', 'POST'])
@login_required
def bank():
    """
    银行信息
    :return:
    """
    form = UserBankForm(request.form)
    if request.method == 'GET':
        bank_info = get_user_bank_row_by_id(current_user.id)
        if bank_info:
            form.bank_name.data = bank_info.bank_name
            form.bank_address.data = bank_info.bank_address
            form.bank_account.data = bank_info.bank_account
            form.status_verified.data = bank_info.status_verified
            form.create_time.data = bank_info.create_time
            form.update_time.data = bank_info.update_time
    if request.method == 'POST':
        if form.validate_on_submit():
            current_time = datetime.utcnow()
            bank_info = get_user_bank_row_by_id(current_user.id)
            bank_data = {
                'bank_name': form.bank_name.data,
                'bank_address': form.bank_address.data,
                'bank_account': form.bank_account.data,
                # 'status_verified': form.status_verified.data,
                'update_time': current_time,
            }
            if bank_info:
                result = edit_user_bank(current_user.id, bank_data)
            else:
                bank_data['create_time'] = current_time
                result = add_user_bank(bank_data)
            if result:
                flash(u'Edit Success', 'success')
            if not result:
                flash(u'Edit Failed', 'warning')
        # flash(form.errors, 'warning')  # 调试打开

    # flash(u'Hello, %s' % current_user.id, 'info')  # 测试打开
    return render_template('user/bank.html', title='bank', form=form)


@bp_user.route('/profile/', methods=['GET', 'POST'])
@login_required
def profile():
    """
    用户基本信息
    """
    form = UserProfileForm(request.form)
    if request.method == 'GET':
        user_info = get_user_profile_row_by_id(current_user.id)
        if user_info:
            form.user_pid.data = user_info.user_pid
            form.nickname.data = user_info.nickname
            form.avatar_url.data = user_info.avatar_url
            form.email.data = user_info.email
            form.area_id.data = user_info.area_id
            form.area_code.data = user_info.area_code
            form.phone.data = user_info.phone
            form.birthday.data = user_info.birthday
            form.id_card.data = user_info.id_card
            form.create_time.data = user_info.create_time
            form.update_time.data = user_info.update_time
    if request.method == 'POST':
        if form.validate_on_submit():
            current_time = datetime.utcnow()
            # 手机号码国际化
            area_id = form.area_id.data
            area_code = area_code_map.get(area_id, '86')
            user_info = {
                'email': form.email.data,
                'area_id': area_id,
                'area_code': area_code,
                'phone': form.phone.data,
                'birthday': form.birthday.data,
                'update_time': current_time,
            }
            result = edit_user_profile(current_user.id, user_info)
            if result == 1:
                flash(u'Edit Success', 'success')
            if result == 0:
                flash(u'Edit Failed', 'warning')
        # flash(form.errors, 'warning')  # 调试打开

    # flash(u'Hello, %s' % current_user.id, 'info')  # 测试打开
    return render_template('user/profile.html', title='profile', form=form)


@bp_user.route('/setting/', methods=['GET', 'POST'])
@login_required
def setting():
    """
    设置
    """
    # return "Hello, World!\nSetting!"
    form = UserProfileForm(request.form)
    if request.method == 'GET':
        from app_frontend.api.user_profile import get_user_profile_row_by_id
        user_info = get_user_profile_row_by_id(current_user.id)
        if user_info:
            form.nickname.data = user_info.nickname
            form.avatar_url.data = user_info.avatar_url
            form.email.data = user_info.email
            form.phone.data = user_info.phone
            form.birthday.data = user_info.birthday
            form.create_time.data = user_info.create_time
            form.update_time.data = user_info.update_time
            # form.last_ip.data = user_info.last_ip
    if request.method == 'POST':
        if form.validate_on_submit():
            # todo 判断邮箱是否重复
            from app_frontend.api.user import edit_user
            from datetime import datetime
            user_info = {
                'nickname': form.nickname.data,
                'avatar_url': form.avatar_url.data,
                'email': form.email.data,
                'phone': form.phone.data,
                'birthday': form.birthday.data,
                'update_time': datetime.utcnow(),
                # 'last_ip': request.headers.get('X-Forwarded-For', request.remote_addr),
            }
            result = edit_user(current_user.id, user_info)
            if result == 1:
                flash(u'Edit Success', 'success')
            if result == 0:
                flash(u'Edit Failed', 'warning')
        flash(form.errors, 'warning')  # 调试打开
    # flash(u'Hello, %s' % current_user.id, 'info')  # 测试打开
    return render_template('./setting.html', title='setting', form=form)


@bp_user.route('/team/')
@bp_user.route('/team/<int:page>/')
@login_required
def team(page=1):
    """
    团队
    :param page:
    :return:
    """
    condition = {
        'user_pid': current_user.id
    }
    status_active = request.args.get('status_active', '', type=str)
    status_lock = request.args.get('status_lock', '', type=str)
    if status_active:
        condition['status_active'] = status_active
    if status_lock:
        condition['status_lock'] = status_lock

    pagination = get_user_team_rows(
        page,
        PER_PAGE_FRONTEND,
        **condition)
    return render_template('user/team.html', title='team', pagination=pagination)


@bp_user.route('/ajax_active/', methods=['GET', 'POST'])
@login_required
def ajax_active():
    """
    用户激活
    :return:
    """
    if request.method == 'POST' and request.is_xhr:
        form = request.form
        user_id = form.get('user_id', 0, type=int)

        try:
            # 参数校验
            if not user_id:
                raise Exception(u'参数错误，用户激活操作失败')

            # 用户异常处理
            user_info = get_user_row_by_id(user_id)

            if not user_info:
                raise Exception(u'异常操作，此用户不存在')
            if user_info.status_delete == int(STATUS_DEL_OK):
                raise Exception(u'异常操作，此用户已删除')
            if user_info.status_active == int(STATUS_ACTIVE_OK):
                raise Exception(u'异常操作，不能重复操作')

            user_profile_info = get_user_profile_row_by_id(user_id)
            if not user_profile_info:
                raise Exception(u'异常操作，此用户不存在')
            if user_profile_info.user_pid != current_user.id:
                raise Exception(u'异常操作，无此用户权限')

            # 更新激活状态
            current_time = datetime.utcnow()
            user_data = {
                'status_active': STATUS_ACTIVE_OK,
                'active_time': current_time,
                'update_time': current_time,
            }
            result = edit_user(user_id, user_data)
            # todo 扣除激活码的数量
            if result == 1:
                return json.dumps({'success': u'用户激活操作成功'})
            if result == 0:
                return json.dumps({'error': u'用户激活操作失败'})
        except Exception as e:
            print traceback.print_exc()
            return json.dumps({'error': e.message})
    abort(404)
