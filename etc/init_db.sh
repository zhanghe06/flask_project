#!/usr/bin/env bash


cd ../
# 初始化数据库
sqlite3 flask.db < schema.sql
# 添加测试数据
sqlite3 flask.db < etc/create_test_data.sql
# 生成 model
sqlacodegen sqlite:///flask.db --outfile app/models.py
