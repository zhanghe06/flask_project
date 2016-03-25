#!/usr/bin/env python
# encoding: utf-8

"""
@author: zhanghe
@software: PyCharm
@file: views.py
@time: 16-1-7 上午12:10
"""


from app import app, login_manager
from flask import render_template, request, url_for, send_from_directory, session, flash, redirect, g, jsonify
from app.forms import RegForm, LoginForm, BlogAddForm, BlogEditForm, UserForm
from app.login import LoginUser
from flask.ext.login import login_user, logout_user, current_user, login_required
import os


@login_manager.user_loader
def load_user(user_id):
    """
    如果 user_id 无效，它应该返回 None （ 而不是抛出异常 ）。
    :param user_id:
    :return:
    """
    return LoginUser.query.get(int(user_id))


@app.before_request
def before_request():
    g.user = current_user


@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'img/favicon.ico', mimetype='image/vnd.microsoft.icon')


@app.route('/')
@app.route('/index')
def index():
    # return "Hello, World!"
    return render_template('index.html', title='home')


@app.route('/about')
def about():
    # return "Hello, World!\nAbout!"
    return render_template('about.html', title='about')


@app.route('/contact')
def contact():
    # return "Hello, World!\nContact!"
    return render_template('contact.html', title='contact')


@app.route('/blog/list/')
@app.route('/blog/list/<int:page>/')
def blog_list(page=1):
    # return "Hello, World!\nBlog List!"
    from blog import get_blog_rows
    per_page = 8
    pagination = get_blog_rows(page, per_page)
    return render_template('blog/list.html', title='blog_list', pagination=pagination)


@app.route('/blog/new/')
@app.route('/blog/new/<int:page>/')
def blog_new(page=1):
    # return "Hello, World!\nBlog New!"
    from blog import get_blog_rows, get_blog_list_counter, get_blog_list_container_status
    per_page = 8
    pagination = get_blog_rows(page, per_page)
    id_list = [item.id for item in pagination.items]
    blog_counter_list = get_blog_list_counter(id_list)
    # 状态设置
    login_user_id = g.user.get_id()
    blog_container_status_list = get_blog_list_container_status(id_list, login_user_id)
    return render_template(
        'blog/new.html',
        title='blog_new',
        pagination=pagination,
        blog_counter_list=blog_counter_list,
        blog_container_status_list=blog_container_status_list
    )


@app.route('/blog/hot/')
@app.route('/blog/hot/<int:page>/')
def blog_hot(page=1):
    # return "Hello, World!\nBlog Hot!"
    from blog import get_blog_rows
    per_page = 8
    pagination = get_blog_rows(page, per_page)
    return render_template('blog/hot.html', title='blog_hot', pagination=pagination)


@app.route('/blog/edit/<int:blog_id>/', methods=['GET', 'POST'])
@login_required
def blog_edit(blog_id):
    # return "Hello, World!\nBlog Edit!"
    form = BlogEditForm(request.form)
    if request.method == 'GET':
        from blog import get_blog_row_by_id
        blog_info = get_blog_row_by_id(blog_id)
        if blog_info:
            form.author.data = blog_info.author
            form.title.data = blog_info.title
            form.pub_date.data = blog_info.pub_date
        else:
            return redirect(url_for('index'))
    if request.method == 'POST':
        if form.validate_on_submit():
            from blog import edit_blog
            from datetime import datetime
            blog_info = {
                'author': form.author.data,
                'title': form.title.data,
                'pub_date': form.pub_date.data,
                'edit_time': datetime.utcnow(),
            }
            result = edit_blog(blog_id, blog_info)
            if result == 1:
                flash(u'Edit Success', 'success')
                return redirect(request.args.get('next') or url_for('blog_list'))
            if result == 0:
                flash(u'Edit Failed', 'warning')
        flash(form.errors, 'warning')  # 调试打开
    flash(u'Hello, %s' % current_user.email, 'info')  # 测试打开
    return render_template('blog/edit.html', title='blog_edit', blog_id=blog_id, form=form)


@app.route('/blog/add/', methods=['GET', 'POST'])
@login_required
def blog_add():
    # return "Hello, World!\nBlog Add!"
    form = BlogAddForm(request.form)
    if request.method == 'POST':
        if form.validate_on_submit():
            from blog import add_blog
            from datetime import datetime
            blog_info = {
                'author': form.author.data,
                'title': form.title.data,
                'pub_date': form.pub_date.data,
                'add_time': datetime.utcnow(),
                'edit_time': datetime.utcnow(),
            }
            result = add_blog(blog_info)
            if result is None:
                flash(u'Add Failed', 'warning')
            else:
                flash(u'Add Success', 'success')
                return redirect(url_for('blog_edit', blog_id=result))
        flash(form.errors, 'warning')  # 调试打开
    # flash(u'Hello, %s' % current_user.email, 'info')  # 测试打开
    return render_template('blog/add.html', title='blog_add', form=form)


