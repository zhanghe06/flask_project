#!/usr/bin/env bash

base_path=`dirname $0`/../

cd ${base_path}

source .env/bin/activate

supervisord -c etc/supervisord.conf

supervisorctl -c etc/supervisord.conf reload

supervisorctl -c etc/supervisord.conf stop all

supervisorctl -c etc/supervisord.conf start all

sudo ln -s -b `pwd`/etc/nginx.conf /etc/nginx/conf.d/flask_app_nginx.conf

sudo /etc/init.d/nginx reload
