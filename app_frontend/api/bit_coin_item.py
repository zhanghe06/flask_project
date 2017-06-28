#!/usr/bin/env python
# encoding: utf-8

"""
@author: zhanghe
@software: PyCharm
@file: bit_coin_item.py
@time: 2017/6/28 下午2:00
"""


from app_frontend.models import BitCoinItem
from app_frontend.tools.db import get_row, get_rows, get_row_by_id, add, edit, delete


def get_bit_coin_item_row_by_id(bit_coin_item_id):
    """
    通过 id 获取钱包信息
    :param bit_coin_item_id:
    :return: None/object
    """
    return get_row_by_id(BitCoinItem, bit_coin_item_id)


def get_bit_coin_item_row(*args, **kwargs):
    """
    获取钱包信息
    :param args:
    :param kwargs:
    :return: None/object
    """
    return get_row(BitCoinItem, *args, **kwargs)


def add_bit_coin_item(bit_coin_item_data):
    """
    添加钱包信息
    :param bit_coin_item_data:
    :return: None/Value of wallet.id
    """
    return add(BitCoinItem, bit_coin_item_data)


def edit_bit_coin_item(bit_coin_item_id, bit_coin_item_data):
    """
    修改钱包信息
    :param bit_coin_item_id:
    :param bit_coin_item_data:
    :return: Number of affected rows (Example: 0/1)
    """
    return edit(BitCoinItem, bit_coin_item_id, bit_coin_item_data)


def delete_bit_coin_item(bit_coin_item_id):
    """
    删除钱包信息
    :param bit_coin_item_id:
    :return: Number of affected rows (Example: 0/1)
    """
    return delete(BitCoinItem, bit_coin_item_id)


def get_bit_coin_item_rows(page=1, per_page=10, *args, **kwargs):
    """
    获取钱包列表（分页）
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
    rows = get_rows(BitCoinItem, page, per_page, *args, **kwargs)
    return rows
