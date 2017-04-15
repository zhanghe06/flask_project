#!/usr/bin/env python
# encoding: utf-8

"""
@author: zhanghe
@software: PyCharm
@file: reg.py
@time: 2017/3/10 下午11:00
"""

from datetime import datetime

from flask import request, render_template, redirect, url_for, flash

from app_frontend import app

from flask import Blueprint


bp_reg = Blueprint('reg', __name__, url_prefix='/reg')


@bp_reg.route('/', methods=['GET', 'POST'])
def index():
    """
    注册
    """
    # return "Hello, World!\nReg!"
    from app_frontend.forms.reg import RegForm
    form = RegForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            # 添加用户信息

            current_time = datetime.utcnow()
            user_data = {
                'email': form.email.data,
                'create_time': current_time,
                'update_time': current_time,
                'last_ip': request.headers.get('X-Forwarded-For', request.remote_addr)
            }
            from app_frontend.api.user import add_user
            user_id = add_user(user_data)
            # 添加授权信息

            user_auth_data = {
                'user_id': user_id,
                'auth_type': 'email',
                'auth_key': form.email.data,
                'auth_secret': form.password.data
            }
            from app_frontend.api.user_auth import add_user_auth
            user_auth_id = add_user_auth(user_auth_data)
            if user_auth_id:
                flash(u'%s, Thanks for registering' % form.email.data, 'success')
                # todo 发送邮箱校验邮件
                email_validate_content = {
                    'mail_from': 'System Support<support@zhendi.me>',
                    'mail_to': form.email.data,
                    'mail_subject': 'verify reg email',
                    'mail_html': 'verify reg email address in mailbox'
                }
                from app_frontend import send_cloud_client
                send_email_result = send_cloud_client.mail_send(**email_validate_content)
                # 调试邮件发送结果
                if send_email_result.get('result') is False:
                    flash(send_email_result.get('message'), 'warning')
                else:
                    flash(send_email_result.get('message'), 'success')
                # https://www.***.com/email/signup/uuid
            else:
                flash(u'%s, Sorry, register error' % form.email.data, 'warning')
            return redirect(url_for('auth.login'))
        # 闪现消息 success info warning danger
        flash(form.errors, 'warning')  # 调试打开
    return render_template('reg/index.html', title='reg', form=form)


@bp_reg.route('/phone/', methods=['GET', 'POST'])
def phone():
    """
    手机注册
    """
    # return "Hello, World!\nReg!"
    from app_frontend.forms.reg import RegPhoneForm
    form = RegPhoneForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            # 添加用户信息

            current_time = datetime.utcnow()
            user_data = {
                'phone': form.phone.data,
                'create_time': current_time,
                'update_time': current_time,
                'last_ip': request.headers.get('X-Forwarded-For', request.remote_addr)
            }
            from app_frontend.api.user import add_user
            user_id = add_user(user_data)
            # 添加授权信息

            user_auth_data = {
                'user_id': user_id,
                'auth_type': 'phone',
                'auth_key': form.email.data,
                'auth_secret': form.password.data
            }
            from app_frontend.api.user_auth import add_user_auth
            user_auth_id = add_user_auth(user_auth_data)
            if user_auth_id:
                flash(u'%s, Thanks for registering' % form.email.data, 'success')
                # todo 发送邮箱校验邮件
                email_validate_content = {
                    'mail_from': 'System Support<support@zhendi.me>',
                    'mail_to': form.email.data,
                    'mail_subject': 'verify reg email',
                    'mail_html': 'verify reg email address in mailbox'
                }
                from app_frontend import send_cloud_client
                send_email_result = send_cloud_client.mail_send(**email_validate_content)
                # 调试邮件发送结果
                if send_email_result.get('result') is False:
                    flash(send_email_result.get('message'), 'warning')
                else:
                    flash(send_email_result.get('message'), 'success')
                # https://www.***.com/email/signup/uuid
            else:
                flash(u'%s, Sorry, register error' % form.email.data, 'warning')
            return redirect(url_for('auth.login'))
        # 闪现消息 success info warning danger
        flash(form.errors, 'warning')  # 调试打开
    return render_template('reg/phone.html', title='reg', form=form)


