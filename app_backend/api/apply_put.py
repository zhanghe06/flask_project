#!/usr/bin/env python
# encoding: utf-8

"""
@author: zhanghe
@software: PyCharm
@file: apply_put.py
@time: 2017/4/13 下午9:45
"""


from datetime import datetime
import traceback

from app_backend.models import ApplyGet, Order, ApplyPut
from app_backend.tools.db import get_row, get_rows_by_ids, get_lists, get_rows, get_row_by_id, add, edit, delete
from app_backend.database import db
from app_common.maps.status_audit import STATUS_AUDIT_SUCCESS
from app_common.maps.status_order import STATUS_ORDER_COMPLETED, STATUS_ORDER_PROCESSING


def get_apply_put_row_by_id(apply_put_id):
    """
    通过 id 获取投资申请信息
    :param apply_put_id:
    :return: None/object
    """
    return get_row_by_id(ApplyPut, apply_put_id)


def get_apply_put_row(*args, **kwargs):
    """
    获取投资申请信息
    :param args:
    :param kwargs:
    :return: None/object
    """
    return get_row(ApplyPut, *args, **kwargs)


def add_apply_put(apply_put_data):
    """
    添加投资申请信息
    :param apply_put_data:
    :return: None/Value of apply_put.id
    """
    return add(ApplyPut, apply_put_data)


def edit_apply_put(apply_put_id, apply_put_data):
    """
    修改投资申请信息
    :param apply_put_id:
    :param apply_put_data:
    :return: Number of affected rows (Example: 0/1)
    """
    return edit(ApplyPut, apply_put_id, apply_put_data)


def delete_apply_put(apply_put_id):
    """
    删除投资申请信息
    :param apply_put_id:
    :return: Number of affected rows (Example: 0/1)
    """
    return delete(ApplyPut, apply_put_id)


def get_apply_put_rows_by_ids(ids):
    """
    获取投资申请列表
    :param ids:
    :return: list
    """
    return get_rows_by_ids(ApplyPut, ids)


def get_apply_put_lists(*args, **kwargs):
    """
    获取投资申请列表
    :param args:
    :param kwargs:
    :return: None/list
    """
    return get_lists(ApplyPut, *args, **kwargs)


def get_apply_put_rows(page=1, per_page=10, *args, **kwargs):
    """
    获取投资申请列表（分页）
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
    rows = get_rows(ApplyPut, page, per_page, *args, **kwargs)
    return rows


def apply_put_match(apply_put_id, apply_get_ids, accept_split=0):
    """
    投资申请匹配
    :param apply_put_id:
    :param apply_get_ids:
    :param accept_split:
    :return:
    """
    from app_backend.api.apply_get import get_apply_get_rows_by_ids

    apply_put_info = get_apply_put_row_by_id(apply_put_id)

    # 判断是否已经匹配
    if apply_put_info.status_order == STATUS_ORDER_COMPLETED:
        raise Exception(u'不能重复匹配')
    apply_get_list = get_apply_get_rows_by_ids(apply_get_ids)

    # 判断是否同一个人
    apply_get_user_ids = [apply_get_item.user_id for apply_get_item in apply_get_list]
    if apply_put_info.user_id in apply_get_user_ids:
        raise Exception(u'不能匹配给自己')

    # 判断金额
    money_need_match = apply_put_info.money_apply - apply_put_info.money_order

    apply_get_amount = sum(
        [apply_get_item.money_apply - apply_get_item.money_order for apply_get_item in apply_get_list])
    # 如果接收拆分，判断被拆金额是否大于被匹配金额
    if accept_split:
        if money_need_match < apply_get_amount:
            raise Exception(u'选择金额太大')
    elif money_need_match != apply_get_amount:
        raise Exception(u'金额不匹配')

    # 循环提现申请，生成对应的订单
    try:
        money_order = 0
        for apply_get_item in apply_get_list:
            money_match = apply_get_item.money_apply - apply_get_item.money_order
            current_time = datetime.utcnow()

            order_info = {
                'apply_put_id': apply_put_id,
                'apply_get_id': apply_get_item.id,
                'apply_put_uid': apply_put_info.user_id,
                'apply_get_uid': apply_get_item.user_id,
                'money': money_match,
                'status_audit': STATUS_AUDIT_SUCCESS,
                'audit_time': current_time,
                'create_time': current_time,
                'update_time': current_time,
            }
            db.session.add(Order(**order_info))

            # 更新提现申请状态
            apply_get_update_info = {
                'money_order': apply_get_item.money_order + money_match,
                'status_order': STATUS_ORDER_COMPLETED,
                'update_time': current_time,
            }
            apply_get_obj = db.session.query(ApplyGet).filter(ApplyGet.id == apply_get_item.id)
            apply_get_obj.update(apply_get_update_info)

            money_order += money_match

        # 更新投资订单金额和申请状态
        current_time = datetime.utcnow()
        apply_put_update_info = {
            'money_order': money_order,
            'status_order': STATUS_ORDER_COMPLETED if money_order == money_need_match else STATUS_ORDER_PROCESSING,
            'update_time': current_time,
        }
        # result = edit_apply_get(apply_get_id, apply_get_update_info)
        apply_put_obj = db.session.query(ApplyPut).filter(ApplyPut.id == apply_put_id)
        result = apply_put_obj.update(apply_put_update_info)

        db.session.commit()
        return result
    except Exception as e:
        print traceback.print_exc()
        db.session.rollback()
        raise e
