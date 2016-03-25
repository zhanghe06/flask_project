#!/usr/bin/env python
# encoding: utf-8

"""
@author: zhanghe
@software: PyCharm
@file: author.py
@time: 16-1-17 上午12:05
"""


from app.models import Author
from app.tools.db import get_row, get_rows, get_row_by_id, add, edit, delete


def get_author_row_by_id(author_id):
    """
    通过 id 获取博客信息
    :param author_id:
    :return: None/object
    """
    return get_row_by_id(Author, author_id)


def get_author_row(*args, **kwargs):
    """
    获取博客信息
    :param args:
    :param kwargs:
    :return: None/object
    """
    return get_row(Author, *args, **kwargs)


def add_author(author_data):
    """
    添加博客信息
    :param author_data:
    :return: None/Value of author.id
    """
    return add(Author, author_data)


def edit_author(author_id, author_data):
    """
    修改博客信息
    :param author_id:
    :param author_data:
    :return: Number of affected rows (Example: 0/1)
    """
    return edit(Author, author_id, author_data)


def delete_author(author_id):
    """
    删除博客信息
    :param author_id:
    :return: Number of affected rows (Example: 0/1)
    """
    return delete(Author, author_id)


def get_author_rows(page=1, per_page=10, *args, **kwargs):
    """
    获取博客列表（分页）
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
    rows = get_rows(Author, page, per_page, *args, **kwargs)
    return rows
