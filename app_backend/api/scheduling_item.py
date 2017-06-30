#!/usr/bin/env python
# encoding: utf-8

"""
@author: zhanghe
@software: PyCharm
@file: scheduling_item.py
@time: 2017/6/29 下午8:46
"""


from app_backend.models import SchedulingItem
from app_backend.tools.db import get_row, get_rows, get_row_by_id, add, edit, delete


def get_scheduling_item_item_row_by_id(scheduling_item_item_id):
    """
    通过 id 获取排单明细信息
    :param scheduling_item_item_id:
    :return: None/object
    """
    return get_row_by_id(SchedulingItem, scheduling_item_item_id)


def get_scheduling_item_item_row(*args, **kwargs):
    """
    获取排单明细信息
    :param args:
    :param kwargs:
    :return: None/object
    """
    return get_row(SchedulingItem, *args, **kwargs)


def add_scheduling_item(scheduling_item_item_data):
    """
    添加排单明细信息
    :param scheduling_item_item_data:
    :return: None/Value of score.id
    """
    return add(SchedulingItem, scheduling_item_item_data)


def edit_scheduling_item(scheduling_item_item_id, scheduling_item_item_data):
    """
    修改排单明细信息
    :param scheduling_item_item_id:
    :param scheduling_item_item_data:
    :return: Number of affected rows (Example: 0/1)
    """
    return edit(SchedulingItem, scheduling_item_item_id, scheduling_item_item_data)


def delete_scheduling_item(scheduling_item_item_id):
    """
    删除排单明细信息
    :param scheduling_item_item_id:
    :return: Number of affected rows (Example: 0/1)
    """
    return delete(SchedulingItem, scheduling_item_item_id)


def get_scheduling_item_item_rows(page=1, per_page=10, *args, **kwargs):
    """
    获取排单明细列表（分页）
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
    rows = get_rows(SchedulingItem, page, per_page, *args, **kwargs)
    return rows
