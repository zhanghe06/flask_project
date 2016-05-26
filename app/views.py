#!/usr/bin/env python
# encoding: utf-8

"""
@author: zhanghe
@software: PyCharm
@file: views.py
@time: 16-1-7 上午12:10
"""


from app import app, login_manager, oauth_github, oauth_qq, oauth_weibo, send_cloud_client, qi_niu_client
from flask import render_template, request, url_for, send_from_directory, session, flash, redirect, g, jsonify, Markup
from app.forms import RegForm, LoginForm, BlogAddForm, BlogEditForm, UserForm
from app.login import LoginUser
from flask.ext.login import login_user, logout_user, current_user, login_required
import os
import json


@login_manager.user_loader
def load_user(user_id):
    """
    如果 user_id 无效，它应该返回 None （ 而不是抛出异常 ）。
    :param user_id:
    :return:
    """
    return LoginUser.query.get(int(user_id))


@app.before_request
def before_request():
    """
    当前用户信息
    """
    g.user = current_user


@app.route('/favicon.ico')
def favicon():
    """
    首页ico图标
    """
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'img/favicon.ico', mimetype='image/vnd.microsoft.icon')


@app.route('/')
@app.route('/index')
def index():
    """
    网站首页
    """
    # return "Hello, World!"
    return render_template('index.html', title='home')


@app.route('/about')
def about():
    """
    关于网站
    """
    # return "Hello, World!\nAbout!"
    return render_template('about.html', title='about')


@app.route('/contact')
def contact():
    """
    联系方式
    """
    # return "Hello, World!\nContact!"
    return render_template('contact.html', title='contact')


@app.route('/blog/list/')
@app.route('/blog/list/<int:page>/')
def blog_list(page=1):
    """
    博客列表
    """
    # return "Hello, World!\nBlog List!"
    from blog import get_blog_rows
    per_page = 8
    pagination = get_blog_rows(page, per_page)
    return render_template('blog/list.html', title='blog_list', pagination=pagination)


@app.route('/blog/new/')
@app.route('/blog/new/<int:page>/')
def blog_new(page=1):
    """
    最新博客
    """
    # return "Hello, World!\nBlog New!"
    from blog import get_blog_rows, get_blog_list_counter, get_blog_list_container_status
    per_page = 8
    pagination = get_blog_rows(page, per_page)
    id_list = [item.id for item in pagination.items]
    blog_counter_list = get_blog_list_counter(id_list)
    # 状态设置
    login_user_id = g.user.get_id()
    blog_container_status_list = get_blog_list_container_status(id_list, login_user_id)
    return render_template(
        'blog/new.html',
        title='blog_new',
        pagination=pagination,
        blog_counter_list=blog_counter_list,
        blog_container_status_list=blog_container_status_list
    )


@app.route('/blog/hot/')
@app.route('/blog/hot/<int:page>/')
def blog_hot(page=1):
    """
    热门博客
    """
    # return "Hello, World!\nBlog Hot!"
    from blog import get_blog_rows
    per_page = 8
    pagination = get_blog_rows(page, per_page)
    return render_template('blog/hot.html', title='blog_hot', pagination=pagination)


@app.route('/blog/edit/<int:blog_id>/', methods=['GET', 'POST'])
@login_required
def blog_edit(blog_id):
    """
    博客编辑
    """
    # return "Hello, World!\nBlog Edit!"
    form = BlogEditForm(request.form)
    if request.method == 'GET':
        from blog import get_blog_row_by_id
        blog_info = get_blog_row_by_id(blog_id)
        if blog_info:
            form.author.data = blog_info.author
            form.title.data = blog_info.title
            form.pub_date.data = blog_info.pub_date
        else:
            return redirect(url_for('index'))
    if request.method == 'POST':
        if form.validate_on_submit():
            from blog import edit_blog
            from datetime import datetime
            blog_info = {
                'author': form.author.data,
                'title': form.title.data,
                'pub_date': form.pub_date.data,
                'edit_time': datetime.utcnow(),
            }
            result = edit_blog(blog_id, blog_info)
            if result == 1:
                flash(u'Edit Success', 'success')
                return redirect(request.args.get('next') or url_for('blog_list'))
            if result == 0:
                flash(u'Edit Failed', 'warning')
        flash(form.errors, 'warning')  # 调试打开
    flash(u'Hello, %s' % current_user.email, 'info')  # 测试打开
    return render_template('blog/edit.html', title='blog_edit', blog_id=blog_id, form=form)


