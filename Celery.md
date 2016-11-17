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
