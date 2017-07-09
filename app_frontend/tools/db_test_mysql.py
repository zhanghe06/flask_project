#!/usr/bin/env python
# encoding: utf-8

"""
@author: zhanghe
@software: PyCharm
@file: db_test_mysql.py
@time: 16-3-25 下午11:35
"""


import unittest
from app_frontend.tools.system import get_memory_usage
from config import SQLALCHEMY_DATABASE_URI
import os


class TestDB(unittest.TestCase):
    """
    数据库操作测试用例
    """
    def setUp(self):
        """
        测试前准备环境的搭建
        """
        # 备份数据
        cmd = os.path.join(BASE_DIR, 'etc/db_dump.sh')
        os.system(cmd)
        # 准备测试数据
        cmd = os.path.join(BASE_DIR, 'etc/db_init.sh')
        os.system(cmd)
        print
        pass

    def test_get_row_by_id(self):
        """
        测试 通过主键获取信息
        """
        print self.test_get_row_by_id.__doc__.strip()
        from app.tools.db import get_row_by_id
        from app.models import User
        # 测试有记录的场景
        row = get_row_by_id(User, 1)
        assert row.id == 1
        assert row.email == 'admin@gmail.com'
        assert row.nickname == 'Admin'
        # 测试无记录的场景
        row = get_row_by_id(User, 100)
        assert row is None

    def test_get_rows_by_ids(self):
        """
        测试 通过主键列表获取信息列表
        """
        print self.test_get_rows_by_ids.__doc__.strip()
        from app.tools.db import get_rows_by_ids
        from app.models import User
        # # 测试有记录的场景
        rows = get_rows_by_ids(User, [1, 2, 3])
        assert len(rows) == 3
        assert rows[0].id == 1
        assert rows[0].email == 'admin@gmail.com'
        assert rows[0].nickname == 'Admin'
        # 测试无记录的场景
        rows = get_rows_by_ids(User, [100])
        assert rows == []

    def test_get_row(self):
        """
        测试 获取信息
        """
        print self.test_get_row.__doc__.strip()
        from app.tools.db import get_row
        from app.models import User
        # 测试有记录的场景一
        row = get_row(User, User.id > 1)
        assert row.id == 2
        assert row.email == 'guest@gmail.com'
        assert row.nickname == 'Guest'
        # 测试有记录的场景二
        row = get_row(User, nickname='Guest')
        assert row.id == 2
        assert row.email == 'guest@gmail.com'
        assert row.nickname == 'Guest'
        # 测试有记录的场景三
        row = get_row(User, **{'nickname': 'Guest'})
        assert row.id == 2
        assert row.email == 'guest@gmail.com'
        assert row.nickname == 'Guest'
        # 测试无记录的场景
        row = get_row(User, User.id == 100)
        assert row is None

    def test_count(self):
        """
        测试 计数
        """
        print self.test_count.__doc__.strip()
        from app.tools.db import count
        from app.models import User
        # 测试带查询条件并结果大于0的场景
        rows_count = count(User, User.id > 0, User.id < 100)
        assert rows_count == 3
        # 测试带查询条件并结果等于0的场景
        rows_count = count(User, User.id > 100)
        assert rows_count == 0
        # 测试无查询条件并结果大于0的场景
        rows_count = count(User)
        assert rows_count == 3

    def test_add(self):
        """
        测试 添加信息
        """
        print self.test_add.__doc__.strip()
        from app.tools.db import add
        from app.models import User
        # 测试正确的场景
        user_info = {
            'email': 'bob@gmail.com',
            'password': '123456',
            'nickname': 'Bob',
        }
        result = add(User, user_info)
        assert result == 4
        # 测试错误的场景
        user_info = {
            'email': 'error@gmail.com',
            'password': '123456',
            # 'nickname': 'Error',
        }
        try:
            result = add(User, user_info)
        except Exception as e:
            assert e.message == '(sqlite3.IntegrityError) NOT NULL constraint failed: user.nickname'
        assert result == 4

    def tearDown(self):
        """
        测试后环境的还原
        """
        # 恢复数据
        cmd = os.path.join(BASE_DIR, 'etc/db_restore.sh')
        os.system(cmd)
        # 获取内存消耗
        get_memory_usage()
        pass


if __name__ == '__main__':
    unittest.main()


"""
Testing started at 上午12:59 ...

测试 添加信息
[pid:24399]内存使用28.22M

测试 计数
[pid:24399]内存使用28.63M

测试 获取信息
[pid:24399]内存使用28.69M

测试 通过主键获取信息
[pid:24399]内存使用28.69M

测试 通过主键列表获取信息列表
[pid:24399]内存使用28.72M

Process finished with exit code 0
"""