@app.route('/blog/add/', methods=['GET', 'POST'])
@login_required
def blog_add():
    """
    博客添加
    """
    # return "Hello, World!\nBlog Add!"
    form = BlogAddForm(request.form)
    if request.method == 'POST':
        if form.validate_on_submit():
            from blog import add_blog
            from datetime import datetime
            blog_info = {
                'author': form.author.data,
                'title': form.title.data,
                'pub_date': form.pub_date.data,
                'add_time': datetime.utcnow(),
                'edit_time': datetime.utcnow(),
            }
            result = add_blog(blog_info)
            if result is None:
                flash(u'Add Failed', 'warning')
            else:
                flash(u'Add Success', 'success')
                return redirect(url_for('blog_edit', blog_id=result))
        flash(form.errors, 'warning')  # 调试打开
    # flash(u'Hello, %s' % current_user.email, 'info')  # 测试打开
    return render_template('blog/add.html', title='blog_add', form=form)


@app.route('/blog/del/', methods=['GET', 'POST'])
def blog_delete():
    """
    博客删除
    """
    if request.method == 'GET':
        login_user_id = g.user.get_id()
        # 权限判断，只能删除自己的 blog todo
        if login_user_id is None:
            return jsonify(result=False)
        blog_id = request.args.get('blog_id', 0, type=int)
        from blog import delete_blog
        result = delete_blog(blog_id)
        if result == 1:
            return jsonify(result=True)
        else:
            return jsonify(result=False)


@app.route('/blog/stat/', methods=['GET', 'POST'])
def blog_stat():
    """
    博客统计
    http://localhost:5000/blog/stat/?blog_id=2&stat_type=favor&num=2
    :return:
    """
    if request.method == 'GET':
        login_user_id = g.user.get_id()
        if login_user_id is None:
            return jsonify(result=False)
        blog_id = request.args.get('blog_id', 0, type=int)
        stat_type = request.args.get('stat_type', '', type=str)
        # num = request.args.get('num', 0, type=int)
        from tools.stat import set_blog_stat
        result = set_blog_stat(stat_type, login_user_id, blog_id)
        return jsonify(result)


@app.route('/reg/', methods=['GET', 'POST'])
def reg():
    """
    注册
    """
    # return "Hello, World!\nReg!"
    form = RegForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            # 添加用户信息
            from user import add_user
            from datetime import datetime
            current_time = datetime.utcnow()
            user_data = {
                'email': form.email.data,
                'create_time': current_time,
                'update_time': current_time,
                'last_ip': request.remote_addr
            }
            user_id = add_user(user_data)
            # 添加授权信息
            from user_auth import add_user_auth
            user_auth_data = {
                'user_id': user_id,
                'auth_type': 'email',
                'auth_key': form.email.data,
                'auth_secret': form.password.data
            }
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
                send_email_result = send_cloud_client.mail_send(**email_validate_content)
                # 调试邮件发送结果
                if send_email_result.get('result') is False:
                    flash(send_email_result.get('message'), 'warning')
                else:
                    flash(send_email_result.get('message'), 'success')
                # https://www.***.com/email/signup/uuid
            else:
                flash(u'%s, Sorry, register error' % form.email.data, 'warning')
            return redirect(url_for('login'))
        # 闪现消息 success info warning danger
        flash(form.errors, 'warning')  # 调试打开
    return render_template('reg.html', title='reg', form=form)


@app.route('/email/sign')
def email_sign():
    """
    邮箱签名(带过期时间)
    http://localhost:5000/email/sign?email=zhang_he06@163.com
    """
    email = request.args.get('email', '')
    from itsdangerous import TimestampSigner
    s = TimestampSigner(app.config['SECRET_KEY'])
    return s.sign(email)


@app.route('/email/check')
def email_check():
    """
    校验邮箱有效性
    http://localhost:5000/email/check?sign=zhang_he06@163.com.ChstqQ.5jODirLaRF2yU0CLtZz2EmoHt4c
    """
    sign = request.args.get('sign', '')
    from itsdangerous import TimestampSigner, SignatureExpired, BadTimeSignature
    s = TimestampSigner(app.config['SECRET_KEY'])
    try:
        # email = s.unsign(sign, max_age=5)  # 5秒过期
        email = s.unsign(sign, max_age=30*24*60*60)  # １个月过期
        # return email
        # 校验通过，更新邮箱验证状态
        from user_auth import update_user_auth_rows
        result = update_user_auth_rows({'verified': 1}, **{'auth_type': 'email', 'auth_key': email})
        if result == 1:
            flash(u'%s, Your mailbox has been verified' % email, 'success')
            return redirect(url_for('login'))
        else:
            flash(u'%s, Sorry, Your mailbox validation failed' % email, 'warning')
    except SignatureExpired as e:
        # 处理签名超时
        flash(e.message, 'warning')
    except BadTimeSignature as e:
        # 处理签名错误
        flash(e.message, 'warning')
    return redirect(url_for('reg'))


