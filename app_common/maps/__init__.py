#!/usr/bin/env python
# encoding: utf-8

"""
@author: zhanghe
@software: PyCharm
@file: __init__.py.py
@time: 2017/4/14 上午1:52
"""


# 激活状态（0未激活，1已激活）
status_active_list = [('', u'全部'), (0, u'未激活'), (1, u'已激活')]

# 锁定状态（0未锁定，1已锁定）
status_lock_list = [('', u'全部'), (0, u'正常'), (1, u'锁定')]

# 删除状态（0未删除，1已删除）
status_delete_list = [('', u'全部'), (0, u'正常'), (1, u'删除')]

# 认证状态（0未认证，1已认证）
status_verified_list = [('', u'全部'), (0, u'未认证'), (1, u'已认证')]

# 申请状态:0:待生效，1:已生效，2:取消
status_apply_list = [('', u'全部'), (0, u'待生效'), (1, u'已生效'), (2, u'取消')]

# 订单状态:0:待匹配，1:部分匹配，2:完全匹配
status_order_list = [('', u'全部'), (0, u'待匹配'), (1, u'部分匹配'), (2, u'完全匹配')]

# 支付状态:0:待支付，1:支付成功，2:支付失败
status_pay_list = [('', u'全部'), (0, u'待支付'), (1, u'支付成功'), (2, u'支付失败')]

# 收款状态:0:待收款，1:收款成功，2:收款失败
status_rec_list = [('', u'全部'), (0, u'待收款'), (1, u'收款成功'), (2, u'收款失败')]

# 审核状态:0:待审核，1:审核通过，2:审核失败
status_audit_list = [('', u'全部'), (0, u'待审核'), (1, u'审核通过'), (2, u'审核失败')]

# 认证类型（0账号，1邮箱，2手机，3qq，4微信，5微博）
type_auth_list = [('', u'全部'), (0, u'未知'), (1, u'邮箱'), (2, u'手机'), (3, u'QQ'), (4, u'微信'), (5, u'微博')]

# 申请类型:0:自主添加，1:系统生成
type_apply_list = [('', u'全部'), (0, u'自主添加'), (1, u'系统生成')]

# 支付/收款方式:0:不限，1:银行转账，2:数字货币，3:支付宝，4:微信
type_pay_list = [('', u'全部'), (0, u'不限'), (1, u'银行转账'), (2, u'数字货币'), (3, u'支付宝'), (4, u'微信')]

# 提现类型:0:钱包余额，1:数字货币
type_withdraw_list = [('', u'全部'), (0, u'钱包余额'), (1, u'数字货币')]

# 钱包类型（1：收、2：支）

# 钱包明细状态:0:待生效，1:已生效，2:作废

# 积分类型（1：加、2：减）

# 管理角色:0:普通，1:高级，2:系统
role_admin_list = [('', u'全部'), (0, u'普通'), (1, u'高级'), (2, u'系统')]

