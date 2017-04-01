#!/usr/bin/env python
# encoding: utf-8

"""
@author: zhanghe
@software: PyCharm
@file: stat.py
@time: 16-2-22 下午11:08
"""


from application.api.blog import get_blog_counter, set_blog_counter, add_blog_stat_item, get_blog_container_status
from application.api.user import add_user_stat_item

# 定义支持的统计类型
stat_type_list = [
    'favor',  # 支持数
    'decry',  # 反对数
    'follow',  # 关注数
    'fans',  # 粉丝数
    'view',  # 点击数
    'collect',  # 收藏数
    'flag'  # 举报数
]


def set_blog_stat(stat_type, uid, item_id, num=1):
    """
    设置 blog 统计
    :param stat_type:
    :param uid:
    :param item_id:
    :param num:
    :return:
    """
    blog_status = add_blog_stat_item(stat_type, item_id, uid)  # 更新blog容器
    user_status = add_user_stat_item(stat_type, uid, item_id)  # 更新user容器
    if blog_status == 1 and user_status == 1:
        count = set_blog_counter(item_id, stat_type, num)  # 更新计数器
    else:
        # 如果已经更新容器，计数器不需更新
        count = get_blog_counter(item_id)
    status = get_blog_container_status(item_id, uid)
    result = {
        'count': count,
        'status': status
    }
    return result


if __name__ == '__main__':
    pass
