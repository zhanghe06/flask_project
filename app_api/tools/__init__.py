#!/usr/bin/env python
# encoding: utf-8

"""
@author: zhanghe
@software: PyCharm
@file: __init__.py.py
@time: 2017/4/24 下午9:04
"""


import json
import hashlib
from datetime import date, datetime
from decimal import Decimal


def md5(source_str):
    """
    md5加密
    :param source_str:
    :return:
    """
    return hashlib.md5(source_str.encode("utf8") if isinstance(source_str, unicode) else source_str).hexdigest()


def json_default(obj):
    """
    支持datetime的json encode
    TypeError: datetime.datetime(2015, 10, 21, 8, 42, 54) is not JSON serializable
    :param obj:
    :return:
    """
    if isinstance(obj, datetime):
        return obj.strftime('%Y-%m-%d %H:%M:%S')
    elif isinstance(obj, date):
        return obj.strftime('%Y-%m-%d')
    elif isinstance(obj, Decimal):
        return str(obj)
    else:
        raise TypeError('%r is not JSON serializable' % obj)


if __name__ == '__main__':
    print md5('123456')  # e10adc3949ba59abbe56e057f20f883e
