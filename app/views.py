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
from .forms import LoginForm


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


@app.route('/reg')
def reg():
    # return "Hello, World!\nReg!"
    return render_template('reg.html', title='reg')


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


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            # if request.form['username'] == 'admin':
            if form.username.data == 'admin':
                session['logged_in'] = True
                flash('You were logged in')
                return redirect(url_for('index'))
    return render_template('login.html', title='login', form=form)


@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    flash('You were logged out')
    return redirect(url_for('index'))
