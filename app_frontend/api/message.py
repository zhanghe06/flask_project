#!/usr/bin/env python
# encoding: utf-8

"""
@author: zhanghe
@software: PyCharm
@file: message.py
@time: 2017/4/29 下午2:30
"""


from app_frontend.models import Message
from app_frontend.tools.db import get_row, get_rows, get_row_by_id, add, edit, delete


def get_message_row_by_id(order_id):
    """
    通过 id 获取留言信息
    :param order_id:
    :return: None/object
    """
    return get_row_by_id(Message, order_id)


def get_message_row(*args, **kwargs):
    """
    获取留言信息
    :param args:
    :param kwargs:
    :return: None/object
    """
    return get_row(Message, *args, **kwargs)


def add_message(order_data):
    """
    添加留言信息
    :param order_data:
    :return: None/Value of order.id
    """
    return add(Message, order_data)


def edit_message(order_id, order_data):
    """
    修改留言信息
    :param order_id:
    :param order_data:
    :return: Number of affected rows (Example: 0/1)
    """
    return edit(Message, order_id, order_data)


def delete_message(order_id):
    """
    删除留言信息
    :param order_id:
    :return: Number of affected rows (Example: 0/1)
    """
    return delete(Message, order_id)


def get_message_rows(page=1, per_page=10, *args, **kwargs):
    """
    获取留言列表（分页）
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
    rows = get_rows(Message, page, per_page, *args, **kwargs)
    return rows
