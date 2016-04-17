#!/usr/bin/env python
# encoding: utf-8

"""
@author: zhanghe
@software: PyCharm
@file: db_test.py
@time: 16-3-25 下午11:35
"""


import unittest


class TestDB(unittest.TestCase):
    """
    数据库操作测试用例
    """
    def setUp(self):
        """
        测试前准备环境的搭建
        :return:
        """
        pass

    def test_get_row_by_id(self):
        """
        测试 通过 id 获取信息
        :return:
        """
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
        测试 通过一组 ids 获取信息列表
        """
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
        :return:
        """
        from app.tools.db import get_row
        from app.models import User
        # 测试有记录的场景
        row = get_row(User, User.id > 1)
        assert row.id == 2
        assert row.email == 'guest@gmail.com'
        assert row.nickname == 'Guest'
        # 测试无记录的场景
        row = get_row(User, User.id == 100)
        assert row is None

    def tearDown(self):
        """
        测试后环境的还原
        :return:
        """
        pass


if __name__ == '__main__':
    unittest.main()
