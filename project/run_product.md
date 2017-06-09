## 项目配置步骤[生产环境]

设置环境变量
```
echo product > config/config.env
```

marriadb
```
cd docker/marriadb

sh docker_run_product.sh

# 建立数据库 导入测试数据(注意需要等待以上步骤数据库完全建好)
sh db_init.sh
```

redis
```
cd docker/redis

sh docker_run_aof.sh
```

rabbitmq
```
cd docker/rabbitmq

sh docker_run.sh
```


## 每次更新表结构，需要更新 models
```
python gen.py create_models app_frontend
python gen.py create_models app_backend
```
