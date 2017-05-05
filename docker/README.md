## Docker

### 测试环境
ubuntu-16.04.2-server-amd64

### 安装
```
curl -sSL https://get.daocloud.io/docker | sh
```

### 建立 docker 用户组
建立 docker 组：
```
sudo groupadd docker
```
将当前用户加入 docker 组：
```
sudo usermod -aG docker $USER
```

### 加速配置
https://www.daocloud.io/mirror#accelerator-doc
```
curl -sSL https://get.daocloud.io/daotools/set_mirror.sh | sudo sh -s http://12248bc3.m.daocloud.io
```

### 镜像配置

Python
https://hub.docker.com/_/python/
```
docker pull python:2.7.13
```

Nginx
https://hub.docker.com/_/nginx/
```
docker pull nginx
```

MariaDB
https://hub.docker.com/_/mariadb/
```
docker pull mariadb
```

RabbitMQ
https://hub.docker.com/_/rabbitmq/
```
docker pull rabbitmq
```

MongoDB
https://hub.docker.com/_/mongo/
```
docker pull mongo
```

## 查看容器信息

查看容器ip地址
```
docker inspect --format '{{ .NetworkSettings.IPAddress }}' [容器ID]
```
