#!/usr/bin/env python
# encoding: utf-8

"""
@author: zhanghe
@software: PyCharm
@file: invite.py
@time: 2017/4/28 上午10:53
"""


from flask import render_template, request, flash, redirect, url_for
from flask_login import current_user, login_required
from itsdangerous import URLSafeSerializer
from app_common.tools import md5
from app_frontend import app
from app_frontend.forms.user import UserProfileForm, UserAuthForm, UserBankForm
from app_frontend.api.user_profile import get_user_profile_row_by_id, edit_user_profile
from app_frontend.api.user_bank import get_user_bank_row_by_id, add_user_bank, edit_user_bank
from app_frontend.api.user_auth import get_user_auth_row_by_id, get_user_auth_row, edit_user_auth
from app_frontend.api.user import edit_user
from app_common.maps.auth_type import *
from datetime import datetime
from flask import Blueprint


bp_invite = Blueprint('invite', __name__, url_prefix='/invite')


@bp_invite.route('/', methods=['GET', 'POST'])
@login_required
def index():
    uid = current_user.id
    s = URLSafeSerializer('')
    s.dumps({'uid': uid})

    return request.args.get('i')