# 区号代码
area_code_list = [
    {
        u'亚洲': [
            {
                "phone_pre": "+0086",
                "short_code": "CN",
                "area_code": 86,
                "name_c": u"中国",
                "name_e": "China",
                "country_area": u"亚洲",
                "id": 0
            },
            {
                "phone_pre": "+00852",
                "short_code": "HK",
                "area_code": 852,
                "name_c": u"中国香港",
                "name_e": "Hongkong",
                "country_area": u"亚洲",
                "id": 1
            },
            {
                "phone_pre": "+00853",
                "short_code": "MO",
                "area_code": 853,
                "name_c": u"中国澳门",
                "name_e": "Macao",
                "country_area": u"亚洲",
                "id": 2
            },
            {
                "phone_pre": "+00886",
                "short_code": "TW",
                "area_code": 886,
                "name_c": u"中国台湾",
                "name_e": "Taiwan",
                "country_area": u"亚洲",
                "id": 3
            },
            {
                "phone_pre": "+0060",
                "short_code": "MY",
                "area_code": 60,
                "name_c": u"马来西亚",
                "name_e": "Malaysia",
                "country_area": u"亚洲",
                "id": 4
            },
            {
                "phone_pre": "+0065",
                "short_code": "SG",
                "area_code": 65,
                "name_c": u"新加坡",
                "name_e": "Singapore",
                "country_area": u"亚洲",
                "id": 5
            },
            {
                "phone_pre": "+0062",
                "short_code": "ID",
                "area_code": 62,
                "name_c": u"印度尼西亚",
                "name_e": "Indonesia",
                "country_area": u"亚洲",
                "id": 6
            },
            {
                "phone_pre": "+0063",
                "short_code": "PH",
                "area_code": 63,
                "name_c": u"菲律宾",
                "name_e": "Philippines",
                "country_area": u"亚洲",
                "id": 7
            },
            {
                "phone_pre": "+0066",
                "short_code": "TH",
                "area_code": 66,
                "name_c": u"泰国",
                "name_e": "Thailand",
                "country_area": u"亚洲",
                "id": 8
            },
            {
                "phone_pre": "+0073",
                "short_code": "KZ",
                "area_code": 73,
                "name_c": u"哈萨克斯坦",
                "name_e": "Kazakhstan",
                "country_area": u"亚洲",
                "id": 9
            },
            {
                "phone_pre": "+0081",
                "short_code": "JP",
                "area_code": 81,
                "name_c": u"日本",
                "name_e": "Japan",
                "country_area": u"亚洲",
                "id": 10
            },
            {
                "phone_pre": "+0082",
                "short_code": "KR",
                "area_code": 82,
                "name_c": u"韩国",
                "name_e": "Korea",
                "country_area": u"亚洲",
                "id": 11
            },
            {
                "phone_pre": "+0084",
                "short_code": "VN",
                "area_code": 84,
                "name_c": u"越南",
                "name_e": "Vietnam",
                "country_area": u"亚洲",
                "id": 12
            },
            {
                "phone_pre": "+0090",
                "short_code": "TR",
                "area_code": 90,
                "name_c": u"土耳其",
                "name_e": "Turkey",
                "country_area": u"亚洲",
                "id": 13
            },
            {
                "phone_pre": "+0091",
                "short_code": "IN",
                "area_code": 91,
                "name_c": u"印度",
                "name_e": "India",
                "country_area": u"亚洲",
                "id": 14
            },
            {
                "phone_pre": "+0092",
                "short_code": "PK",
                "area_code": 92,
                "name_c": u"巴基斯坦",
                "name_e": "Pakistan",
                "country_area": u"亚洲",
                "id": 15
            },
            {
                "phone_pre": "+0093",
                "short_code": "AF",
                "area_code": 93,
                "name_c": u"阿富汗",
                "name_e": "Afghanistan",
                "country_area": u"亚洲",
                "id": 16
            },
            {
                "phone_pre": "+0094",
                "short_code": "LK",
                "area_code": 94,
                "name_c": u"斯里兰卡",
                "name_e": "Sri Lanka",
                "country_area": u"亚洲",
                "id": 17
            },
            {
                "phone_pre": "+0095",
                "short_code": "MM",
                "area_code": 95,
                "name_c": u"缅甸",
                "name_e": "Burma",
                "country_area": u"亚洲",
                "id": 18
            },
            {
                "phone_pre": "+0098",
                "short_code": "IR",
                "area_code": 98,
                "name_c": u"伊朗",
                "name_e": "Iran",
                "country_area": u"亚洲",
                "id": 19
            },
            {
                "phone_pre": "+00374",
                "short_code": "AM",
                "area_code": 374,
                "name_c": u"亚美尼亚",
                "name_e": "Armenia",
                "country_area": u"亚洲",
                "id": 20
            },
            {
                "phone_pre": "+00673",
                "short_code": "BN",
                "area_code": 673,
                "name_c": u"文莱",
                "name_e": "Brunei",
                "country_area": u"亚洲",
                "id": 21
            },
            {
                "phone_pre": "+00855",
                "short_code": "KH",
                "area_code": 855,
                "name_c": u"柬埔寨",
                "name_e": "Cambodia",
                "country_area": u"亚洲",
                "id": 22
            },
            {
                "phone_pre": "+00856",
                "short_code": "LA",
                "area_code": 856,
                "name_c": u"老挝",
                "name_e": "Laos",
                "country_area": u"亚洲",
                "id": 23
            },
            {
                "phone_pre": "+00880",
                "short_code": "BD",
                "area_code": 880,
                "name_c": u"孟加拉国",
                "name_e": "Bangladesh",
                "country_area": u"亚洲",
                "id": 24
            },
            {
                "phone_pre": "+00960",
                "short_code": "MV",
                "area_code": 960,
                "name_c": u"马尔代夫",
                "name_e": "Maldives",
                "country_area": u"亚洲",
                "id": 25
            },
            {
                "phone_pre": "+00961",
                "short_code": "LB",
                "area_code": 961,
                "name_c": u"黎巴嫩",
                "name_e": "Lebanon",
                "country_area": u"亚洲",
                "id": 26
            },
            {
                "phone_pre": "+00962",
                "short_code": "JO",
                "area_code": 962,
                "name_c": u"约旦",
                "name_e": "Jordan",
                "country_area": u"亚洲",
                "id": 27
            },
            {
                "phone_pre": "+00963",
                "short_code": "SY",
                "area_code": 963,
                "name_c": u"叙利亚",
                "name_e": "Syria",
                "country_area": u"亚洲",
                "id": 28
            },
            {
                "phone_pre": "+00964",
                "short_code": "IQ",
                "area_code": 964,
                "name_c": u"伊拉克",
                "name_e": "Iraq",
                "country_area": u"亚洲",
                "id": 29
            },
            {
                "phone_pre": "+00965",
                "short_code": "KW",
                "area_code": 965,
                "name_c": u"科威特",
                "name_e": "Kuwait",
                "country_area": u"亚洲",
                "id": 30
            },
            {
                "phone_pre": "+00966",
                "short_code": "SA",
                "area_code": 966,
                "name_c": u"沙特阿拉伯",
                "name_e": "Saudi Arabia",
                "country_area": u"亚洲",
                "id": 31
            },
            {
                "phone_pre": "+00967",
                "short_code": "YE",
                "area_code": 967,
                "name_c": u"也门",
                "name_e": "Yemen",
                "country_area": u"亚洲",
                "id": 32
            },
            {
                "phone_pre": "+00968",
                "short_code": "OM",
                "area_code": 968,
                "name_c": u"阿曼",
                "name_e": "Oman",
                "country_area": u"亚洲",
                "id": 33
            },
            {
                "phone_pre": "+00971",
                "short_code": "AE",
                "area_code": 971,
                "name_c": u"阿拉伯联合酋长国",
                "name_e": "Arab Emirates",
                "country_area": u"亚洲",
                "id": 34
            },
            {
                "phone_pre": "+00972",
                "short_code": "IL",
                "area_code": 972,
                "name_c": u"以色列",
                "name_e": "Israel",
                "country_area": u"亚洲",
                "id": 35
            },
            {
                "phone_pre": "+00973",
                "short_code": "BH",
                "area_code": 973,
                "name_c": u"巴林",
                "name_e": "Bahrain",
                "country_area": u"亚洲",
                "id": 36
            },
            {
                "phone_pre": "+00974",
                "short_code": "QA",
                "area_code": 974,
                "name_c": u"卡塔尔",
                "name_e": "Qatar",
                "country_area": u"亚洲",
                "id": 37
            },
            {
                "phone_pre": "+00976",
                "short_code": "MN",
                "area_code": 976,
                "name_c": u"蒙古",
                "name_e": "Mongolia",
                "country_area": u"亚洲",
                "id": 38
            },
            {
                "phone_pre": "+00977",
                "short_code": "NP",
                "area_code": 977,
                "name_c": u"尼泊尔",
                "name_e": "Nepal",
                "country_area": u"亚洲",
                "id": 39
            },
            {
                "phone_pre": "+00992",
                "short_code": "TJ",
                "area_code": 992,
                "name_c": u"塔吉克斯坦",
                "name_e": "Tajikistan",
                "country_area": u"亚洲",
                "id": 40
            },
            {
                "phone_pre": "+00993",
                "short_code": "TM",
                "area_code": 993,
                "name_c": u"土库曼斯坦",
                "name_e": "Turkmenistan",
                "country_area": u"亚洲",
                "id": 41
            },
            {
                "phone_pre": "+00994",
                "short_code": "AZ",
                "area_code": 994,
                "name_c": u"阿塞拜疆",
                "name_e": "Azerbaijan",
                "country_area": u"亚洲",
                "id": 42
            },
            {
                "phone_pre": "+00995",
                "short_code": "GE",
                "area_code": 995,
                "name_c": u"格鲁吉亚",
                "name_e": "Georgia",
                "country_area": u"亚洲",
                "id": 43
            },
            {
                "phone_pre": "+00996",
                "short_code": "KG",
                "area_code": 996,
                "name_c": u"吉尔吉斯斯坦",
                "name_e": "Kyrgyzstan",
                "country_area": u"亚洲",
                "id": 44
            },
            {
                "phone_pre": "+00998",
                "short_code": "UZ",
                "area_code": 998,
                "name_c": u"乌兹别克斯坦",
                "name_e": "Uzbekistan",
                "country_area": u"亚洲",
                "id": 45
            },
        ]},
    {
        u'欧洲': [
            {
                "phone_pre": "+0044",
                "short_code": "GB",
                "area_code": 44,
                "name_c": u"英国",
                "name_e": "United Kiongdom",
                "country_area": u"欧洲",
                "id": 47
            },
            {
                "phone_pre": "+0049",
                "short_code": "DE",
                "area_code": 49,
                "name_c": u"德国",
                "name_e": "Germany",
                "country_area": u"欧洲",
                "id": 48
            },
            {
                "phone_pre": "+007",
                "short_code": "RU",
                "area_code": 7,
                "name_c": u"俄罗斯",
                "name_e": "Russia",
                "country_area": u"欧洲",
                "id": 49
            },
            {
                "phone_pre": "+0030",
                "short_code": "GR",
                "area_code": 30,
                "name_c": u"希腊",
                "name_e": "Greece",
                "country_area": u"欧洲",
                "id": 50
            },
            {
                "phone_pre": "+0031",
                "short_code": "NL",
                "area_code": 31,
                "name_c": u"荷兰",
                "name_e": "Netherlands",
                "country_area": u"欧洲",
                "id": 51
            },
            {
                "phone_pre": "+0032",
                "short_code": "BE",
                "area_code": 32,
                "name_c": u"比利时",
                "name_e": "Belgium",
                "country_area": u"欧洲",
                "id": 52
            },
            {
                "phone_pre": "+0033",
                "short_code": "FR",
                "area_code": 33,
                "name_c": u"法国",
                "name_e": "France",
                "country_area": u"欧洲",
                "id": 53
            },
            {
                "phone_pre": "+0034",
                "short_code": "ES",
                "area_code": 34,
                "name_c": u"西班牙",
                "name_e": "Spain",
                "country_area": u"欧洲",
                "id": 54
            },
            {
                "phone_pre": "+0036",
                "short_code": "HU",
                "area_code": 36,
                "name_c": u"匈牙利",
                "name_e": "Hungary",
                "country_area": u"欧洲",
                "id": 55
            },
            {
                "phone_pre": "+0039",
                "short_code": "IT",
                "area_code": 39,
                "name_c": u"意大利",
                "name_e": "Italy",
                "country_area": u"欧洲",
                "id": 56
            },
            {
                "phone_pre": "+0040",
                "short_code": "RO",
                "area_code": 40,
                "name_c": u"罗马尼亚",
                "name_e": "Romania",
                "country_area": u"欧洲",
                "id": 57
            },
            {
                "phone_pre": "+0041",
                "short_code": "CH",
                "area_code": 41,
                "name_c": u"瑞士",
                "name_e": "Switzerland",
                "country_area": u"欧洲",
                "id": 58
            },
            {
                "phone_pre": "+0043",
                "short_code": "AT",
                "area_code": 43,
                "name_c": u"奥地利",
                "name_e": "Austria",
                "country_area": u"欧洲",
                "id": 59
            },
            {
                "phone_pre": "+0045",
                "short_code": "DK",
                "area_code": 45,
                "name_c": u"丹麦",
                "name_e": "Denmark",
                "country_area": u"欧洲",
                "id": 60
            },
            {
                "phone_pre": "+0046",
                "short_code": "SE",
                "area_code": 46,
                "name_c": u"瑞典",
                "name_e": "Sweden",
                "country_area": u"欧洲",
                "id": 61
            },
            {
                "phone_pre": "+0047",
                "short_code": "NO",
                "area_code": 47,
                "name_c": u"挪威",
                "name_e": "Norway",
                "country_area": u"欧洲",
                "id": 62
            },
            {
                "phone_pre": "+0048",
                "short_code": "PL",
                "area_code": 48,
                "name_c": u"波兰",
                "name_e": "Poland",
                "country_area": u"欧洲",
                "id": 63
            },
            {
                "phone_pre": "+00350",
                "short_code": "GI",
                "area_code": 350,
                "name_c": u"直布罗陀",
                "name_e": "Gibraltar",
                "country_area": u"欧洲",
                "id": 64
            },
            {
                "phone_pre": "+00351",
                "short_code": "PT",
                "area_code": 351,
                "name_c": u"葡萄牙",
                "name_e": "Portugal",
                "country_area": u"欧洲",
                "id": 65
            },
            {
                "phone_pre": "+00352",
                "short_code": "LU",
                "area_code": 352,
                "name_c": u"卢森堡",
                "name_e": "Luxembourg",
                "country_area": u"欧洲",
                "id": 66
            },
            {
                "phone_pre": "+00353",
                "short_code": "IE",
                "area_code": 353,
                "name_c": u"爱尔兰",
                "name_e": "Ireland",
                "country_area": u"欧洲",
                "id": 67
            },
            {
                "phone_pre": "+00354",
                "short_code": "IS",
                "area_code": 354,
                "name_c": u"冰岛",
                "name_e": "Iceland",
                "country_area": u"欧洲",
                "id": 68
            },
            {
                "phone_pre": "+00355",
                "short_code": "AL",
                "area_code": 355,
                "name_c": u"阿尔巴尼亚",
                "name_e": "Albania",
                "country_area": u"欧洲",
                "id": 69
            },
            {
                "phone_pre": "+00356",
                "short_code": "MT",
                "area_code": 356,
                "name_c": u"马耳他",
                "name_e": "Malta",
                "country_area": u"欧洲",
                "id": 70
            },
            {
                "phone_pre": "+00357",
                "short_code": "CY",
                "area_code": 357,
                "name_c": u"塞浦路斯",
                "name_e": "Cyprus",
                "country_area": u"欧洲",
                "id": 71
            },
            {
                "phone_pre": "+00358",
                "short_code": "FI",
                "area_code": 358,
                "name_c": u"芬兰",
                "name_e": "Finland",
                "country_area": u"欧洲",
                "id": 72
            },
            {
                "phone_pre": "+00359",
                "short_code": "BG",
                "area_code": 359,
                "name_c": u"保加利亚",
                "name_e": "Bulgaria",
                "country_area": u"欧洲",
                "id": 73
            },
            {
                "phone_pre": "+00370",
                "short_code": "LT",
                "area_code": 370,
                "name_c": u"立陶宛",
                "name_e": "Lithuania",
                "country_area": u"欧洲",
                "id": 74
            },
            {
                "phone_pre": "+00371",
                "short_code": "LV",
                "area_code": 371,
                "name_c": u"拉脱维亚",
                "name_e": "Latvia",
                "country_area": u"欧洲",
                "id": 75
            },
            {
                "phone_pre": "+00372",
                "short_code": "EE",
                "area_code": 372,
                "name_c": u"爱沙尼亚",
                "name_e": "Estonia",
                "country_area": u"欧洲",
                "id": 76
            },
            {
                "phone_pre": "+00373",
                "short_code": "MD",
                "area_code": 373,
                "name_c": u"摩尔多瓦",
                "name_e": "Moldova",
                "country_area": u"欧洲",
                "id": 77
            },
            {
                "phone_pre": "+00375",
                "short_code": "BY",
                "area_code": 375,
                "name_c": u"白俄罗斯",
                "name_e": "Belarus",
                "country_area": u"欧洲",
                "id": 78
            },
            {
                "phone_pre": "+00377",
                "short_code": "MC",
                "area_code": 377,
                "name_c": u"摩纳哥",
                "name_e": "Monaco",
                "country_area": u"欧洲",
                "id": 79
            },
            {
                "phone_pre": "+00378",
                "short_code": "SM",
                "area_code": 378,
                "name_c": u"圣马力诺",
                "name_e": "San Marino",
                "country_area": u"欧洲",
                "id": 80
            },
            {
                "phone_pre": "+00380",
                "short_code": "UA",
                "area_code": 380,
                "name_c": u"乌克兰",
                "name_e": "Ukraine",
                "country_area": u"欧洲",
                "id": 81
            },
            {
                "phone_pre": "+00386",
                "short_code": "SI",
                "area_code": 386,
                "name_c": u"斯洛文尼亚",
                "name_e": "Slovenia",
                "country_area": u"欧洲",
                "id": 82
            },
            {
                "phone_pre": "+00420",
                "short_code": "CZ",
                "area_code": 420,
                "name_c": u"捷克",
                "name_e": "Czech",
                "country_area": u"欧洲",
                "id": 83
            },
            {
                "phone_pre": "+00421",
                "short_code": "SK",
                "area_code": 421,
                "name_c": u"斯洛伐克",
                "name_e": "Slovak",
                "country_area": u"欧洲",
                "id": 84
            },
            {
                "phone_pre": "+00423",
                "short_code": "LI",
                "area_code": 423,
                "name_c": u"列支敦士登",
                "name_e": "Liechtenstein",
                "country_area": u"欧洲",
                "id": 85
            },
        ]
    },
    {
        u'南美洲': [
            {
                "phone_pre": "+0051",
                "short_code": "PE",
                "area_code": 51,
                "name_c": u"秘鲁",
                "name_e": "Peru",
                "country_area": u"南美洲",
                "id": 86
            },
            {
                "phone_pre": "+0052",
                "short_code": "MX",
                "area_code": 52,
                "name_c": u"墨西哥",
                "name_e": "Mexico",
                "country_area": u"南美洲",
                "id": 87
            },
            {
                "phone_pre": "+0053",
                "short_code": "CU",
                "area_code": 53,
                "name_c": u"古巴",
                "name_e": "Cuba",
                "country_area": u"南美洲",
                "id": 88
            },
            {
                "phone_pre": "+0054",
                "short_code": "AR",
                "area_code": 54,
                "name_c": u"阿根廷",
                "name_e": "Argentina",
                "country_area": u"南美洲",
                "id": 89
            },
            {
                "phone_pre": "+0055",
                "short_code": "BR",
                "area_code": 55,
                "name_c": u"巴西",
                "name_e": "Brazil",
                "country_area": u"南美洲",
                "id": 90
            },
            {
                "phone_pre": "+0056",
                "short_code": "CL",
                "area_code": 56,
                "name_c": u"智利",
                "name_e": "Chile",
                "country_area": u"南美洲",
                "id": 91
            },
            {
                "phone_pre": "+0057",
                "short_code": "CO",
                "area_code": 57,
                "name_c": u"哥伦比亚",
                "name_e": "Colombia",
                "country_area": u"南美洲",
                "id": 92
            },
            {
                "phone_pre": "+0058",
                "short_code": "VE",
                "area_code": 58,
                "name_c": u"委内瑞拉",
                "name_e": "Venezuela",
                "country_area": u"南美洲",
                "id": 93
            },
            {
                "phone_pre": "+00501",
                "short_code": "BZ",
                "area_code": 501,
                "name_c": u"伯利兹",
                "name_e": "Belize",
                "country_area": u"南美洲",
                "id": 94
            },
            {
                "phone_pre": "+00503",
                "short_code": "SV",
                "area_code": 503,
                "name_c": u"萨尔瓦多",
                "name_e": "EI Salvador",
                "country_area": u"南美洲",
                "id": 95
            },
            {
                "phone_pre": "+00504",
                "short_code": "HN",
                "area_code": 504,
                "name_c": u"洪都拉斯",
                "name_e": "Honduras",
                "country_area": u"南美洲",
                "id": 96
            },
            {
                "phone_pre": "+00505",
                "short_code": "NI",
                "area_code": 505,
                "name_c": u"尼加拉瓜",
                "name_e": "Nicaragua",
                "country_area": u"南美洲",
                "id": 97
            },
            {
                "phone_pre": "+00506",
                "short_code": "CR",
                "area_code": 506,
                "name_c": u"哥斯达黎加",
                "name_e": "Costa Rica",
                "country_area": u"南美洲",
                "id": 98
            },
            {
                "phone_pre": "+00507",
                "short_code": "PA",
                "area_code": 507,
                "name_c": u"巴拿马",
                "name_e": "Panama",
                "country_area": u"南美洲",
                "id": 99
            },
            {
                "phone_pre": "+00509",
                "short_code": "HT",
                "area_code": 509,
                "name_c": u"海地",
                "name_e": "Haiti",
                "country_area": u"南美洲",
                "id": 100
            },
            {
                "phone_pre": "+00591",
                "short_code": "BO",
                "area_code": 591,
                "name_c": u"玻利维亚",
                "name_e": "Bolivia",
                "country_area": u"南美洲",
                "id": 101
            },
            {
                "phone_pre": "+00592",
                "short_code": "GY",
                "area_code": 592,
                "name_c": u"圭亚那",
                "name_e": "Guyana",
                "country_area": u"南美洲",
                "id": 102
            },
            {
                "phone_pre": "+00593",
                "short_code": "EC",
                "area_code": 593,
                "name_c": u"厄瓜多尔",
                "name_e": "Ecuador",
                "country_area": u"南美洲",
                "id": 103
            },
            {
                "phone_pre": "+00594",
                "short_code": "GF",
                "area_code": 594,
                "name_c": u"法属圭亚那",
                "name_e": "French Guiana",
                "country_area": u"南美洲",
                "id": 104
            },
            {
                "phone_pre": "+00595",
                "short_code": "PY",
                "area_code": 595,
                "name_c": u"巴拉圭",
                "name_e": "Paraguay",
                "country_area": u"南美洲",
                "id": 105
            },
            {
                "phone_pre": "+00596",
                "short_code": "MQ",
                "area_code": 596,
                "name_c": u"马提尼克",
                "name_e": "Martinique",
                "country_area": u"南美洲",
                "id": 106
            },
            {
                "phone_pre": "+00597",
                "short_code": "SR",
                "area_code": 597,
                "name_c": u"苏里南",
                "name_e": "Suriname",
                "country_area": u"南美洲",
                "id": 107
            },
            {
                "phone_pre": "+00598",
                "short_code": "UY",
                "area_code": 598,
                "name_c": u"乌拉圭",
                "name_e": "Uruguay",
                "country_area": u"南美洲",
                "id": 108
            },
        ]
    },
    {
        u'北美洲': [
            {
                "phone_pre": "+001",
                "short_code": "US",
                "area_code": 1,
                "name_c": u"美国",
                "name_e": "America",
                "country_area": u"北美洲",
                "id": 163
            },
            {
                "phone_pre": "+001",
                "short_code": "CA",
                "area_code": 1,
                "name_c": u"加拿大",
                "name_e": "Canada",
                "country_area": u"北美洲",
                "id": 164
            },
            {
                "phone_pre": "+00502",
                "short_code": "GT",
                "area_code": 502,
                "name_c": u"瓜地马拉",
                "name_e": "Guatemala",
                "country_area": u"北美洲",
                "id": 165
            },
            {
                "phone_pre": "+001242",
                "short_code": "BS",
                "area_code": 1242,
                "name_c": u"巴哈马",
                "name_e": "Bahamas",
                "country_area": u"北美洲",
                "id": 166
            },
            {
                "phone_pre": "+001246",
                "short_code": "BB",
                "area_code": 1246,
                "name_c": u"巴巴多斯",
                "name_e": "Barbados",
                "country_area": u"北美洲",
                "id": 167
            },
            {
                "phone_pre": "+001264",
                "short_code": "AI",
                "area_code": 1264,
                "name_c": u"安圭拉岛",
                "name_e": "Anguilla",
                "country_area": u"北美洲",
                "id": 168
            },
            {
                "phone_pre": "+001268",
                "short_code": "AG",
                "area_code": 1268,
                "name_c": u"安提瓜和巴布达",
                "name_e": "Antigua and Barbuda",
                "country_area": u"北美洲",
                "id": 169
            },
            {
                "phone_pre": "+001345",
                "short_code": "KY",
                "area_code": 1345,
                "name_c": u"开曼群岛",
                "name_e": "Cayman Islands",
                "country_area": u"北美洲",
                "id": 170
            },
            {
                "phone_pre": "+001473",
                "short_code": "GD",
                "area_code": 1473,
                "name_c": u"格林纳达",
                "name_e": "Grenada",
                "country_area": u"北美洲",
                "id": 171
            },
            {
                "phone_pre": "+001758",
                "short_code": "LC",
                "area_code": 1758,
                "name_c": u"圣卢西亚",
                "name_e": "Saint Lucia",
                "country_area": u"北美洲",
                "id": 172
            },
            {
                "phone_pre": "+001787",
                "short_code": "PR",
                "area_code": 1787,
                "name_c": u"波多黎各",
                "name_e": "Puerto Rico",
                "country_area": u"北美洲",
                "id": 173
            },
            {
                "phone_pre": "+001809",
                "short_code": "DO",
                "area_code": 1809,
                "name_c": u"多米尼加共和国",
                "name_e": "Dominican",
                "country_area": u"北美洲",
                "id": 174
            },
            {
                "phone_pre": "+001868",
                "short_code": "TT",
                "area_code": 1868,
                "name_c": u"特立尼达和多巴哥",
                "name_e": "Trinidad and Tobago",
                "country_area": u"北美洲",
                "id": 175
            },
            {
                "phone_pre": "+001876",
                "short_code": "JM",
                "area_code": 1876,
                "name_c": u"牙买加",
                "name_e": "Jamaica",
                "country_area": u"北美洲",
                "id": 176
            },
        ]
    },
    {
        u'非洲': [
            {
                "phone_pre": "+0020",
                "short_code": "EG",
                "area_code": 20,
                "name_c": u"埃及",
                "name_e": "Egypt",
                "country_area": u"非洲",
                "id": 109
            },
            {
                "phone_pre": "+0027",
                "short_code": "ZA",
                "area_code": 27,
                "name_c": u"南非",
                "name_e": "South Africa",
                "country_area": u"非洲",
                "id": 110
            },
            {
                "phone_pre": "+00212",
                "short_code": "MA",
                "area_code": 212,
                "name_c": u"摩洛哥",
                "name_e": "Morocco",
                "country_area": u"非洲",
                "id": 111
            },
            {
                "phone_pre": "+00213",
                "short_code": "DZ",
                "area_code": 213,
                "name_c": u"阿尔及利亚",
                "name_e": "Algeria",
                "country_area": u"非洲",
                "id": 112
            },
            {
                "phone_pre": "+00216",
                "short_code": "TN",
                "area_code": 216,
                "name_c": u"突尼斯",
                "name_e": "Tunisia",
                "country_area": u"非洲",
                "id": 113
            },
            {
                "phone_pre": "+00218",
                "short_code": "LY",
                "area_code": 218,
                "name_c": u"利比亚",
                "name_e": "Libya",
                "country_area": u"非洲",
                "id": 114
            },
            {
                "phone_pre": "+00220",
                "short_code": "GM",
                "area_code": 220,
                "name_c": u"冈比亚",
                "name_e": "Gambia",
                "country_area": u"非洲",
                "id": 115
            },
            {
                "phone_pre": "+00221",
                "short_code": "SN",
                "area_code": 221,
                "name_c": u"塞内加尔",
                "name_e": "Senegal",
                "country_area": u"非洲",
                "id": 116
            },
            {
                "phone_pre": "+00223",
                "short_code": "ML",
                "area_code": 223,
                "name_c": u"马里",
                "name_e": "Mali",
                "country_area": u"非洲",
                "id": 117
            },
            {
                "phone_pre": "+00224",
                "short_code": "GN",
                "area_code": 224,
                "name_c": u"几内亚",
                "name_e": "Guinea",
                "country_area": u"非洲",
                "id": 118
            },
            {
                "phone_pre": "+00225",
                "short_code": "CI",
                "area_code": 225,
                "name_c": u"科特迪瓦",
                "name_e": "Ivory Coast",
                "country_area": u"非洲",
                "id": 119
            },
            {
                "phone_pre": "+00226",
                "short_code": "BF",
                "area_code": 226,
                "name_c": u"布基纳法索",
                "name_e": "Burkina Faso",
                "country_area": u"非洲",
                "id": 120
            },
            {
                "phone_pre": "+00227",
                "short_code": "NE",
                "area_code": 227,
                "name_c": u"尼日尔",
                "name_e": "Niger",
                "country_area": u"非洲",
                "id": 121
            },
            {
                "phone_pre": "+00228",
                "short_code": "TG",
                "area_code": 228,
                "name_c": u"多哥",
                "name_e": "Togo",
                "country_area": u"非洲",
                "id": 122
            },
            {
                "phone_pre": "+00229",
                "short_code": "BJ",
                "area_code": 229,
                "name_c": u"贝宁",
                "name_e": "Benin",
                "country_area": u"非洲",
                "id": 123
            },
            {
                "phone_pre": "+00230",
                "short_code": "MU",
                "area_code": 230,
                "name_c": u"毛里求斯",
                "name_e": "Mauritius",
                "country_area": u"非洲",
                "id": 124
            },
            {
                "phone_pre": "+00231",
                "short_code": "LR",
                "area_code": 231,
                "name_c": u"利比里亚",
                "name_e": "Liberia",
                "country_area": u"非洲",
                "id": 125
            },
            {
                "phone_pre": "+00232",
                "short_code": "SL",
                "area_code": 232,
                "name_c": u"塞拉利昂",
                "name_e": "Sierra Leone",
                "country_area": u"非洲",
                "id": 126
            },
            {
                "phone_pre": "+00233",
                "short_code": "GH",
                "area_code": 233,
                "name_c": u"加纳",
                "name_e": "Ghana",
                "country_area": u"非洲",
                "id": 127
            },
            {
                "phone_pre": "+00234",
                "short_code": "NG",
                "area_code": 234,
                "name_c": u"尼日利亚",
                "name_e": "Nigeria",
                "country_area": u"非洲",
                "id": 128
            },
            {
                "phone_pre": "+00235",
                "short_code": "TD",
                "area_code": 235,
                "name_c": u"乍得",
                "name_e": "Chad",
                "country_area": u"非洲",
                "id": 129
            },
            {
                "phone_pre": "+00236",
                "short_code": "CF",
                "area_code": 236,
                "name_c": u"中非共和国",
                "name_e": "Central Africa",
                "country_area": u"非洲",
                "id": 130
            },
            {
                "phone_pre": "+00237",
                "short_code": "CM",
                "area_code": 237,
                "name_c": u"喀麦隆",
                "name_e": "Cameroon",
                "country_area": u"非洲",
                "id": 131
            },
            {
                "phone_pre": "+00239",
                "short_code": "ST",
                "area_code": 239,
                "name_c": u"圣多美和普林西比",
                "name_e": "Sao Tome and Principe",
                "country_area": u"非洲",
                "id": 132
            },
            {
                "phone_pre": "+00241",
                "short_code": "GA",
                "area_code": 241,
                "name_c": u"加蓬",
                "name_e": "Gabon",
                "country_area": u"非洲",
                "id": 133
            },
            {
                "phone_pre": "+00243",
                "short_code": "CG",
                "area_code": 243,
                "name_c": u"刚果民主共和国",
                "name_e": "Congo",
                "country_area": u"非洲",
                "id": 134
            },
            {
                "phone_pre": "+00244",
                "short_code": "AO",
                "area_code": 244,
                "name_c": u"安哥拉",
                "name_e": "Angola",
                "country_area": u"非洲",
                "id": 135
            },
            {
                "phone_pre": "+00248",
                "short_code": "SC",
                "area_code": 248,
                "name_c": u"塞舌尔",
                "name_e": "Seychelles",
                "country_area": u"非洲",
                "id": 136
            },
            {
                "phone_pre": "+00249",
                "short_code": "SD",
                "area_code": 249,
                "name_c": u"苏丹",
                "name_e": "Sudan",
                "country_area": u"非洲",
                "id": 137
            },
            {
                "phone_pre": "+00251",
                "short_code": "ET",
                "area_code": 251,
                "name_c": u"埃塞俄比亚",
                "name_e": "Ethiopia",
                "country_area": u"非洲",
                "id": 138
            },
            {
                "phone_pre": "+00252",
                "short_code": "SO",
                "area_code": 252,
                "name_c": u"索马里",
                "name_e": "Somali",
                "country_area": u"非洲",
                "id": 139
            },
            {
                "phone_pre": "+00253",
                "short_code": "DJ",
                "area_code": 253,
                "name_c": u"吉布提",
                "name_e": "Djibouti",
                "country_area": u"非洲",
                "id": 140
            },
            {
                "phone_pre": "+00254",
                "short_code": "KE",
                "area_code": 254,
                "name_c": u"肯尼亚",
                "name_e": "Kenya",
                "country_area": u"非洲",
                "id": 141
            },
            {
                "phone_pre": "+00255",
                "short_code": "TZ",
                "area_code": 255,
                "name_c": u"坦桑尼亚",
                "name_e": "Tanzania",
                "country_area": u"非洲",
                "id": 142
            },
            {
                "phone_pre": "+00256",
                "short_code": "UG",
                "area_code": 256,
                "name_c": u"乌干达",
                "name_e": "Uganda",
                "country_area": u"非洲",
                "id": 143
            },
            {
                "phone_pre": "+00257",
                "short_code": "BI",
                "area_code": 257,
                "name_c": u"布隆迪",
                "name_e": "Burundi",
                "country_area": u"非洲",
                "id": 144
            },
            {
                "phone_pre": "+00258",
                "short_code": "MZ",
                "area_code": 258,
                "name_c": u"莫桑比克",
                "name_e": "Mozambique",
                "country_area": u"非洲",
                "id": 145
            },
            {
                "phone_pre": "+00260",
                "short_code": "ZM",
                "area_code": 260,
                "name_c": u"赞比亚",
                "name_e": "Zambia",
                "country_area": u"非洲",
                "id": 146
            },
            {
                "phone_pre": "+00261",
                "short_code": "MG",
                "area_code": 261,
                "name_c": u"马达加斯加",
                "name_e": "Madagascar",
                "country_area": u"非洲",
                "id": 147
            },
            {
                "phone_pre": "+00263",
                "short_code": "ZW",
                "area_code": 263,
                "name_c": u"津巴布韦",
                "name_e": "Zimbabwe",
                "country_area": u"非洲",
                "id": 148
            },
            {
                "phone_pre": "+00264",
                "short_code": "NA",
                "area_code": 264,
                "name_c": u"纳米比亚",
                "name_e": "Namibia",
                "country_area": u"非洲",
                "id": 149
            },
            {
                "phone_pre": "+00265",
                "short_code": "MW",
                "area_code": 265,
                "name_c": u"马拉维",
                "name_e": "Malawi",
                "country_area": u"非洲",
                "id": 150
            },
            {
                "phone_pre": "+00266",
                "short_code": "LS",
                "area_code": 266,
                "name_c": u"莱索托",
                "name_e": "Lesotho",
                "country_area": u"非洲",
                "id": 151
            },
            {
                "phone_pre": "+00267",
                "short_code": "BW",
                "area_code": 267,
                "name_c": u"博茨瓦纳",
                "name_e": "Botswana",
                "country_area": u"非洲",
                "id": 152
            },
            {
                "phone_pre": "+00268",
                "short_code": "SZ",
                "area_code": 268,
                "name_c": u"斯威士兰",
                "name_e": "Swaziland",
                "country_area": u"非洲",
                "id": 153
            },
        ]
    },
    {
        u'大洋洲': [
            {
                "phone_pre": "+0061",
                "short_code": "AU",
                "area_code": 61,
                "name_c": u"澳大利亚",
                "name_e": "Australia",
                "country_area": u"大洋洲",
                "id": 154
            },
            {
                "phone_pre": "+0064",
                "short_code": "NZ",
                "area_code": 64,
                "name_c": u"新西兰",
                "name_e": "New Zealand",
                "country_area": u"大洋洲",
                "id": 155
            },
            {
                "phone_pre": "+00675",
                "short_code": "PG",
                "area_code": 675,
                "name_c": u"巴布亚新几内亚",
                "name_e": "Papua New Guinea",
                "country_area": u"大洋洲",
                "id": 156
            },
            {
                "phone_pre": "+00676",
                "short_code": "TO",
                "area_code": 676,
                "name_c": u"汤加",
                "name_e": "Tonga",
                "country_area": u"大洋洲",
                "id": 157
            },
            {
                "phone_pre": "+00677",
                "short_code": "SB",
                "area_code": 677,
                "name_c": u"所罗门群岛",
                "name_e": "Solomon Is",
                "country_area": u"大洋洲",
                "id": 158
            },
            {
                "phone_pre": "+00679",
                "short_code": "FJ",
                "area_code": 679,
                "name_c": u"斐济",
                "name_e": "Fiji",
                "country_area": u"大洋洲",
                "id": 159
            },
            {
                "phone_pre": "+00682",
                "short_code": "CK",
                "area_code": 682,
                "name_c": u"库克群岛",
                "name_e": "Cook Islands",
                "country_area": u"大洋洲",
                "id": 160
            },
            {
                "phone_pre": "+001671",
                "short_code": "GU",
                "area_code": 1671,
                "name_c": u"关岛",
                "name_e": "Guam",
                "country_area": u"大洋洲",
                "id": 161
            },
        ]
    },
    {
        u'太平洋': [
            {
                "phone_pre": "+00689",
                "short_code": "PF",
                "area_code": 689,
                "name_c": u"法属波利尼西亚",
                "name_e": "French Polynesia",
                "country_area": u"太平洋",
                "id": 46
            },
        ]
    },
    {
        u'大西洋': [
            {
                "phone_pre": "+001441",
                "short_code": "BM",
                "area_code": 1441,
                "name_c": u"百慕大群岛",
                "name_e": "Bermuda",
                "country_area": u"大西洋",
                "id": 162
            },
        ]
    }
]


