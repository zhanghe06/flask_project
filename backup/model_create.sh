#!/usr/bin/env bash


base_path=`dirname $0`/../
cd ${base_path}
# 生成 model
sqlacodegen sqlite:///flask.db --outfile app/models.py
# 替换 model 关键内容
sed -i "s/from sqlalchemy.ext.declarative import declarative_base/from database import db/g" app/models.py
sed -i "s/Base = declarative_base()/Base = db.Model/g" app/models.py
