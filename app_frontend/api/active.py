#!/usr/bin/env python
# encoding: utf-8

"""
@author: zhanghe
@software: PyCharm
@file: active.py
@time: 2017/5/14 上午1:42
"""


from datetime import datetime
from app_backend.database import db
from app_frontend.api.user import get_user_row_by_id
from app_frontend.api.user_profile import get_user_profile_row_by_id
from app_frontend.models import Active, ActiveItem, User
from app_frontend.tools.db import get_row, get_rows, get_row_by_id, add, edit, delete
from app_common.maps.status_audit import *
from app_common.maps.type_active import *
from app_common.maps.status_active import *


def get_active_row_by_id(active_id):
    """
    通过 id 获取激活信息
    :param active_id:
    :return: None/object
    """
    return get_row_by_id(Active, active_id)


def get_active_row(*args, **kwargs):
    """
    获取激活信息
    :param args:
    :param kwargs:
    :return: None/object
    """
    return get_row(Active, *args, **kwargs)


def add_active(active_data):
    """
    添加激活信息
    :param active_data:
    :return: None/Value of active.id
    """
    return add(Active, active_data)


def edit_active(active_id, active_data):
    """
    修改激活信息
    :param active_id:
    :param active_data:
    :return: Number of affected rows (Example: 0/1)
    """
    return edit(Active, active_id, active_data)


def delete_active(active_id):
    """
    删除激活信息
    :param active_id:
    :return: Number of affected rows (Example: 0/1)
    """
    return delete(Active, active_id)


def get_active_rows(page=1, per_page=10, *args, **kwargs):
    """
    获取激活列表（分页）
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
    rows = get_rows(Active, page, per_page, *args, **kwargs)
    return rows


def user_active(user_id, user_id_active, amount=1):
    """
    用户激活
    :param user_id:
    :param user_id_active:
    :param amount:
    :return:
    """
    try:
        active_obj = db.session.query(Active).filter(Active.user_id == user_id)
        active_info = active_obj.first()

        # 检查剩余激活次数
        if not active_info or active_info.amount < amount:
            raise Exception(u'剩余激活次数不够')

        current_time = datetime.utcnow()

        # 扣除激活码剩余数量
        active_data = {
            'user_id': user_id,
            'amount': active_info.amount - amount,
            'update_time': current_time,
        }
        active_obj.update(active_data)

        # 添加激活码消费明细
        active_item_data = {
            'user_id': user_id,
            'type': TYPE_ACTIVE_USER,
            'amount': amount,
            'sc_id': user_id_active,
            'status_audit': STATUS_AUDIT_SUCCESS,
            'audit_time': current_time,
            'create_time': current_time,
            'update_time': current_time,
        }
        db.session.add(ActiveItem(**active_item_data))

        # 更新激活
        user_data = {
            'status_active': STATUS_ACTIVE_OK,
            'active_time': current_time,
            'update_time': current_time,
        }
        active_obj = db.session.query(User).filter(User.id == user_id_active)
        active_obj.update(user_data)

        db.session.commit()
        return True
    except Exception as e:
        db.session.rollback()
        raise e


def give_active(user_id, user_id_active, amount=1):
    """
    赠送激活数量
    :param user_id:
    :param user_id_active:
    :param amount:
    :return:
    """
    try:
        active_obj = db.session.query(Active).filter(Active.user_id == user_id)
        active_info = active_obj.first()

        # 检查剩余激活次数
        if not active_info or active_info.amount < amount:
            raise Exception(u'剩余激活次数不够')

        current_time = datetime.utcnow()

        # 扣除激活码剩余数量
        active_data = {
            'user_id': user_id,
            'amount': active_info.amount - amount,
            'update_time': current_time,
        }
        active_obj.update(active_data)

        # 添加激活码消费明细
        active_item_data = {
            'user_id': user_id,
            'type': TYPE_ACTIVE_GIVE,
            'amount': amount,
            'sc_id': user_id_active,
            'status_audit': STATUS_AUDIT_SUCCESS,
            'audit_time': current_time,
            'create_time': current_time,
            'update_time': current_time,
        }
        db.session.add(ActiveItem(**active_item_data))

        # 新增接收用户激活码总数量
        active_obj = db.session.query(Active).filter(Active.user_id == user_id_active)
        active_info = active_obj.first()
        if active_info:
            active_data = {
                'user_id': user_id_active,
                'amount': active_info.amount + amount,
                'update_time': current_time,
            }
            active_obj.update(active_data)
        else:
            active_data = {
                'user_id': user_id_active,
                'amount': amount,
                'create_time': current_time,
                'update_time': current_time,
            }
            db.session.add(Active(**active_data))

        db.session.commit()
        return True
    except Exception as e:
        db.session.rollback()
        raise e
