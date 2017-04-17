Flower: Real-time Celery web-monitor

https://flower.readthedocs.io/en/latest/


Install Flower
```
$ pip install flower
```

Running the flower command
```
$ celery flower -A app.celery_worker.celery_app --port=5555
$ celery flower -A app.celery_worker.celery_app --port=5555 --broker=redis://localhost:6379/0 --broker_api=redis://localhost:6379/0
```

```
$ open http://localhost:5555
```

http://flower.readthedocs.io/en/latest/config.html#broker-api

```
$ flower -A app.celery_worker.celery_app --broker_api=http://guest:guest@rabbit@zhanghedeMacBook-Pro:15672/api/
```
