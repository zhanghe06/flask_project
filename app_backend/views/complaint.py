#!/usr/bin/env python
# encoding: utf-8

"""
@author: zhanghe
@software: PyCharm
@file: complaint.py
@time: 2017/4/30 下午10:31
"""


from datetime import datetime
from flask import redirect
from flask import render_template, request, flash, g
from flask import url_for
from flask_login import current_user, login_required
import flask_excel as excel

from app_backend import app
from app_backend.forms.admin import AdminProfileForm
from app_backend.models import User, UserProfile
from app_backend.api.order import get_order_rows, get_order_row
from app_backend.forms.order import OrderSearchForm

from flask import Blueprint


bp_complaint = Blueprint('complaint', __name__, url_prefix='/complaint')


@bp_complaint.route('/list/', methods=['GET', 'POST'])
@login_required
def lists():
    """
    投诉列表
    :return:
    """
    return render_template('complaint/list.html', title='complaint_list')
