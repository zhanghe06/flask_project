#!/usr/bin/env bash

# 初始化数据库，添加测试数据

cd ../
sqlite3 flask.db < schema.sql
sqlite3 flask.db < etc/create_test_data.sql
