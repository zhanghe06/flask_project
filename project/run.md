## 项目配置步骤

marriadb
```
cd docker/marriadb

docker run \
    -h mariadb \
    --name mariadb \
    -v ${PWD}/data:/var/lib/mysql \
    -e MYSQL_ROOT_PASSWORD='2qFG#E!SYxrw' \
    -e MYSQL_DATABASE='flask' \
    -e MYSQL_USER='www' \
    -e MYSQL_PASSWORD='@9xJkaU*JWsa' \
    -p 3306:3306 \
    -d \
    mariadb:10.1.23 --log-bin --binlog-format=MIXED

# 建立数据库 导入测试数据
mysql -h127.0.0.1 -uroot -p'2qFG#E!SYxrw' < ../../db/schema/mysql.sql
mysql -h127.0.0.1 -uroot -p'2qFG#E!SYxrw' < ../../db/data/mysql.sql
```

redis
```
cd docker/marriadb

docker run \
    -h redis \
    --name redis \
    -v ${PWD}/data:/data \
    -p 6379:6379 \
    -d \
    redis:3.2.8 \
    redis-server
```

rabbitmq
```
cd docker/rabbitmq

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
```


## 每次更新表结构，需要更新 models
```
python gen.py create_models app_frontend
python gen.py create_models app_backend
```
