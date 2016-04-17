#!/usr/bin/env python
# encoding: utf-8

"""
@author: zhanghe
@software: PyCharm
@file: sys.py
@time: 16-4-17 下午11:59
"""


import os


def get_memory_usage():
    """
    获取当前进程内存使用情况(单位M)
    """
    # 获取当前脚本的进程ID
    pid = os.getpid()
    # 获取当前脚本占用的内存
    cmd = 'ps -p %s -o rss=' % pid
    output = os.popen(cmd)
    result = output.read()
    if result == '':
        memory_usage_value = 0
    else:
        memory_usage_value = int(result.strip())
    memory_usage_format = memory_usage_value / 1024.0
    print '[pid:%s]内存使用%.2fM' % (pid, memory_usage_format)


if __name__ == '__main__':
    get_memory_usage()
