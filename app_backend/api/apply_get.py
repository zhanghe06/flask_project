#!/usr/bin/env python
# encoding: utf-8

"""
@author: zhanghe
@software: PyCharm
@file: apply_get.py
@time: 2017/4/13 上午11:27
"""


from datetime import datetime
import traceback

from sqlalchemy import func

from app_backend.database import db
from app_backend.models import ApplyGet, Order, ApplyPut
from app_backend.tools.db import get_row, get_rows_by_ids, get_lists, get_rows, get_row_by_id, add, edit, delete
from app_common.maps.status_audit import STATUS_AUDIT_SUCCESS
from app_common.maps.status_order import STATUS_ORDER_COMPLETED, STATUS_ORDER_PROCESSING
from app_common.tools.date_time import get_current_day_time_ends, get_hours, time_local_to_utc, \
    get_current_month_time_ends, get_days, get_current_year_time_ends, get_months


def get_apply_get_row_by_id(apply_get_id):
    """
    通过 id 获取提现申请信息
    :param apply_get_id:
    :return: None/object
    """
    return get_row_by_id(ApplyGet, apply_get_id)


def get_apply_get_row(*args, **kwargs):
    """
    获取提现申请信息
    :param args:
    :param kwargs:
    :return: None/object
    """
    return get_row(ApplyGet, *args, **kwargs)


def add_apply_get(apply_get_data):
    """
    添加提现申请信息
    :param apply_get_data:
    :return: None/Value of apply_get.id
    """
    return add(ApplyGet, apply_get_data)


def edit_apply_get(apply_get_id, apply_get_data):
    """
    修改提现申请信息
    :param apply_get_id:
    :param apply_get_data:
    :return: Number of affected rows (Example: 0/1)
    """
    return edit(ApplyGet, apply_get_id, apply_get_data)


def delete_apply_get(apply_get_id):
    """
    删除提现申请信息
    :param apply_get_id:
    :return: Number of affected rows (Example: 0/1)
    """
    return delete(ApplyGet, apply_get_id)


def get_apply_get_rows_by_ids(ids):
    """
    获取提现申请列表通过主键列表
    :param ids:
    :return: list
    """
    return get_rows_by_ids(ApplyGet, ids)


def get_apply_get_lists(*args, **kwargs):
    """
    获取提现申请列表
    :param args:
    :param kwargs:
    :return: None/list
    """
    return get_lists(ApplyGet, *args, **kwargs)


