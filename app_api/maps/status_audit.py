#!/usr/bin/env python
# encoding: utf-8

"""
@author: zhanghe
@software: PyCharm
@file: status_audit.py
@time: 2017/4/29 上午10:51
"""


# 审核状态:0:待审核，1:审核通过，2:审核失败
STATUS_AUDIT_HANDING = '0'
STATUS_AUDIT_SUCCESS = '1'
STATUS_AUDIT_CANCEL = '2'

STATUS_AUDIT_DICT = {
    0: u'待审核',
    1: u'审核通过',
    2: u'审核失败',
}
