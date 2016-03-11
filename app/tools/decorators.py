#!/usr/bin/env python
# encoding: utf-8

"""
@author: zhanghe
@software: PyCharm
@file: decorators.py
@time: 16-3-11 下午3:08
"""


from threading import Thread


def async(f):
    """
    基于线程的异步调用装饰器
    :param f:
    :return:
    """
    def wrapper(*args, **kwargs):
        thr = Thread(target=f, args=args, kwargs=kwargs)
        thr.start()
    return wrapper
