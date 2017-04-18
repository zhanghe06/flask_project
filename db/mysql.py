#!/usr/bin/env python
# encoding: utf-8

"""
@author: zhanghe
@software: PyCharm
@file: mysql.py
@time: 17-4-18 下午4:22
"""


import os
import sys
from config import BASE_DIR, DB_MYSQL as DB

DB_SCHEMA_PATH = os.path.join(BASE_DIR, 'db/schema/mysql.sql')
DUMP_FILE_PATH = os.path.join(BASE_DIR, 'db/backup/mysql.sql')


def create_db():
    """
    建库 建表
    """
    cmd = 'mysql -h%s -P%s -u%s -p%s < %s' % (DB['host'], DB['port'], DB['user'], DB['passwd'], DB_SCHEMA_PATH)
    print cmd
    output = os.popen(cmd)
    result = output.read()
    print result


def dump_db():
    """
    备份数据
    """
    cmd = 'mysqldump -h%s -P%s -u%s -p%s %s --skip-lock-tables > %s' % (DB['host'], DB['port'], DB['user'], DB['passwd'], DB['db'], DUMP_FILE_PATH)
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
$ python db/mysql.py create_db

导出建表语句（备份数据库）
$ python db/mysql.py dump_db
"""


if __name__ == '__main__':
    run()
