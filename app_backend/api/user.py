#!/usr/bin/env python
# encoding: utf-8

"""
@user: zhanghe
@software: PyCharm
@file: user.py
@time: 17-4-21 下午10:42
"""


from datetime import datetime
from sqlalchemy.sql import func

from app_backend.database import db
from app_backend import app
from app_backend.models import User
from app_backend.models import UserBank
from app_backend.models import UserProfile
from app_backend.tools.db import get_row, get_rows, get_row_by_id, add, edit, delete
from app_common.maps.status_lock import *
from app_common.tools.date_time import get_hours, get_days, get_months, time_local_to_utc
from app_common.tools.date_time import get_current_day_time_ends
from app_common.tools.date_time import get_current_month_time_ends
from app_common.tools.date_time import get_current_year_time_ends

PER_PAGE_BACKEND = app.config['PER_PAGE_BACKEND']


def get_user_row_by_id(user_id):
    """
    通过 id 获取用户信息
    :param user_id:
    :return: None/object
    """
    return get_row_by_id(User, user_id)


def get_user_row(*args, **kwargs):
    """
    获取用户信息
    :param args:
    :param kwargs:
    :return: None/object
    """
    return get_row(User, *args, **kwargs)


def add_user(user_data):
    """
    添加用户信息
    :param user_data:
    :return: None/Value of user.id
    """
    return add(User, user_data)


def edit_user(user_id, user_data):
    """
    修改用户信息
    :param user_id:
    :param user_data:
    :return: Number of affected rows (Example: 0/1)
    """
    return edit(User, user_id, user_data)


def delete_user(user_id):
    """
    删除用户信息
    :param user_id:
    :return: Number of affected rows (Example: 0/1)
    """
    return delete(User, user_id)


def get_user_rows(page=1, per_page=10, *args, **kwargs):
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
    rows = get_rows(User, page, per_page, *args, **kwargs)
    return rows


def get_user_detail_rows(page=1, per_page=10, *args, **kwargs):
    """
    获取用户详细信息列表（分页）
        User
        UserProfile
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
    rows = User.query. \
        outerjoin(UserProfile, User.id == UserProfile.user_id). \
        outerjoin(UserBank, User.id == UserBank.user_id). \
        add_entity(UserProfile). \
        add_entity(UserBank). \
        filter(*args). \
        filter_by(**kwargs). \
        paginate(page, PER_PAGE_BACKEND, False)
    return rows


def lock(user_id):
    """
    锁定用户
    :param user_id:
    :return: Number of affected rows (Example: 0/1)
    """
    current_time = datetime.utcnow()
    user_data = {
        'status_lock': STATUS_LOCK_OK,
        'lock_time': current_time,
        'update_time': current_time
    }
    result = edit_user(user_id, user_data)
    return result


def unlock(user_id):
    """
    解锁用户
    :param user_id:
    :return: Number of affected rows (Example: 0/1)
    """
    current_time = datetime.utcnow()
    user_data = {
        'status_lock': STATUS_LOCK_NO,
        'update_time': current_time
    }
    result = edit_user(user_id, user_data)
    return result


def user_reg_stats(time_based='hour'):
    """
    用户注册统计
    :return:
    """
    result, rows = {}, {}
    # 按小时统计
    if time_based == 'hour':
        start_time, end_time = get_current_day_time_ends()
        hours = get_hours()
        result = dict(zip(hours, [0] * len(hours)))
        rows = db.session \
            .query(func.hour(User.create_time).label('hour'), func.count(User.id)) \
            .filter(User.create_time >= time_local_to_utc(start_time), User.create_time <= time_local_to_utc(end_time)) \
            .group_by('hour') \
            .limit(len(hours)) \
            .all()
        result.update(dict(rows))
        return [(hour, result[hour]) for hour in hours]
    # 按日期统计
    if time_based == 'date':
        start_time, end_time = get_current_month_time_ends()
        days = get_days()
        result = dict(zip(days, [0] * len(days)))
        rows = db.session \
            .query(func.hour(User.create_time).label('date'), func.count(User.id)) \
            .filter(User.create_time >= time_local_to_utc(start_time), User.create_time <= time_local_to_utc(end_time)) \
            .group_by('date') \
            .limit(len(days)) \
            .all()
        result.update(dict(rows))
        return result
    # 按月份统计
    if time_based == 'month':
        start_time, end_time = get_current_year_time_ends()
        months = get_months()
        result = dict(zip(months, [0] * len(months)))
        rows = db.session \
            .query(func.hour(User.create_time).label('month'), func.count(User.id)) \
            .filter(User.create_time >= time_local_to_utc(start_time), User.create_time <= time_local_to_utc(end_time)) \
            .group_by('month') \
            .limit(len(months)) \
            .all()
    result.update(dict(rows))
    return result
