#!/usr/bin/env bash

[ -d ${PWD}/data ] || mkdir -p ${PWD}/data

docker run \
    -h redis \
    --name redis \
    -v ${PWD}/data:/data \
    -p 6379:6379 \
    -d \
    redis:3.2.8 \
    redis-server --appendonly yes
