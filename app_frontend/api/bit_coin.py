#!/usr/bin/env python
# encoding: utf-8

"""
@author: zhanghe
@software: PyCharm
@file: bit_coin.py
@time: 2017/5/5 下午7:56
"""


from app_frontend.models import BitCoin
from app_frontend.tools.db import get_row, get_rows, get_row_by_id, add, edit, delete


def get_bit_coin_row_by_id(bit_coin_id):
    """
    通过 id 获取数字货币信息
    :param bit_coin_id:
    :return: None/object
    """
    return get_row_by_id(BitCoin, bit_coin_id)


def get_bit_coin_row(*args, **kwargs):
    """
    获取数字货币信息
    :param args:
    :param kwargs:
    :return: None/object
    """
    return get_row(BitCoin, *args, **kwargs)


def add_bit_coin(bit_coin_data):
    """
    添加数字货币信息
    :param bit_coin_data:
    :return: None/Value of bit_coin.id
    """
    return add(BitCoin, bit_coin_data)


def edit_bit_coin(bit_coin_id, bit_coin_data):
    """
    修改数字货币信息
    :param bit_coin_id:
    :param bit_coin_data:
    :return: Number of affected rows (Example: 0/1)
    """
    return edit(BitCoin, bit_coin_id, bit_coin_data)


def delete_bit_coin(bit_coin_id):
    """
    删除数字货币信息
    :param bit_coin_id:
    :return: Number of affected rows (Example: 0/1)
    """
    return delete(BitCoin, bit_coin_id)


def get_bit_coin_rows(page=1, per_page=10, *args, **kwargs):
    """
    获取数字货币列表（分页）
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
    rows = get_rows(BitCoin, page, per_page, *args, **kwargs)
    return rows
