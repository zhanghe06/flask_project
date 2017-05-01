#!/usr/bin/env python
# encoding: utf-8

"""
@author: zhanghe
@software: PyCharm
@file: filters.py
@time: 2017/4/13 下午2:33
@desc: 自定义过滤器
"""
from itsdangerous import URLSafeSerializer

from app_frontend import app
from app_frontend.api.user_profile import get_user_profile_row_by_id
from app_frontend.api.wallet import get_wallet_row_by_id
from app_frontend.api.score import get_score_row_by_id
from app_frontend.api.bonus import get_bonus_row_by_id
from app_common.maps.level_type import LEVEL_TYPE_DICT
from app_common.maps.type_apply import TYPE_APPLY_DICT
from app_common.maps.auth_type import AUTH_TYPE_DICT
from app_common.maps.status_audit import STATUS_AUDIT_DICT
from app_common.maps.status_apply import STATUS_APPLY_DICT
from app_common.maps.status_order import STATUS_ORDER_DICT
from app_common.maps.status_delete import STATUS_DEL_DICT
from app_common.maps.status_pay import STATUS_PAY_DICT
from app_common.maps.status_rec import STATUS_REC_DICT
import time


@app.template_filter('reverse')
def reverse_filter(s):
    return s[::-1]


@app.template_filter('url_t')
def url_t_filter(s):
    return '%s?t=%s' % (s, time.time())


@app.template_filter('time_diff_pretty')
def time_diff_pretty_filter(delta_s):
    """
    时间差友好显示
    {{ 1234 | time_diff_pretty }} >> 2分34秒
    :param delta_s:
    :return:
    """
    delta_s *= 1.00
    result = u''
    if delta_s >= (365 * 24 * 60 * 60):
        count = int(delta_s / (365 * 24 * 60 * 60))
        result += u'%s年' % count
        delta_s -= count * 365 * 24 * 60 * 60
    if delta_s >= (30 * 24 * 60 * 60):
        count = int(delta_s / (30 * 24 * 60 * 60))
        result += u'%s月' % count
        delta_s -= count * 30 * 24 * 60 * 60
    if delta_s >= (24 * 60 * 60):
        count = int(delta_s / (24 * 60 * 60))
        result += u'%s天' % count
        delta_s -= count * 24 * 60 * 60
    if delta_s >= (60 * 60):
        count = int(delta_s / (60 * 60))
        result += u'%s小时' % count
        delta_s -= count * 60 * 60
    if delta_s >= 60:
        count = int(delta_s / 60)
        result += u'%s分' % count
        delta_s -= count * 60
    if delta_s > 0:
        count = int(delta_s)
        result += u'%s秒' % count
    return result


@app.template_filter('user_name_level')
def filter_user_name_level(user_id):
    """
    用户中心显示用户名和等级
    :param user_id:
    :return:
    """
    row = get_user_profile_row_by_id(user_id)
    return u'%s(%s)' % (row.nickname, LEVEL_TYPE_DICT.get(row.level_type, u'普通')) if row else u'游客'


@app.template_filter('user_wallet')
def filter_user_wallet(user_id):
    """
    用户钱包余额
    :param user_id:
    :return:
    """
    row = get_wallet_row_by_id(user_id)
    return row.amount_current if row else 0


@app.template_filter('user_score')
def filter_user_score(user_id):
    """
    用户积分余额
    :param user_id:
    :return:
    """
    row = get_score_row_by_id(user_id)
    return row.amount if row else 0


@app.template_filter('user_bonus')
def filter_user_bonus(user_id):
    """
    用户奖金余额
    :param user_id:
    :return:
    """
    row = get_bonus_row_by_id(user_id)
    return row.amount if row else 0


@app.template_filter('user_invite_link')
def filter_user_invite_link(user_id):
    """
    用户邀请链接参数
    :param user_id:
    :return:
    """
    s = URLSafeSerializer(app.config.get('USER_INVITE_LINK_SIGN_KEY', ''))
    link_param = s.dumps({'user_id': user_id})
    return link_param


@app.template_filter('type_apply')
def filter_type_apply(type_apply_id):
    """
    申请类型
    :param type_apply_id:
    :return:
    """
    return TYPE_APPLY_DICT.get(type_apply_id, u'')


@app.template_filter('auth_type')
def filter_auth_type(auth_type_id):
    """
    认证类型
    :param auth_type_id:
    :return:
    """
    return AUTH_TYPE_DICT.get(auth_type_id, u'')


@app.template_filter('status_apply')
def filter_status_apply(status_apply_id):
    """
    申请状态
    :param status_apply_id:
    :return:
    """
    return STATUS_APPLY_DICT.get(status_apply_id, u'')


@app.template_filter('status_audit')
def filter_status_audit(status_audit_id):
    """
    审核状态
    :param status_audit_id:
    :return:
    """
    return STATUS_AUDIT_DICT.get(status_audit_id, u'')


@app.template_filter('status_order')
def filter_status_order(status_order_id):
    """
    订单状态
    :param status_order_id:
    :return:
    """
    return STATUS_ORDER_DICT.get(status_order_id, u'')


@app.template_filter('status_delete')
def filter_status_delete(status_delete_id):
    """
    删除状态
    :param status_delete_id:
    :return:
    """
    return STATUS_DEL_DICT.get(status_delete_id, u'')


@app.template_filter('status_pay')
def filter_status_pay(status_pay_id):
    """
    支付状态
    :param status_pay_id:
    :return:
    """
    return STATUS_PAY_DICT.get(status_pay_id, u'')


@app.template_filter('status_rec')
def filter_status_rec(status_rec_id):
    """
    收款状态
    :param status_rec_id:
    :return:
    """
    return STATUS_REC_DICT.get(status_rec_id, u'')
