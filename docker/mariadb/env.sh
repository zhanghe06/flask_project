#!/usr/bin/env bash

docker run \
    -it \
    --link mariadb:mysql \
    --rm \
    mariadb:10.1.23 \
    env
