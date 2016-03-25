#!/usr/bin/env python
# encoding: utf-8

"""
@author: zhanghe
@software: PyCharm
@file: run.py
@time: 16-1-7 上午12:12
"""


from app import app

import signal
import os


def handle_pdb(sig, frame):
    from remote_pdb import RemotePdb
    print sig, frame
    RemotePdb('0.0.0.0', 48110).set_trace()

signal.signal(signal.SIGUSR1, handle_pdb)
print('pid:%s' % os.getpid())

app.debug = True  # 调试模式，生产环境必须去掉
app.run(host='0.0.0.0', port=5000)  # 端口号必须为整型
