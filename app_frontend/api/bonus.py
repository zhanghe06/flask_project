#!/usr/bin/env python
# encoding: utf-8

"""
@author: zhanghe
@software: PyCharm
@file: bonus.py
@time: 2017/5/2 上午12:36
"""


from app_frontend.models import Bonu
from app_frontend.tools.db import get_row, get_rows, get_row_by_id, add, edit, delete


def get_bonus_row_by_id(bonus_id):
    """
    通过 id 获取奖金信息
    :param bonus_id:
    :return: None/object
    """
    return get_row_by_id(Bonu, bonus_id)


def get_bonus_row(*args, **kwargs):
    """
    获取奖金信息
    :param args:
    :param kwargs:
    :return: None/object
    """
    return get_row(Bonu, *args, **kwargs)


def add_bonus(bonus_data):
    """
    添加奖金信息
    :param bonus_data:
    :return: None/Value of wallet.id
    """
    return add(Bonu, bonus_data)


def edit_bonus(bonus_id, bonus_data):
    """
    修改奖金信息
    :param bonus_id:
    :param bonus_data:
    :return: Number of affected rows (Example: 0/1)
    """
    return edit(Bonu, bonus_id, bonus_data)


def delete_bonus(bonus_id):
    """
    删除奖金信息
    :param bonus_id:
    :return: Number of affected rows (Example: 0/1)
    """
    return delete(Bonu, bonus_id)


def get_bonus_rows(page=1, per_page=10, *args, **kwargs):
    """
    获取奖金列表（分页）
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
    rows = get_rows(Bonu, page, per_page, *args, **kwargs)
    return rows
