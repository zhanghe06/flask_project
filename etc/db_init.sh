#!/usr/bin/env bash


base_path=`dirname $0`/../
cd ${base_path}
# 初始化数据库
sqlite3 flask.db < schema.sql
# 添加测试数据
sqlite3 flask.db < etc/data_test.sql
# 生成 model
./etc/model_create.sh
