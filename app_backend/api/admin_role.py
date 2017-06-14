#!/usr/bin/env python
# encoding: utf-8

"""
@author: zhanghe
@software: PyCharm
@file: admin_role.py
@time: 2017/6/14 上午11:07
"""


from app_backend.models import AdminRole
from app_backend.tools.db import get_row, get_rows, get_row_by_id, add, edit, delete, get_lists


def get_admin_role_row_by_id(admin_role_id):
    """
    通过 id 获取角色信息
    :param admin_role_id:
    :return: None/object
    """
    return get_row_by_id(AdminRole, admin_role_id)


def get_admin_role_row(*args, **kwargs):
    """
    获取角色信息
    :param args:
    :param kwargs:
    :return: None/object
    """
    return get_row(AdminRole, *args, **kwargs)


def add_admin_role(admin_role_data):
    """
    添加角色信息
    :param admin_role_data:
    :return: None/Value of author.id
    """
    return add(AdminRole, admin_role_data)


def edit_admin_role(admin_role_id, admin_role_data):
    """
    修改角色信息
    :param admin_role_id:
    :param admin_role_data:
    :return: Number of affected rows (Example: 0/1)
    """
    return edit(AdminRole, admin_role_id, admin_role_data)


def delete_admin_role(admin_role_id):
    """
    删除角色信息
    :param admin_role_id:
    :return: Number of affected rows (Example: 0/1)
    """
    return delete(AdminRole, admin_role_id)


def get_admin_role_rows(page=1, per_page=10, *args, **kwargs):
    """
    获取角色列表（分页）
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
    rows = get_rows(AdminRole, page, per_page, *args, **kwargs)
    return rows


def get_admin_role_lists(*args, **kwargs):
    """
    获取角色列表
    :param args:
    :param kwargs:
    :return: None/list
    """
    return get_lists(AdminRole, *args, **kwargs)
