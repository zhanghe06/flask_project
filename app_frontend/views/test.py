#!/usr/bin/env python
# encoding: utf-8

"""
@author: zhanghe
@software: PyCharm
@file: test.py
@time: 2017/3/18 上午12:30
"""


from app_frontend import app, login_manager, oauth_github, oauth_qq, oauth_weibo, send_cloud_client, qi_niu_client
from flask import render_template, request, url_for, send_from_directory, session, flash, redirect, g, jsonify, Markup, abort
# from application.forms import RegForm, LoginForm, BlogAddForm, BlogEditForm, UserForm
from app_frontend.login import LoginUser
from flask_login import login_user, logout_user, current_user, login_required
import os
import json
from werkzeug.contrib.cache import SimpleCache
cache = SimpleCache()  # 默认最大支持500个key, 超时时间5分钟, 参数可配置


# log测试
@app.route('/test_log/')
def test_log():
    """
    log测试
    """
    import logging
    log = logging.getLogger('app')
    log.debug('info message')
    log.info('info message')
    log.error('error message')
    return 'log测试'


# 缓存测试
@app.route('/test_cache/')
def test_cache():
    """
    缓存测试
    5.01s >> 9ms
    """
    import time
    rv = cache.get('my-item')
    if rv is None:
        time.sleep(5)
        rv = 'Hello, Cache!'
        cache.set('my-item', rv, timeout=5 * 10)
    return rv


# 后台任务测试
@app.route('/test_send_task/')
def test_send_task(x=100, y=200):
    """
    后台发送任务测试
    http://localhost:8000/test_send_task/?x=100&y=200
    """
    from app_frontend.tasks import add, mul, xsum

    x = int(request.args.get('x', x))
    y = int(request.args.get('y', y))

    add_res = add.delay(x, y)
    mul_res = mul.delay(x, y)
    xsum_res = xsum.delay([x, y])
    result = ''
    result += '<a href="http://localhost:8000/test_task_add_result/%s/">%s</a><br/>' % (add_res.id, add_res.id)
    result += '<a href="http://localhost:8000/test_task_mul_result/%s/">%s</a><br/>' % (mul_res.id, mul_res.id)
    result += '<a href="http://localhost:8000/test_task_xsum_result/%s/">%s</a><br/>' % (xsum_res.id, xsum_res.id)
    return result


@app.route('/test_task_send_get/')
def test_task_send_get(x=100, y=200):
    """
    后台发送任务并获取结果测试
    http://localhost:8000/test_task_send_get/?x=100&y=200
    """
    from app_frontend.tasks import add, mul, xsum

    x = int(request.args.get('x', x))
    y = int(request.args.get('y', y))

    add_res = add.delay(x, y)
    mul_res = mul.delay(x, y)
    xsum_res = xsum.delay([x, y])
    import time
    time.sleep(0.0005)
    result = {
        'add_res': add_res.get(timeout=1.0) if add_res.state == 'SUCCESS' else '...',
        'mul_res': mul_res.get(timeout=1.0) if mul_res.state == 'SUCCESS' else '...',
        'xsum_res': xsum_res.get(timeout=1.0) if xsum_res.state == 'SUCCESS' else '...'
    }
    return json.dumps(result)


@app.route('/test_task_add_result/<task_id>/')
def test_task_add_result(task_id):
    """
    后台任务测试结果
    http://localhost:8000/test_task_add_result/xxxxxx/
    """
    from app_frontend.tasks import add, mul, xsum
    result = add.AsyncResult(task_id).get(timeout=1.0)
    return repr(result)


@app.route('/test_task_mul_result/<task_id>/')
def test_task_mul_result(task_id):
    """
    后台任务测试结果
    http://localhost:8000/test_task_mul_result/xxxxxx/
    """
    from app_frontend.tasks import add, mul, xsum
    result = mul.AsyncResult(task_id).get(timeout=1.0)
    return repr(result)


@app.route('/test_task_xsum_result/<task_id>/')
def test_task_xsum_result(task_id):
    """
    后台任务测试结果
    http://localhost:8000/test_task_xsum_result/xxxxxx/
    """
    from app_frontend.tasks import add, mul, xsum
    result = xsum.AsyncResult(task_id).get(timeout=1.0)
    return repr(result)


@app.route("/test_exception")
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


@app.route('/file/save')
def save():
    """
    保存文件到七牛
    """
    data = 'data to save'
    filename = 'filename'
    ret, info = qi_niu_client.save(data, filename)
    return str(ret)


@app.route('/file/delete')
def delete():
    """
    删除七牛空间中的文件
    """
    filename = 'filename'
    ret, info = qi_niu_client.delete(filename)
    return str(ret)


@app.route('/file/url')
def url():
    """
    根据文件名获取对应的公开URL
    """
    filename = 'filename'
    return qi_niu_client.url(filename)


@app.route("/email/")
def send_email():
    """
    邮件发送
    """
    try:
        from app_frontend.emails import send_email
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
