#!/usr/bin/env python
# encoding: utf-8

"""
@author: zhanghe
@software: PyCharm
@file: file.py
@time: 16-3-29 下午2:21
"""


import os
import glob


def read_files(file_dir='*', suffix='*'):
    """
    读取目录下指定文件
    :param file_dir:
    :param suffix:
    :return:
    """
    try:
        for file_name in glob.glob(r'%s*.%s' % (file_dir, suffix)):
            if os.path.isfile(file_name):
                print file_name, os.path.abspath(file_name)
    except OSError:
        print u'读取文件失败'
    except Exception, e:
        print e.message


if __name__ == '__main__':
    read_files()
