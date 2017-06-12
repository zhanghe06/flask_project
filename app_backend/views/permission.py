#!/usr/bin/env python
# encoding: utf-8

"""
@author: zhanghe
@software: PyCharm
@file: permission.py
@time: 2017/6/12 下午8:29
"""


from datetime import datetime
import json

from flask import abort
from flask import redirect
from flask import render_template, request, flash, g
from flask import url_for
from flask_login import current_user, login_required

from app_backend import app
from app_backend.api.apply_get import get_apply_get_rows, get_apply_get_rows_by_ids, edit_apply_get

from app_backend.forms.admin import AdminProfileForm
from app_backend.forms.apply_get import ApplyGetSearchForm
from app_backend.models import User, ApplyGet, UserProfile, ApplyPut
from app_backend.api.apply_put import get_apply_put_rows, get_apply_put_row, get_apply_put_row_by_id, edit_apply_put, apply_put_match, \
    apply_put_stats
from app_backend.api.order import get_order_row, get_order_rows, get_order_lists, add_order, get_put_match_order_rows
from app_backend.forms.apply_put import ApplyPutSearchForm

from app_common.maps.status_delete import *
from app_common.maps.status_order import *
from app_common.maps.status_pay import *
from app_common.maps.status_rec import *
from app_common.maps.status_audit import *
from app_common.tools.date_time import time_local_to_utc

PER_PAGE_BACKEND = app.config['PER_PAGE_BACKEND']

from flask import Blueprint


bp_apply_put = Blueprint('apply_put', __name__, url_prefix='/apply_put')


@bp_apply_put.route('/list/')
@bp_apply_put.route('/list/<int:page>/')
@login_required
def lists(page=1):
    pass
