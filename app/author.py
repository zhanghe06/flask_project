#!/usr/bin/env python
# encoding: utf-8

"""
@author: zhanghe
@software: PyCharm
@file: author.py
@time: 16-1-17 上午12:05
"""


from database import db_session
from models import Author


def get_row(author_id):
    """
    获取作者信息
    :param author_id:
    :return: None/object
    """
    row = db_session.query(Author).filter(Author.id == author_id).first()
    print row
    if row:
        print row.id, row.name, row.email
    return row


def add(author_data):
    """
    添加作者信息
    :param author_data:
    :return: None/Value of author.id
    """
    author = Author(**author_data)
    db_session.add(author)
    db_session.commit()
    print author.id
    return author.id


def edit(author_id, author_info):
    """
    修改作者信息
    :param author_id:
    :param author_info:
    :return: Number of affected rows (Example: 0/1)
    """
    author = db_session.query(Author).filter(Author.id == author_id)
    result = author.update(author_info)
    db_session.commit()
    print result
    return result


def delete(author_id):
    """
    删除作者信息
    :param author_id:
    :return: Number of affected rows (Example: 0/1)
    """
    author = db_session.query(Author).filter(Author.id == author_id)
    result = author.delete()
    db_session.commit()
    print result
    return result


def get_rows(page=1, per_page=10, condition=None):
    """
    获取作者列表（分页）
    Usage:
        items: 信息列表
        has_next: 如果本页之后还有超过一个分页，则返回True
        has_prev: 如果本页之前还有超过一个分页，则返回True
        next_num: 返回下一页的页码
        prev_num: 返回上一页的页码
        iter_pages(): 页码列表
        iter_pages(left_edge=2, left_current=2, right_current=5, right_edge=2) 页码列表默认参数
    :param page:
    :param per_page:
    :param condition:
    :return:
    """
    rows = Author.query.filter(eval(condition)).paginate(page, per_page, False)
    return rows


def test():
    """
    测试
    :return:
    """
    # 测试获取
    get_row(5)
    # 测试添加
    author_info = {
        'name': 'Bob',
        'email': 'bob@gmail.com'
    }
    add(author_info)
    # 测试修改
    edit(6, {'name': 'Emma'})
    # 测试删除
    delete(6)


def test_get_rows():
    """
    测试列表获取
    :return:
    """
    rows = get_rows(condition='Author.id > 2')
    for item in rows.items:
        print item.id, item.name, item.email


if __name__ == '__main__':
    # test()
    test_get_rows()
