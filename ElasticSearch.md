## ElasticSearch 2.x

参考： [https://www.elastic.co/guide/en/elasticsearch/reference/current/setup-repositories.html](https://www.elastic.co/guide/en/elasticsearch/reference/current/setup-repositories.html)

Download and install the Public Signing Key:
```
$ wget -qO - https://packages.elastic.co/GPG-KEY-elasticsearch | sudo apt-key add -
```

Save the repository definition to /etc/apt/sources.list.d/elasticsearch-2.x.list:
```
$ echo "deb http://packages.elastic.co/elasticsearch/2.x/debian stable main" | sudo tee -a /etc/apt/sources.list.d/elasticsearch-2.x.list
```

Run apt-get update and the repository is ready for use. You can install it with:
```
$ sudo apt-get update && sudo apt-get install elasticsearch
```

Configure Elasticsearch to automatically start during bootup.
If your distribution is using SysV init (Ubuntu 14.04 LTS), then you will need to run:
```
$ sudo update-rc.d elasticsearch defaults 95 10
```
Otherwise if your distribution is using systemd (Ubuntu 16.04 LTS):
```
$ sudo /bin/systemctl daemon-reload
$ sudo /bin/systemctl enable elasticsearch.service
```

Start Elasticsearch Server
```
$ sudo /etc/init.d/elasticsearch start
 * Starting Elasticsearch Server             [ OK ]
$ sudo /etc/init.d/elasticsearch status
 * elasticsearch is running
```

Test by curl
```
$ curl -X GET 'http://localhost:9200'
{
  "name" : "Sub-Mariner",
  "cluster_name" : "elasticsearch",
  "version" : {
    "number" : "2.3.1",
    "build_hash" : "bd980929010aef404e7cb0843e61d0665269fc39",
    "build_timestamp" : "2016-04-04T12:25:05Z",
    "build_snapshot" : false,
    "lucene_version" : "5.5.0"
  },
  "tagline" : "You Know, for Search"
}
```

[http://localhost:9200/](http://localhost:9200/)


## Plugin

### elasticsearch-head

A web front end for an Elasticsearch cluster

Install elasticsearch-head for Elasticsearch 2.x
```
$ sudo /usr/share/elasticsearch/bin/plugin install mobz/elasticsearch-head
```

[https://github.com/mobz/elasticsearch-head](https://github.com/mobz/elasticsearch-head)

[http://localhost:9200/_plugin/head/](http://localhost:9200/_plugin/head/)

