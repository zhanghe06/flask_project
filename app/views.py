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


@app.route('/blog/list')
def blog_list():
    # return "Hello, World!\nBlog List!"
    return render_template('blog/list.html', title='blog_list')


@app.route('/blog/new')
def blog_new():
    # return "Hello, World!\nBlog New!"
    return render_template('blog/new.html', title='blog_new')


@app.route('/blog/hot')
def blog_hot():
    # return "Hello, World!\nBlog Hot!"
    return render_template('blog/hot.html', title='blog_hot')


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