area_code_map = {
    '0': '86',  # [CN]中国(China) 亚洲
    '1': '852',  # [HK]中国香港(Hongkong) 亚洲
    '2': '853',  # [MO]中国澳门(Macao) 亚洲
    '3': '886',  # [TW]中国台湾(Taiwan) 亚洲
    '4': '60',  # [MY]马来西亚(Malaysia) 亚洲
    '5': '65',  # [SG]新加坡(Singapore) 亚洲
    '6': '62',  # [ID]印度尼西亚(Indonesia) 亚洲
    '7': '63',  # [PH]菲律宾(Philippines) 亚洲
    '8': '66',  # [TH]泰国(Thailand) 亚洲
    '9': '73',  # [KZ]哈萨克斯坦(Kazakhstan) 亚洲
    '10': '81',  # [JP]日本(Japan) 亚洲
    '11': '82',  # [KR]韩国(Korea) 亚洲
    '12': '84',  # [VN]越南(Vietnam) 亚洲
    '13': '90',  # [TR]土耳其(Turkey) 亚洲
    '14': '91',  # [IN]印度(India) 亚洲
    '15': '92',  # [PK]巴基斯坦(Pakistan) 亚洲
    '16': '93',  # [AF]阿富汗(Afghanistan) 亚洲
    '17': '94',  # [LK]斯里兰卡(Sri Lanka) 亚洲
    '18': '95',  # [MM]缅甸(Burma) 亚洲
    '19': '98',  # [IR]伊朗(Iran) 亚洲
    '20': '374',  # [AM]亚美尼亚(Armenia) 亚洲
    '21': '673',  # [BN]文莱(Brunei) 亚洲
    '22': '855',  # [KH]柬埔寨(Cambodia) 亚洲
    '23': '856',  # [LA]老挝(Laos) 亚洲
    '24': '880',  # [BD]孟加拉国(Bangladesh) 亚洲
    '25': '960',  # [MV]马尔代夫(Maldives) 亚洲
    '26': '961',  # [LB]黎巴嫩(Lebanon) 亚洲
    '27': '962',  # [JO]约旦(Jordan) 亚洲
    '28': '963',  # [SY]叙利亚(Syria) 亚洲
    '29': '964',  # [IQ]伊拉克(Iraq) 亚洲
    '30': '965',  # [KW]科威特(Kuwait) 亚洲
    '31': '966',  # [SA]沙特阿拉伯(Saudi Arabia) 亚洲
    '32': '967',  # [YE]也门(Yemen) 亚洲
    '33': '968',  # [OM]阿曼(Oman) 亚洲
    '34': '971',  # [AE]阿拉伯联合酋长国(Arab Emirates) 亚洲
    '35': '972',  # [IL]以色列(Israel) 亚洲
    '36': '973',  # [BH]巴林(Bahrain) 亚洲
    '37': '974',  # [QA]卡塔尔(Qatar) 亚洲
    '38': '976',  # [MN]蒙古(Mongolia) 亚洲
    '39': '977',  # [NP]尼泊尔(Nepal) 亚洲
    '40': '992',  # [TJ]塔吉克斯坦(Tajikistan) 亚洲
    '41': '993',  # [TM]土库曼斯坦(Turkmenistan) 亚洲
    '42': '994',  # [AZ]阿塞拜疆(Azerbaijan) 亚洲
    '43': '995',  # [GE]格鲁吉亚(Georgia) 亚洲
    '44': '996',  # [KG]吉尔吉斯斯坦(Kyrgyzstan) 亚洲
    '45': '998',  # [UZ]乌兹别克斯坦(Uzbekistan) 亚洲
    '46': '689',  # [PF]法属波利尼西亚(French Polynesia) 太平洋
    '47': '44',  # [GB]英国(United Kiongdom) 欧洲
    '48': '49',  # [DE]德国(Germany) 欧洲
    '49': '7',  # [RU]俄罗斯(Russia) 欧洲
    '50': '30',  # [GR]希腊(Greece) 欧洲
    '51': '31',  # [NL]荷兰(Netherlands) 欧洲
    '52': '32',  # [BE]比利时(Belgium) 欧洲
    '53': '33',  # [FR]法国(France) 欧洲
    '54': '34',  # [ES]西班牙(Spain) 欧洲
    '55': '36',  # [HU]匈牙利(Hungary) 欧洲
    '56': '39',  # [IT]意大利(Italy) 欧洲
    '57': '40',  # [RO]罗马尼亚(Romania) 欧洲
    '58': '41',  # [CH]瑞士(Switzerland) 欧洲
    '59': '43',  # [AT]奥地利(Austria) 欧洲
    '60': '45',  # [DK]丹麦(Denmark) 欧洲
    '61': '46',  # [SE]瑞典(Sweden) 欧洲
    '62': '47',  # [NO]挪威(Norway) 欧洲
    '63': '48',  # [PL]波兰(Poland) 欧洲
    '64': '350',  # [GI]直布罗陀(Gibraltar) 欧洲
    '65': '351',  # [PT]葡萄牙(Portugal) 欧洲
    '66': '352',  # [LU]卢森堡(Luxembourg) 欧洲
    '67': '353',  # [IE]爱尔兰(Ireland) 欧洲
    '68': '354',  # [IS]冰岛(Iceland) 欧洲
    '69': '355',  # [AL]阿尔巴尼亚(Albania) 欧洲
    '70': '356',  # [MT]马耳他(Malta) 欧洲
    '71': '357',  # [CY]塞浦路斯(Cyprus) 欧洲
    '72': '358',  # [FI]芬兰(Finland) 欧洲
    '73': '359',  # [BG]保加利亚(Bulgaria) 欧洲
    '74': '370',  # [LT]立陶宛(Lithuania) 欧洲
    '75': '371',  # [LV]拉脱维亚(Latvia) 欧洲
    '76': '372',  # [EE]爱沙尼亚(Estonia) 欧洲
    '77': '373',  # [MD]摩尔多瓦(Moldova) 欧洲
    '78': '375',  # [BY]白俄罗斯(Belarus) 欧洲
    '79': '377',  # [MC]摩纳哥(Monaco) 欧洲
    '80': '378',  # [SM]圣马力诺(San Marino) 欧洲
    '81': '380',  # [UA]乌克兰(Ukraine) 欧洲
    '82': '386',  # [SI]斯洛文尼亚(Slovenia) 欧洲
    '83': '420',  # [CZ]捷克(Czech) 欧洲
    '84': '421',  # [SK]斯洛伐克(Slovak) 欧洲
    '85': '423',  # [LI]列支敦士登(Liechtenstein) 欧洲
    '86': '51',  # [PE]秘鲁(Peru) 南美洲
    '87': '52',  # [MX]墨西哥(Mexico) 南美洲
    '88': '53',  # [CU]古巴(Cuba) 南美洲
    '89': '54',  # [AR]阿根廷(Argentina) 南美洲
    '90': '55',  # [BR]巴西(Brazil) 南美洲
    '91': '56',  # [CL]智利(Chile) 南美洲
    '92': '57',  # [CO]哥伦比亚(Colombia) 南美洲
    '93': '58',  # [VE]委内瑞拉(Venezuela) 南美洲
    '94': '501',  # [BZ]伯利兹(Belize) 南美洲
    '95': '503',  # [SV]萨尔瓦多(EI Salvador) 南美洲
    '96': '504',  # [HN]洪都拉斯(Honduras) 南美洲
    '97': '505',  # [NI]尼加拉瓜(Nicaragua) 南美洲
    '98': '506',  # [CR]哥斯达黎加(Costa Rica) 南美洲
    '99': '507',  # [PA]巴拿马(Panama) 南美洲
    '100': '509',  # [HT]海地(Haiti) 南美洲
    '101': '591',  # [BO]玻利维亚(Bolivia) 南美洲
    '102': '592',  # [GY]圭亚那(Guyana) 南美洲
    '103': '593',  # [EC]厄瓜多尔(Ecuador) 南美洲
    '104': '594',  # [GF]法属圭亚那(French Guiana) 南美洲
    '105': '595',  # [PY]巴拉圭(Paraguay) 南美洲
    '106': '596',  # [MQ]马提尼克(Martinique) 南美洲
    '107': '597',  # [SR]苏里南(Suriname) 南美洲
    '108': '598',  # [UY]乌拉圭(Uruguay) 南美洲
    '109': '20',  # [EG]埃及(Egypt) 非洲
    '110': '27',  # [ZA]南非(South Africa) 非洲
    '111': '212',  # [MA]摩洛哥(Morocco) 非洲
    '112': '213',  # [DZ]阿尔及利亚(Algeria) 非洲
    '113': '216',  # [TN]突尼斯(Tunisia) 非洲
    '114': '218',  # [LY]利比亚(Libya) 非洲
    '115': '220',  # [GM]冈比亚(Gambia) 非洲
    '116': '221',  # [SN]塞内加尔(Senegal) 非洲
    '117': '223',  # [ML]马里(Mali) 非洲
    '118': '224',  # [GN]几内亚(Guinea) 非洲
    '119': '225',  # [CI]科特迪瓦(Ivory Coast) 非洲
    '120': '226',  # [BF]布基纳法索(Burkina Faso) 非洲
    '121': '227',  # [NE]尼日尔(Niger) 非洲
    '122': '228',  # [TG]多哥(Togo) 非洲
    '123': '229',  # [BJ]贝宁(Benin) 非洲
    '124': '230',  # [MU]毛里求斯(Mauritius) 非洲
    '125': '231',  # [LR]利比里亚(Liberia) 非洲
    '126': '232',  # [SL]塞拉利昂(Sierra Leone) 非洲
    '127': '233',  # [GH]加纳(Ghana) 非洲
    '128': '234',  # [NG]尼日利亚(Nigeria) 非洲
    '129': '235',  # [TD]乍得(Chad) 非洲
    '130': '236',  # [CF]中非共和国(Central Africa) 非洲
    '131': '237',  # [CM]喀麦隆(Cameroon) 非洲
    '132': '239',  # [ST]圣多美和普林西比(Sao Tome and Principe) 非洲
    '133': '241',  # [GA]加蓬(Gabon) 非洲
    '134': '243',  # [CG]刚果民主共和国(Congo) 非洲
    '135': '244',  # [AO]安哥拉(Angola) 非洲
    '136': '248',  # [SC]塞舌尔(Seychelles) 非洲
    '137': '249',  # [SD]苏丹(Sudan) 非洲
    '138': '251',  # [ET]埃塞俄比亚(Ethiopia) 非洲
    '139': '252',  # [SO]索马里(Somali) 非洲
    '140': '253',  # [DJ]吉布提(Djibouti) 非洲
    '141': '254',  # [KE]肯尼亚(Kenya) 非洲
    '142': '255',  # [TZ]坦桑尼亚(Tanzania) 非洲
    '143': '256',  # [UG]乌干达(Uganda) 非洲
    '144': '257',  # [BI]布隆迪(Burundi) 非洲
    '145': '258',  # [MZ]莫桑比克(Mozambique) 非洲
    '146': '260',  # [ZM]赞比亚(Zambia) 非洲
    '147': '261',  # [MG]马达加斯加(Madagascar) 非洲
    '148': '263',  # [ZW]津巴布韦(Zimbabwe) 非洲
    '149': '264',  # [nan]纳米比亚(Namibia) 非洲
    '150': '265',  # [MW]马拉维(Malawi) 非洲
    '151': '266',  # [LS]莱索托(Lesotho) 非洲
    '152': '267',  # [BW]博茨瓦纳(Botswana) 非洲
    '153': '268',  # [SZ]斯威士兰(Swaziland) 非洲
    '154': '61',  # [AU]澳大利亚(Australia) 大洋洲
    '155': '64',  # [NZ]新西兰(New Zealand) 大洋洲
    '156': '675',  # [PG]巴布亚新几内亚(Papua New Guinea) 大洋洲
    '157': '676',  # [TO]汤加(Tonga) 大洋洲
    '158': '677',  # [SB]所罗门群岛(Solomon Is) 大洋洲
    '159': '679',  # [FJ]斐济(Fiji) 大洋洲
    '160': '682',  # [CK]库克群岛(Cook Islands) 大洋洲
    '161': '1671',  # [GU]关岛(Guam) 大洋洲
    '162': '1441',  # [BM]百慕大群岛(Bermuda) 大西洋
    '163': '1',  # [US]美国(America) 北美洲
    '164': '1',  # [CA]加拿大(Canada) 北美洲
    '165': '502',  # [GT]瓜地马拉(Guatemala) 北美洲
    '166': '1242',  # [BS]巴哈马(Bahamas) 北美洲
    '167': '1246',  # [BB]巴巴多斯(Barbados) 北美洲
    '168': '1264',  # [AI]安圭拉岛(Anguilla) 北美洲
    '169': '1268',  # [AG]安提瓜和巴布达(Antigua and Barbuda) 北美洲
    '170': '1345',  # [KY]开曼群岛(Cayman Islands) 北美洲
    '171': '1473',  # [GD]格林纳达(Grenada) 北美洲
    '172': '1758',  # [LC]圣卢西亚(Saint Lucia) 北美洲
    '173': '1787',  # [PR]波多黎各(Puerto Rico) 北美洲
    '174': '1809',  # [DO]多米尼加共和国(Dominican) 北美洲
    '175': '1868',  # [TT]特立尼达和多巴哥(Trinidad and Tobago) 北美洲
    '176': '1876',  # [JM]牙买加(Jamaica) 北美洲
}


if __name__ == '__main__':
    # html = ['<select>']
    # for area_data in area_code_list:
    #     for area_name, area_list in area_data.items():
    #         html.append('\t<optgroup label="%s">' % area_name)
    #         for country_data in area_list:
    #             html.append('\t\t<option value="%s" data-subtext="%s(%s)">[%s] %s</option>' % (
    #             country_data['id'], country_data['name_c'], country_data['name_e'], country_data['short_code'],
    #             country_data['phone_pre']))
    #         html.append('\t</optgroup>')
    # html.append('</select>')
    # print '\n'.join(html)
    area_code_choices = []
    for m, n in enumerate(area_code_list):
        area_code_choices.append((m, n))
    print area_code_choices
