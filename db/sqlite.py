#!/usr/bin/env python
# encoding: utf-8

"""
@author: zhanghe
@software: PyCharm
@file: sqlite.py
@time: 17-4-18 下午4:22
"""


import os
import sys
from config import current_config

BASE_DIR = current_config['BASE_DIR']
DB = current_config['DB_SQLITE']


DB_SCHEMA_PATH = os.path.join(BASE_DIR, 'db/schema/sqlite.sql')
DUMP_FILE_PATH = os.path.join(BASE_DIR, 'db/backup/sqlite.sql')


def create_db():
    """
    建库 建表
    $ python gen.py create_db
    """
    # 初始化数据库
    cmd = 'sqlite3 %s < %s' % (DB, DB_SCHEMA_PATH)
    print cmd
    output = os.popen(cmd)
    result = output.read()
    print result
    # 添加测试数据
    cmd = 'sqlite3 %s < %s' % (DB, os.path.join(BASE_DIR, 'etc/data_test.sql'))
    print cmd
    output = os.popen(cmd)
    result = output.read()
    print result


def dump_db():
    """
    备份数据
    $ python gen.py dump_db
    """
    # 添加测试数据
    cmd = 'sqlite3 %s ".dump" > %s' % (os.path.join(BASE_DIR, 'flask.db'), os.path.join(BASE_DIR, 'schema.dump.sql'))
    print cmd
    output = os.popen(cmd)
    result = output.read()
    print result


def run():
    """
    入口
    """
    # print sys.argv
    try:
        if len(sys.argv) > 1:
            fun_name = eval(sys.argv[1])
            fun_name()
        else:
            print '缺失参数\n'
            usage()
    except NameError, e:
        print e
        print '未定义的方法[%s]' % sys.argv[1]


def usage():
    print """
建库 建表（初始化数据库）
$ python db/sqlite.py create_db

导出建表语句（备份数据库）
$ python db/sqlite.py dump_db
"""


if __name__ == '__main__':
    run()
