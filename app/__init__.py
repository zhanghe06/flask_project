#!/usr/bin/env python
# encoding: utf-8

"""
@author: zhanghe
@software: PyCharm
@file: __init__.py
@time: 16-1-7 上午12:08
"""


from flask import Flask
# from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object('config')
# db = SQLAlchemy(app)

# 这个 import 语句放在这里, 防止views, models import发生循环import
from app import views, models
