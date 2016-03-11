#!/usr/bin/env python
# encoding: utf-8

"""
@author: zhanghe
@software: PyCharm
@file: __init__.py
@time: 16-1-7 上午12:08
"""


from flask import Flask
from flask.ext.login import LoginManager
from flask.ext.mail import Mail


app = Flask(__name__)
app.config.from_object('config')
login_manager = LoginManager()
login_manager.init_app(app)  # setup_app 方法已淘汰
login_manager.login_view = 'login'
# login_manager.login_message = 'Please log in to access this page.'  # 设置登陆提示消息
login_manager.login_message_category = 'info'  # 设置消息分类

# 生产环境邮箱配置
mail_config = dict(
    MAIL_SERVER='smtp.163.com',
    MAIL_PORT=25,
    MAIL_USERNAME='xxxxxx@163.com',
    MAIL_PASSWORD='xxxxxx',
    MAIL_DEFAULT_SENDER=(u'系统邮箱', 'zhang_he06@163.com')
)

# 本地调试邮箱配置
# mail_config = dict(
#     MAIL_SERVER='localhost',
#     MAIL_PORT=25,
#     MAIL_USERNAME=None,
#     MAIL_PASSWORD=None,
#     MAIL_DEFAULT_SENDER=(u'系统邮箱', 'no-reply@localhost')
#     # MAIL_DEFAULT_SENDER=('no-reply', 'no-reply@localhost')
# )

app.config.update(mail_config)
mail = Mail(app)
# 后台管理人员邮件列表
ADMINS = ['455091702@qq.com']


if not app.debug:
    import logging
    from logging.handlers import SMTPHandler
    credentials = None
    if app.config['MAIL_USERNAME'] or app.config['MAIL_PASSWORD']:
        credentials = (app.config['MAIL_USERNAME'], app.config['MAIL_PASSWORD'])
    mail_handler = SMTPHandler(
        (app.config['MAIL_SERVER'], app.config['MAIL_PORT']),
        app.config['MAIL_DEFAULT_SENDER'][1],
        ADMINS,
        'App Error Message',
        credentials
    )
    mail_handler.setLevel(logging.DEBUG)
    app.logger.addHandler(mail_handler)


# 这个 import 语句放在这里, 防止views, models import发生循环import
from app import views, models
