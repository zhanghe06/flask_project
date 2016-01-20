#!/usr/bin/env python
# encoding: utf-8

"""
@author: zhanghe
@software: PyCharm
@file: run.py
@time: 16-1-7 上午12:12
"""


from app import app

app.debug = True  # 调试模式，生产环境必须去掉
app.run(host='0.0.0.0', port='5000')
