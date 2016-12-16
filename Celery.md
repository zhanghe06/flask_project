## Celery - Distributed Task Queue

https://github.com/celery/celery

http://docs.celeryproject.org/en/latest/index.html

http://www.pythondoc.com/flask/patterns/celery.html

http://www.pythondoc.com/flask-celery/


Choosing a Broker
```
$ sudo apt-get install rabbitmq-server
```

Installing Celery
```
$ pip install celery
$ pip install librabbitmq
```


Application

tasks.py:
```
from celery import Celery

app = Celery('tasks', broker='amqp://guest@localhost//')

@app.task
def add(x, y):
    return x + y
```

Using Celery in your Application

http://docs.celeryproject.org/en/master/getting-started/next-steps.html


## 简单测试

基于 redis

启动 Web server:
```
$ python run.py
```

启动 Celery worker:
```
$ celery worker -A app.celery_worker.celery_app -l INFO
```

启动结果:
```
celery@zhanghedeMBP v4.0.0 (latentcall)

Darwin-16.1.0-x86_64-i386-64bit 2016-11-16 23:48:23

[config]
.> app:         app:0x10f7a8510
.> transport:   redis://localhost:6379//
.> results:     redis://localhost:6379/
.> concurrency: 8 (prefork)
.> task events: OFF (enable -E to monitor tasks in this worker)

[queues]
.> celery           exchange=celery(direct) key=celery


[tasks]
  . app.tasks.add
  . app.tasks.mul
  . app.tasks.xsum

[2016-11-16 23:48:23,710: INFO/MainProcess] Connected to redis://localhost:6379//
[2016-11-16 23:48:23,721: INFO/MainProcess] mingle: searching for neighbors
[2016-11-16 23:48:24,741: INFO/MainProcess] mingle: all alone
[2016-11-16 23:48:24,752: INFO/MainProcess] celery@zhanghedeMBP ready.
```

查看 redis 队列结构
```
127.0.0.1:6379> type "celery-task-meta-cf11bfdb-4c02-4b0a-81f9-ee8ae929926c"
string
127.0.0.1:6379> ttl "celery-task-meta-cf11bfdb-4c02-4b0a-81f9-ee8ae929926c"
85730
127.0.0.1:6379> get "celery-task-meta-cf11bfdb-4c02-4b0a-81f9-ee8ae929926c"
"{\"status\": \"SUCCESS\", \"traceback\": null, \"result\": 300, \"task_id\": \"cf11bfdb-4c02-4b0a-81f9-ee8ae929926c\", \"children\": []}"
127.0.0.1:6379>
```

字符串序列化存储，默认过期时间24小时（86400秒）


## 任务队列系统的三种角色

- 任务生产者
- 任务处理中间方（代理）
- 任务消费者


Using RabbitMQ

http://docs.celeryproject.org/en/latest/getting-started/brokers/rabbitmq.html


## 深入探究


启动 celery 进程
```
127.0.0.1:6379> keys *
1) "_kombu.binding.celery.pidbox"
2) "_kombu.binding.celery"
3) "_kombu.binding.celeryev"
127.0.0.1:6379> type "_kombu.binding.celery.pidbox"
set
127.0.0.1:6379> SMEMBERS "_kombu.binding.celery.pidbox"
1) "\x06\x16\x06\x16celery@zhanghedeMacBook-Pro.local.celery.pidbox"
127.0.0.1:6379> type "_kombu.binding.celery"
set
127.0.0.1:6379> SMEMBERS "_kombu.binding.celery"
1) "celery\x06\x16\x06\x16celery"
127.0.0.1:6379> type "_kombu.binding.celeryev"
set
127.0.0.1:6379> SMEMBERS "_kombu.binding.celeryev"
1) "worker.#\x06\x16\x06\x16celeryev.3389080e-158d-4c9b-a8f6-322e4776c802"
```

