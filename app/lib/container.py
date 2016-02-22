#!/usr/bin/env python
# encoding: utf-8

"""
@author: zhanghe
@software: PyCharm
@file: container.py
@time: 16-2-17 下午3:46
"""


import redis
import time
from copy import deepcopy


redis_client = redis.StrictRedis(host='localhost', port=6379, db=0)


class Container(object):
    """
    容器（数据结构：集合）
    """
    # 定义支持的实体类型
    entity_name_list = ['user', 'blog', 'topic', 'subject', 'product']

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

    # 定义项目容器状态结构
    container_status_dict = {
        'favor': False,  # 支持
        'flag': False,  # 举报
        'collect': False  # 收藏
    }

    def __init__(self, entity_name, prefix='container'):
        if entity_name not in self.entity_name_list:
            raise TypeError(u'类型错误')
        self.entity_name = entity_name
        self.prefix = prefix

    def add_item(self, stat_type, key_id, item_id):
        """
        添加统计项目
        :param stat_type:
        :param key_id:
        :param item_id:
        :return:0/1
        """
        key = "%s:%s:%s:%s" % (self.prefix, self.entity_name, stat_type, key_id)
        return redis_client.zadd(key, time.time(), item_id)

    def del_item(self, stat_type, key_id, item_id):
        """
        删除统计项目
        :param stat_type:
        :param key_id:
        :param item_id:
        :return:0/1
        """
        key = "%s:%s:%s:%s" % (self.prefix, self.entity_name, stat_type, key_id)
        return redis_client.zrem(key, item_id)

    def count_item(self, stat_type, key_id):
        """
        统计相关项目的总数
        :param stat_type:
        :param key_id:
        :return:
        """
        key = "%s:%s:%s:%s" % (self.prefix, self.entity_name, stat_type, key_id)
        return redis_client.zcount(key, 0, time.time())

    def get_items(self, stat_type, key_id, page=1, pagesize=10):
        """
        分页获取相关项目列表(根据时间降序)
        :param stat_type:
        :param key_id:
        :param page:
        :param pagesize:
        :return:[]
        """
        offset = 0
        if page > 1:
            offset = (page - 1) * pagesize
        max_count = (page * pagesize) - 1
        key = "%s:%s:%s:%s" % (self.prefix, self.entity_name, stat_type, key_id)
        item_ids = redis_client.zrevrange(key, offset, max_count)  # 倒序取值
        # item_ids = redis_client.zrange(key, offset, max_count)  # 顺序取值
        return item_ids

    def get_all_items(self, stat_type, key_id):
        """
        获取所有相关项目列表
        :param stat_type:
        :param key_id:
        :return:[]
        """
        key = "%s:%s:%s:%s" % (self.prefix, self.entity_name, stat_type, key_id)
        total = redis_client.zcard(key)
        item_ids = redis_client.zrevrange(key, 0, total - 1, True)
        return item_ids

    def get_item_container_status(self, key_id, item_id):
        """
        获取容器状态
        :param key_id:
        :param item_id:
        :return:
        """
        container_status = deepcopy(self.container_status_dict)
        for stat_type in container_status.keys():
            key = "%s:%s:%s:%s" % (self.prefix, self.entity_name, stat_type, key_id)
            # 无序集合sismember； 有序用 zscore 返回值：None
            if redis_client.zscore(key, item_id):
                container_status[stat_type] = True
        return container_status

    def get_item_list_container_status(self, key_ids, item_id):
        """
        显示列表容器状态
        按原 item_ids 列表顺序返回结果
        :param key_ids:
        :param item_id:
        :return:
        """
        container_list = []
        for key_id in key_ids:
            container_status = self.get_item_container_status(key_id, item_id)
            container_list.append(container_status)
        return container_list


def test_blog_favor():
    """
    测试 blog favor
    """
    obj = Container('blog')
    print obj.add_item('favor', 2, 5)  # 1
    print obj.add_item('favor', 2, 5)  # 0
    print obj.add_item('favor', 2, 6)  # 1
    print obj.get_items('favor', 2)  # ['6', '5']
    print obj.get_items('favor', 3)  # []
    print obj.count_item('favor', 2)  # 2
    print obj.del_item('favor', 3, 5)  # 0
    print obj.count_item('favor', 3)  # 0
    print obj.del_item('favor', 2, 5)  # 1
    print obj.count_item('favor', 2)  # 1
    print obj.del_item('favor', 2, 6)  # 1
    print obj.count_item('favor', 2)  # 0


if __name__ == '__main__':
    test_blog_favor()
