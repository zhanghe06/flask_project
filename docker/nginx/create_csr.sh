#!/usr/bin/env bash

openssl req -new -key conf/ssl/ca.key -out conf/ssl/server.csr
