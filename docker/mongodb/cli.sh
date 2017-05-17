#!/usr/bin/env bash

docker run \
    -it \
    --link mongo:mongo \
    --rm \
    mongo:3.4.4 \
    sh -c 'exec mongo "$MONGO_PORT_27017_TCP_ADDR:$MONGO_PORT_27017_TCP_PORT/test"'
