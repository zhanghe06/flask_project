#!/usr/bin/env python
# encoding: utf-8

"""
@blog: zhanghe
@software: PyCharm
@file: blog.py
@time: 16-1-21 上午10:24
"""


from models import Blog
from tools.db import get_row, get_rows, get_row_by_id, add, edit_by_id, delete_by_id
from lib.counter import Counter
from lib.container import Container


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
    return edit_by_id(Blog, blog_id, blog_data)


def delete_blog(blog_id):
    """
    删除博客信息
    :param blog_id:
    :return: Number of affected rows (Example: 0/1)
    """
    return delete_by_id(Blog, blog_id)


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


def get_blog_counter(blog_id):
    """
    获取blog计数器
    :param blog_id:
    :return:
    """
    blog_cnt_obj = Counter('blog')
    return blog_cnt_obj.counter_blog_item(blog_id)


def set_blog_counter(blog_id, stat_type, num):
    """
    设置blog计数器
    :param blog_id:
    :param stat_type:
    :param num:
    :return:
    """
    blog_cnt_obj = Counter('blog')
    return blog_cnt_obj.set_blog_counter(blog_id, stat_type, num)


def get_blog_list_counter(blog_id_list):
    """
    获取blog计数器
    :param blog_id_list:
    :return:
    """
    blog_cnt_obj = Counter('blog')
    return blog_cnt_obj.counter_blog_list(blog_id_list)


def get_blog_container_status(blog_id, uid):
    """
    获取blog容器状态
    :param blog_id:
    :param uid:
    :return:
    """
    blog_container_obj = Container('blog')
    return blog_container_obj.get_item_container_status(blog_id, uid)


def get_blog_list_container_status(blog_id_list, uid):
    """
    获取blog容器状态
    :param blog_id_list:
    :param uid:
    :return:
    """
    blog_container_obj = Container('blog')
    return blog_container_obj.get_item_list_container_status(blog_id_list, uid)


def add_blog_stat_item(stat_type, blog_id, uid):
    """
    添加blog统计明细
    :param stat_type:
    :param blog_id:
    :param uid:
    :return:
    """
    blog_container_obj = Container('blog')
    return blog_container_obj.add_item(stat_type, blog_id, uid)

if __name__ == '__main__':
    blog_rows = get_blog_rows(1, 10)
    if blog_rows:
        for item in blog_rows.items:
            print item.id, item.author, item.title, item.pub_date

    import json
    print json.dumps(get_blog_counter(['1', '2', '3']), indent=4, ensure_ascii=False)