@app.route('/login/', methods=['GET', 'POST'])
def login():
    """
    登录
    """
    if g.user is not None and g.user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            from user_auth import get_user_auth_row
            condition = {
                'auth_type': 'email',
                'auth_key': form.email.data,
                'auth_secret': form.password.data
            }
            user_auth_info = get_user_auth_row(**condition)
            if user_auth_info is None:
                flash(u'%s, You were logged failed' % form.email.data, 'warning')
                return render_template('login.html', title='login', form=form)
            if user_auth_info.verified == 0:
                flash(u'%s, Please verify email address in mailbox' % form.email.data, 'warning')
                return render_template('login.html', title='login', form=form)
            # session['logged_in'] = True
            # 用户通过验证后，记录登入IP
            from user import edit_user
            edit_user(user_auth_info.user_id, {'last_ip': request.remote_addr})
            # 用 login_user 函数来登入他们
            from user import get_user_row_by_id
            login_user(get_user_row_by_id(user_auth_info.user_id))
            flash(u'%s, You were logged in' % form.email.data, 'success')
            return redirect(request.args.get('next') or url_for('index'))
        flash(form.errors, 'warning')  # 调试打开
    return render_template('login.html', title='login', form=form)


# @app.route('/logout')
# def logout():
#     session.pop('logged_in', None)
#     flash(u'You were logged out')
#     return redirect(url_for('index'))

@app.route('/logout/')
def logout():
    """
    退出登录
    """
    logout_user()
    session.pop('qq_token', None)
    session.pop('weibo_token', None)
    session.pop('github_token', None)
    flash(u'You were logged out', 'info')
    return redirect(url_for('index'))


@app.route('/setting/', methods=['GET', 'POST'])
@login_required
def setting():
    """
    设置
    """
    # return "Hello, World!\nSetting!"
    form = UserForm(request.form)
    if request.method == 'GET':
        from user import get_user_row_by_id
        user_info = get_user_row_by_id(current_user.id)
        if user_info:
            form.nickname.data = user_info.nickname
            form.avatar_url.data = user_info.avatar_url
            form.email.data = user_info.email
            form.phone.data = user_info.phone
            form.birthday.data = user_info.birthday
            form.create_time.data = user_info.create_time
            form.update_time.data = user_info.update_time
            form.last_ip.data = user_info.last_ip
    if request.method == 'POST':
        if form.validate_on_submit():
            # todo 判断邮箱是否重复
            from user import edit_user
            from datetime import datetime
            user_info = {
                'nickname': form.nickname.data,
                'avatar_url': form.avatar_url.data,
                'email': form.email.data,
                'phone': form.phone.data,
                'birthday': form.birthday.data,
                'update_time': datetime.utcnow(),
                'last_ip': request.remote_addr,
            }
            result = edit_user(current_user.id, user_info)
            if result == 1:
                flash(u'Edit Success', 'success')
            if result == 0:
                flash(u'Edit Failed', 'warning')
        flash(form.errors, 'warning')  # 调试打开
    flash(u'Hello, %s' % current_user.email, 'info')  # 测试打开
    return render_template('setting.html', title='setting', form=form)


@app.route('/search/', methods=['GET', 'POST'])
def search():
    """
    搜索
    """
    return 'search result!'


@app.route("/email/")
def send_email():
    """
    邮件发送
    """
    try:
        from emails import send_email
        msg = 'This is a test email!'
        send_email(
            subject=u'邮件主题',
            sender=(u'系统邮箱', 'zhang_he06@163.com'),
            recipients=[(u'尊敬的用户', 'zhang_he06@163.com')],
            html_body=render_template('email.html', message=msg)
        )
        return jsonify({'success': u'邮件发送成功'})
    except Exception, e:
        return jsonify({'error': e.message})


@app.route("/test")
def test():
    """
    测试
    """
    try:
        raise Exception('error test')
    except Exception as e:
        import logging
        logging.error(e)


@app.route("/test_client_ip")
def test_client_ip():
    """
    测试客户端来源ip
    http://localhost:5000/test_client_ip
    curl -H "X-Forwarded-For: 1.2.3.4" http://localhost:5000/test_client_ip
    """
    if not request.headers.getlist("X-Forwarded-For"):
        ip = request.remote_addr
    else:
        ip = request.headers.getlist("X-Forwarded-For")[0]
        # todo 校验 Ip 格式
    return ip


@app.route("/test_down")
def test_down():
    """
    测试下载
    """
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'img/cat.jpg', as_attachment=True)


@app.route("/test/sendcloud")
def test_sendcloud():
    """
    测试 sendcloud
    http://localhost:5000/test/sendcloud
    注意: 用户可以调用模板发送, 也可以普通发送(上传内容发送). 两种发送方式都要求最终的内容和至少一个模板匹配
    """
    # 获取信息
    result = send_cloud_client.userinfo_get()
    # return json.dumps(result)

    # 发送邮件
    email_content = {
        'mail_from': 'System Support<support@zhendi.me>',
        'mail_to': 'zhanghe@wealink.com',
        'mail_subject': '来自SendCloud的第一封邮件！',
        'mail_html': '你太棒了！你已成功的从SendCloud发送了一封测试邮件，接下来快登录前台去完善账户信息吧！'
    }
    send_email_result = send_cloud_client.mail_send(**email_content)
    # 调试邮件发送结果
    return json.dumps(send_email_result)


