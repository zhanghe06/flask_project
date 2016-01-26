#!/usr/bin/env python
# encoding: utf-8

"""
@blog: zhanghe
@software: PyCharm
@file: blog.py
@time: 16-1-21 上午10:24
"""


from models import Blog
from tools import get_row, get_rows, get_row_by_id, add, edit, delete


def get_blog_row_by_id(blog_id):
    """
    通过 id 获取博客信息
    :param blog_id:
    :return: None/object
    """
    return get_row_by_id(Blog, blog_id)


def get_blog_row(*args, **kwargs):
    """
    获取博客信息
    :param args:
    :param kwargs:
    :return: None/object
    """
    return get_row(Blog, *args, **kwargs)


def add_blog(blog_data):
    """
    添加博客信息
    :param blog_data:
    :return: None/Value of blog.id
    """
    return add(Blog, blog_data)


def edit_blog(blog_id, blog_data):
    """
    修改博客信息
    :param blog_id:
    :param blog_data:
    :return: Number of affected rows (Example: 0/1)
    """
    return edit(Blog, blog_id, blog_data)


def delete_blog(blog_id):
    """
    删除博客信息
    :param blog_id:
    :return: Number of affected rows (Example: 0/1)
    """
    return delete(Blog, blog_id)


def get_blog_rows(page=1, per_page=10, *args, **kwargs):
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
    :param args:
    :param kwargs:
    :return:
    """
    rows = get_rows(Blog, page, per_page, *args, **kwargs)
    return rows


if __name__ == '__main__':
    blog_rows = get_blog_rows(1, 10)
    if blog_rows:
        for item in blog_rows.items:
            print item.id, item.author, item.title, item.pub_date
