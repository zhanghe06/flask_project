## Python MongoDB

mongo数据库安装（包含服务端/客户端）
```
$ sudo apt-get install mongodb
```

mongo仅客户端安装
```
$ sudo apt-get install mongodb-clients
```

pymongo安装(虚拟环境不需要sudo)
```
$ sudo pip install pymongo
```

命令行简单命令：
```
> show dbs
> use [db]
> show tables
> show collections
> db.[table/collection].find().pretty()
```

最新版安装记录(3.0版本不支持32位系统，最后一步无法安装)
```
$ sudo apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv 7F0CEB10
$ echo "deb http://repo.mongodb.org/apt/ubuntu "$(lsb_release -sc)"/mongodb-org/3.0 multiverse" | sudo tee /etc/apt/sources.list.d/mongodb-org-3.0.list
$ sudo apt-get update
$ sudo apt-get install -y mongodb-org
```

32位系统安装最新版（最高支持到2.6）方式：
```
$ sudo apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv 7F0CEB10
$ echo 'deb http://downloads-distro.mongodb.org/repo/ubuntu-upstart dist 10gen' | sudo tee /etc/apt/sources.list.d/mongodb.list
$ sudo apt-get update
$ sudo apt-get install -y mongodb-org
```

服务启动关闭重启
```
$ sudo service mongod start
$ sudo service mongod stop
$ sudo service mongod restart
```

参考：

[mongo最新版安装，仅支持64位](https://docs.mongodb.org/manual/tutorial/install-mongodb-on-ubuntu/)

[mongo最新版安装，32位系统](https://docs.mongodb.org/v2.6/tutorial/install-mongodb-on-ubuntu/)

[pymongo安装](http://api.mongodb.org/python/current/installation.html)

[官网教程](http://api.mongodb.org/python/current/tutorial.html)


## Mac 操作

安装
```
brew update
brew install mongodb --with-openssl
```

启动服务
```
mkdir data/db_mongo
mongod --dbpath data/db_mongo
或者
mongod --config /usr/local/etc/mongod.conf
```

## 

创建管理员
```
> use admin
switched to db admin
> db.createUser(
...   {
...     user: "root",
...     pwd: "123456",
...     roles: [ { role: "userAdminAnyDatabase", db: "admin" } ]
...   }
... )
Successfully added user: {
	"user" : "root",
	"roles" : [
		{
			"role" : "userAdminAnyDatabase",
			"db" : "admin"
		}
	]
}
```

开启权限控制
```
mongod --auth --port 27017 --dbpath data/db_mongo
mongo --port 27017 -u "root" -p "123456" --authenticationDatabase "admin"
```

创建普通用户
```
> use admin
> db.auth("root", "1234567")
Error: Authentication failed.
0
> db.auth("root", "123456")
1
```

```
use test
db.createUser(
  {
    user: "www",
    pwd: "123456",
    roles: [ { role: "readWrite", db: "flask_project" } ]
  }
)
```
