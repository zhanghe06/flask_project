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
import flask_excel as excel
from itsdangerous import TimestampSigner

from app_backend import app
from app_backend.forms.user import UserProfileForm, UserSearchForm
from app_backend.models import User
from app_backend.api.user import get_user_rows, get_user_detail_rows
from app_backend.models import User, UserProfile, UserBank

from flask import Blueprint


bp_user = Blueprint('user', __name__, url_prefix='/user')


@bp_user.route('/list/')
@bp_user.route('/list/<int:page>/')
@login_required
def lists(page=1):
    """
    会员列表
    """
    form = UserSearchForm(request.form)

    user_id = request.args.get('user_id', '', type=int)
    user_name = request.args.get('user_name', '', type=str)
    start_time = request.args.get('start_time', '', type=str)
    end_time = request.args.get('end_time', '', type=str)
    status_lock = request.args.get('status_lock', '', type=str)
    op = request.args.get('op', 0, type=int)

    form.user_id.data = user_id
    form.user_name.data = user_name
    form.start_time.data = start_time
    form.end_time.data = end_time
    form.status_lock.data = status_lock

    search_condition_user = []
    search_condition_user_profile = []
    search_condition_user_bank = []
    if user_id:
        search_condition_user.append(User.id == user_id)
    if start_time:
        search_condition_user.append(User.create_time >= start_time)
    if end_time:
        search_condition_user.append(User.create_time <= end_time)
    if user_name:
        search_condition_user_profile.append(UserProfile.nickname == user_name)
    # 处理导出
    if op == 1:
        data_list = []
        query_sets = User.query. \
            filter(*search_condition_user). \
            outerjoin(UserProfile, User.id == UserProfile.user_id). \
            filter(*search_condition_user_profile). \
            outerjoin(UserBank, User.id == UserBank.user_id). \
            filter(*search_condition_user_bank). \
            add_entity(UserProfile). \
            add_entity(UserBank). \
            all()
        column_names = [u'用户编号', u'用户名称', u'银行名称', u'银行地址']
        data_list.append(column_names)
        for (user, user_profile, user_bank) in query_sets:
            row = [
                user.id if user else '',
                user_profile.nickname if user_profile else '',
                user_bank.bank_name if user_bank else '',
                user_bank.bank_address if user_bank else ''
            ]
            data_list.append(row)
        return excel.make_response_from_array(
            data_list,
            "csv",
            file_name="用户列表_%s" % datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        )
    # 处理查询
    pagination = User.query. \
        filter(*search_condition_user). \
        outerjoin(UserProfile, User.id == UserProfile.user_id). \
        filter(*search_condition_user_profile). \
        outerjoin(UserBank, User.id == UserBank.user_id). \
        filter(*search_condition_user_bank). \
        add_entity(UserProfile). \
        add_entity(UserBank). \
        paginate(page, 10, False)

    return render_template('user/list.html', title='user_list', pagination=pagination, form=form)


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
            from app_backend.api.blog import edit_blog
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


@bp_user.route('/del/', methods=['GET', 'POST'])
@login_required
def delete():
    """
    删除用户
    :return:
    """
    pass


@bp_user.route('/stats/', methods=['GET', 'POST'])
@login_required
def stats():
    """
    用户统计
    按日、周、月统计注册量
    :return:
    """
    pass


@bp_user.route('/admin_login/<int:user_id>/', methods=['GET', 'POST'])
@login_required
def admin_login(user_id):
    """
    后台登录前台用户
    :return:
    """
    s = TimestampSigner(app.config.get('ADMIN_TO_USER_LOGIN_SIGN_KEY'))
    user_id_sign = s.sign(str(user_id))
    return redirect('http://0.0.0.0:8000/auth/admin_login/?uid_sign=%s' % user_id_sign)
