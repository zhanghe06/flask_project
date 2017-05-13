#!/usr/bin/env python
# encoding: utf-8

"""
@author: zhanghe
@software: PyCharm
@file: active.py
@time: 2017/5/14 上午1:42
"""


from app_frontend.models import Active
from app_frontend.tools.db import get_row, get_rows, get_row_by_id, add, edit, delete


def get_active_row_by_id(active_id):
    """
    通过 id 获取激活信息
    :param active_id:
    :return: None/object
    """
    return get_row_by_id(Active, active_id)


def get_active_row(*args, **kwargs):
    """
    获取激活信息
    :param args:
    :param kwargs:
    :return: None/object
    """
    return get_row(Active, *args, **kwargs)


def add_order(active_data):
    """
    添加激活信息
    :param active_data:
    :return: None/Value of order.id
    """
    return add(Active, active_data)


def edit_order(active_id, active_data):
    """
    修改激活信息
    :param active_id:
    :param active_data:
    :return: Number of affected rows (Example: 0/1)
    """
    return edit(Active, active_id, active_data)


def delete_order(active_id):
    """
    删除激活信息
    :param active_id:
    :return: Number of affected rows (Example: 0/1)
    """
    return delete(Active, active_id)


def get_active_rows(page=1, per_page=10, *args, **kwargs):
    """
    获取激活列表（分页）
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
    rows = get_rows(Active, page, per_page, *args, **kwargs)
    return rows


