#!/usr/bin/env python
# encoding: utf-8

"""
@author: zhanghe
@software: PyCharm
@file: complaint.py
@time: 2017/4/29 下午2:30
"""


from app_frontend.models import Complaint
from app_frontend.tools.db import get_row, get_rows, get_row_by_id, add, edit, delete


def get_complaint_row_by_id(complaint_id):
    """
    通过 id 获取投诉信息
    :param complaint_id:
    :return: None/object
    """
    return get_row_by_id(Complaint, complaint_id)


def get_complaint_row(*args, **kwargs):
    """
    获取投诉信息
    :param args:
    :param kwargs:
    :return: None/object
    """
    return get_row(Complaint, *args, **kwargs)


def add_complaint(complaint_data):
    """
    添加投诉信息
    :param complaint_data:
    :return: None/Value of order.id
    """
    return add(Complaint, complaint_data)


def edit_complaint(complaint_id, complaint_data):
    """
    修改投诉信息
    :param complaint_id:
    :param complaint_data:
    :return: Number of affected rows (Example: 0/1)
    """
    return edit(Complaint, complaint_id, complaint_data)


def delete_complaint(complaint_id):
    """
    删除投诉信息
    :param complaint_id:
    :return: Number of affected rows (Example: 0/1)
    """
    return delete(Complaint, complaint_id)


def get_complaint_rows(page=1, per_page=10, *args, **kwargs):
    """
    获取投诉列表（分页）
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
    rows = get_rows(Complaint, page, per_page, *args, **kwargs)
    return rows

