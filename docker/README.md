## Docker

### 测试环境
ubuntu-16.04.2-server-amd64

### 安装
```
$ curl -sSL https://get.daocloud.io/docker | sh
```

### 建立 docker 用户组
建立 docker 组：
```
$ sudo groupadd docker
```
将当前用户加入 docker 组：
```
$ sudo usermod -aG docker $USER
```

### 加速配置(重启服务)
https://www.daocloud.io/mirror#accelerator-doc
```
$ curl -sSL https://get.daocloud.io/daotools/set_mirror.sh | sudo sh -s http://12248bc3.m.daocloud.io
$ sudo systemctl restart docker.service
```
查看加速配置
```
$ sudo cat /etc/docker/daemon.json
{"registry-mirrors": ["http://12248bc3.m.daocloud.io"]}
```

### 镜像配置

Python
https://hub.docker.com/_/python/
```
$ sudo docker pull python:2.7.13
```

Nginx
https://hub.docker.com/_/nginx/
```
$ sudo docker pull nginx:1.13.0
```

Redis
https://hub.docker.com/_/redis/
```
$ sudo docker pull redis:3.0.7
```

MariaDB
https://hub.docker.com/_/mariadb/
```
$ sudo docker pull mariadb:10.1.23
```

RabbitMQ
https://hub.docker.com/_/rabbitmq/
```
$ sudo docker pull rabbitmq:3.6.9
```

MongoDB
https://hub.docker.com/_/mongo/
```
$ sudo docker pull mongo:3.4.4
```


## 查看容器信息

查看容器ip地址
```
$ sudo docker inspect --format '{{ .NetworkSettings.IPAddress }}' [容器ID]
```
