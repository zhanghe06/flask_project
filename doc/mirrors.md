## 系统源镜像

http://www.debian.org/mirror/list

http://mirrors.aliyun.com/

若使用阿里云服务器, 将源的域名从 mirrors.aliyun.com 改为 mirrors.aliyuncs.com 不占用公网流量。

以 debian 8.x (jessie) 为例

```
sudo vim /etc/apt/sources.list
```

163源
```
deb http://mirrors.163.com/debian/ jessie main non-free contrib
deb http://mirrors.163.com/debian/ jessie-updates main non-free contrib
deb http://mirrors.163.com/debian/ jessie-backports main non-free contrib
deb-src http://mirrors.163.com/debian/ jessie main non-free contrib
deb-src http://mirrors.163.com/debian/ jessie-updates main non-free contrib
deb-src http://mirrors.163.com/debian/ jessie-backports main non-free contrib
deb http://mirrors.163.com/debian-security/ jessie/updates main non-free contrib
deb-src http://mirrors.163.com/debian-security/ jessie/updates main non-free contrib
```

阿里源
```
deb http://mirrors.aliyun.com/debian/ jessie main non-free contrib
deb http://mirrors.aliyun.com/debian/ jessie-proposed-updates main non-free contrib
deb-src http://mirrors.aliyun.com/debian/ jessie main non-free contrib
deb-src http://mirrors.aliyun.com/debian/ jessie-proposed-updates main non-free contrib
```

```
sudo apt-get update
```


## pypi 镜像

参考：

阿里镜像：http://mirrors.aliyun.com/help/pypi

官方镜像：https://pypi.python.org/mirrors

~/.pip/pip.conf
```
[global]
index-url = http://mirrors.aliyun.com/pypi/simple/

[install]
trusted-host=mirrors.aliyun.com
```
