#!/usr/bin/env python
# encoding: utf-8

"""
@author: zhanghe
@software: PyCharm
@file: login.py
@time: 17-4-20 下午1:46
"""


from app_backend.models import Admin
from flask_login import UserMixin


class LoginUser(Admin, UserMixin):
    """
    用户登陆类
    """
