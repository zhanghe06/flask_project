#!/usr/bin/env bash

docker run \
    -h mariadb \
    --name mariadb \
    -v ${PWD}/data:/var/lib/mysql \
    -e MYSQL_ROOT_PASSWORD='123456' \
    -e MYSQL_DATABASE='project' \
    -e MYSQL_USER='www' \
    -e MYSQL_PASSWORD='123456' \
    -p 3306:3306 \
    -d \
    mariadb:10.1.23 --log-bin --binlog-format=MIXED
