#!/usr/bin/env python
# encoding: utf-8

"""
@user: zhanghe
@software: PyCharm
@file: user_profile.py
@time: 17-4-29 下午16:36
"""


from collections import Iterable
import json
from app_backend.api.user_profile import get_team_tree_recursion


team_tree = get_team_tree_recursion(1)
print dict(team_tree)


if __name__ == '__main__':
    pass
