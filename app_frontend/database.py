#!/usr/bin/env python
# encoding: utf-8

"""
@author: zhanghe
@software: PyCharm
@file: database.py
@time: 16-1-16 下午11:44
"""


from flask_sqlalchemy import SQLAlchemy
from app_frontend import app
db = SQLAlchemy(app)
