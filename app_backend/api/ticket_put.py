#!/usr/bin/env python
# encoding: utf-8

"""
@author: zhanghe
@software: PyCharm
@file: ticket_put.py
@time: 2017/4/24 下午11:27
"""


from app_backend.models import TicketPut
from app_backend.tools.db import get_row, get_rows, get_row_by_id, add, edit, delete


def get_ticket_put_row_by_id(ticket_put_id):
    """
    通过 id 获取付款单信息
    :param ticket_put_id:
    :return: None/object
    """
    return get_row_by_id(TicketPut, ticket_put_id)


def get_ticket_put_row(*args, **kwargs):
    """
    获取付款单信息
    :param args:
    :param kwargs:
    :return: None/object
    """
    return get_row(TicketPut, *args, **kwargs)


def add_ticket_put(ticket_put_data):
    """
    添加付款单信息
    :param ticket_put_data:
    :return: None/Value of ticket_put.id
    """
    return add(TicketPut, ticket_put_data)


def edit_ticket_put(ticket_put_id, ticket_put_data):
    """
    修改付款单信息
    :param ticket_put_id:
    :param ticket_put_data:
    :return: Number of affected rows (Example: 0/1)
    """
    return edit(TicketPut, ticket_put_id, ticket_put_data)


def delete_ticket_put(ticket_put_id):
    """
    删除付款单信息
    :param ticket_put_id:
    :return: Number of affected rows (Example: 0/1)
    """
    return delete(TicketPut, ticket_put_id)


def get_ticket_put_rows(page=1, per_page=10, *args, **kwargs):
    """
    获取付款单列表（分页）
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
    rows = get_rows(TicketPut, page, per_page, *args, **kwargs)
    return rows
