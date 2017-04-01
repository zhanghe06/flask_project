#!/usr/bin/env python
# encoding: utf-8

"""
@author: zhanghe
@software: PyCharm
@file: url.py
@time: 16-3-25 下午3:19
"""


from urlparse import urlparse


def secure_url(url, netloc='', default_url='/'):
    """
    获取安全 url
    不带域名的链接，不需指定 netloc 参数
    有域名的链接，需要指定 netloc 为授权的域名（不带协议）
    :param url:
    :param netloc:
    :param default_url:
    :return:
    """
    parse_result = urlparse(url)
    if parse_result.netloc in ['', netloc]:
        return url
    return default_url


def test():
    """
    测试获取安全url
    :return:
    """
    url = '%2Fblog%2Flist%2F'
    print secure_url(url)


if __name__ == '__main__':
    test()
