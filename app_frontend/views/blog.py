#!/usr/bin/env python
# encoding: utf-8

"""
@author: zhanghe
@software: PyCharm
@file: blog.py
@time: 2017/3/10 下午10:59
"""

import json
import logging
from datetime import datetime

from flask import request, render_template, redirect, url_for, g, abort, flash, jsonify
from flask_login import current_user, login_required

from app_frontend import app

from flask import Blueprint


bp_blog = Blueprint('blog', __name__, url_prefix='/blog')

log = logging.getLogger(__name__)


@bp_blog.route('/index/')
@bp_blog.route('/index/<int:page>/')
def index(page=1):
    """
    博客列表
    """
    # return "Hello, World!\nBlog List!"
    from app_frontend.api.blog import get_blog_rows
    per_page = 8
    pagination = get_blog_rows(page, per_page)
    return render_template('blog/index.html', title='blog_list', pagination=pagination)


@bp_blog.route('/list_edit/')
@bp_blog.route('/list_edit/<int:page>/')
@login_required
def list_edit(page=1):
    """
    博客列表(带编辑)
    """
    # return "Hello, World!\nBlog List!"
    from app_frontend.api.blog import get_blog_rows
    per_page = 8
    pagination = get_blog_rows(page, per_page)
    return render_template('blog/list_edit.html', title='blog_list', pagination=pagination)


@bp_blog.route('/ajax/list_edit/', methods=['GET', 'POST'])
@login_required
def ajax_list_edit():
    """
    博客编辑
    """
    if request.method == 'POST' and request.is_xhr:
        form = request.form

        blog_id = form.get('id', 0, type=int)
        blog_info = {
            'author': form.get('author'),
            'title': form.get('title'),
            'pub_date': datetime.strptime(form.get('pub_date'), "%Y-%m-%d").date(),
            'edit_time': datetime.utcnow(),
        }
        from app_frontend.api.blog import edit_blog
        result = edit_blog(blog_id, blog_info)
        if result == 1:
            return json.dumps({'success': u'Edit Success'})
        if result == 0:
            return json.dumps({'error': u'Edit Error'})
    abort(404)


@bp_blog.route('/new/')
@bp_blog.route('/new/<int:page>/')
def new(page=1):
    """
    最新博客
    """
    # return "Hello, World!\nBlog New!"
    from app_frontend.api.blog import get_blog_rows
    per_page = 8
    pagination = get_blog_rows(page, per_page)
    id_list = [item.id for item in pagination.items]
    from app_frontend.api.blog import get_blog_list_counter
    blog_counter_list = get_blog_list_counter(id_list)
    # 状态设置
    login_user_id = current_user.get_id()
    from app_frontend.api.blog import get_blog_list_container_status
    blog_container_status_list = get_blog_list_container_status(id_list, login_user_id)
    return render_template(
        'blog/new.html',
        title='blog_new',
        pagination=pagination,
        blog_counter_list=blog_counter_list,
        blog_container_status_list=blog_container_status_list
    )


@bp_blog.route('/hot/')
@bp_blog.route('/hot/<int:page>/')
def hot(page=1):
    """
    热门博客
    """
    # return "Hello, World!\nBlog Hot!"
    from app_frontend.api.blog import get_blog_rows
    per_page = 8
    pagination = get_blog_rows(page, per_page)
    return render_template('blog/hot.html', title='blog_hot', pagination=pagination)


@bp_blog.route('/edit/<int:blog_id>/', methods=['GET', 'POST'])
@login_required
def edit(blog_id):
    """
    博客编辑
    """
    # return "Hello, World!\nBlog Edit!"
    from app_frontend.forms.blog import BlogEditForm
    form = BlogEditForm(request.form)
    if request.method == 'GET':
        from app_frontend.api.blog import get_blog_row_by_id
        blog_info = get_blog_row_by_id(blog_id)
        if blog_info:
            form.author.data = blog_info.author
            form.title.data = blog_info.title
            form.pub_date.data = blog_info.pub_date
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


@bp_blog.route('/add/', methods=['GET', 'POST'])
@login_required
def add():
    """
    博客添加
    """
    # return "Hello, World!\nBlog Add!"
    from app_frontend.forms.blog import BlogAddForm
    form = BlogAddForm(request.form)
    if request.method == 'POST':
        if form.validate_on_submit():

            current_time = datetime.utcnow()
            blog_info = {
                'author': form.author.data,
                'title': form.title.data,
                'pub_date': form.pub_date.data,
                'add_time': current_time,
                'edit_time': current_time,
            }
            from app_frontend.api.blog import add_blog
            result = add_blog(blog_info)
            if result is None:
                flash(u'Add Failed', 'warning')
            else:
                flash(u'Add Success', 'success')
                return redirect(url_for('blog.edit', blog_id=result))
        flash(form.errors, 'warning')  # 调试打开
    # flash(u'Hello, %s' % current_user.email, 'info')  # 测试打开
    return render_template('blog/add.html', title='blog_add', form=form)


@bp_blog.route('/del/', methods=['GET', 'POST'])
def delete():
    """
    博客删除
    """
    if request.method == 'GET':
        login_user_id = current_user.get_id()
        # 权限判断，只能删除自己的 blog todo
        if login_user_id is None:
            return jsonify(result=False)
        blog_id = request.args.get('blog_id', 0, type=int)
        from app_frontend.api.blog import delete_blog
        result = delete_blog(blog_id)
        if result == 1:
            return jsonify(result=True)
        else:
            return jsonify(result=False)


@bp_blog.route('/stat/', methods=['GET', 'POST'])
def stat():
    """
    博客统计
    http://localhost:5000/blog/stat/?blog_id=2&stat_type=favor&num=2
    :return:
    """
    if request.method == 'GET':
        login_user_id = current_user.get_id()
        if login_user_id is None:
            return jsonify(result=False)
        blog_id = request.args.get('blog_id', 0, type=int)
        stat_type = request.args.get('stat_type', '', type=str)
        # num = request.args.get('num', 0, type=int)
        from app_frontend.tools.stat import set_blog_stat
        result = set_blog_stat(stat_type, login_user_id, blog_id)
        return jsonify(result)
