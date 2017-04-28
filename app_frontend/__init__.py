#!/usr/bin/env python
# encoding: utf-8

"""
@author: zhanghe
@software: PyCharm
@file: __init__.py
@time: 16-1-7 上午12:08
"""

from logging.config import dictConfig

from flask import Flask
from flask_login import LoginManager
from flask_moment import Moment
from flask_oauthlib.client import OAuth

from app_frontend.lib.qiniu_store import QiNiuClient
from app_frontend.lib.redis_session import RedisSessionInterface
from app_frontend.lib.sendcloud import SendCloudClient
from app_frontend.middlewares import HTTPMethodOverrideMiddleware


app = Flask(__name__)
app.config.from_object('config')
app.wsgi_app = HTTPMethodOverrideMiddleware(app.wsgi_app)
app.session_interface = RedisSessionInterface(prefix='session:user:', **app.config['REDIS'])

login_manager = LoginManager()
login_manager.init_app(app)  # setup_app 方法已淘汰
login_manager.login_view = 'auth.index'
# login_manager.login_message = 'Please log in to access this page.'  # 设置登陆提示消息
login_manager.login_message_category = 'info'  # 设置消息分类

# Moment 时间插件
moment = Moment(app)

# SendCloud 邮件
send_cloud_client = SendCloudClient(app)

# 七牛云存储
qi_niu_client = QiNiuClient(app)

# 第三方开放授权登陆
oauth = OAuth(app)

# GitHub
oauth_github = oauth.remote_app(
    'github',
    **app.config['GITHUB_OAUTH']
)

# QQ
oauth_qq = oauth.remote_app(
    'qq',
    **app.config['QQ_OAUTH']
)

# WeiBo
oauth_weibo = oauth.remote_app(
    'weibo',
    **app.config['WEIBO_OAUTH']
)

# Google
# 要银子，妹的


# 配置日志
dictConfig(app.config['LOG_CONFIG'])

if not app.config['DEBUG']:
    import logging
    from logging.handlers import SMTPHandler
    credentials = None
    if app.config['MAIL_USERNAME'] or app.config['MAIL_PASSWORD']:
        credentials = (app.config['MAIL_USERNAME'], app.config['MAIL_PASSWORD'])
    mail_handler = SMTPHandler(
        (app.config['MAIL_SERVER'], app.config['MAIL_PORT']),
        app.config['MAIL_DEFAULT_SENDER'][1],
        app.config['ADMINS'],
        'App Error Message',
        credentials
    )
    mail_handler.setLevel(logging.DEBUG)
    app.logger.addHandler(mail_handler)


# 这个 import 语句放在这里, 防止views, models import发生循环import
from app_frontend import models, tasks

# 导入视图（不使用蓝图的单模式方式）
from app_frontend import views

# 导入视图（不使用蓝图的多模块方式）
# from application.views import auth
# from application.views import blog
# from application.views import reg
# from application.views import site
# from application.views import user

# 导入蓝图（使用蓝图的多模块方式）
from app_frontend.views.captcha import bp_captcha
from app_frontend.views.auth import bp_auth
from app_frontend.views.blog import bp_blog
from app_frontend.views.file import bp_file
from app_frontend.views.reg import bp_reg
from app_frontend.views.user import bp_user
from app_frontend.views.credit import bp_credit
from app_frontend.views.apply import bp_apply
from app_frontend.views.order import bp_order
from app_frontend.views.score import bp_score
from app_frontend.views.wallet import bp_wallet
from app_frontend.views.ticket_get import bp_ticket_get
from app_frontend.views.ticket_put import bp_ticket_put

# 注册蓝图
app.register_blueprint(bp_captcha)
app.register_blueprint(bp_auth)
app.register_blueprint(bp_blog)
app.register_blueprint(bp_file)
app.register_blueprint(bp_reg)
app.register_blueprint(bp_user)
app.register_blueprint(bp_credit)
app.register_blueprint(bp_apply)
app.register_blueprint(bp_order)
app.register_blueprint(bp_score)
app.register_blueprint(bp_wallet)
app.register_blueprint(bp_ticket_get)
app.register_blueprint(bp_ticket_put)

# 导入自定义过滤器
from app_frontend import filters
