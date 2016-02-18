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


redis_client = redis.StrictRedis(host='localhost', port=6379, db=0)


class Container(object):
    """
    容器
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

    def __init__(self, entity_name, prefix='container'):
        if entity_name not in self.entity_name_list:
            raise TypeError(u'类型错误')
        self.entity_name = entity_name
        self.prefix = prefix

    def add_item(self, stat_type, item_id, uid):
        """
        添加物品统计的用户
        :param stat_type:
        :param item_id:
        :param uid:
        :return:
        """
        key = "%s:%s:%s:%s" % (self.prefix, self.entity_name, stat_type, item_id)
        return redis_client.zadd(key, time.time(), uid)

    def del_item(self, stat_type, item_id, uid):
        """
        删除物品统计的用户
        :param stat_type:
        :param item_id:
        :param uid:
        :return:
        """
        key = "%s:%s:%s:%s" % (self.prefix, self.entity_name, stat_type, item_id)
        return redis_client.zrem(key, uid)

    def count_item(self, stat_type, item_id):
        """
        统计物品关联的用户的总数
        :param stat_type:
        :param item_id:
        :return:
        """
        key = "%s:%s:%s:%s" % (self.prefix, self.entity_name, stat_type, item_id)
        return redis_client.zcount(key, 0, time.time())

    def get_items(self, stat_type, item_id, page=1, pagesize=10):
        """
        分页获取物品关联的用户(根据时间降序)
        :param stat_type:
        :param item_id:
        :param page:
        :param pagesize:
        :return:
        """
        offset = 0
        if page > 1:
            offset = (page - 1) * pagesize
        max_count = (page * pagesize) - 1
        key = "%s:%s:%s:%s" % (self.prefix, self.entity_name, stat_type, item_id)
        u_ids = redis_client.zrevrange(key, offset, max_count)  # 倒序取值
        # u_ids = redis_client.zrange(key, offset, max_count)  # 顺序取值
        return u_ids

    def get_all_items(self, stat_type, item_id):
        """
        获取物品关联的所有用户
        :param stat_type:
        :param item_id:
        :return:
        """
        key = "%s:%s:%s:%s" % (self.prefix, self.entity_name, stat_type, item_id)
        total = redis_client.zcard(key)
        u_ids = redis_client.zrevrange(key, 0, total - 1, True)
        return u_ids


def test_blog_favor():
    """
    测试 blog favor
    """
    obj = Container('blog')
    print obj.add_item('favor', 2, 5)  # 1
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
