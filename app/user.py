#!/usr/bin/env python
# encoding: utf-8

"""
@user: zhanghe
@software: PyCharm
@file: user.py
@time: 16-1-23 下午11:42
"""


from login import LoginUser
from tools.db import get_row, get_rows, get_row_by_id, add, edit_by_id, delete_by_id
from lib.container import Container


def get_user_row_by_id(user_id):
    """
    通过 id 获取用户信息
    :param user_id:
    :return: None/object
    """
    return get_row_by_id(LoginUser, user_id)


def get_user_row(*args, **kwargs):
    """
    获取用户信息
    :param args:
    :param kwargs:
    :return: None/object
    """
    return get_row(LoginUser, *args, **kwargs)


def add_user(user_data):
    """
    添加用户信息
    :param user_data:
    :return: None/Value of user.id
    """
    return add(LoginUser, user_data)


def edit_user(user_id, user_data):
    """
    修改用户信息
    :param user_id:
    :param user_data:
    :return: Number of affected rows (Example: 0/1)
    """
    return edit_by_id(LoginUser, user_id, user_data)


def delete_user(user_id):
    """
    删除用户信息
    :param user_id:
    :return: Number of affected rows (Example: 0/1)
    """
    return delete_by_id(LoginUser, user_id)


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
    rows = get_rows(LoginUser, page, per_page, *args, **kwargs)
    return rows


def add_user_stat_item(stat_type, uid, blog_id):
    """
    添加user统计明细
    :param stat_type:
    :param blog_id:
    :param uid:
    :return:
    """
    blog_container_obj = Container('user')
    return blog_container_obj.add_item(stat_type, uid, blog_id)