web 页面发起任务请求（broker 为 redis, backend 为 rabbit） 
http://localhost:8000/test_send_task/?x=100&y=200
```
127.0.0.1:6379> KEYS *
1) "7755e27bbb534c058e46037417ab4e30\x06\x169"
2) "_kombu.binding.celeryresults"
3) "_kombu.binding.celery"
4) "_kombu.binding.celery.pidbox"
5) "2a5e68d9b44342778b5709dd69b2f465\x06\x169"
6) "_kombu.binding.celeryev"
7) "0377bc1c0e5d4a3ca5d27a06a162ba53\x06\x169"
127.0.0.1:6379> type "_kombu.binding.celeryresults"
set
127.0.0.1:6379> SMEMBERS "_kombu.binding.celeryresults"
1) "0377bc1c0e5d4a3ca5d27a06a162ba53\x06\x16\x06\x160377bc1c0e5d4a3ca5d27a06a162ba53"
2) "2a5e68d9b44342778b5709dd69b2f465\x06\x16\x06\x162a5e68d9b44342778b5709dd69b2f465"
3) "7755e27bbb534c058e46037417ab4e30\x06\x16\x06\x167755e27bbb534c058e46037417ab4e30"
127.0.0.1:6379> type "7755e27bbb534c058e46037417ab4e30\x06\x169"
list
127.0.0.1:6379> ttl "7755e27bbb534c058e46037417ab4e30\x06\x169"
(integer) -1
127.0.0.1:6379> LRANGE "7755e27bbb534c058e46037417ab4e30\x06\x169" 0 -1
1) "{\"body\": \"eyJzdGF0dXMiOiAiU1VDQ0VTUyIsICJ0cmFjZWJhY2siOiBudWxsLCAicmVzdWx0IjogMzAwLCAidGFza19pZCI6ICI3NzU1ZTI3Yi1iYjUzLTRjMDUtOGU0Ni0wMzc0MTdhYjRlMzAiLCAiY2hpbGRyZW4iOiBbXX0=\", \"headers\": {}, \"content-type\": \"application/json\", \"properties\": {\"priority\": 0, \"body_encoding\": \"base64\", \"correlation_id\": \"7755e27b-bb53-4c05-8e46-037417ab4e30\", \"delivery_info\": {\"routing_key\": \"7755e27bbb534c058e46037417ab4e30\", \"exchange\": \"celeryresults\"}, \"delivery_mode\": 2, \"delivery_tag\": \"a157be8b-55ca-44cd-8ebe-993ab032b067\"}, \"content-encoding\": \"utf-8\"}"
```

查看记录结构
```
In [1]: result = "{\"body\": \"eyJzdGF0dXMiOiAiU1VDQ0VTUyIsICJ0cmFjZWJhY2siOiBudWxsLCAicmVzdWx0IjogMzAwLCAidGFza19pZCI6ICI3NzU1ZTI3Yi1iYjUzLTRjMDUtOGU0Ni0wMzc0MTdhYjRlMzAiLCAiY2hpb
   ...: GRyZW4iOiBbXX0=\", \"headers\": {}, \"content-type\": \"application/json\", \"properties\": {\"priority\": 0, \"body_encoding\": \"base64\", \"correlation_id\": \"7755e27
   ...: b-bb53-4c05-8e46-037417ab4e30\", \"delivery_info\": {\"routing_key\": \"7755e27bbb534c058e46037417ab4e30\", \"exchange\": \"celeryresults\"}, \"delivery_mode\": 2, \"deli
   ...: very_tag\": \"a157be8b-55ca-44cd-8ebe-993ab032b067\"}, \"content-encoding\": \"utf-8\"}"

In [2]: import json

In [3]: print json.dumps(json.loads(result), indent=4, ensure_ascii=False)
{
    "body": "eyJzdGF0dXMiOiAiU1VDQ0VTUyIsICJ0cmFjZWJhY2siOiBudWxsLCAicmVzdWx0IjogMzAwLCAidGFza19pZCI6ICI3NzU1ZTI3Yi1iYjUzLTRjMDUtOGU0Ni0wMzc0MTdhYjRlMzAiLCAiY2hpbGRyZW4iOiBbXX0=",
    "headers": {},
    "content-type": "application/json",
    "properties": {
        "body_encoding": "base64",
        "delivery_info": {
            "routing_key": "7755e27bbb534c058e46037417ab4e30",
            "exchange": "celeryresults"
        },
        "delivery_mode": 2,
        "priority": 0,
        "correlation_id": "7755e27b-bb53-4c05-8e46-037417ab4e30",
        "delivery_tag": "a157be8b-55ca-44cd-8ebe-993ab032b067"
    },
    "content-encoding": "utf-8"
}
```

