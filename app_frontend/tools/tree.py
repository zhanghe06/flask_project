#!/usr/bin/env python
# encoding: utf-8

"""
@author: zhanghe
@software: PyCharm
@file: tree.py
@time: 2017/5/31 下午9:25
"""


from collections import defaultdict


def tree():
    """
    定义一棵树
    python 字典的特性，赋值操作必须事先声明，所以这里使用 collections 很方便的为字典设置初始值
    :return:
    """
    return defaultdict(tree)