@bp_reg.route('/email/', methods=['GET', 'POST'])
def email():
    """
    邮箱注册
    """
    # return "Hello, World!\nReg!"
    from app_frontend.forms.reg import RegForm
    form = RegForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            # 添加用户信息

            current_time = datetime.utcnow()
            user_data = {
                'email': form.email.data,
                'create_time': current_time,
                'update_time': current_time,
                'last_ip': request.headers.get('X-Forwarded-For', request.remote_addr)
            }
            from app_frontend.api.user import add_user
            user_id = add_user(user_data)
            # 添加授权信息

            user_auth_data = {
                'user_id': user_id,
                'auth_type': 'email',
                'auth_key': form.email.data,
                'auth_secret': form.password.data
            }
            from app_frontend.api.user_auth import add_user_auth
            user_auth_id = add_user_auth(user_auth_data)
            if user_auth_id:
                flash(u'%s, Thanks for registering' % form.email.data, 'success')
                # todo 发送邮箱校验邮件
                email_validate_content = {
                    'mail_from': 'System Support<support@zhendi.me>',
                    'mail_to': form.email.data,
                    'mail_subject': 'verify reg email',
                    'mail_html': 'verify reg email address in mailbox'
                }
                from app_frontend import send_cloud_client
                send_email_result = send_cloud_client.mail_send(**email_validate_content)
                # 调试邮件发送结果
                if send_email_result.get('result') is False:
                    flash(send_email_result.get('message'), 'warning')
                else:
                    flash(send_email_result.get('message'), 'success')
                # https://www.***.com/email/signup/uuid
            else:
                flash(u'%s, Sorry, register error' % form.email.data, 'warning')
            return redirect(url_for('auth.login'))
        # 闪现消息 success info warning danger
        flash(form.errors, 'warning')  # 调试打开
    return render_template('reg/email.html', title='reg', form=form)


@bp_reg.route('/agreement/')
def agreement():
    """
    注册协议
    :return:
    """
    return 'agreement'


@bp_reg.route('/email/sign')
def email_sign():
    """
    邮箱签名(带过期时间)
    http://localhost:5000/email/sign?email=zhang_he06@163.com
    """
    email = request.args.get('email', '')
    from itsdangerous import TimestampSigner
    from app_frontend import app
    s = TimestampSigner(app.config['SECRET_KEY'])
    return s.sign(email)


@bp_reg.route('/email/check')
def email_check():
    """
    校验邮箱有效性
    http://localhost:5000/email/check?sign=zhang_he06@163.com.ChstqQ.5jODirLaRF2yU0CLtZz2EmoHt4c
    """
    sign = request.args.get('sign', '')
    from itsdangerous import TimestampSigner, SignatureExpired, BadTimeSignature
    from app_frontend import app
    s = TimestampSigner(app.config['SECRET_KEY'])
    try:
        # email = s.unsign(sign, max_age=5)  # 5秒过期
        email = s.unsign(sign, max_age=30*24*60*60)  # １个月过期
        # return email
        # 校验通过，更新邮箱验证状态
        from app_frontend.api.user_auth import update_user_auth_rows
        result = update_user_auth_rows({'verified': 1}, **{'auth_type': 'email', 'auth_key': email})
        if result == 1:
            flash(u'%s, Your mailbox has been verified' % email, 'success')
            return redirect(url_for('auth.login'))
        else:
            flash(u'%s, Sorry, Your mailbox validation failed' % email, 'warning')
    except SignatureExpired as e:
        # 处理签名超时
        flash(e.message, 'warning')
    except BadTimeSignature as e:
        # 处理签名错误
        flash(e.message, 'warning')
    return redirect(url_for('reg.index'))