查看 body 内容
```
In [4]: import base64

In [5]: base64.b64decode('eyJzdGF0dXMiOiAiU1VDQ0VTUyIsICJ0cmFjZWJhY2siOiBudWxsLCAicmVzdWx0IjogMzAwLCAidGFza19pZCI6ICI3NzU1ZTI3Yi1iYjUzLTRjMDUtOGU0Ni0wMzc0MTdhYjRlMzAiLCAiY2hpbGRy
   ...: ZW4iOiBbXX0=')
Out[5]: '{"status": "SUCCESS", "traceback": null, "result": 300, "task_id": "7755e27b-bb53-4c05-8e46-037417ab4e30", "children": []}'
```

取出任务id 7755e27b-bb53-4c05-8e46-037417ab4e30 的结果 
http://localhost:8000/test_task_add_result/7755e27b-bb53-4c05-8e46-037417ab4e30/
```
127.0.0.1:6379> keys *
1) "_kombu.binding.celeryresults"
2) "_kombu.binding.celery"
3) "_kombu.binding.celery.pidbox"
4) "2a5e68d9b44342778b5709dd69b2f465\x06\x169"
5) "_kombu.binding.celeryev"
6) "0377bc1c0e5d4a3ca5d27a06a162ba53\x06\x169"
127.0.0.1:6379> SMEMBERS "_kombu.binding.celeryresults"
1) "0377bc1c0e5d4a3ca5d27a06a162ba53\x06\x16\x06\x160377bc1c0e5d4a3ca5d27a06a162ba53"
2) "2a5e68d9b44342778b5709dd69b2f465\x06\x16\x06\x162a5e68d9b44342778b5709dd69b2f465"
3) "7755e27bbb534c058e46037417ab4e30\x06\x16\x06\x167755e27bbb534c058e46037417ab4e30"
```
任务的结果被取出之后立即被删除


方式二、web 页面发起任务请求（同时设置 broker, backend 为 redis） 
http://localhost:8000/test_send_task/?x=100&y=200
```
127.0.0.1:6379> keys *
1) "celery-task-meta-cce9eb23-5c6c-4852-a9fd-9100108a0b36"
2) "_kombu.binding.celery"
3) "celery-task-meta-7133e2f6-8d01-453f-b5ff-bd6d9d4cb90c"
4) "_kombu.binding.celery.pidbox"
5) "celery-task-meta-8ab29192-06fb-4438-b4d3-951765b5e10b"
6) "_kombu.binding.celeryev"
127.0.0.1:6379> type "celery-task-meta-cce9eb23-5c6c-4852-a9fd-9100108a0b36"
string
127.0.0.1:6379> ttl "celery-task-meta-cce9eb23-5c6c-4852-a9fd-9100108a0b36"
(integer) 85943
127.0.0.1:6379> get "celery-task-meta-cce9eb23-5c6c-4852-a9fd-9100108a0b36"
"{\"status\": \"SUCCESS\", \"traceback\": null, \"result\": 20000, \"task_id\": \"cce9eb23-5c6c-4852-a9fd-9100108a0b36\", \"children\": []}"
```
任务结果字符串序列化存储，默认过期时间24小时（86400秒）

取出任务id cce9eb23-5c6c-4852-a9fd-9100108a0b36 的结果 
http://localhost:8000/test_task_mul_result/cce9eb23-5c6c-4852-a9fd-9100108a0b36/
```
127.0.0.1:6379> keys *
1) "celery-task-meta-cce9eb23-5c6c-4852-a9fd-9100108a0b36"
2) "_kombu.binding.celery"
3) "celery-task-meta-7133e2f6-8d01-453f-b5ff-bd6d9d4cb90c"
4) "_kombu.binding.celery.pidbox"
5) "celery-task-meta-8ab29192-06fb-4438-b4d3-951765b5e10b"
6) "_kombu.binding.celeryev"
127.0.0.1:6379> ttl "celery-task-meta-cce9eb23-5c6c-4852-a9fd-9100108a0b36"
(integer) 85789
127.0.0.1:6379> get "celery-task-meta-cce9eb23-5c6c-4852-a9fd-9100108a0b36"
"{\"status\": \"SUCCESS\", \"traceback\": null, \"result\": 20000, \"task_id\": \"cce9eb23-5c6c-4852-a9fd-9100108a0b36\", \"children\": []}"
```
任务的结果还缓存在 redis


