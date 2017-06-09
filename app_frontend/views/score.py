#!/usr/bin/env python
# encoding: utf-8

"""
@author: zhanghe
@software: PyCharm
@file: score.py
@time: 2017/4/25 下午1:25
"""


from datetime import datetime
from flask import redirect
from flask import render_template, request, flash, g
from flask import url_for
from flask_login import current_user, login_required

from app_frontend import app
from app_frontend.api.score import get_score_rows

from app_frontend.api.score_charity_item import get_score_charity_item_rows
from app_frontend.api.score_digital_item import get_score_digital_item_rows
from app_frontend.api.score_expense_item import get_score_expense_item_rows

from flask import Blueprint


bp_score = Blueprint('score', __name__, url_prefix='/score')


@bp_score.route('/list/')
@bp_score.route('/list/<int:page>/')
@login_required
def lists(page=1):
    """
    积分列表
    """

    pagination = get_score_rows(page)
    return render_template('score/list.html', title='score_list', pagination=pagination)


@bp_score.route('/add/', methods=['GET', 'POST'])
@login_required
def add():
    """
    创建积分
    :return:
    """
    pass


@bp_score.route('/del/', methods=['GET', 'POST'])
@login_required
def delete():
    """
    删除积分
    :return:
    """
    pass


@bp_score.route('/stats/', methods=['GET', 'POST'])
@login_required
def stats():
    """
    积分统计
    :return:
    """
    pass


@bp_score.route('/charity/list/', methods=['GET', 'POST'])
@bp_score.route('/charity/list/<int:page>/')
@login_required
def charity_lists(page=1):
    """
    慈善积分
    :return:
    """
    condition = {'user_id': current_user.id}

    # 积分类型:（1：获得、2：消费）
    score_type = request.args.get('score_type', 0, type=int)

    if score_type:
        condition['type'] = score_type

    pagination = get_score_charity_item_rows(page, **condition)
    return render_template('score/charity_list.html', title='score_charity_list', pagination=pagination)


@bp_score.route('/digital/list/', methods=['GET', 'POST'])
@bp_score.route('/digital/list/<int:page>/')
@login_required
def digital_lists(page=1):
    """
    数字积分
    :return:
    """
    condition = {'user_id': current_user.id}

    # 积分类型:（1：获得、2：消费）
    score_type = request.args.get('score_type', 0, type=int)

    if score_type:
        condition['type'] = score_type

    pagination = get_score_digital_item_rows(page, **condition)
    return render_template('score/digital_list.html', title='score_digital_list', pagination=pagination)


@bp_score.route('/expense/list/', methods=['GET', 'POST'])
@bp_score.route('/expense/list/<int:page>/')
@login_required
def expense_lists(page=1):
    """
    消费积分
    :return:
    """
    condition = {'user_id': current_user.id}

    # 积分类型:（1：获得、2：消费）
    score_type = request.args.get('score_type', 0, type=int)

    if score_type:
        condition['type'] = score_type

    pagination = get_score_expense_item_rows(page, **condition)
    return render_template('score/expense_list.html', title='score_expense_list', pagination=pagination)
