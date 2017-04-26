#!/usr/bin/env python
# encoding: utf-8

"""
@author: zhanghe
@software: PyCharm
@file: credit.py
@time: 2017/4/23 下午11:47
"""


from flask import render_template, request, flash
from flask_login import current_user, login_required
import json
from app_frontend import app
from app_frontend.forms.user import UserProfileForm
from app_frontend.api.user_profile import get_user_profile_row_by_id, edit_user_profile
from datetime import datetime
from flask import Blueprint, g
from app_frontend.api.credit import get_user_credit_row_by_id
from app_api.tools import json_default


bp_credit = Blueprint('credit', __name__, url_prefix='/credit')


@bp_credit.route('/', methods=['GET', 'POST'])
@login_required
def index():
    return render_template('credit/index.html', title='credit')


@bp_credit.route('/ajax/get_user_data/', methods=['GET', 'POST'])
def ajax_get_user_data():
    """
    获取用户声望信息
    :return:
    """
    login_user_id = current_user.id
    info = get_user_credit_row_by_id(login_user_id)
    if info:
        data = {
            'result': True,
            'values': [
                info.behavior,          # 行为偏好
                info.characteristics,   # 身份特质
                info.connections,       # 人脉关系
                info.history,           # 信用历史
                info.performance        # 履约能力
            ]
        }
        return json.dumps(data, default=json_default)
