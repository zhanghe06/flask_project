#!/usr/bin/env python
# encoding: utf-8

"""
@author: zhanghe
@software: PyCharm
@file: date.py
@time: 2017/6/10 下午6:00
"""


import time
import calendar
from datetime import datetime, timedelta, date


def get_current_day_time_ends():
    """
    获取当天开始结束时刻
    :return:
    """
    today = datetime.today()
    start_time = datetime(today.year, today.month, today.day, 0, 0, 0)
    end_time = datetime(today.year, today.month, today.day, 23, 59, 59)
    return start_time, end_time


def get_current_month_time_ends():
    """
    获取当月开始结束时刻
    :return:
    """
    today = datetime.today()
    _, days = calendar.monthrange(today.year, today.month)
    start_time = datetime(today.year, today.month, 1, 0, 0, 0)
    end_time = datetime(today.year, today.month, days, 23, 59, 59)
    return start_time, end_time


def get_current_year_time_ends():
    """
    获取当年开始结束时刻
    :return:
    """
    today = datetime.today()
    start_time = datetime(today.year, 1, 1, 0, 0, 0)
    end_time = datetime(today.year, 12, 31, 23, 59, 59)
    return start_time, end_time


def get_hours(zerofill=True):
    """
    列出1天所有24小时
    :return:
    """
    if zerofill:
        return ['%02d' % i for i in range(24)]
    else:
        return range(24)


def get_days(year=1970, month=1, zerofill=True):
    """
    列出当月的所有日期
    :param year:
    :param month:
    :param zerofill:
    :return:
    """
    year = int(year)
    month = int(month)
    _, days = calendar.monthrange(year, month)
    if zerofill:
        return ['%02d' % i for i in range(1, days+1)]
    else:
        return range(1, days+1)


def get_weeks():
    """
    列出所有星期
    :return:
    """
    return [u'周一', u'周二', u'周三', u'周四', u'周五', u'周六', u'周日']


def get_months(zerofill=True):
    """
    列出1年所有12月份
    :return:
    """
    if zerofill:
        return ['%02d' % i for i in range(1, 13)]
    else:
        return [i for i in range(1, 13)]


def time_local_to_utc(local_time):
    """
    本地时间转UTC时间
    :param local_time:
    :return:
    """
    # 字符串处理
    if isinstance(local_time, str) and len(local_time) == 10:
        local_time = datetime.strptime(local_time, '%Y-%m-%d')
    elif isinstance(local_time, str) and len(local_time) >= 19:
        local_time = datetime.strptime(local_time[:19], '%Y-%m-%d %H:%M:%S')
    elif not (isinstance(local_time, datetime) or isinstance(local_time, date)):
        local_time = datetime.now()
    # 时间转换
    utc_time = local_time + timedelta(seconds=time.timezone)
    return utc_time


def time_utc_to_local(utc_time):
    """
    UTC时间转本地时间
    :param utc_time:
    :return:
    """
    # 字符串处理
    if isinstance(utc_time, str) and len(utc_time) == 10:
        utc_time = datetime.strptime(utc_time, '%Y-%m-%d')
    elif isinstance(utc_time, str) and len(utc_time) >= 19:
        utc_time = datetime.strptime(utc_time[:19], '%Y-%m-%d %H:%M:%S')
    elif not (isinstance(utc_time, datetime) or isinstance(utc_time, date)):
        utc_time = datetime.utcnow()
    # 时间转换
    local_time = utc_time - timedelta(seconds=time.timezone)
    return local_time


if __name__ == '__main__':
    print get_current_day_time_ends()
    print get_current_month_time_ends()
    print get_current_year_time_ends()

    print get_hours()
    print get_days(2017, 2)
    print get_days(2017, 2, True)
    print get_weeks()
    print get_months()

    print time.timezone
    # 时间对象本地时间与UTC时间互转
    print datetime.now(), time_local_to_utc(datetime.now())
    print datetime.utcnow(), time_utc_to_local(datetime.utcnow())
    # 字符串本地时间转UTC时间
    print '2017-01-01', time_local_to_utc(datetime.strptime('2017-01-01', '%Y-%m-%d'))
    print '2017-01-01 00:00:00', time_local_to_utc(datetime.strptime('2017-01-01 00:00:00', '%Y-%m-%d %H:%M:%S'))
    # 字符串UTC时间转本地时间
    print '2017-01-01', time_utc_to_local(datetime.strptime('2017-01-01', '%Y-%m-%d'))
    print '2017-01-01 00:00:00', time_utc_to_local(datetime.strptime('2017-01-01 00:00:00', '%Y-%m-%d %H:%M:%S'))

    # 日期对象本地时间与UTC时间互转
    local_date = date(*time.localtime()[:3])
    print local_date, type(local_date), time_local_to_utc(local_date)
    utc_date = date(*time.strptime('2009-09-07', '%Y-%m-%d')[:3])
    print utc_date, type(utc_date), time_utc_to_local(utc_date)
