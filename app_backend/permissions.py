#!/usr/bin/env python
# encoding: utf-8

"""
@author: zhanghe
@software: PyCharm
@file: permissions.py
@time: 2017/6/8 下午11:16
"""


from flask_principal import Permission, RoleNeed


# 模块权限
permission_user = Permission(RoleNeed(u'会员'))
permission_order = Permission(RoleNeed(u'订单'))
permission_msg = Permission(RoleNeed(u'留言'))
permission_admin = Permission(RoleNeed(u'运营'))
permission_stats = Permission(RoleNeed(u'统计'))
permission_other = Permission(RoleNeed(u'其它'))
