#!/usr/bin/env bash

docker build \
        --rm=true \
        -t flask_project \
        -f Dockerfile ..
