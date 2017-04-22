#!/usr/bin/env python
# encoding: utf-8

"""
@author: zhanghe
@software: PyCharm
@file: database.py
@time: 17-4-20 下午13:44
"""


from flask_sqlalchemy import SQLAlchemy
from app_backend import app
db = SQLAlchemy(app, session_options={'autocommit': True})
