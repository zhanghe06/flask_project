#!/usr/bin/env python
# encoding: utf-8

"""
@author: zhanghe
@software: PyCharm
@file: order_bill.py
@time: 2017/5/13 下午11:24
"""


from app_frontend.models import OrderBill
from app_frontend.tools.db import get_row, get_rows, get_row_by_id, add, edit, delete, get_lists, count


def get_order_bill_row_by_id(order_bill_id):
    """
    通过 id 获取订单支付凭证信息
    :param order_bill_id:
    :return: None/object
    """
    return get_row_by_id(OrderBill, order_bill_id)


def get_order_bill_row(*args, **kwargs):
    """
    获取订单支付凭证信息
    :param args:
    :param kwargs:
    :return: None/object
    """
    return get_row(OrderBill, *args, **kwargs)


def add_order_bill(order_data):
    """
    添加订单支付凭证信息
    :param order_data:
    :return: None/Value of order.id
    """
    return add(OrderBill, order_data)


def edit_order_bill(order_bill_id, order_data):
    """
    修改订单支付凭证信息
    :param order_bill_id:
    :param order_data:
    :return: Number of affected rows (Example: 0/1)
    """
    return edit(OrderBill, order_bill_id, order_data)


def delete_order_bill(order_bill_id):
    """
    删除订单支付凭证信息
    :param order_bill_id:
    :return: Number of affected rows (Example: 0/1)
    """
    return delete(OrderBill, order_bill_id)


def get_order_bill_rows(page=1, per_page=10, *args, **kwargs):
    """
    获取订单支付凭证列表（分页）
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
    rows = get_rows(OrderBill, page, per_page, *args, **kwargs)
    return rows


def get_order_bill_lists(*args, **kwargs):
    """
    获取订单支付凭证列表
    :param args:
    :param kwargs:
    :return: None/list
    """
    return get_lists(OrderBill, *args, **kwargs)


def get_order_bill_count(*args, **kwargs):
    """
    获取订单支付凭证个数
    :param args:
    :param kwargs:
    :return: 0/Number（int）
    """
    return count(OrderBill, *args, **kwargs)
