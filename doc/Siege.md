## Siege 压力测试


100并发，发生2次
```
$ siege -c 100 -r 2 http://0.0.0.0:8010/performance/
```

自带的web服务
```
Transactions:                200 hits
Availability:             100.00 %
Elapsed time:               3.21 secs
Data transferred:           0.00 MB
Response time:              0.95 secs
Transaction rate:          62.31 trans/sec
Throughput:             0.00 MB/sec
Concurrency:               59.36
Successful transactions:         200
Failed transactions:               0
Longest transaction:            1.55
Shortest transaction:           0.15
```

Gunicorn
```
Transactions:               200 hits
Availability:             100.00 %
Elapsed time:               1.66 secs
Data transferred:           0.00 MB
Response time:              0.34 secs
Transaction rate:         120.48 trans/sec
Throughput:             0.00 MB/sec
Concurrency:               40.89
Successful transactions:         200
Failed transactions:               0
Longest transaction:            0.66
Shortest transaction:           0.04
```

Gunicorn 性能也只是 Flask 自带服务的一倍
