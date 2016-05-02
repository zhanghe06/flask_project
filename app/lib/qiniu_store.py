#!/usr/bin/env python
# encoding: utf-8

"""
@author: zhanghe
@software: PyCharm
@file: qiniu.py
@time: 16-5-2 下午1:41
"""


from urlparse import urljoin
import qiniu


class QiNiuClient(object):
    """
    七牛云存储
    """
    def __init__(self, app=None):
        """
        初始化应用
        """
        if app is not None:
            self._access_key = app.config.get('QINIU_ACCESS_KEY', '')
            self._secret_key = app.config.get('QINIU_SECRET_KEY', '')
            self._bucket_name = app.config.get('QINIU_BUCKET_NAME', '')
            domain = app.config.get('QINIU_BUCKET_DOMAIN')
            if not domain:
                self._base_url = 'http://' + self._bucket_name + '.qiniudn.com'
            else:
                self._base_url = 'http://' + domain

    def save(self, data, filename=None):
        """
        保存
        """
        auth = qiniu.Auth(self._access_key, self._secret_key)
        token = auth.upload_token(self._bucket_name)
        return qiniu.put_data(token, filename, data)

    def delete(self, filename):
        """
        删除
        """
        auth = qiniu.Auth(self._access_key, self._secret_key)
        bucket = qiniu.BucketManager(auth)
        return bucket.delete(self._bucket_name, filename)

    def url(self, filename):
        """
        链接
        """
        return urljoin(self._base_url, filename)


if __name__ == '__main__':
    pass