@app.route('/save')
def save():
    """
    保存文件到七牛
    """
    data = 'data to save'
    filename = 'filename'
    ret, info = qi_niu_client.save(data, filename)
    return str(ret)


@app.route('/delete')
def delete():
    """
    删除七牛空间中的文件
    """
    filename = 'filename'
    ret, info = qi_niu_client.delete(filename)
    return str(ret)


@app.route('/url')
def url():
    """
    根据文件名获取对应的公开URL
    """
    filename = 'filename'
    return qi_niu_client.url(filename)


# # 第三方登陆（QQ）
def json_to_dict(x):
    """
    OAuthResponse class can't not parse the JSON data with content-type
    text/html, so we need reload the JSON data manually
    :param x:
    :return:
    """
    if x.find('callback') > -1:
        pos_lb = x.find('{')
        pos_rb = x.find('}')
        x = x[pos_lb:pos_rb + 1]
    try:
        return json.loads(x, encoding='utf-8')
    except:
        return x


def update_qq_api_request_data(data={}):
    """
    Update some required parameters for OAuth2.0 API calls
    :param data:
    :return:
    """
    defaults = {
        'openid': session.get('qq_openid'),
        'access_token': session.get('qq_token')[0],
        'oauth_consumer_key': app.config['consumer_key'],
    }
    defaults.update(data)
    return defaults


@app.route('/user_info')
def get_user_info():
    if 'qq_token' in session:
        data = update_qq_api_request_data()
        resp = oauth_qq.get('/user/get_user_info', data=data)
        return jsonify(status=resp.status, data=resp.data)
    return redirect(url_for('login_qq'))


@app.route('/login/qq/')
def login_qq():
    return oauth_qq.authorize(callback=url_for('authorized_qq', _external=True))


@app.route('/login/authorized/qq/')
def authorized_qq():
    resp = oauth_qq.authorized_response()
    if resp is None:
        return 'Access denied: reason=%s error=%s' % (
            request.args['error_reason'],
            request.args['error_description']
        )
    session['qq_token'] = (resp['access_token'], '')

    # Get openid via access_token, openid and access_token are needed for API calls
    resp = oauth_qq.get('/oauth2.0/me', {'access_token': session['qq_token'][0]})
    resp = json_to_dict(resp.data)
    if isinstance(resp, dict):
        session['qq_openid'] = resp.get('openid')

    return redirect(url_for('get_user_info'))


@oauth_qq.tokengetter
def get_qq_oauth_token():
    return session.get('qq_token')


# 第三方登陆（WeiBo）
# @app.route('/')
# def index():
#     if 'oauth_token' in session:
#         access_token = session['oauth_token'][0]
#         resp = weibo.get('statuses/home_timeline.json')
#         return jsonify(resp.data)
#     return redirect(url_for('login'))


@app.route('/login/weibo/')
def login_weibo():
    return oauth_weibo.authorize(callback=url_for('authorized_weibo',
        next=request.args.get('next') or request.referrer or None,
        _external=True))


@app.route('/login/authorized/weibo/')
def authorized_weibo():
    resp = oauth_weibo.authorized_response()
    if resp is None:
        return 'Access denied: reason=%s error=%s' % (
            request.args['error_reason'],
            request.args['error_description']
        )
    session['oauth_token'] = (resp['access_token'], '')
    return redirect(url_for('index'))


@oauth_weibo.tokengetter
def get_weibo_oauth_token():
    return session.get('oauth_token')


def change_weibo_header(uri, headers, body):
    """Since weibo is a rubbish server, it does not follow the standard,
    we need to change the authorization header for it."""
    auth = headers.get('Authorization')
    if auth:
        auth = auth.replace('Bearer', 'OAuth2')
        headers['Authorization'] = auth
    return uri, headers, body

oauth_weibo.pre_request = change_weibo_header


# 第三方登陆（GitHub）
@app.route('/login/github/')
def login_github():
    return oauth_github.authorize(callback=url_for('authorized_github', _external=True))


@app.route('/login/authorized/github/')
def authorized_github():
    resp = oauth_github.authorized_response()
    if resp is None:
        return 'Access denied: reason=%s error=%s' % (
            request.args['error'],
            request.args['error_description']
        )
    session['github_token'] = (resp['access_token'], '')
    me = oauth_github.get('user')
    return jsonify(me.data)


@oauth_github.tokengetter
def get_github_oauth_token():
    return session.get('github_token')
