#!/usr/bin/env bash


[ -d logs ] || mkdir logs

PROJECT_PATH=`(cd ../;pwd)`
CONFIG_MODE_TEXT=`cat ${PROJECT_PATH}/config/config.env`

# docker rm $(docker ps -a -q)

# 后台运行
docker run \
        --name scrapy_project_${CONFIG_MODE_TEXT} \
        -h scrapy_project_${CONFIG_MODE_TEXT} \
        --dns=202.96.209.5 \
        --privileged \
        --cap-add SYS_PTRACE \
        --restart=always \
        -e TZ=Asia/Shanghai \
        -v `(cd ../;pwd)`:/scrapy_project \
        -d \
        scrapy_project \
        supervisord -c etc/supervisord.conf
