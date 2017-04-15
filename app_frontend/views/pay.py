#!/usr/bin/env python
# encoding: utf-8

"""
@author: zhanghe
@software: PyCharm
@file: pay.py
@time: 2017/3/18 上午12:29
"""


import json
import logging
from datetime import datetime

from flask import request, render_template, redirect, url_for, g, abort, flash, jsonify
from flask_login import current_user, login_required

from app_frontend import app

log = logging.getLogger(__name__)


# 第三方支付（支付宝）
@app.route('/pay/alipay/')
def pay_alipay():
    return 'alipay'


# 第三方支付（微信）
@app.route('/pay/wechat/')
def pay_wechat():
    return 'wechat'
