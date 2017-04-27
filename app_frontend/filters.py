#!/usr/bin/env python
# encoding: utf-8

"""
@author: zhanghe
@software: PyCharm
@file: filters.py
@time: 2017/4/13 下午2:33
@desc: 自定义过滤器
"""


from app_frontend import app
from app_frontend.api.user_profile import get_user_profile_row_by_id
from app_api.maps.level_type import LEVEL_TYPE_DICT
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
