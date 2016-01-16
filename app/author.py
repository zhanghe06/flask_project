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
    :return:
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
    :return:
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
    :return:
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
    :return:
    """
    author = db_session.query(Author).filter(Author.id == author_id)
    result = author.delete()
    db_session.commit()
    print result
    return result


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


if __name__ == '__main__':
    test()
