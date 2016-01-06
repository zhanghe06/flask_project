#!/usr/bin/env python
# encoding: utf-8

"""
@author: zhanghe
@software: PyCharm
@file: views.py
@time: 16-1-7 上午12:10
"""


from app import app


@app.route('/')
@app.route('/index')
def index():
    return "Hello, World!"
