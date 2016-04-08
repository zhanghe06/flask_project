#!/usr/bin/env bash

# 定义参数
db_name='database_name'     # 远程数据库名称
db_user='xxxxxx'            # 登录用户
db_pass='xxxxxx'            # 登录密码
db_port='3306'              # 远程数据库端口
db_host='127.0.0.1'         # 远程数据库IP

table_name='table_name'     # 数据表名
column_list='id,name,date'  # 批量导入字段名称列表（有序）

csv_file='/tmp/batch_export.csv'
sql_file='/tmp/batch_import.sql'

repeat_action='IGNORE'      # 对导入唯一键重复数据的处理（REPLACE/IGNORE）

# 组装sql语句
#echo "use ${db_name};LOAD DATA LOCAL INFILE '${csv_file}' ${repeat_action} INTO TABLE ${table_name} FIELDS TERMINATED BY '\t' ENCLOSED BY '\"' LINES TERMINATED BY '\n' (${column_list});" > ${sql_file}

# 批量导入数据
#time mysql -h ${db_host} -P ${db_port} -u ${db_user} -p${db_pass} < ${sql_file}

# 查找目录下所有指定类型的文件
file_list=`ls /tmp`
for file in ${file_list}
do
    if [ ${file##*.} == 'csv' ]
    then
        echo ${file}
    fi
done
