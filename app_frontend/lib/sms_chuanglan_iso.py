#!/usr/bin/env python
# encoding: utf-8

"""
@author: zhanghe
@software: PyCharm
@file: sms_chuanglan_iso.py.py
@time: 2017/3/3 下午10:03
"""


import requests


from config import current_config

REQUESTS_TIME_OUT = current_config.REQUESTS_TIME_OUT


class SmsChuangLanIsoApi(object):
    """
    创蓝国际短信接口
    """
    ISENDURL = 'http://222.73.117.140:8044/mt'  # 单发接口
    IQUERYURL = 'http://222.73.117.140:8044/bi'  # 查询余额接口
    BAT_SENDURL = 'http://222.73.117.140:8044/batchmt'  # 群发接口

    ERROR_DICT = {
        '0': u'提交成功',
        '101': u'无此用户',
        '102': u'密码错',
        '103': u'提交过快（提交速度超过流速限制）',
        '104': u'系统忙（因平台侧原因，暂时无法处理提交的短信）',
        '105': u'敏感短信（短信内容包含敏感词）',
        '106': u'消息长度错（>536或<=0）',
        '107': u'包含错误的手机号码',
        '108': u'手机号码个数错（群发>50000或<=0）',
        '109': u'无发送额度（该用户可用短信数已使用完）',
        '110': u'不在发送时间内',
        '113': u'extno格式错（非数字或者长度不对）',
        '116': u'签名不合法或未带签名（用户必须带签名的前提下）',
        '117': u'IP地址认证错,请求调用的IP地址不是系统登记的IP地址',
        '118': u'用户没有相应的发送权限（账号被禁止发送）',
        '119': u'用户已过期',
        '120': u'违反放盗用策略(日发限制) --自定义添加',
        '121': u'必填参数。是否需要状态报告，取值true或false',
        '122': u'5分钟内相同账号提交相同消息内容过多',
        '123': u'发送类型错误',
        '124': u'白模板匹配错误',
        '125': u'匹配驳回模板，提交失败',
        '126': u'审核通过模板匹配错误',
    }

    def __init__(self, account, password):
        self._sendUrl = ''  # 发送短信接口url
        self._queryBalanceUrl = ''  # 查询余额接口url
        self._un = account  # 接口账号
        self._pw = password  # 接口密码

    def send_international(self, phone, content, is_report=0):
        """
        发送国际短信
        :param phone:
        :param content:
        :param is_report:
        :return:
        """
        params = {
            'un': self._un,
            'pw': self._pw,
            'sm': content,
            'da': phone,
            'rd': is_report,
            'rf': 2,
            'tf': 3,
        }
        result = requests.get(self.ISENDURL, params, timeout=REQUESTS_TIME_OUT or 30).json()
        return result

    def query_balance_international(self):
        """
        查询余额
        :return:
        """
        params = {
            'un': self._un,
            'pw': self._pw,
            'rf': 2,
        }
        result = requests.get(self.IQUERYURL, params, timeout=REQUESTS_TIME_OUT or 30).json()
        return result


if __name__ == '__main__':
    sms_client = SmsChuangLanIsoApi('接口账号', '接口账号')
    # print sms_client.send_international('8613800000000', '欢迎您注册九重天会员，此次注册验证码为1234，请在2分钟内进入验证。【九重天】', 1)
    print sms_client.query_balance_international()


"""
账号错误：
{u'r': u'101', u'success': False}
密码错误：
{u'r': u'102', u'success': False}
国内号码不加86，收不到短信，但是返回True
{u'id': u'17030322181000000859', u'success': True}
国内号码添加86，收到短信，也返回True
{u'id': u'17030322211000000868', u'success': True}
国内错误号码
"""
