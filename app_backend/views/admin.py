#!/usr/bin/env python
# encoding: utf-8

"""
@author: zhanghe
@software: PyCharm
@file: admin.py
@time: 2017/4/22 下午5:02
"""


import json
from datetime import datetime

from flask import abort
from flask import redirect
from flask import render_template, request, flash, g
from flask import url_for
from flask_login import current_user, login_required

from app_common.maps import area_code_map
from app_common.tools import md5
from app_backend import app
from app_backend.forms.admin import AdminProfileForm, AdminAddForm, AdminEditForm
from app_backend.models import User
from app_backend.api.admin import get_admin_rows, get_admin_row, edit_admin, add_admin, get_admin_row_by_id
from app_common.maps.status_delete import *

from flask import Blueprint


bp_admin = Blueprint('admin', __name__, url_prefix='/admin')


@bp_admin.route('/profile/', methods=['GET', 'POST'])
@login_required
def profile():
    """
    当前登录管理员信息
    :return:
    """
    admin_id = current_user.id
    # return render_template('admin/profile.html', title='admin_profile')

    form = AdminProfileForm(request.form)
    if request.method == 'GET':
        admin_info = get_admin_row_by_id(admin_id)
        if admin_info:
            form.id.data = admin_info.id
            form.username.data = admin_info.username
            form.password.data = ''
            form.area_id.data = admin_info.area_id
            form.phone.data = admin_info.phone
            form.role.data = admin_info.role
            form.create_time.data = admin_info.create_time
            form.update_time.data = admin_info.update_time
    if request.method == 'POST':
        if form.validate_on_submit():
            current_time = datetime.utcnow()
            # 手机号码国际化
            area_id = form.area_id.data
            area_code = area_code_map.get(area_id, '86')
            admin_info = {
                'username': form.username.data,
                'area_id': area_id,
                'area_code': area_code,
                'phone': form.phone.data,
                'role': form.role.data,
                'create_time': current_time,
                'update_time': current_time,
            }
            if form.password.data:
                admin_info['password'] = md5(form.password.data)

            result = edit_admin(admin_id, admin_info)
            if result == 1:
                flash(u'Edit Success', 'success')
                return redirect(url_for('admin.lists'))
            else:
                flash(u'Edit Failed', 'warning')
                # flash(form.errors, 'warning')  # 调试打开

    return render_template('admin/profile.html', title='admin_profile', form=form)


@bp_admin.route('/list/')
@bp_admin.route('/list/<int:page>/')
@login_required
def lists(page=1):
    """
    管理列表
    """
    pagination = get_admin_rows(page)
    return render_template('admin/list.html', title='admin_list', pagination=pagination)


@bp_admin.route('/add/', methods=['GET', 'POST'])
@login_required
def add():
    """
    添加管理
    """
    # return render_template('admin/add.html', title='admin_add')

    form = AdminAddForm(request.form)
    if request.method == 'POST':
        if form.validate_on_submit():
            current_time = datetime.utcnow()
            # 手机号码国际化
            area_id = form.area_id.data
            area_code = area_code_map.get(area_id, '86')
            admin_info = {
                'username': form.username.data,
                'password': md5(form.password.data),
                'area_id': area_id,
                'area_code': area_code,
                'phone': form.phone.data,
                'role': form.role.data,
                'create_time': current_time,
                'update_time': current_time,
            }
            admin_uid = add_admin(admin_info)
            if admin_uid:
                flash(u'Add Success', 'success')
                return redirect(url_for('admin.lists'))
            else:
                flash(u'Add Failed', 'warning')
    # flash(form.errors, 'warning')  # 调试打开
    return render_template('admin/add.html', title='admin_add', form=form)


@bp_admin.route('/edit/<int:admin_id>', methods=['GET', 'POST'])
@login_required
def edit(admin_id):
    """
    编辑管理成员
    """
    form = AdminEditForm(request.form)
    if request.method == 'GET':
        admin_info = get_admin_row_by_id(admin_id)
        if admin_info:
            form.id.data = admin_info.id
            form.username.data = admin_info.username
            form.password.data = ''
            form.area_id.data = admin_info.area_id
            form.phone.data = admin_info.phone
            form.role.data = admin_info.role
            form.create_time.data = admin_info.create_time
            form.update_time.data = admin_info.update_time
    if request.method == 'POST':
        if form.validate_on_submit():
            current_time = datetime.utcnow()
            # 手机号码国际化
            area_id = form.area_id.data
            area_code = area_code_map.get(area_id, '86')
            admin_info = {
                'username': form.username.data,
                'area_id': area_id,
                'area_code': area_code,
                'phone': form.phone.data,
                'role': form.role.data,
                'create_time': current_time,
                'update_time': current_time,
            }
            if form.password.data:
                admin_info['password'] = md5(form.password.data)

            result = edit_admin(admin_id, admin_info)
            if result == 1:
                flash(u'Edit Success', 'success')
                return redirect(url_for('admin.lists'))
            else:
                flash(u'Edit Failed', 'warning')
        # flash(form.errors, 'warning')  # 调试打开

    return render_template('admin/edit.html', title='admin_edit', form=form)


@bp_admin.route('/ajax/del/', methods=['GET', 'POST'])
@login_required
def ajax_delete():
    """
    删除管理
    :return:
    """
    if request.method == 'GET' and request.is_xhr:
        admin_uid = request.args.get('admin_uid', 0, type=int)
        if not admin_uid:
            return json.dumps({'error': u'删除失败'})
        current_time = datetime.utcnow()
        admin_data = {
            'status_delete': STATUS_DEL_OK,
            'delete_time': current_time,
            'update_time': current_time
        }
        result = edit_admin(admin_uid, admin_data)
        if result == 1:
            return json.dumps({'success': u'删除成功'})
        if result == 0:
            return json.dumps({'error': u'删除失败'})
    abort(404)
