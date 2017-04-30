#!/usr/bin/env bash

# 备份数据

base_path=`dirname $0`/../
cd ${base_path}
sqlite3 flask.db ".dump" > schema.dump.sql
