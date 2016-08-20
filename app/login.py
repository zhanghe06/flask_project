#!/usr/bin/env python
# encoding: utf-8

"""
@author: zhanghe
@software: PyCharm
@file: login.py
@time: 16-1-26 下午6:46
"""


from app.models import User
from flask_login import UserMixin


class LoginUser(User, UserMixin):
    """
    用户登陆类
    """
