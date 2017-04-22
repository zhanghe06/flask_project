#!/usr/bin/env python
# encoding: utf-8

"""
@author: zhanghe
@software: PyCharm
@file: __init__.py
@time: 16-2-22 下午11:05
"""


import hashlib


def md5(source_str):
    """
    md5加密
    :param source_str:
    :return:
    """
    return hashlib.md5(source_str.encode("utf8") if isinstance(source_str, unicode) else source_str).hexdigest()


if __name__ == '__main__':
    print md5('123456')  # e10adc3949ba59abbe56e057f20f883e