方式三、broker 为 rabbit, backend 为 rabbit

开启 celery 实例
```
✗ celery worker -A app.celery_worker.celery_app -l INFO
```

查看队列情况
```
➜  ~ rabbitmqctl list_queues
Listing queues ...
celery@zhanghedeMacBook-Pro.local.celery.pidbox	0
celery	0
celeryev.831c6f64-0e51-465a-8a32-ad8647708704	0
```

web 页面发起任务请求 http://localhost:8000/test_send_task/?x=100&y=200
```
➜  ~ rabbitmqctl list_queues
Listing queues ...
226f45e6588840dd8cee49a539364e16	1
celery@zhanghedeMacBook-Pro.local.celery.pidbox	0
celery	0
fdf36b63accd4dffb6be7625c5cb4eca	1
celeryev.831c6f64-0e51-465a-8a32-ad8647708704	0
6401f4de1c924385b8708d36611d694d	1
```

取出任务id 226f45e6-5888-40dd-8cee-49a539364e16 的结果 
http://localhost:8000/test_task_mul_result/226f45e6-5888-40dd-8cee-49a539364e16/
```
➜  ~ rabbitmqctl list_queues
Listing queues ...
celery@zhanghedeMacBook-Pro.local.celery.pidbox	0
celery	0
fdf36b63accd4dffb6be7625c5cb4eca	1
celeryev.831c6f64-0e51-465a-8a32-ad8647708704	0
6401f4de1c924385b8708d36611d694d	1
```

查看队列内部消息结构
```
➜  ~ rabbitmqadmin get queue=celery requeue=true -f pretty_json
[]
➜  ~ rabbitmqadmin get queue=celery@zhanghedeMacBook-Pro.local.celery.pidbox requeue=true -f pretty_json
[]
➜  ~ rabbitmqadmin get queue=celeryev.831c6f64-0e51-465a-8a32-ad8647708704 requeue=true -f pretty_json
[]
➜  ~ rabbitmqadmin get queue=6401f4de1c924385b8708d36611d694d requeue=true
+----------------------------------+---------------+---------------+----------------------------------------------------------------------------------------------------------------------------+---------------+------------------+-------------+
|           routing_key            |   exchange    | message_count |                                                          payload                                                           | payload_bytes | payload_encoding | redelivered |
+----------------------------------+---------------+---------------+----------------------------------------------------------------------------------------------------------------------------+---------------+------------------+-------------+
| 6401f4de1c924385b8708d36611d694d | celeryresults | 0             | {"status": "SUCCESS", "traceback": null, "result": 300, "task_id": "6401f4de-1c92-4385-b870-8d36611d694d", "children": []} | 122           | string           | True        |
+----------------------------------+---------------+---------------+----------------------------------------------------------------------------------------------------------------------------+---------------+------------------+-------------+
➜  ~ rabbitmqadmin get queue=a8d21881e1254526be1077689c80988e requeue=true -f pretty_json
[
  {
    "exchange": "celeryresults",
    "message_count": 0,
    "payload": "{\"status\": \"SUCCESS\", \"traceback\": null, \"result\": 300, \"task_id\": \"a8d21881-e125-4526-be10-77689c80988e\", \"children\": []}",
    "payload_bytes": 122,
    "payload_encoding": "string",
    "properties": {
      "content_encoding": "utf-8",
      "content_type": "application/json",
      "correlation_id": "a8d21881-e125-4526-be10-77689c80988e",
      "delivery_mode": 2,
      "headers": {},
      "priority": 0
    },
    "redelivered": false,
    "routing_key": "a8d21881e1254526be1077689c80988e"
  }
]
```


### 场景测试

- 只设置 broker 为 redis
- 同时设置 broker, backend 为 redis
- broker 为 redis, backend 为 rabbit
- 同时设置 broker, backend 为 rabbit
