## UbuntuServer
ubuntu-16.04.2-server-amd64
```
$ lsb_release -a
No LSB modules are available.
Distributor ID:	Ubuntu
Description:	Ubuntu 16.04.2 LTS
Release:	16.04
Codename:	xenial
$ lsb_release -c
Codename:	xenial
```

### 服务器安装 OpenSSH服务
OpenSSH是SSH的替代软件，而且是免费的
```
$ sudo apt-get install openssh-server
$ /etc/init.d/ssh status
```

### 更换国内源
参考：[http://wiki.ubuntu.org.cn/源列表](http://wiki.ubuntu.org.cn/源列表)

```
$ sudo cp /etc/apt/sources.list /etc/apt/sources.list_backup
$ sudo vim /etc/apt/sources.list
```
替换：
```
deb http://mirrors.aliyun.com/ubuntu/ xenial main restricted universe multiverse
deb http://mirrors.aliyun.com/ubuntu/ xenial-security main restricted universe multiverse
deb http://mirrors.aliyun.com/ubuntu/ xenial-updates main restricted universe multiverse
deb http://mirrors.aliyun.com/ubuntu/ xenial-proposed main restricted universe multiverse
deb http://mirrors.aliyun.com/ubuntu/ xenial-backports main restricted universe multiverse
deb-src http://mirrors.aliyun.com/ubuntu/ xenial main restricted universe multiverse
deb-src http://mirrors.aliyun.com/ubuntu/ xenial-security main restricted universe multiverse
deb-src http://mirrors.aliyun.com/ubuntu/ xenial-updates main restricted universe multiverse
deb-src http://mirrors.aliyun.com/ubuntu/ xenial-proposed main restricted universe multiverse
deb-src http://mirrors.aliyun.com/ubuntu/ xenial-backports main restricted universe multiverse
```
更新：
```
$ sudo apt-get update
```

### docker 安装

准备 add-apt-repository
```
$ sudo apt-get install python-software-properties
$ sudo apt-get install software-properties-common
```

1. Set up the repository
```
$ sudo apt-get -y install \
  apt-transport-https \
  ca-certificates \
  curl

$ curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -

$ sudo add-apt-repository \
       "deb [arch=amd64] https://download.docker.com/linux/ubuntu \
       $(lsb_release -cs) \
       stable"

$ sudo apt-get update
```

2. Get Docker CE
```
$ sudo apt-get -y install docker-ce
```

```
$ sudo docker -v
Docker version 17.03.1-ce, build c6d412e
```
