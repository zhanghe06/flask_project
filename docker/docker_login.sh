#!/usr/bin/env bash



PROJECT_PATH=`(cd ../;pwd)`
CONFIG_MODE_TEXT=`cat ${PROJECT_PATH}/config/config.env`

# 登录容器
docker exec -it flask_project_${CONFIG_MODE_TEXT} bash
