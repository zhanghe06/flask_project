#!/usr/bin/env python
# encoding: utf-8

"""
@user: zhanghe
@software: PyCharm
@file: user_profile.py
@time: 17-4-29 下午16:36
"""


from app_backend.models import UserProfile
from app_backend.tools.db import get_row, get_rows, get_lists, get_row_by_id, add, edit, delete
from app_common.tools.tree import tree


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


def get_child_users(user_id):
    """
    获取子节点
    :param user_id:
    :return:
    """
    condition = {
        'user_pid': user_id
    }
    rows = get_lists(UserProfile, **condition)
    return [(row.user_id, row.nickname, row.type_level) for row in rows]


def get_team_tree(user_id):
    """
    获取用户团队3层树形结构
    :param user_id:
    :return:
    """
    team = tree()
    child_users = get_child_users(user_id)
    for user1 in child_users:
        team[user1] = {}
        child_users2 = get_child_users(user1[0])
        for user2 in child_users2:
            team[user1][user2] = {}
            child_users3 = get_child_users(user2[0])
            for user3 in child_users3:
                team[user1][user2][user3] = {}
    # print json.dumps(team, indent=4)
    return team


# def get_team_tree_recursion(user_ids, result):
#     """
#     递归获取用户团队树形结构
#     :param user_ids:
#     :param result:
#     :return:
#     """
#     for user_id in user_ids:
#         child_users = get_child_users(user_id)
#         result.append(child_users)
#         child_user_ids = [child_user[0] for child_user in child_users]
#         print '-'*10, child_user_ids
#         return get_team_tree_recursion(child_user_ids, result)
#
#     if not user_ids:
#         print 'hhhh'
#         return result
#
#
# def get_user_relationship(user_ids):
#     """
#     获取用户层级关系
#     :param user_ids:
#     :return:
#     """
#     result = []
#     return get_team_tree_recursion(user_ids, result)


def get_team_tree_recursion(user_id, team=None, node=None):
    """
    递归获取用户团队树形结构
    :param user_id:
    :param team:
    :param node:
    :return:
    """
    if not team:
        team = tree()
        node = team
    child_users = get_child_users(user_id)
    for child_user in child_users:
        team[child_user] = {}
        node = child_user
        user_id_next = child_user[0]
        get_team_tree_recursion(user_id_next, team, node)
    return team
