#!/usr/bin/env python
# encoding: utf-8

"""
@blog: zhanghe
@software: PyCharm
@file: blog.py
@time: 16-1-21 上午10:24
"""


from database import db_session
from models import Blog


def get_row(blog_id):
    """
    获取博客信息
    :param blog_id:
    :return: None/object
    """
    row = db_session.query(Blog).filter(Blog.id == blog_id).first()
    print row
    if row:
        print row.id, row.author, row.title, row.pub_date
    return row


def add(blog_data):
    """
    添加博客信息
    :param blog_data:
    :return: None/Value of blog.id
    """
    blog = Blog(**blog_data)
    db_session.add(blog)
    db_session.commit()
    print blog.id
    return blog.id


def edit(blog_id, blog_info):
    """
    修改博客信息
    :param blog_id:
    :param blog_info:
    :return: Number of affected rows (Example: 0/1)
    """
    blog = db_session.query(Blog).filter(Blog.id == blog_id)
    result = blog.update(blog_info)
    db_session.commit()
    print result
    return result


def delete(blog_id):
    """
    删除博客信息
    :param blog_id:
    :return: Number of affected rows (Example: 0/1)
    """
    blog = db_session.query(Blog).filter(Blog.id == blog_id)
    result = blog.delete()
    db_session.commit()
    print result
    return result


def get_rows(page=1, per_page=10, condition=None):
    """
    获取博客列表（分页）
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
    if condition is None:
        rows = Blog.query.filter().paginate(page, per_page, False)
    else:
        rows = Blog.query.filter(eval(condition)).paginate(page, per_page, False)
    return rows


def test():
    """
    测试
    :return:
    """
    # 测试获取
    get_row(5)
    # 测试添加
    blog_info = {
        'author': 'Bob',
        'title': 'Before Sunset',
        'pub_date': '2016-01-16 10:18:52'
    }
    add(blog_info)
    # 测试修改
    edit(11, {'pub_date': '2016-01-16 10:18:52'})
    # 测试删除
    delete(11)


def test_get_rows():
    """
    测试列表获取
    :return:
    """
    rows = get_rows(condition='Blog.id > 2')
    rows = get_rows()
    for item in rows.items:
        print item.id, item.author, item.title, item.pub_date


if __name__ == '__main__':
    # test()
    test_get_rows()
