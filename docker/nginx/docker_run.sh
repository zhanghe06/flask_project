#!/usr/bin/env bash

docker run \
    -h nginx \
    --name nginx \
    -v ${PWD}/conf/nginx.conf:/etc/nginx/nginx.conf:ro \
    -v ${PWD}/conf/ssl:/etc/nginx/ssl:ro \
    -v ${PWD}/conf/conf.d:/etc/nginx/conf.d:ro \
    -v ${PWD}/log:/var/log/nginx \
    -p 80:80 \
    -p 443:443 \
    -d \
    nginx:1.13.0
