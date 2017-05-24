## 生成证书

证书生成工具：

https://certificatetools.com/


可以通过以下步骤生成一个简单的证书：

首先，进入你想创建证书和私钥的目录，例如：
```
$ cd ssl
```

创建服务器私钥，命令会让你输入一个口令(为了简便：123456, 强烈不推荐)：
```
$ openssl genrsa -des3 -out ca.key 1024
```
```
Generating RSA private key, 1024 bit long modulus
.............................++++++
......++++++
e is 65537 (0x10001)
Enter pass phrase for ca.key:
Verifying - Enter pass phrase for ca.key:
```

创建签名请求的证书（CSR）：
```
$ openssl req -new -key ca.key -out server.csr
```
```
Enter pass phrase for ca.key:
You are about to be asked to enter information that will be incorporated
into your certificate request.
What you are about to enter is what is called a Distinguished Name or a DN.
There are quite a few fields but you can leave some blank
For some fields there will be a default value,
If you enter '.', the field will be left blank.
-----
Country Name (2 letter code) [AU]:CN
State or Province Name (full name) [Some-State]:Shanghai
Locality Name (eg, city) []:HuangPu
Organization Name (eg, company) [Internet Widgits Pty Ltd]:Shanghai Flask Project Ltd
Organizational Unit Name (eg, section) []:Flask Organization
Common Name (e.g. server FQDN or YOUR name) []:*.app.com
Email Address []:admin@app.com

Please enter the following 'extra' attributes
to be sent with your certificate request
A challenge password []:
An optional company name []:Shanghai Flask App Ltd
```

在加载SSL支持的Nginx并使用上述私钥时除去必须的口令：
```
$ openssl rsa -in ca.key -out server.key
```
```
Enter pass phrase for ca.key:
writing RSA key
```

最后标记证书使用上述私钥和CSR：
```
$ openssl x509 -req -days 365 -in server.csr -signkey server.key -extfile v3.ext -out server.crt
```
```
Signature ok
subject=/C=CN/ST=Shanghai/L=HuangPu/O=Shanghai Flask Project Ltd/OU=Flask Organization/CN=*.app.com/emailAddress=admin@app.com
Getting Private key
```

## 配置 Nginx

修改Nginx配置文件，让其包含新标记的证书和私钥：
```
server {
    server_name www.app.com;
    listen 443;
    ssl on;
    ssl_certificate /home/zhanghe/code/flask_project/ssl/server.crt;
    ssl_certificate_key /home/zhanghe/code/flask_project/ssl/server.key;
}
```
重启 nginx。

这样就可以通过以下方式访问：
[https://www.app.com](https://www.app.com)

另外还可以加入如下代码实现80端口重定向到443
```
server {
    listen 80;
    server_name www.app.com;
    rewrite ^(.*) https://$server_name$1 permanent;
}
```

访问页面，会出现提示：该网站的安全证书不受信任！

仍然继续访问, https 标识为 X

三道杠 >> 设置 >> HTTPS/SSL >> 管理证书 >> 证书管理器 >> 授权中心 >> 导入 >> 选择证书 >> 勾选信任该证书，以标识网站的身份。

再次访问，图标变为绿色，心情瞬间变好了。
