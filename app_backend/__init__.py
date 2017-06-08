#!/usr/bin/env python
# encoding: utf-8

"""
@author: zhanghe
@software: PyCharm
@file: __init__.py
@time: 2017/4/9 上午10:11
"""

from logging.config import dictConfig

from flask import Flask
from flask_login import LoginManager
from flask_moment import Moment
from flask_oauthlib.client import OAuth
from flask_principal import Principal, Permission, RoleNeed

from app_backend.lib.qiniu_store import QiNiuClient
from app_backend.lib.redis_session import RedisSessionInterface
from app_backend.lib.sendcloud import SendCloudClient
from app_backend.lib.sms_chuanglan_iso import SmsChuangLanIsoApi


app = Flask(__name__)
app.config.from_object('config')
app.config['REMEMBER_COOKIE_NAME'] = 'r_a'
app.session_cookie_name = 's_a'
app.session_interface = RedisSessionInterface(prefix='s:a:', **app.config['REDIS'])

login_manager = LoginManager()
login_manager.init_app(app)  # setup_app 方法已淘汰
login_manager.login_view = 'login'
login_manager.login_message = u'请登录后操作'  # 设置登录提示消息
login_manager.login_message_category = 'info'  # 设置消息分类

# 权限管理插件
principals = Principal(app)

# Moment 时间插件
moment = Moment(app)

# 短信通道
sms_client = SmsChuangLanIsoApi(app.config['SMS']['UN'], app.config['SMS']['PW'])

# SendCloud 邮件
send_cloud_client = SendCloudClient(app)

# 七牛云存储
qi_niu_client = QiNiuClient(app)

# 第三方开放授权登录
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
from app_backend import models, tasks

# 导入视图（不使用蓝图的单模式方式）
from app_backend import views

# 导入视图（不使用蓝图的多模块方式）
# from application.views import auth
# from application.views import blog
# from application.views import reg
# from application.views import site
# from application.views import user

# 导入蓝图（使用蓝图的多模块方式）
from app_backend.views.admin import bp_admin
from app_backend.views.apply_get import bp_apply_get
from app_backend.views.apply_put import bp_apply_put
from app_backend.views.order import bp_order
from app_backend.views.score import bp_score
from app_backend.views.wallet import bp_wallet
# from app_backend.views.blog import bp_blog
# from app_backend.views.file import bp_file
# from app_backend.views.reg import bp_reg
from app_backend.views.user import bp_user
from app_backend.views.settings import bp_settings
from app_backend.views.complaint import bp_complaint
from app_backend.views.message import bp_message


# 注册蓝图
app.register_blueprint(bp_admin)
app.register_blueprint(bp_apply_get)
app.register_blueprint(bp_apply_put)
app.register_blueprint(bp_order)
app.register_blueprint(bp_score)
app.register_blueprint(bp_wallet)
# app.register_blueprint(bp_blog)
# app.register_blueprint(bp_file)
# app.register_blueprint(bp_reg)
app.register_blueprint(bp_user)
app.register_blueprint(bp_settings)
app.register_blueprint(bp_complaint)
app.register_blueprint(bp_message)

# 导入自定义过滤器
from app_backend import filters
