#!/usr/bin/env bash

backup_file_name=`date '+%Y%m%d%H%M%S'`'.sql'

docker exec mariadb \
    sh -c 'exec mysqldump --all-databases -uroot -p"$MYSQL_ROOT_PASSWORD"' > backup/${backup_file_name}
