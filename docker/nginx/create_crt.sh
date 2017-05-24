#!/usr/bin/env bash

openssl x509 -req -days 365 -in conf/ssl/server.csr -signkey conf/ssl/server.key -extfile conf/ssl/v3.ext -out conf/ssl/server.crt
