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
from datetime import timedelta

from app_common.maps.status_active import STATUS_ACTIVE_DICT
from app_common.maps.status_lock import STATUS_LOCK_DICT
from app_common.maps.type_order import TYPE_ORDER_DICT
from app_frontend import app
from app_frontend.api.user_profile import get_user_profile_row_by_id
from app_frontend.api.wallet import get_wallet_row_by_id
from app_frontend.api.bit_coin import get_bit_coin_row_by_id
from app_frontend.api.score import get_score_row_by_id
from app_frontend.api.bonus import get_bonus_row_by_id
from app_frontend.api.active import get_active_row_by_id
from app_common.maps.type_level import TYPE_LEVEL_DICT
from app_common.maps.type_apply import TYPE_APPLY_DICT
from app_common.maps.type_auth import TYPE_AUTH_DICT
from app_common.maps.type_active import TYPE_ACTIVE_DICT
from app_common.maps.type_score import TYPE_SCORE_DICT
from app_common.maps.status_audit import STATUS_AUDIT_DICT
from app_common.maps.status_apply import STATUS_APPLY_DICT
from app_common.maps.status_order import STATUS_ORDER_DICT
from app_common.maps.status_delete import STATUS_DEL_DICT
from app_common.maps.status_pay import STATUS_PAY_DICT
from app_common.maps.status_rec import STATUS_REC_DICT
import time


@app.template_filter('project_name')
def project_name_filter(s):
    """
    显示项目名称
    :param s:
    :return:
    """
    return app.config.get('PROJECT_NAME', s)


@app.template_filter('icp_code')
def icp_code_filter(s):
    """
    显示ICP备案号
    :param s:
    :return:
    """
    return app.config.get('ICP_CODE', s)


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


@app.template_filter('time_delta')
def filter_time_delta(last_time, delta=0):
    """
    获取偏移后的时间
    :param last_time:
    :param delta:
    :return:
    """
    current_time = last_time + timedelta(seconds=delta)
    return current_time


@app.template_filter('user_name_level')
def filter_user_name_level(user_id):
    """
    用户中心显示用户名和等级
    :param user_id:
    :return:
    """
    row = get_user_profile_row_by_id(user_id)
    return u'%s(%s)' % (row.nickname, TYPE_LEVEL_DICT.get(row.type_level, u'普通')) if row else u'游客'


@app.template_filter('nickname')
def filter_nickname(user_id):
    """
    显示用户名称
    :param user_id:
    :return:
    """
    user_info = get_user_profile_row_by_id(user_id)
    return user_info.nickname if user_info else u'系统用户'


@app.template_filter('user_wallet')
def filter_user_wallet(user_id):
    """
    用户钱包余额
    :param user_id:
    :return:
    """
    row = get_wallet_row_by_id(user_id)
    return row.amount_current if row else 0


@app.template_filter('user_bit_coin')
def filter_user_bit_coin(user_id):
    """
    用户数字货币
    :param user_id:
    :return:
    """
    row = get_bit_coin_row_by_id(user_id)
    return row.amount if row else 0


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


@app.template_filter('user_active')
def filter_user_active(user_id):
    """
    用户激活码量
    :param user_id:
    :return:
    """
    row = get_active_row_by_id(user_id)
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


@app.template_filter('type_level')
def filter_type_level(type_level_id):
    """
    用户等级
    :param type_level_id:
    :return:
    """
    return TYPE_LEVEL_DICT.get(type_level_id, u'')


@app.template_filter('type_apply')
def filter_type_apply(type_apply_id):
    """
    申请类型
    :param type_apply_id:
    :return:
    """
    return TYPE_APPLY_DICT.get(type_apply_id, u'')


@app.template_filter('type_order')
def filter_type_order(type_order_id):
    """
    订单类型
    :param type_order_id:
    :return:
    """
    return TYPE_ORDER_DICT.get(type_order_id, u'')


@app.template_filter('type_auth')
def filter_type_auth(type_auth_id):
    """
    认证类型
    :param type_auth_id:
    :return:
    """
    return TYPE_AUTH_DICT.get(type_auth_id, u'')


@app.template_filter('type_active')
def filter_type_active(type_active_id):
    """
    激活类型
    :param type_active_id:
    :return:
    """
    return TYPE_ACTIVE_DICT.get(type_active_id, u'')


@app.template_filter('type_score')
def filter_type_score(type_score_id):
    """
    积分类型
    :param type_score_id:
    :return:
    """
    return TYPE_SCORE_DICT.get(type_score_id, u'')


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


@app.template_filter('status_active')
def filter_status_active(status_active_id):
    """
    激活状态
    :param status_active_id:
    :return:
    """
    return STATUS_ACTIVE_DICT.get(status_active_id, u'')


@app.template_filter('status_lock')
def filter_status_lock(status_lock_id):
    """
    锁定状态
    :param status_lock_id:
    :return:
    """
    return STATUS_LOCK_DICT.get(status_lock_id, u'')

