#!/usr/bin/env python
# encoding: utf-8

"""
@author: zhanghe
@software: PyCharm
@file: score.py
@time: 2017/4/25 下午1:29
"""


from app_frontend.models import Score
from app_frontend.tools.db import get_row, get_rows, get_row_by_id, add, edit, delete


def get_score_row_by_id(score_id):
    """
    通过 id 获取积分信息
    :param score_id:
    :return: None/object
    """
    return get_row_by_id(Score, score_id)


def get_score_row(*args, **kwargs):
    """
    获取积分信息
    :param args:
    :param kwargs:
    :return: None/object
    """
    return get_row(Score, *args, **kwargs)


def add_score(score_data):
    """
    添加积分信息
    :param score_data:
    :return: None/Value of score.id
    """
    return add(Score, score_data)


def edit_score(score_id, score_data):
    """
    修改积分信息
    :param score_id:
    :param score_data:
    :return: Number of affected rows (Example: 0/1)
    """
    return edit(Score, score_id, score_data)


def delete_score(score_id):
    """
    删除积分信息
    :param score_id:
    :return: Number of affected rows (Example: 0/1)
    """
    return delete(Score, score_id)


def get_score_rows(page=1, per_page=10, *args, **kwargs):
    """
    获取积分列表（分页）
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
    rows = get_rows(Score, page, per_page, *args, **kwargs)
    return rows
