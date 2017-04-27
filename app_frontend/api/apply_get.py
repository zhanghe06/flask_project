#!/usr/bin/env python
# encoding: utf-8

"""
@author: zhanghe
@software: PyCharm
@file: apply_get.py
@time: 2017/4/13 上午11:27
"""


from app_frontend.models import ApplyGet
from app_frontend.tools.db import get_row, get_rows, get_row_by_id, add, edit, delete


def get_apply_get_row_by_id(apply_get_id):
    """
    通过 id 获取提现申请信息
    :param apply_get_id:
    :return: None/object
    """
    return get_row_by_id(ApplyGet, apply_get_id)


def get_apply_get_row(*args, **kwargs):
    """
    获取提现申请信息
    :param args:
    :param kwargs:
    :return: None/object
    """
    return get_row(ApplyGet, *args, **kwargs)


def add_apply_get(apply_get_data):
    """
    添加提现申请信息
    :param apply_get_data:
    :return: None/Value of apply_get.id
    """
    return add(ApplyGet, apply_get_data)


def edit_apply_get(apply_get_id, apply_get_data):
    """
    修改提现申请信息
    :param apply_get_id:
    :param apply_get_data:
    :return: Number of affected rows (Example: 0/1)
    """
    return edit(ApplyGet, apply_get_id, apply_get_data)


def delete_apply_get(apply_get_id):
    """
    删除提现申请信息
    :param apply_get_id:
    :return: Number of affected rows (Example: 0/1)
    """
    return delete(ApplyGet, apply_get_id)


def get_apply_get_rows(page=1, per_page=10, *args, **kwargs):
    """
    获取提现申请列表（分页）
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
    rows = get_rows(ApplyGet, page, per_page, *args, **kwargs)
    return rows
