#!/usr/bin/env python
# encoding: utf-8

"""
@author: zhanghe
@software: PyCharm
@file: cron_send_sms.py
@time: 2017/4/5 下午8:59
"""


import schedule
import time
import traceback
import sys


from app_frontend.tools.send_sms import get_server_tunnel, run_send_sms


def schedule_send_sms():
    """
    短信发送调度器 - 循环调度、定时调度
    :return:
    """
    try:
        run_send_sms()

        schedule.every(60).seconds.do(lambda: run_send_sms())

        while True:
            schedule.run_pending()
            time.sleep(1)
    except KeyboardInterrupt:
        print 'Stop Schedule'
    except Exception as e:
        print e.message
        traceback.print_exc()


def schedule_send_sms_ssh_tunnel():
    """
    短信发送调度器(隧道连接) - 循环调度、定时调度
    :return:
    """
    server = get_server_tunnel()
    server.start()  # start ssh sever
    print 'Server connected via SSH'
    try:
        run_send_sms(server)

        schedule.every(60).seconds.do(lambda: run_send_sms(server))

        while True:
            schedule.run_pending()
            time.sleep(1)
    except KeyboardInterrupt:
        print 'Stop Schedule'
    except Exception as e:
        print e.message
        traceback.print_exc()
    finally:
        server.close()  # stop ssh sever
        print 'Server disconnected via SSH'


def run_schedule():
    """
    调度器入口
    :return:
    """
    print sys.argv
    if sys.argv.pop() == 'ssh_tunnel':
        schedule_send_sms_ssh_tunnel()
    else:
        schedule_send_sms()


if __name__ == '__main__':
    run_schedule()
