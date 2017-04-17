#!/usr/bin/env python
# encoding: utf-8

"""
@author: zhanghe
@software: PyCharm
@file: captcha.py
@time: 16-6-10 上午1:01
"""


from flask import Blueprint, request, make_response, session, abort
import StringIO
import json
from app_frontend.lib.captcha import Captcha
from app_frontend import app


bp_captcha = Blueprint('captcha', __name__, url_prefix='/captcha')

params = {
    'size': (68, 34),
    'fg_color': (180, 180, 180),
    'line_color': (100, 100, 100),
    'point_color': (100, 100, 100)
}
# captcha_client = Captcha(**params)


@bp_captcha.route('/get_code/<code_type>/')
def get_code(code_type):
    """
    http://localhost:8000/captcha/get_code/reg/?t=1234
    """
    if code_type not in app.config['CAPTCHA_ENTITY']:
        abort(404)
    code_img, code_str = Captcha(**params).get()
    # 保存 code_str
    code_key = '%s:%s' % ('code_str', code_type)
    session[code_key] = code_str
    # 返回验证码图片
    buf = StringIO.StringIO()
    code_img.save(buf, 'JPEG', quality=70)
    buf_str = buf.getvalue()
    response = make_response(buf_str)
    response.headers['Content-Type'] = 'image/jpeg'
    code_img.close()
    buf.close()
    return response


@bp_captcha.route('/check_code/<code_type>/')
def check_code(code_type):
    """
    校验验证码
    http://localhost:8000/captcha/check_code/reg/?code_str=7E6G
    """
    if code_type not in app.config['CAPTCHA_ENTITY']:
        abort(404)
    code_str = request.args.get('code_str', '', type=str)
    code_key = '%s:%s' % ('code_str', code_type)
    return json.dumps({'result': code_str.upper() == session[code_key].upper()})

