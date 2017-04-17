#!/usr/bin/env python
# encoding: utf-8

"""
@author: zhanghe
@software: PyCharm
@file: send_sms.py
@time: 2017/4/5 下午1:47
"""


from sshtunnel import SSHTunnelForwarder
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from app_frontend.lib.sms_chuanglan_iso import SmsChuangLanIsoApi
import time
from config import SSH_CONFIG, SMS


# 隧道配置
SSH_IP = SSH_CONFIG['IP']
SSH_PORT = SSH_CONFIG['PORT']
SSH_USERNAME = SSH_CONFIG['USERNAME']
SSH_PASSWORD = SSH_CONFIG['PASSWORD']

# DB配置
DB_MYSQL = SSH_CONFIG['DB_MYSQL']


# 短信接口配置
UN = SMS['UN']           # 创蓝账号
PW = SMS['PW']           # 创蓝密码


def get_server_tunnel():
    """
    获取连接隧道
    :return:
    """
    server_tunnel = SSHTunnelForwarder(
        (SSH_IP, SSH_PORT),
        ssh_password=SSH_PASSWORD,
        ssh_username=SSH_USERNAME,
        remote_bind_address=(DB_MYSQL['host'], DB_MYSQL['port']))
    return server_tunnel


def get_db_session(server_tunnel=None):
    """
    获取db_session
    :param server_tunnel:
    :return:
    """
    if server_tunnel:
        local_port = str(server_tunnel.local_bind_port)

        sqlalchemy_database_uri_mysql = \
            'mysql+mysqldb://%s:%s@%s:%s/%s?charset=utf8' % \
            (DB_MYSQL['user'], DB_MYSQL['passwd'], DB_MYSQL['host'], local_port, DB_MYSQL['db'])
    else:
        sqlalchemy_database_uri_mysql = \
            'mysql+mysqldb://%s:%s@%s:%s/%s?charset=utf8' % \
            (DB_MYSQL['user'], DB_MYSQL['passwd'], DB_MYSQL['host'], DB_MYSQL['port'], DB_MYSQL['db'])
    engine = create_engine(sqlalchemy_database_uri_mysql)

    # connect to DB
    DB_Session = sessionmaker(autocommit=True, autoflush=True, bind=engine)
    session = DB_Session()
    return session


def run_send_sms(server_tunnel=None):
    """
    短信发送
    :return:
    """
    if server_tunnel and not server_tunnel.is_active:
        server.start()  # start ssh sever
        print 'Server reconnected via SSH'
    session = get_db_session(server_tunnel)
    print 'Database session created'

    sms_client = SmsChuangLanIsoApi(UN, PW)

    # test data retrieval
    while 1:
        sql_fetch = "SELECT * FROM ot_sms WHERE sent_st=0 limit 100"
        sql_edit = 'UPDATE ot_sms SET sent_st=:sent_st WHERE id=:id;'
        rows = session.execute(sql_fetch).fetchall()
        for row in rows:
            # 处理中
            session.execute(sql_edit, {'id': row['id'], 'sent_st': 1})
            # 发送信息
            print time.strftime('%Y-%m-%d %H:%M:%S'), row['mobile'], row['msg']

            result = sms_client.send_international('86%s' % row['mobile'], row['msg'])
            print result
            if result['success']:
                print session.execute(sql_edit, {'id': row['id'], 'sent_st': 2}).rowcount
            else:
                print session.execute(sql_edit, {'id': row['id'], 'sent_st': 3}).rowcount
    # server.stop()  # stop ssh sever


if __name__ == '__main__':
    # 隧道模式
    server = get_server_tunnel()
    server.start()
    run_send_sms(server)
    server.stop()
    # 普通模式
    run_send_sms()


"""
✗ pip install sshtunnel
✗ pip install MySQL-python
✗ pip install schedule
"""