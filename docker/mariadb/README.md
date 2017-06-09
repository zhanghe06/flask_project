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


查看环境变量
```
$ sh env.sh
```

客户端连接
```
$ sh cli.sh
```

建库建表
```
$ sh db_init.sh
```

备份数据
```
$ sh db_dump.sh
```
