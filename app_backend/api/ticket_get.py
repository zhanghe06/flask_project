#!/usr/bin/env python
# encoding: utf-8

"""
@author: zhanghe
@software: PyCharm
@file: ticket_get.py
@time: 2017/4/24 下午11:27
"""


from app_backend.models import TicketGet
from app_backend.tools.db import get_row, get_rows, get_row_by_id, add, edit, delete


def get_ticket_get_row_by_id(ticket_get_id):
    """
    通过 id 获取收款单信息
    :param ticket_get_id:
    :return: None/object
    """
    return get_row_by_id(TicketGet, ticket_get_id)


def get_ticket_get_row(*args, **kwargs):
    """
    获取收款单信息
    :param args:
    :param kwargs:
    :return: None/object
    """
    return get_row(TicketGet, *args, **kwargs)


def add_ticket_get(ticket_get_data):
    """
    添加收款单信息
    :param ticket_get_data:
    :return: None/Value of ticket_get.id
    """
    return add(TicketGet, ticket_get_data)


def edit_ticket_get(ticket_get_id, ticket_get_data):
    """
    修改收款单信息
    :param ticket_get_id:
    :param ticket_get_data:
    :return: Number of affected rows (Example: 0/1)
    """
    return edit(TicketGet, ticket_get_id, ticket_get_data)


def delete_ticket_get(ticket_get_id):
    """
    删除收款单信息
    :param ticket_get_id:
    :return: Number of affected rows (Example: 0/1)
    """
    return delete(TicketGet, ticket_get_id)


def get_ticket_get_rows(page=1, per_page=10, *args, **kwargs):
    """
    获取收款单列表（分页）
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
    rows = get_rows(TicketGet, page, per_page, *args, **kwargs)
    return rows
