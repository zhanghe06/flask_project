#!/usr/bin/env python
# encoding: utf-8

"""
@author: zhanghe
@software: PyCharm
@file: penetration.py
@time: 2017/5/16 上午11:56
"""


import json
from datetime import datetime

from flask import Blueprint
from flask import request
from jinja2 import Environment

bp_penetration = Blueprint('penetration', __name__, url_prefix='/penetration')


@bp_penetration.route('/')
@bp_penetration.route('/index/')
def index():
    """
    渗透测试，生成环境需要关掉蓝图
    """
    name = request.values.get('name', 'world')
    # 不安全的两种方式
    output = Environment().from_string('Hello ' + name + '!').render()
    # output = Environment().from_string('Hello %s!' % name).render()
    # 安全方式
    # output = Environment().from_string('Hello {{name}}!').render(name=name)

    return output

"""
tplmap 环境依赖
pip install PyYAML
pip install requests
"""
