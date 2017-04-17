#!/usr/bin/env python
# encoding: utf-8

"""
@author: zhanghe
@software: PyCharm
@file: output.py
@time: 2017/4/17 下午11:15
"""

import pandas as pd
import json


def area_code_list():
    file_path = '全球区号.xlsx'
    df = pd.read_excel(file_path, sheetname='code')  # sheet_name=str(0)
    print list(df.keys())
    for i in df.values:
        code_dict = {
            'id': i[0],
            'name_c': i[1],
            'area_code': i[2],
            'phone_pre': '+00%s' % i[2],
            'country_area': i[3],
            'short_code': i[4],
            'name_e': i[5]
        }
        print json.dumps(code_dict, indent=4, ensure_ascii=False)+','


def area_code_map():
    file_path = '全球区号.xlsx'
    df = pd.read_excel(file_path, sheetname='code')  # sheet_name=str(0)
    print list(df.keys())
    for i in df.values:
        print '%s: \'%s\',  # [%s]%s(%s) %s' % (i[0], i[2], i[4], i[1], i[5], i[3])


if __name__ == '__main__':
    area_code_list()
    area_code_map()
