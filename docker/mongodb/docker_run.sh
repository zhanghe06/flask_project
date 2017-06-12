#!/usr/bin/env bash

docker run \
        -h mongo \
        --name mongo \
        -v ${PWD}/data/db:/data/db \
        -p 27017:27017 \
        -d \
        mongo:3.4.4
