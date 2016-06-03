# Flask 缓存

参考：[http://www.pythondoc.com/flask/patterns/caching.html](http://www.pythondoc.com/flask/patterns/caching.html)

Flask 本身不提供缓存，但是它的基础库之一 Werkzeug 有一些非常基本的缓存支持。

- SimpleCache
- MemcachedCache
- RedisCache
- FileSystemCache


测试如下：

views.py

```
from werkzeug.contrib.cache import SimpleCache
cache = SimpleCache()  # 默认最大支持500个key, 超时时间5分钟, 参数可配置
```

```
@app.route('/test_cache/')
def test_cache():
    """
    缓存测试
    5.01s >> 9ms
    """
    import time
    rv = cache.get('my-item')
    if rv is None:
        time.sleep(5)
        rv = 'Hello, Cache!'
        cache.set('my-item', rv, timeout=5 * 10)
    return rv
```
