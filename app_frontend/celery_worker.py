#!/usr/bin/env python
# encoding: utf-8

"""
@author: zhanghe
@software: PyCharm
@file: celery_worker.py
@time: 2016/11/17 下午2:51
"""

from application import app
from celery import Celery


def make_celery(application):
    celery = Celery(application.import_name,
                    broker=application.config['CELERY_BROKER_URL'],
                    backend=application.config['CELERY_RESULT_BACKEND']
                    )
    # celery.conf.update(application.config)
    TaskBase = celery.Task

    class ContextTask(TaskBase):
        abstract = True

        def __call__(self, *args, **kwargs):
            with application.app_context():
                return TaskBase.__call__(self, *args, **kwargs)

    celery.Task = ContextTask
    return celery


celery_app = make_celery(app)
