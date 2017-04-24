#!/usr/bin/env python
# encoding: utf-8

"""
@author: zhanghe
@software: PyCharm
@file: credit.py
@time: 2017/4/24 下午4:22
"""


from app_frontend.models import Credit
from app_frontend.tools.db import get_row, get_rows, get_row_by_id, add, edit, delete, update_rows


def get_user_credit_row_by_id(user_credit_id):
    """
    通过 id 获取用户声望信息
    :param user_credit_id:
    :return: None/object
    """
    return get_row_by_id(Credit, user_credit_id)


def get_user_credit_row(*args, **kwargs):
    """
    获取用户声望信息
    :param args:
    :param kwargs:
    :return: None/object
    """
    return get_row(Credit, *args, **kwargs)


def add_user_credit(user_credit_data):
    """
    添加用户声望信息
    :param user_credit_data:
    :return: None/Value of user.id
    """
    return add(Credit, user_credit_data)


def edit_user_credit(user_credit_id, user_credit_data):
    """
    修改用户声望信息
    :param user_credit_id:
    :param user_credit_data:
    :return: Number of affected rows (Example: 0/1)
    """
    return edit(Credit, user_credit_id, user_credit_data)


def delete_user_credit(user_credit_id):
    """
    删除用户信息
    :param user_credit_id:
    :return: Number of affected rows (Example: 0/1)
    """
    return delete(Credit, user_credit_id)


def get_user_credit_rows(page=1, per_page=10, *args, **kwargs):
    """
    获取用户声望列表（分页）
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
    rows = get_rows(Credit, page, per_page, *args, **kwargs)
    return rows


def update_user_credit_rows(data, *args, **kwargs):
    """
    批量更新用户声望信息
    """
    return update_rows(Credit, data, *args, **kwargs)