@app.route('/blog/del/', methods=['GET', 'POST'])
def blog_delete():
    if request.method == 'GET':
        login_user_id = g.user.get_id()
        # 权限判断，只能删除自己的 blog todo
        if login_user_id is None:
            return jsonify(result=False)
        blog_id = request.args.get('blog_id', 0, type=int)
        from blog import delete_blog
        result = delete_blog(blog_id)
        if result == 1:
            return jsonify(result=True)
        else:
            return jsonify(result=False)


@app.route('/blog/stat/', methods=['GET', 'POST'])
def blog_stat():
    """
    http://localhost:5000/blog/stat/?blog_id=2&stat_type=favor&num=2
    :return:
    """
    if request.method == 'GET':
        login_user_id = g.user.get_id()
        if login_user_id is None:
            return jsonify(result=False)
        blog_id = request.args.get('blog_id', 0, type=int)
        stat_type = request.args.get('stat_type', '', type=str)
        # num = request.args.get('num', 0, type=int)
        from tools.stat import set_blog_stat
        result = set_blog_stat(stat_type, login_user_id, blog_id)
        return jsonify(result)


@app.route('/reg', methods=['GET', 'POST'])
def reg():
    # return "Hello, World!\nReg!"
    form = RegForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            flash(u'%s, Thanks for registering' % form.email.data, 'success')
            return redirect(url_for('login'))
        # 闪现消息 success info warning danger
        flash(form.errors, 'warning')  # 调试打开
    return render_template('reg.html', title='reg', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if g.user is not None and g.user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            from user import get_user_row
            condition = {
                'email': form.email.data,
                'password': form.password.data
            }
            user_info = get_user_row(**condition)
            if user_info is None:
                flash(u'%s, You were logged failed' % form.email.data, 'warning')
                return render_template('login.html', title='login', form=form)
            # session['logged_in'] = True
            # 用户通过验证后，用 login_user 函数来登入他们
            login_user(user_info)
            flash(u'%s, You were logged in' % form.email.data, 'success')
            return redirect(request.args.get('next') or url_for('index'))
        flash(form.errors, 'warning')  # 调试打开
    return render_template('login.html', title='login', form=form)


# @app.route('/logout')
# def logout():
#     session.pop('logged_in', None)
#     flash(u'You were logged out')
#     return redirect(url_for('index'))

@app.route('/logout')
def logout():
    logout_user()
    flash(u'You were logged out', 'info')
    return redirect(url_for('index'))


@app.route('/setting/', methods=['GET', 'POST'])
@login_required
def setting():
    # return "Hello, World!\nSetting!"
    form = UserForm(request.form)
    if request.method == 'GET':
        # from user import get_user_row_by_id
        # user_info = get_user_row_by_id(user.id)
        # if user_info:
        form.email.data = current_user.email
        form.password.data = current_user.password
        form.nickname.data = current_user.nickname
        form.birthday.data = current_user.birthday
        form.create_time.data = current_user.create_time
        form.update_time.data = current_user.update_time
        form.last_ip.data = current_user.last_ip
    if request.method == 'POST':
        if form.validate_on_submit():
            # todo 判断邮箱是否重复
            from user import edit_user
            from datetime import datetime
            user_info = {
                'email': form.email.data,
                'nickname': form.nickname.data,
                'birthday': form.birthday.data,
                'update_time': datetime.utcnow(),
                'last_ip': request.remote_addr,
            }
            result = edit_user(current_user.id, user_info)
            if result == 1:
                flash(u'Edit Success', 'success')
            if result == 0:
                flash(u'Edit Failed', 'warning')
        flash(form.errors, 'warning')  # 调试打开
    flash(u'Hello, %s' % current_user.email, 'info')  # 测试打开
    return render_template('setting.html', title='setting', form=form)


@app.route('/search/', methods=['GET', 'POST'])
def search():
    return 'search result!'


@app.route("/email/")
def send_email():
    try:
        from emails import send_email
        msg = 'This is a test email!'
        send_email(
            subject=u'邮件主题',
            sender=(u'系统邮箱', 'zhang_he06@163.com'),
            recipients=[(u'尊敬的用户', 'zhang_he06@163.com')],
            html_body=render_template('email.html', message=msg)
        )
        return jsonify({'success': u'邮件发送成功'})
    except Exception, e:
        return jsonify({'error': e.message})


@app.route("/test")
def test():
    try:
        raise Exception('error test')
    except Exception as e:
        import logging
        logging.error(e)
