#!/usr/bin/env bash

docker run \
    -it \
    --link mariadb:mysql \
    --rm \
    mariadb:10.1.23 \
    sh -c 'exec mysql -h"$MYSQL_PORT_3306_TCP_ADDR" -P"$MYSQL_PORT_3306_TCP_PORT" -uroot -p"$MYSQL_ENV_MYSQL_ROOT_PASSWORD"'
