#!/usr/bin/env python
# encoding: utf-8

"""
@author: zhanghe
@software: PyCharm
@file: gen.py
@time: 16-6-19 下午7:07
"""


import os
import sys
from app import app
BASE_DIR = app.config['BASE_DIR']
SQLALCHEMY_DATABASE_URI = app.config['SQLALCHEMY_DATABASE_URI']


def create_models():
    """
    创建 model
    $ python gen.py gen_models
    """
    file_path = os.path.join(BASE_DIR, 'app/models.py')
    cmd = 'sqlacodegen %s --outfile %s' % (SQLALCHEMY_DATABASE_URI, file_path)

    output = os.popen(cmd)
    result = output.read()
    print result

    # 更新 model 文件
    with open(file_path, 'r') as f:
        lines = f.readlines()

    with open(file_path, 'w') as f:
        # 替换 model 关键内容
        lines[3] = 'from database import db\n'
        lines[6] = 'Base = db.Model\n'
        # 新增 model 转 dict 方法

        lines.insert(10, 'def to_dict(self):\n')
        lines.insert(11, '    """\n')
        lines.insert(12, '    model 对象转 字典\n')
        lines.insert(13, '    model_obj.to_dict()\n')
        lines.insert(14, '    """\n')
        lines.insert(15, '    return {c.name: getattr(self, c.name, None) for c in self.__table__.columns}\n')
        lines.insert(16, '\n')
        lines.insert(17, 'Base.to_dict = to_dict\n')
        lines.insert(18, '\n\n')
        f.write(''.join(lines))


def create_db():
    """
    建库 建表
    $ python gen.py create_db
    """
    # 初始化数据库
    cmd = 'sqlite3 %s < %s' % (os.path.join(BASE_DIR, 'flask.db'), os.path.join(BASE_DIR, 'schema.sql'))
    print cmd
    output = os.popen(cmd)
    result = output.read()
    print result
    # 添加测试数据
    cmd = 'sqlite3 %s < %s' % (os.path.join(BASE_DIR, 'flask.db'), os.path.join(BASE_DIR, 'etc/data_test.sql'))
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
    """
    使用说明
    """
    print """
创建(更新)model
$ python gen.py create_models

初始化数据库
$ python gen.py create_db

备份数据
$ python gen.py dump_db
"""


if __name__ == '__main__':
    run()
