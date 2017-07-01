#!/usr/bin/env python
# encoding: utf-8

"""
@author: zhanghe
@software: PyCharm
@file: tools.py
@time: 16-1-25 下午8:39
"""

# todo get_rows order_by
# todo insert ignore


from app_backend.database import db
from sqlalchemy.inspection import inspect


def get_row_by_id(model_name, pk_id):
    """
    通过 id 获取信息
    :param model_name:
    :param pk_id:
    :return: None/object
    """
    try:
        row = db.session.query(model_name).get(pk_id)
        db.session.commit()
        return row
    except Exception as e:
        db.session.rollback()
        raise e


def get_rows_by_ids(model_name, pk_ids):
    """
    通过一组 ids 获取信息列表
    :param model_name:
    :param pk_ids:
    :return: list
    """
    try:
        model_pk = inspect(model_name).primary_key[0]
        rows = db.session.query(model_name).filter(model_pk.in_(pk_ids)).all()
        db.session.commit()
        return rows
    except Exception as e:
        db.session.rollback()
        raise e


def get_limit_rows_by_last_id(model_name, last_pk_id, limit_num, *args, **kwargs):
    """
    通过最后一个主键 id 获取最新信息列表
    适用场景：
    1、动态加载
    2、快速定位
    :param model_name:
    :param last_pk_id:
    :param limit_num:
    :param args:
    :param kwargs:
    :return: list
    """
    try:
        model_pk = inspect(model_name).primary_key[0]
        rows = db.session.query(model_name).filter(model_pk > last_pk_id, *args).filter_by(**kwargs).limit(limit_num).all()
        db.session.commit()
        return rows
    except Exception as e:
        db.session.rollback()
        raise e


def get_row(model_name, *args, **kwargs):
    """
    获取信息
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
    try:
        row = db.session.query(model_name).filter(*args).filter_by(**kwargs).first()
        db.session.commit()
        return row
    except Exception as e:
        db.session.rollback()
        raise e


def get_lists(model_name, *args, **kwargs):
    """
    获取列表信息
    Usage:
        # 方式一
        get_lists(User, User.id > 1)
        # 方式二
        test_condition = {
            'name': "Larry"
        }
        get_lists(User, **test_condition)
    :param model_name:
    :param args:
    :param kwargs:
    :return: None/list
    """
    try:
        lists = db.session.query(model_name).filter(*args).filter_by(**kwargs).all()
        db.session.commit()
        return lists
    except Exception as e:
        db.session.rollback()
        raise e


def count(model_name, *args, **kwargs):
    """
    计数
    Usage:
        # 方式一
        count(User, User.id > 1)
        # 方式二
        test_condition = {
            'name': "Larry"
        }
        count(User, **test_condition)
    :param model_name:
    :param args:
    :param kwargs:
    :return: 0/Number（int）
    """
    try:
        result_count = db.session.query(model_name).filter(*args).filter_by(**kwargs).count()
        db.session.commit()
        return result_count
    except Exception as e:
        db.session.rollback()
        raise e


def add(model_name, data):
    """
    添加信息
    :param model_name:
    :param data:
    :return: None/Value of model_obj.PK
    """
    model_obj = model_name(**data)
    try:
        db.session.add(model_obj)
        db.session.commit()
        return inspect(model_obj).identity[0]
    except Exception as e:
        db.session.rollback()
        raise e


def edit(model_name, pk_id, data):
    """
    修改信息
    :param model_name:
    :param pk_id:
    :param data:
    :return: Number of affected rows (Example: 0/1)
    """
    model_pk = inspect(model_name).primary_key[0]
    try:
        model_obj = db.session.query(model_name).filter(model_pk == pk_id)
        result = model_obj.update(data)
        db.session.commit()
        return result
    except Exception as e:
        db.session.rollback()
        raise e


def merge(model_name, data):
    """
    覆盖信息(没有新增，存在更新)
    数据中必须带主键字段
    :param model_name:
    :param data:
    :return: Value of PK
    """
    model_obj = model_name(**data)
    try:
        r = db.session.merge(model_obj)
        db.session.commit()
        return inspect(r).identity[0]
    except Exception as e:
        db.session.rollback()
        raise e


def increase(model_name, pk_id, field, num=1):
    """
    字段自增
    :param model_name:
    :param pk_id:
    :param field:
    :param num:
    :return: Number of affected rows (Example: 0/1)
    """
    model_pk = inspect(model_name).primary_key[0]
    try:
        model_obj = db.session.query(model_name).filter(model_pk == pk_id)
        value = getattr(model_name, field) + num
        data = {
            field: value
        }
        result = model_obj.update(data)
        db.session.commit()
        return result
    except Exception as e:
        db.session.rollback()
        raise e


def delete(model_name, pk_id):
    """
    删除信息
    :param model_name:
    :param pk_id:
    :return: Number of affected rows (Example: 0/1)
    """
    model_pk = inspect(model_name).primary_key[0]
    try:
        model_obj = db.session.query(model_name).filter(model_pk == pk_id)
        result = model_obj.delete()
        db.session.commit()
        return result
    except Exception as e:
        db.session.rollback()
        raise e


def get_rows(model_name, page=1, per_page=10, *args, **kwargs):
    """
    获取信息列表（分页）
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
    try:
        rows = model_name.query. \
            filter(*args). \
            filter_by(**kwargs). \
            order_by(inspect(model_name).primary_key[0].desc()). \
            paginate(page, per_page, False)
        db.session.commit()
        return rows
    except Exception as e:
        db.session.rollback()
        raise e


