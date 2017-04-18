#!/usr/bin/env python
# encoding: utf-8

"""
@author: zhanghe
@software: PyCharm
@file: postgresql.py
@time: 17-4-18 下午4:22
"""


import os
import sys
from config import BASE_DIR, DB_PG as DB

DB_SCHEMA_PATH = os.path.join(BASE_DIR, 'db/schema/postgresql.sql')
DUMP_FILE_PATH = os.path.join(BASE_DIR, 'db/backup/postgresql.sql')


def create_db():
    """
    建库 建表
    """
    cmd = 'psql -h%s -p%s -U%s -W -d%s -f %s' % (DB['host'], DB['port'], DB['user'], DB['database'], DB_SCHEMA_PATH)
    print cmd
    output = os.popen(cmd)
    result = output.read()
    print result


def dump_db():
    """
    备份数据
    如果只是导出建表结构 需要加上参数 -s
    """
    cmd = 'pg_dump -h%s -p%s -U%s -W -d%s -f %s' % (DB['host'], DB['port'], DB['user'], DB['database'], DUMP_FILE_PATH)
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
$ python db/postgresql.py create_db

导出建表语句（备份数据库）
$ python db/postgresql.py dump_db
"""


if __name__ == '__main__':
    run()
