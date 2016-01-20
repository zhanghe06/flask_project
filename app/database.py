#!/usr/bin/env python
# encoding: utf-8

"""
@author: zhanghe
@software: PyCharm
@file: database.py
@time: 16-1-16 下午11:44
"""


from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

from config import SQLALCHEMY_DATABASE_URI

from flask.ext.sqlalchemy import SQLAlchemy
from app import app
db = SQLAlchemy(app)

# 初始化数据库连接
engine = create_engine(SQLALCHEMY_DATABASE_URI, convert_unicode=True)

# 创建 db_session
db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))
