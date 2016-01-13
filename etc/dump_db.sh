#!/usr/bin/env bash

# 备份数据

cd ../
sqlite3 flask.db ".dump" > schema.dump.sql
