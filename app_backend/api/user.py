#!/usr/bin/env python
# encoding: utf-8

"""
@user: zhanghe
@software: PyCharm
@file: user.py
@time: 17-4-21 下午10:42
"""


from app_frontend.models import User
from app_backend.models import UserProfile
from app_frontend.tools.db import get_row, get_rows, get_row_by_id, add, edit, delete


def get_user_row_by_id(user_id):
    """
    通过 id 获取用户信息
    :param user_id:
    :return: None/object
    """
    return get_row_by_id(User, user_id)


def get_user_row(*args, **kwargs):
    """
    获取用户信息
    :param args:
    :param kwargs:
    :return: None/object
    """
    return get_row(User, *args, **kwargs)


def add_user(user_data):
    """
    添加用户信息
    :param user_data:
    :return: None/Value of user.id
    """
    return add(User, user_data)


def edit_user(user_id, user_data):
    """
    修改用户信息
    :param user_id:
    :param user_data:
    :return: Number of affected rows (Example: 0/1)
    """
    return edit(User, user_id, user_data)


def delete_user(user_id):
    """
    删除用户信息
    :param user_id:
    :return: Number of affected rows (Example: 0/1)
    """
    return delete(User, user_id)


def get_user_rows(page=1, per_page=10, *args, **kwargs):
    """
    获取用户列表（分页）
    Usage:
        items: 信息列表
        has_next: 如果本页之后还有超过一个分页，则返回True
        has_prev: 如果本页之前还有超过一个分页，则返回True
        next_num: 返回下一页的页码
        prev_num: 返回上一页的页码
        iter_pages(): 页码列表
        iter_pages(left_edge=2, left_current=2, right_current=5, right_edge=2) 页码列表默认参数
    :param page:
    :param per_page:
    :param args:
    :param kwargs:
    :return:
    """
    rows = get_rows(User, page, per_page, *args, **kwargs)
    return rows


def get_user_profile_rows(page=1, per_page=10, *args, **kwargs):
    """
    获取用户基本信息列表（分页）
    Usage:
        items: 信息列表
        has_next: 如果本页之后还有超过一个分页，则返回True
        has_prev: 如果本页之前还有超过一个分页，则返回True
        next_num: 返回下一页的页码
        prev_num: 返回上一页的页码
        iter_pages(): 页码列表
        iter_pages(left_edge=2, left_current=2, right_current=5, right_edge=2) 页码列表默认参数
    :param page:
    :param per_page:
    :param args:
    :param kwargs:
    :return:
    """
    rows = User.query.join(UserProfile, User.id == UserProfile.id).filter(*args).filter_by(**kwargs).paginate(page, per_page, False)
    return rows
