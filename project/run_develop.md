## 项目配置步骤[开发环境]

设置环境变量
```
echo develop > config/config.env
```

开启 mariadb 服务
```
cd docker/mariadb

sh docker_run_develop.sh

# 建立数据库 导入测试数据(注意需要等待以上步骤数据库完全建好)
sh db_init.sh
```

开启 redis 服务
```
cd docker/redis

sh docker_run_rdb.sh
```

开启 rabbitmq 服务
```
cd docker/rabbitmq

sh docker_run.sh
```

启动项目
```
cd docker

sh docker_run.sh
```


## 每次更新表结构，需要更新 models
```
python gen.py create_models app_frontend
python gen.py create_models app_backend
```