def insert_rows(model_name, data_list):
    """
    批量插入数据（遇到主键/唯一索引重复，忽略报错，继续执行下一条插入任务）
    注意：
    Warning: Duplicate entry
    警告有可能会提示：
    UnicodeEncodeError: 'ascii' codec can't encode characters in position 17-20: ordinal not in range(128)
    处理：
    import sys

    reload(sys)
    sys.setdefaultencoding('utf8')

    sql 语句大小限制
    show VARIABLES like '%max_allowed_packet%';
    参考：http://dev.mysql.com/doc/refman/5.7/en/packet-too-large.html

    :param model_name:
    :param data_list:
    :return:
    """
    try:
        result = db.session.execute(model_name.__table__.insert().prefix_with('IGNORE'), data_list)
        db.session.commit()
        return result.rowcount
    except Exception as e:
        db.session.rollback()
        raise e


def update_rows(model_name, data, *args, **kwargs):
    """
    批量修改数据
    :param model_name:
    :param data:
    :param args:
    :param kwargs:
    :return:
    """
    try:
        model_obj = db.session.query(model_name).filter(*args).filter_by(**kwargs)
        result = model_obj.update(data, synchronize_session=False)
        db.session.commit()
        return result
    except Exception as e:
        db.session.rollback()
        raise e


def update_rows_by_ids(model_name, pk_ids, data):
    """
    根据一组主键id 批量修改数据
    """
    model_pk = inspect(model_name).primary_key[0]
    try:
        model_obj = db.session.query(model_name).filter(model_pk.in_(pk_ids))
        result = model_obj.update(data, synchronize_session=False)
        db.session.commit()
        return result
    except Exception as e:
        db.session.rollback()
        raise e


def test_user():
    """
    测试 User
    :return:
    """
    from app.models import User
    print '\n测试增删改查'
    # 测试获取
    row = get_row_by_id(User, 1)
    print row
    if row:
        print row.id, row.email, row.nickname
    # 测试添加
    user_info = {
        'email': 'admin@gmail.com',
        # 'password': '123456',
        'nickname': 'Admin',
    }
    # 测试计数
    result_count = count(User, User.id > 1, **{'id': 2})
    print result_count

    result = add(User, user_info)
    print result
    # # 测试修改
    # result = edit(User, 2, {'nickname': 'Emma'})
    # print result
    # # 测试删除
    # result = delete(User, 2)
    # print result
    #
    print '\n测试单条信息'
    test_condition = {
        'nickname': "Larry"
    }
    row = get_row(User, **test_condition)
    print row
    if row:
        print row.id, row.email, row.nickname
    row = get_row(User, User.id > 0, id=3)
    print row
    if row:
        print row.id, row.email, row.nickname


def test_blog():
    """
    测试 Blog
    :return:
    """
    from app.models import Blog
    print '测试通过上一次id获取列表信息'
    rows = get_limit_rows_by_last_id(Blog, 1, 4, Blog.id > 2, **{'id': 7})
    if rows:
        for item in rows:
            print item.id, item.author, item.title, item.pub_date

    print '测试列表信息'
    rows = get_rows(Blog, 1, 10, Blog.id > 0, Blog.id < 9, **{'id': 7})
    if rows:
        for item in rows.items:
            print item.id, item.author, item.title, item.pub_date


def test_transaction():
    """
    测试事务
    """
    from app.models import User
    from datetime import datetime
    print '\n测试事务'

    try:
        current_time = datetime.utcnow()
        user_info_01 = {
            'nickname': 'rose',
            'avatar_url': '',
            'email': 'rose@gmail.com',
            'phone': '13818731111',
            'create_time': current_time,
            'update_time': current_time,
            'last_ip': '0.0.0.0'
        }
        model_obj_01 = User(**user_info_01)
        db.session.add(model_obj_01)
        db.session.flush()
        print inspect(model_obj_01).identity[0]

        user_info_02 = {
            'nickname': 'pit',
            'avatar_url': '',
            'email': 'pit@gmail.com',
            'phone': '13818730000',
            'create_time': current_time,
            'update_time': current_time,
            'last_ip': '0.0.0.0'
        }
        model_obj_02 = User(**user_info_02)
        db.session.add(model_obj_02)
        db.session.flush()
        print inspect(model_obj_02).identity[0]

    except Exception as e:
        db.session.rollback()
        raise e


def test_label():
    """
    测试字符串截取和别名
    SqLite substr
    MySql left
    :return:
    """
    from app.models import User
    from sqlalchemy import func
    rows = db.session.query(User.id, func.substr(User.nickname, 2).label('nickname_new'),
                            User.create_time).filter().order_by(User.nickname, User.create_time.desc()).all()
    for row in rows:
        print row.id, row.nickname_new, row.create_time


def test_join():
    from app_backend.models import User, UserProfile
    # rows = db.session.query(User, UserProfile).outerjoin(UserProfile, User.id == UserProfile.user_id).order_by(User.id.desc()).all()
    # for row in rows:
    #     print row[0].__dict__, row[1].__dict__
    # paginate = User.query.join(UserProfile, User.id == UserProfile.user_id).add_columns(User.id, UserProfile.nickname).order_by(User.id.desc()).paginate(1, 10, False)
    paginate = User.query.join(UserProfile, User.id == UserProfile.user_id).add_entity(UserProfile).order_by(User.id.desc()).paginate(1, 10, False)
    print paginate.items
    for (a, b) in paginate.items:
        print a.id, b.user_id


if __name__ == '__main__':
    # test_user()
    # test_blog()
    # test_transaction()
    # test_label()
    test_join()
