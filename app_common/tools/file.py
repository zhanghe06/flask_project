#!/usr/bin/env python
# encoding: utf-8

"""
@author: zhanghe
@software: PyCharm
@file: file.py
@time: 2017/5/11 下午9:36
"""


from datetime import datetime
from app_frontend import app


def allowed_file(filename):
    """
    校验文件类型
    """
    return '.' in filename and filename.rsplit('.', 1)[1] in app.config['ALLOWED_EXTENSIONS']


def get_extend_type(filename):
    """
    获取文件扩展
    :param filename:
    :return:
    """
    if allowed_file(filename):
        return filename.rsplit('.', 1)[1]
    else:
        return ''


def get_file_size(file_obj):
    """
    获取文件大小
    :param file_obj:
    :return:
    """
    file_obj.seek(0, 2)  # Seek to the end of the file
    size = file_obj.tell()  # Get the position of EOF
    file_obj.seek(0)  # Reset the file position to the beginning
    return size


def create_file_name(file_obj):
    """
    创建文件名称
    :param file_obj:
    :return:
    """
    # from werkzeug.utils import secure_filename
    # file_name = secure_filename(file_obj.filename)
    extend_type = get_extend_type(file_obj.filename)
    file_name = datetime.utcnow().strftime('%Y%m%d%H%M%S%f')
    return '%s.%s' % (file_name, extend_type) if extend_type else file_obj.filename


def validate(file_obj):
    """
    文件尺寸校验
    :param file_obj:
    :return:
    """
    if not allowed_file(file_obj.filename):
        raise Exception(u'文件类型暂不支持')
    file_size = get_file_size(file_obj)
    if file_size < app.config['MIN_CONTENT_LENGTH']:
        raise Exception(u'文件太小，未到最低要求')
    elif file_size > app.config['MAX_CONTENT_LENGTH']:
        raise Exception(u'文件太大，超过最大限制')
    else:
        return True
