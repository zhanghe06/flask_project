#!/usr/bin/env python
# encoding: utf-8

"""
@author: zhanghe
@software: PyCharm
@file: log_test.py
@time: 16-4-10 上午12:24
"""

from config import LOG_CONFIG
import logging
from logging.config import dictConfig

# 配置日志
dictConfig(LOG_CONFIG)


def test_app():
    """
    测试日志_app
    """
    log = logging.getLogger('app')
    log.info('This is a app info!')
    log.error('This is a app error!')


def test_db():
    """
    测试日志_db
    """
    log = logging.getLogger('db')
    log.info('This is a db info!')
    log.error('This is a db error!')


if __name__ == '__main__':
    test_app()
    test_db()
