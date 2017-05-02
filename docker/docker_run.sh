#!/usr/bin/env bash


[ -d logs ] || mkdir logs

PROJECT_PATH=`(cd ../;pwd)`
CONFIG_MODE_TEXT=`cat ${PROJECT_PATH}/config/config.env`

# docker rm $(docker ps -a -q)

# 后台运行
docker run \
        --name flask_project_${CONFIG_MODE_TEXT} \
        -h flask_project_${CONFIG_MODE_TEXT} \
        --dns=223.5.5.5 \
        --dns=223.6.6.6 \
        --privileged \
        --cap-add SYS_PTRACE \
        --restart=always \
        -e TZ=Asia/Shanghai \
        -v `(cd ../;pwd)`:/flask_project \
        -d \
        -p 8000:8000 \
        -p 8010:8010 \
        -p 9001:9001 \
        flask_project \
        supervisord -c etc/supervisord.conf