def get_apply_get_rows(page=1, per_page=10, *args, **kwargs):
    """
    获取提现申请列表（分页）
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
    rows = get_rows(ApplyGet, page, per_page, *args, **kwargs)
    return rows


def apply_get_match(apply_get_id, apply_put_ids, accept_split=0):
    """
    提现申请匹配
    :param apply_get_id:
    :param apply_put_ids:
    :param accept_split:
    :return:
    """
    from app_backend.api.apply_put import get_apply_put_rows_by_ids

    apply_get_info = get_apply_get_row_by_id(apply_get_id)

    # 判断是否已经匹配
    if apply_get_info.status_order == int(STATUS_ORDER_COMPLETED):
        raise Exception(u'不能重复匹配')
    apply_put_list = get_apply_put_rows_by_ids(apply_put_ids)

    # 判断是否同一个人
    apply_put_user_ids = [apply_put_item.user_id for apply_put_item in apply_put_list]
    if apply_get_info.user_id in apply_put_user_ids:
        raise Exception(u'不能匹配给自己')

    # 判断金额
    money_need_match = apply_get_info.money_apply - apply_get_info.money_order

    apply_put_amount = sum([apply_put_item.money_apply-apply_put_item.money_order for apply_put_item in apply_put_list])
    # 如果接收拆分，判断被拆金额是否大于被匹配金额
    if accept_split:
        if money_need_match < apply_put_amount:
            raise Exception(u'选择金额太大')
    elif money_need_match != apply_put_amount:
        raise Exception(u'金额不匹配')

    # 循环投资申请，生成对应的订单
    try:
        money_order = 0
        for apply_put_item in apply_put_list:
            money_match = apply_put_item.money_apply - apply_put_item.money_order
            current_time = datetime.utcnow()

            order_info = {
                'apply_put_id': apply_put_item.id,
                'apply_get_id': apply_get_id,
                'apply_put_uid': apply_put_item.user_id,
                'apply_get_uid': apply_get_info.user_id,
                'money': money_match,
                'status_audit': STATUS_AUDIT_SUCCESS,
                'audit_time': current_time,
                'create_time': current_time,
                'update_time': current_time,
            }
            db.session.add(Order(**order_info))

            # 更新投资申请状态
            apply_put_update_info = {
                'money_order': apply_put_item.money_order + money_match,
                'status_order': STATUS_ORDER_COMPLETED,
                'update_time': current_time,
            }
            apply_put_obj = db.session.query(ApplyPut).filter(ApplyPut.id == apply_put_item.id)
            apply_put_obj.update(apply_put_update_info)

            money_order += money_match

        # 更新提现订单金额和申请状态
        current_time = datetime.utcnow()
        apply_get_update_info = {
            'money_order': money_order,
            'status_order': STATUS_ORDER_COMPLETED if money_order == money_need_match else STATUS_ORDER_PROCESSING,
            'update_time': current_time,
        }
        # result = edit_apply_get(apply_get_id, apply_get_update_info)
        apply_get_obj = db.session.query(ApplyGet).filter(ApplyGet.id == apply_get_id)
        result = apply_get_obj.update(apply_get_update_info)

        db.session.commit()
        return result
    except Exception as e:
        print traceback.print_exc()
        db.session.rollback()
        raise e


def apply_get_stats(time_based='hour'):
    """
    提现申请统计
    :return:
    """
    # 按小时统计
    if time_based == 'hour':
        start_time, end_time = get_current_day_time_ends()
        hours = get_hours()
        result = dict(zip(hours, [0] * len(hours)))
        rows = db.session \
            .query(func.hour(ApplyGet.create_time).label('hour'), func.count(ApplyGet.id)) \
            .filter(ApplyGet.create_time >= time_local_to_utc(start_time), ApplyGet.create_time <= time_local_to_utc(end_time)) \
            .group_by('hour') \
            .limit(len(hours)) \
            .all()
        result.update(dict(rows))
        return [(hour, result[hour]) for hour in hours]
    # 按日期统计
    if time_based == 'date':
        start_time, end_time = get_current_month_time_ends()
        today = datetime.today()
        days = get_days(year=today.year, month=today.month)
        days_full = get_days(year=today.year, month=today.month, full=True)
        result = dict(zip(days_full, [0] * len(days_full)))
        rows = db.session \
            .query(func.date(ApplyGet.create_time).label('date'), func.count(ApplyGet.id)) \
            .filter(ApplyGet.create_time >= time_local_to_utc(start_time), ApplyGet.create_time <= time_local_to_utc(end_time)) \
            .group_by('date') \
            .limit(len(days_full)) \
            .all()
        result.update(dict(rows))
        return [(days[i], result[day]) for i, day in enumerate(days_full)]
    # 按月份统计
    if time_based == 'month':
        start_time, end_time = get_current_year_time_ends()
        months = get_months(False)
        months_zerofill = get_months()
        result = dict(zip(months, [0] * len(months)))
        rows = db.session \
            .query(func.month(ApplyGet.create_time).label('month'), func.count(ApplyGet.id)) \
            .filter(ApplyGet.create_time >= time_local_to_utc(start_time), ApplyGet.create_time <= time_local_to_utc(end_time)) \
            .group_by('month') \
            .limit(len(months)) \
            .all()
        result.update(dict(rows))
        return [(months_zerofill[i], result[month]) for i, month in enumerate(months)]
