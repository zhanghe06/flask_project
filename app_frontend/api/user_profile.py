#!/usr/bin/env python
# encoding: utf-8

"""
@user: zhanghe
@software: PyCharm
@file: user_profile.py
@time: 16-1-23 下午11:42
"""


from app_frontend.models import UserProfile
from app_frontend.tools.db import get_row, get_rows, get_row_by_id, add, edit, delete


def get_user_profile_row_by_id(user_id):
    """
    通过 id 获取用户信息
    :param user_id:
    :return: None/object
    """
    return get_row_by_id(UserProfile, user_id)


def get_user_profile_row(*args, **kwargs):
    """
    获取用户信息
    :param args:
    :param kwargs:
    :return: None/object
    """
    return get_row(UserProfile, *args, **kwargs)


def add_user_profile(user_data):
    """
    添加用户信息
    :param user_data:
    :return: None/Value of user.id
    """
    return add(UserProfile, user_data)


def edit_user_profile(user_id, user_data):
    """
    修改用户信息
    :param user_id:
    :param user_data:
    :return: Number of affected rows (Example: 0/1)
    """
    return edit(UserProfile, user_id, user_data)


def delete_user_profile(user_id):
    """
    删除用户信息
    :param user_id:
    :return: Number of affected rows (Example: 0/1)
    """
    return delete(UserProfile, user_id)


def get_user_profile_rows(page=1, per_page=10, *args, **kwargs):
    """
    获取用户列表（分页）
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
    rows = get_rows(UserProfile, page, per_page, *args, **kwargs)
    return rows


def user_profile_is_complete(user_id):
    """
    用户基本信息是否完整
    :param user_id:
    :return:
    """
    user_profile_info = get_row_by_id(UserProfile, user_id)
    if not user_profile_info:
        return False
    if user_profile_info.nickname and user_profile_info.phone and user_profile_info.id_card:
        return True
    return False


def get_p_uid_list(user_id):
    """
    获取父级用户id列表
    :param user_id:
    :return:
    """
    result = []
    # 一级
    user_profile_info = get_row_by_id(UserProfile, user_id)
    if not (user_profile_info and user_profile_info.user_pid):
        return result

    result.append(user_profile_info.user_pid)
    user_id = user_profile_info.user_pid

    # 二级
    user_profile_info = get_row_by_id(UserProfile, user_id)
    if not (user_profile_info and user_profile_info.user_pid):
        return result

    result.append(user_profile_info.user_pid)
    user_id = user_profile_info.user_pid

    # 三级
    user_profile_info = get_row_by_id(UserProfile, user_id)
    if not (user_profile_info and user_profile_info.user_pid):
        return result

    result.append(user_profile_info.user_pid)
    return result
