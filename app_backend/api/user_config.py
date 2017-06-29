#!/usr/bin/env python
# encoding: utf-8

"""
@author: zhanghe
@software: PyCharm
@file: user_config.py
@time: 2017/6/29 上午11:41
"""


from app_backend.models import UserConfig
from app_backend.tools.db import get_row, get_rows, get_row_by_id, add, edit, merge, delete


def get_user_config_row_by_id(user_config_id):
    """
    通过 id 获取用户配置信息
    :param user_config_id:
    :return: None/object
    """
    return get_row_by_id(UserConfig, user_config_id)


def get_user_config_row(*args, **kwargs):
    """
    获取用户配置信息
    :param args:
    :param kwargs:
    :return: None/object
    """
    return get_row(UserConfig, *args, **kwargs)


def add_user_config(user_config_data):
    """
    添加用户配置信息
    :param user_config_data:
    :return: None/Value of wallet.id
    """
    return add(UserConfig, user_config_data)


def edit_user_config(user_config_id, user_config_data):
    """
    修改用户配置信息
    :param user_config_id:
    :param user_config_data:
    :return: Number of affected rows (Example: 0/1)
    """
    return edit(UserConfig, user_config_id, user_config_data)


def merge_user_config(user_config_data):
    """
    填充用户配置信息
    :param user_config_data:
    :return: Value of PK
    """
    return merge(UserConfig, user_config_data)


def delete_user_config(user_config_id):
    """
    删除用户配置信息
    :param user_config_id:
    :return: Number of affected rows (Example: 0/1)
    """
    return delete(UserConfig, user_config_id)


def get_user_config_rows(page=1, per_page=10, *args, **kwargs):
    """
    获取用户配置列表（分页）
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
    rows = get_rows(UserConfig, page, per_page, *args, **kwargs)
    return rows

