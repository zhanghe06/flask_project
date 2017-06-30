#!/usr/bin/env python
# encoding: utf-8

"""
@author: zhanghe
@software: PyCharm
@file: scheduling.py
@time: 2017/6/29 下午8:46
"""


from datetime import datetime

from app_backend.database import db
from app_backend.models import Scheduling, SchedulingItem
from app_backend.tools.db import get_row, get_rows, get_row_by_id, add, edit, delete
from app_common.maps.status_audit import STATUS_AUDIT_SUCCESS
from app_common.maps.type_scheduling import TYPE_SCHEDULING_GIVE


def get_scheduling_row_by_id(scheduling_id):
    """
    通过 id 获取排单信息
    :param scheduling_id:
    :return: None/object
    """
    return get_row_by_id(Scheduling, scheduling_id)


def get_scheduling_row(*args, **kwargs):
    """
    获取排单信息
    :param args:
    :param kwargs:
    :return: None/object
    """
    return get_row(Scheduling, *args, **kwargs)


def add_scheduling(scheduling_data):
    """
    添加排单信息
    :param scheduling_data:
    :return: None/Value of score.id
    """
    return add(Scheduling, scheduling_data)


def edit_scheduling(scheduling_id, scheduling_data):
    """
    修改排单信息
    :param scheduling_id:
    :param scheduling_data:
    :return: Number of affected rows (Example: 0/1)
    """
    return edit(Scheduling, scheduling_id, scheduling_data)


def delete_scheduling(scheduling_id):
    """
    删除排单信息
    :param scheduling_id:
    :return: Number of affected rows (Example: 0/1)
    """
    return delete(Scheduling, scheduling_id)


def get_scheduling_rows(page=1, per_page=10, *args, **kwargs):
    """
    获取排单列表（分页）
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
    rows = get_rows(Scheduling, page, per_page, *args, **kwargs)
    return rows


def give_scheduling(user_id_scheduling, amount=1):
    """
    赠送排单数量
    :param user_id_scheduling:
    :param amount:
    :return:
    """
    try:
        current_time = datetime.utcnow()

        # 添加排单币消费明细
        scheduling_item_data = {
            'user_id': 0,
            'type': TYPE_SCHEDULING_GIVE,
            'amount': amount,
            'sc_id': user_id_scheduling,
            'status_audit': STATUS_AUDIT_SUCCESS,
            'audit_time': current_time,
            'create_time': current_time,
            'update_time': current_time,
        }
        db.session.add(SchedulingItem(**scheduling_item_data))

        # 新增接收用户排单币总数量
        scheduling_obj = db.session.query(Scheduling).filter(Scheduling.user_id == user_id_scheduling)
        scheduling_info = scheduling_obj.first()
        if scheduling_info:
            scheduling_data = {
                'user_id': user_id_scheduling,
                'amount': scheduling_info.amount + amount,
                'update_time': current_time,
            }
            scheduling_obj.update(scheduling_data)
        else:
            scheduling_data = {
                'user_id': user_id_scheduling,
                'amount': amount,
                'create_time': current_time,
                'update_time': current_time,
            }
            db.session.add(Scheduling(**scheduling_data))

        db.session.commit()
        return True
    except Exception as e:
        db.session.rollback()
        raise e
