#!/usr/bin/env python
# encoding: utf-8

"""
@author: zhanghe
@software: PyCharm
@file: scheduling.py
@time: 2017/6/29 下午8:46
"""


from app_frontend.models import Scheduling
from app_frontend.tools.db import get_row, get_rows, get_row_by_id, add, edit, delete


def get_scheduling_row_by_id(scheduling_id):
    """
    通过 id 获取排单信息
    :param scheduling_id:
    :return: None/object
    """
    return get_row_by_id(Scheduling, scheduling_id)


def get_scheduling_row(*args, **kwargs):
    """
    获取排单信息
    :param args:
    :param kwargs:
    :return: None/object
    """
    return get_row(Scheduling, *args, **kwargs)


def add_scheduling(scheduling_data):
    """
    添加排单信息
    :param scheduling_data:
    :return: None/Value of score.id
    """
    return add(Scheduling, scheduling_data)


def edit_scheduling(scheduling_id, scheduling_data):
    """
    修改排单信息
    :param scheduling_id:
    :param scheduling_data:
    :return: Number of affected rows (Example: 0/1)
    """
    return edit(Scheduling, scheduling_id, scheduling_data)


def delete_scheduling(scheduling_id):
    """
    删除排单信息
    :param scheduling_id:
    :return: Number of affected rows (Example: 0/1)
    """
    return delete(Scheduling, scheduling_id)


def get_scheduling_rows(page=1, per_page=10, *args, **kwargs):
    """
    获取排单列表（分页）
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
    rows = get_rows(Scheduling, page, per_page, *args, **kwargs)
    return rows
