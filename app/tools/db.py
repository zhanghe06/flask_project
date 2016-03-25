#!/usr/bin/env python
# encoding: utf-8

"""
@author: zhanghe
@software: PyCharm
@file: tools.py
@time: 16-1-25 下午8:39
"""


from ..database import db_session


def get_row_by_id(model_name, pk_id):
    """
    通过 id 获取信息
    :param model_name:
    :param pk_id:
    :return: None/object
    """
    row = db_session.query(model_name).get(pk_id)
    return row


def get_row(model_name, *args, **kwargs):
    """
    获取用户信息
    Usage:
        # 方式一
        get_row(User, User.id > 1)
        # 方式二
        test_condition = {
            'name': "Larry"
        }
        get_row(User, **test_condition)
    :param model_name:
    :param args:
    :param kwargs:
    :return: None/object
    """
    if args:
        row = db_session.query(model_name).filter(*args).first()
        return row
    if kwargs:
        row = db_session.query(model_name).filter_by(**kwargs).first()
        return row
    return None


def add(model_name, data):
    """
    添加用户信息
    :param model_name:
    :param data:
    :return: None/Value of model_obj.id
    """
    model_obj = model_name(**data)
    db_session.add(model_obj)
    db_session.commit()
    return model_obj.id


def edit_by_id(model_name, pk_id, data):
    """
    修改用户信息
    :param model_name:
    :param pk_id:
    :param data:
    :return: Number of affected rows (Example: 0/1)
    """
    model_obj = db_session.query(model_name).filter(model_name.id == pk_id)
    result = model_obj.update(data)
    db_session.commit()
    return result


def delete_by_id(model_name, pk_id):
    """
    删除用户信息
    :param model_name:
    :param pk_id:
    :return: Number of affected rows (Example: 0/1)
    """
    model_obj = db_session.query(model_name).filter(model_name.id == pk_id)
    result = model_obj.delete()
    db_session.commit()
    return result


def get_rows(model_name, page=1, per_page=10, *args, **kwargs):
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
    :param model_name:
    :param page:
    :param per_page:
    :param args:
    :param kwargs:
    :return: None/object
    """
    if args:
        rows = model_name.query.filter(*args).paginate(page, per_page, False)
        return rows
    if kwargs:
        rows = model_name.query.filter_by(**kwargs).paginate(page, per_page, False)
        return rows
    return model_name.query.paginate(page, per_page, False)


def test_user():
    """
    测试 User
    :return:
    """
    from ..models import User
    print '\n测试增删改查'
    # 测试获取
    row = get_row_by_id(User, 1)
    print row
    if row:
        print row.id, row.email, row.nickname
    # 测试添加
    user_info = {
        'email': 'bob@gmail.com',
        'password': '123456',
        'nickname': 'Bob',
    }
    result = add(User, user_info)
    print result
    # 测试修改
    result = edit_by_id(User, 2, {'nickname': 'Emma'})
    print result
    # 测试删除
    result = delete_by_id(User, 2)
    print result

    print '\n测试单条信息'
    test_condition = {
        'nickname': "Larry"
    }
    row = get_row(User, **test_condition)
    print row
    if row:
        print row.id, row.email, row.nickname
    row = get_row(User, User.id > 0)
    print row
    if row:
        print row.id, row.email, row.nickname

    print '测试列表信息'
    rows = get_rows(User, 1, 10, User.id > 0, User.id < 5)
    if rows:
        for item in rows.items:
            print item.id, item.email, item.nickname

    rows = get_rows(User, 1, 10, **{'nickname': "Bob"})
    if rows:
        for item in rows.items:
            print item.id, item.email, item.nickname


if __name__ == '__main__':
    test_user()
