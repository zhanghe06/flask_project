#!/usr/bin/env python
# encoding: utf-8

"""
@user: zhanghe
@software: PyCharm
@file: user.py
@time: 16-1-23 下午11:42
"""


from database import db_session
from models import User


def get_row_by_id(user_id):
    """
    通过 id 获取用户信息
    :param user_id:
    :return: None/object
    """
    row = db_session.query(User).filter(User.id == user_id).first()
    return row


def get_row(*args, **kwargs):
    """
    获取用户信息
    Usage:
        # 方式一
        get_row(User.id > 1)
        # 方式二
        test_condition = {
            'name': "Larry"
        }
        get_row(**test_condition)
    :param args:
    :param kwargs:
    :return: None/object
    """
    if args:
        row = db_session.query(User).filter(*args).first()
        return row
    if kwargs:
        row = db_session.query(User).filter_by(**kwargs).first()
        return row
    return None


def add(user_data):
    """
    添加用户信息
    :param user_data:
    :return: None/Value of user.id
    """
    user = User(**user_data)
    db_session.add(user)
    db_session.commit()
    return user.id


def edit(user_id, user_info):
    """
    修改用户信息
    :param user_id:
    :param user_info:
    :return: Number of affected rows (Example: 0/1)
    """
    user = db_session.query(User).filter(User.id == user_id)
    result = user.update(user_info)
    db_session.commit()
    return result


def delete(user_id):
    """
    删除用户信息
    :param user_id:
    :return: Number of affected rows (Example: 0/1)
    """
    user = db_session.query(User).filter(User.id == user_id)
    result = user.delete()
    db_session.commit()
    return result


def get_rows(page=1, per_page=10, *args, **kwargs):
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
    :return: None/object
    """
    if args:
        rows = User.query.filter(*args).paginate(page, per_page, False)
        return rows
    if kwargs:
        rows = User.query.filter_by(**kwargs).paginate(page, per_page, False)
        return rows
    return None


def test():
    """
    测试
    :return:
    """
    print '测试增删改查'
    # 测试获取
    row = get_row_by_id(5)
    print row
    if row:
        print row.id, row.email, row.nickname
    # 测试添加
    user_info = {
        'email': 'bob@gmail.com',
        'password': '123456',
        'nickname': 'Bob',
    }
    result = add(user_info)
    print result
    # 测试修改
    result = edit(2, {'nickname': 'Emma'})
    print result
    # 测试删除
    result = delete(2)
    print result


def test_get_row():
    """
    测试信息获取
    :return:
    """
    print '测试单条信息'
    test_condition = {
        'nickname': "Larry"
    }
    row = get_row(**test_condition)
    print row
    if row:
        print row.id, row.email, row.nickname

    row = get_row(User.id > 1)
    print row
    if row:
        print row.id, row.email, row.nickname


def test_get_rows():
    """
    测试列表获取
    :return:
    """
    print '测试列表信息'
    rows = get_rows(1, 10, User.id > 2, User.id < 5)
    for item in rows.items:
        print item.id, item.email, item.nickname

    rows = get_rows(1, 10, **{'nickname': "Larry"})
    for item in rows.items:
        print item.id, item.email, item.nickname


if __name__ == '__main__':
    # test()
    test_get_row()
    test_get_rows()
