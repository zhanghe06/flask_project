#!/usr/bin/env bash

# 恢复数据

base_path=`dirname $0`/../
cd ${base_path}
# 清空历史库
rm -f flask.db
# 恢复数据库
sqlite3 flask.db < schema.dump.sql
# 重建 model
./etc/model_create.sh
