#!/usr/bin/env python
# encoding: utf-8

"""
@author: zhanghe
@software: PyCharm
@file: bank.py
@time: 2017/4/26 下午1:46
"""


from app_frontend.models import UserBank
from app_frontend.tools.db import get_row, get_rows, get_row_by_id, add, edit, delete, update_rows


def get_user_bank_row_by_id(user_bank_id):
    """
    通过 id 获取用户银行信息
    :param user_bank_id:
    :return: None/object
    """
    return get_row_by_id(UserBank, user_bank_id)


def get_user_bank_row(*args, **kwargs):
    """
    获取用户银行信息
    :param args:
    :param kwargs:
    :return: None/object
    """
    return get_row(UserBank, *args, **kwargs)


def add_user_bank(user_bank_data):
    """
    添加用户银行信息
    :param user_bank_data:
    :return: None/Value of user.id
    """
    return add(UserBank, user_bank_data)


def edit_user_bank(user_bank_id, user_bank_data):
    """
    修改用户银行信息
    :param user_bank_id:
    :param user_bank_data:
    :return: Number of affected rows (Example: 0/1)
    """
    return edit(UserBank, user_bank_id, user_bank_data)


def delete_user_bank(user_bank_id):
    """
    删除用户银行信息
    :param user_bank_id:
    :return: Number of affected rows (Example: 0/1)
    """
    return delete(UserBank, user_bank_id)


def get_user_bank_rows(page=1, per_page=10, *args, **kwargs):
    """
    获取用户银行列表（分页）
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
    rows = get_rows(UserBank, page, per_page, *args, **kwargs)
    return rows


def update_user_bank_rows(data, *args, **kwargs):
    """
    批量更新用户银行信息
    """
    return update_rows(UserBank, data, *args, **kwargs)
