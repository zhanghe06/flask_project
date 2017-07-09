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

from app_common.maps.status_audit import STATUS_AUDIT_SUCCESS
from app_common.maps.status_delete import STATUS_DEL_NO
from app_common.maps.status_order import STATUS_ORDER_COMPLETED
from app_common.tools.date_time import get_current_day_time_ends, get_current_month_time_ends
from app_frontend.database import db
from app_common.maps.type_withdraw import *
from app_common.maps.type_pay import *
from app_common.maps.type_payment import *
from app_common.maps.status_apply import *
from app_common.maps.type_apply import *
from app_frontend.models import ApplyGet, Wallet, WalletItem, BitCoin, BitCoinItem
from app_frontend.tools.db import get_row, get_rows, get_row_by_id, add, edit, delete, count


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


def user_apply_get(user_id, type_pay, type_withdraw, money_apply):
    """
    用户提现申请 - 事务
    :param user_id:
    :param type_pay:
    :param type_withdraw:
    :param money_apply:
    :return:
    """
    try:
        current_time = datetime.utcnow()
        # 新增用户提现申请记录
        apply_get_data = {
            'user_id': user_id,
            'type_apply': TYPE_APPLY_USER,
            'type_pay': type_pay,
            'type_withdraw': type_withdraw,
            'money_apply': money_apply,
            'status_apply': STATUS_APPLY_SUCCESS,
            'create_time': current_time,
            'update_time': current_time,
        }

        apply_get_obj = ApplyGet(**apply_get_data)
        db.session.add(apply_get_obj)
        db.session.flush()
        apply_get_id = apply_get_obj.id

        # 新增钱包、数字货币支出明细
        if type_withdraw == TYPE_WITHDRAW_WALLET:
            # 新增钱包明细
            wallet_item_info = {
                'user_id': user_id,
                'type': TYPE_PAYMENT_EXPENSE,
                'amount': money_apply,
                'sc_id': apply_get_id,
                # 'note': u'',
                'status_audit': STATUS_AUDIT_SUCCESS,
                'create_time': current_time,
                'update_time': current_time,
            }
            db.session.add(WalletItem(**wallet_item_info))

            # 获取钱包总额
            wallet_info = db.session.query(Wallet).filter(Wallet.user_id == user_id).first()
            amount_current = wallet_info.amount_current if wallet_info else 0
            # 更新(新增)钱包总额
            wallet_data = {
                'user_id': user_id,
                'amount_current': amount_current - money_apply,
                'create_time': current_time,
                'update_time': current_time,
            }
            db.session.merge(Wallet(**wallet_data))
        # 更新钱包、数字货币余额
        if type_withdraw == TYPE_WITHDRAW_BIT_COIN:
            # 新增数字货币明细
            bit_coin_item_info = {
                'user_id': user_id,
                'type': TYPE_PAYMENT_EXPENSE,
                'amount': money_apply,
                'sc_id': apply_get_id,
                # 'note': u'',
                'status_audit': STATUS_AUDIT_SUCCESS,
                'create_time': current_time,
                'update_time': current_time,
            }
            db.session.add(BitCoinItem(**bit_coin_item_info))

            # 获取数字货币总额
            bit_coin_info = db.session.query(BitCoin).filter(BitCoin.user_id == user_id).first()
            amount = bit_coin_info.amount if bit_coin_info else 0
            # 更新(新增)数字货币总额
            bit_coin_data = {
                'user_id': user_id,
                'amount': amount - money_apply,
                'create_time': current_time,
                'update_time': current_time,
            }
            db.session.merge(BitCoin(**bit_coin_data))
        # 提交事务
        db.session.commit()
        return True
    except Exception as e:
        print traceback.print_exc()
        db.session.rollback()  # 回滚事务
        raise e


def get_current_day_get_amount(user_id=None):
    """
    获取当天提现总额
    :return:
    """
    start_time, end_time = get_current_day_time_ends()
    condition = [
        ApplyGet.create_time >= start_time,
        ApplyGet.create_time <= end_time
    ]
    if user_id:
        condition.append(ApplyGet.user_id == user_id)
    res = db.session \
        .query(func.sum(ApplyGet.money_apply).label('amount')) \
        .filter(*condition) \
        .first()
    return res.amount or 0


def get_current_month_get_amount(user_id=None):
    """
    获取当月提现总额
    :return:
    """
    start_time, end_time = get_current_month_time_ends()
    condition = [
        ApplyGet.create_time >= start_time,
        ApplyGet.create_time <= end_time
    ]
    if user_id:
        condition.append(ApplyGet.user_id == user_id)
    res = db.session \
        .query(func.sum(ApplyGet.money_apply).label('amount')) \
        .filter(*condition) \
        .first()
    return res.amount or 0


def get_get_processing_amount(user_id):
    """
    获取用户提现申请未匹配总金额
    :param user_id:
    :return:
    """
    condition = [
        ApplyGet.user_id == user_id,
        ApplyGet.status_order <= int(STATUS_ORDER_COMPLETED),
        ApplyGet.status_delete == int(STATUS_DEL_NO)
    ]
    res = db.session \
        .query(func.sum(ApplyGet.money_apply).label('money_apply_amount'),
               func.sum(ApplyGet.money_order).label('money_order_amount')) \
        .filter(*condition) \
        .first()
    return (res.money_apply_amount or 0) - (res.money_order_amount or 0)


def get_get_processing_count(user_id):
    """
    获取用户提现申请未匹配总单数
    :param user_id:
    :return:
    """
    condition = [
        ApplyGet.user_id == user_id,
        ApplyGet.status_order <= int(STATUS_ORDER_COMPLETED),
        ApplyGet.status_delete == int(STATUS_DEL_NO)
    ]
    num = count(ApplyGet, *condition)
    return num
