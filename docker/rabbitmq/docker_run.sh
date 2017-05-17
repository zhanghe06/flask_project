#!/usr/bin/env bash

docker run \
        -h rabbitmq \
        --name rabbitmq \
        -v ${PWD}/data:/var/lib/rabbitmq \
        -p 4369:4369 \
        -p 5671:5671 \
        -p 5672:5672 \
        -p 25672:25672 \
        -d \
        rabbitmq:3.6.9
