#!/usr/bin/env python
# encoding: utf-8

"""
@author: zhanghe
@software: PyCharm
@file: permissions.py
@time: 2017/6/8 下午11:16
"""


from collections import namedtuple
from functools import partial

from flask_login import current_user
from flask_principal import identity_loaded, Permission, RoleNeed, \
     UserNeed


from app_common.maps.role_admin import *

#
# ROLE_ADMIN_SYSTEM = 1
# ROLE_ADMIN_CS = 2
# ROLE_ADMIN_OP = 3
# ROLE_ADMIN_MARKET = 4
# ROLE_ADMIN_SALES = 5
# ROLE_ADMIN_JUNIOR = 6
# ROLE_ADMIN_SENIOR = 7
#
# ROLE_ADMIN_DICT = {
#     1: u'系统',
#     2: u'客服',
#     3: u'运营',
#     4: u'市场',
#     5: u'销售',
#     6: u'普通',
#     7: u'高级',
# }


class RolePermission(Permission):
    """
    角色权限
    """
    def __init__(self, role_id):
        # 获取角色对应模块权限
        role_needs = []
        model_ids = []  # todo
        for model_id in model_ids:
            role_need = RoleNeed(unicode(model_id))
            role_needs.append(role_need)
        super(RolePermission, self).__init__(*role_needs)


admin_permission = RolePermission(0)

permission_system = RolePermission(ROLE_ADMIN_DICT.get(ROLE_ADMIN_SYSTEM))
permission_cs = RolePermission(ROLE_ADMIN_DICT.get(ROLE_ADMIN_CS))
permission_op = RolePermission(ROLE_ADMIN_DICT.get(ROLE_ADMIN_OP))
permission_market = RolePermission(ROLE_ADMIN_DICT.get(ROLE_ADMIN_MARKET))
permission_sales = RolePermission(ROLE_ADMIN_DICT.get(ROLE_ADMIN_SALES))
permission_junior = RolePermission(ROLE_ADMIN_DICT.get(ROLE_ADMIN_JUNIOR))
permission_senior = RolePermission(ROLE_ADMIN_DICT.get(ROLE_ADMIN_SENIOR))


# 角色 模块
#