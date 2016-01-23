#!/usr/bin/env python
# encoding: utf-8

"""
@author: zhanghe
@software: PyCharm
@file: views.py
@time: 16-1-7 上午12:10
"""


from app import app
from flask import render_template, request, url_for, session, flash, redirect
from .forms import RegForm, LoginForm, BlogForm


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
    from blog import get_rows
    per_page = 8
    pagination = get_rows(page, per_page)
    return render_template('blog/list.html', title='blog_list', pagination=pagination)


@app.route('/blog/new/')
@app.route('/blog/new/<int:page>/')
def blog_new(page=1):
    # return "Hello, World!\nBlog New!"
    from blog import get_rows
    per_page = 8
    pagination = get_rows(page, per_page)
    return render_template('blog/new.html', title='blog_new', pagination=pagination)


@app.route('/blog/hot/')
@app.route('/blog/hot/<int:page>/')
def blog_hot(page=1):
    # return "Hello, World!\nBlog Hot!"
    from blog import get_rows
    per_page = 8
    pagination = get_rows(page, per_page)
    return render_template('blog/hot.html', title='blog_hot', pagination=pagination)


@app.route('/blog/edit/<int:blog_id>/', methods=['GET', 'POST'])
def blog_edit(blog_id):
    # return "Hello, World!\nBlog Edit!"
    form = BlogForm(request.form)
    if request.method == 'GET':
        from blog import get_row
        blog_info = get_row(blog_id)
        if blog_info:
            form.author.data = blog_info.author
            form.title.data = blog_info.title
            form.pub_date.data = blog_info.pub_date
        else:
            return redirect(url_for('index'))
    if request.method == 'POST':
        from blog import edit
        blog_info = {
            'author': form.author.data,
            'title': form.title.data,
            'pub_date': form.pub_date.data,
        }
        result = edit(blog_id, blog_info)
        if result == 1:
            flash(u'Edit Success', 'success')
        if result == 0:
            flash(u'Edit Failed', 'warning')
    return render_template('blog/edit.html', title='blog_edit', blog_id=blog_id, form=form)


@app.route('/reg', methods=['GET', 'POST'])
def reg():
    # return "Hello, World!\nReg!"
    form = RegForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            flash(u'%s, Thanks for registering' % form.username.data, 'success')
            return redirect(url_for('login'))
        # 闪现消息 success info warning danger
        flash(form.errors, 'warning')  # 调试打开
    return render_template('reg.html', title='reg', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            # if request.form['username'] == 'admin':
            # if form.username.data == 'admin':
            session['logged_in'] = True
            flash(u'%s, You were logged in' % form.username.data, 'success')
            return redirect(url_for('index'))
        flash(form.errors, 'warning')  # 调试打开
    return render_template('login.html', title='login', form=form)


@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    flash(u'You were logged out')
    return redirect(url_for('index'))
