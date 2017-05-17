MariaDB
https://hub.docker.com/_/mariadb/
```
$ sudo docker pull mariadb:10.1.23
```

环境变量 | 说明
--- | ---
MYSQL_ROOT_PASSWORD | 创建root用户密码
MYSQL_USER | 创建用户
MYSQL_PASSWORD | 创建用户密码


容器启动后，项目根目录，建库建表，初始化数据
$ mysql -h127.0.0.1 -uroot -p123456 < db/schema/mysql.sql
$ mysql -h127.0.0.1 -uroot -p123456 < db/data/mysql.sql
