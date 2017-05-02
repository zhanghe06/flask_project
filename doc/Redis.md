## Installation

http://redis.io/download

Download, extract and compile Redis with:
```
$ wget http://download.redis.io/releases/redis-3.2.4.tar.gz
$ tar xzf redis-3.2.4.tar.gz
$ cd redis-3.2.4
$ make
```

```
$ src/redis-server
```

```
$ src/redis-cli
```

配置软链(Mac)
```
$ ln -s /Users/zhanghe/tools/redis-3.2.4/src/redis-server /usr/local/bin/redis-server
$ ln -s /Users/zhanghe/tools/redis-3.2.4/src/redis-cli /usr/local/bin/redis-cli
```


## 配置

修改配置：redis.conf
```
protected-mode yes
>>
protected-mode no

# masterauth <master-password>
>>
masterauth 123456

# requirepass foobared
>>
requirepass 123456

bind 127.0.0.1
>>
bind 0.0.0.0
```

重启服务
```
redis-cli shutdown
redis-server redis.conf
```
