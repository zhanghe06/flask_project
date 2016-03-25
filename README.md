## Flask 项目模拟


依赖 redis

部署模式下，同时依赖 nginx

### 项目演示步骤
```
$ cd flask_project
$ virtualenv flask.env
$ source flask.env/bin/activate
$ pip install -r requirements.txt
$ chmod a+x ./etc/db_init.sh
$ ./etc/db_init.sh
```

普通模式启动服务
```
$ ./run.py
```

部署模式启动服务
```
$ supervisord -c etc/supervisord.conf
$ supervisorctl -c etc/supervisord.conf restart all
```

页面结构：

前台展示
```
index.html
blog.html
    /blog/new.html
    /blog/hot.html
    /blog/01.html
    /blog/02.html
about.html
contact.html
```

用户中心
````
user/
    reg.html
    login.html
    index.html
    blog/
        list.html
        add.html
        edit.html
````

后台管理
```
admin/
    login.html
    index.html
    blog.html
    post.html
    site.html
```

项目结构：
```
flask_project/
    app/
        __init__.py
        forms.py
        models.py
        views.py
        static/
            css/
            fonts/
            js/
        templates/
    config.py
    run.py
```


### 安装 flask 以及扩展

创建并进入虚拟环境
```
$ virtualenv flask.env
$ source flask.env/bin/activate
```

初始模块及扩展安装
```
$ pip install Flask
$ pip install Flask-Login
$ pip install Flask-Mail
$ pip install Flask-SQLAlchemy
$ pip install Flask-WTF
$ pip install Flask-OAuthlib
$ pip install sqlacodegen
$ pip install gunicorn
$ pip install supervisor
$ pip freeze > requirements.txt
```

服务部署安装方式
```
$ pip install -r requirements.txt
```


### 创建目录结构

```
$ mkdir app
$ mkdir app/static
$ mkdir app/templates
$ mkdir tmp
```

在 Pycharm 中设置 templates 目录
```
app/templates 目录右键 >> Mark Directory As >> Template Folder
File >> Settings >> Languages & Frameworks >> Python Template Languages >> Template Language: jinja2
```


### 引入 Bootstrap

Bootstrap 是最受欢迎的 HTML、CSS 和 JS 框架，用于开发响应式布局、移动设备优先的 WEB 项目。

Bootstrap 官网：[http://v3.bootcss.com/](http://v3.bootcss.com/)


### 启动 web 服务
```
$ chmod a+x run.py
$ ./run.py
# 可以 Ctrl-C 来终止服务
```

浏览器访问：

[http://localhost:5000](http://localhost:5000)

[http://localhost:5000/index](http://localhost:5000/index)



### 如何生成强壮的密钥
```
In [1]: import os
In [2]: os.urandom(24)
Out[2]: '\x03\xabjR\xbbg\x82\x0b{\x96f\xca\xa8\xbdM\xb0x\xdbK%\xf2\x07\r\x8c'
```


### 创建数据库

模拟数据
```
INSERT INTO author(name, email) VALUES('Mark', 'mark@gmail.com');
INSERT INTO author(name, email) VALUES('Jacob', 'jacob@gmail.com');
INSERT INTO author(name, email) VALUES('Larry', 'larry@gmail.com');
INSERT INTO author(name, email) VALUES('Tom', 'tom@gmail.com');
INSERT INTO author(name, email) VALUES('Lily', 'lily@gmail.com');
```
```
INSERT INTO blog(author, title, pub_date) VALUES('Mark', 'The old man and the sea', '2016-01-11 11:01:05');
INSERT INTO blog(author, title, pub_date) VALUES('Jacob', 'The fault in our stars', '2016-01-11 20:23:27');
INSERT INTO blog(author, title, pub_date) VALUES('Larry', 'The Great Gatsby', '2016-01-11 23:15:18');
INSERT INTO blog(author, title, pub_date) VALUES('Tom', 'Sense and Sensibility', '2016-01-12 12:25:34');
INSERT INTO blog(author, title, pub_date) VALUES('Tom', 'Pride and Prejudice', '2016-01-12 13:17:25');
INSERT INTO blog(author, title, pub_date) VALUES('Lily', 'Game of Thrones', '2016-01-12 14:53:01');
INSERT INTO blog(author, title, pub_date) VALUES('Mark', 'Charlie and the Chocolate Factory', '2016-01-12 15:13:17');
INSERT INTO blog(author, title, pub_date) VALUES('Larry', 'Harry Potter and the Sorcerer''s Stone', '2016-01-12 19:32:15');
INSERT INTO blog(author, title, pub_date) VALUES('Larry', 'The house on mango street', '2016-01-12 01:43:42');
INSERT INTO blog(author, title, pub_date) VALUES('Jacob', 'And then there were none', '2016-01-13 16:17:32');
```

注意：插入内容中如果存在半角单引号（'），需要替换为2个单引号（''）
前提是插入内容在两个单引号之间，存入数据库会自动转义为1个单引号


生成建表语句（备份）
```
$ sqlite3 flask.db ".dump" > schema.sql
```


创建数据库（恢复）:
```
$ sqlite3 flask.db < schema.sql
```

etc 目录下已经创建好脚本（初始化数据，备份数据）
```
$ chmod a+x db_init.sh
$ chmod a+x db_dump.sh
$ ./db_init.sh
```


### SQLAlchemy

python 的一种 ORM 框架

ORM：Object-Relational Mapping

把关系数据库的表结构映射到对象上

使用 Flask-SQLAlchemy 进行数据库管理
```
Database engine     URL
---------------     ---
MySQL               mysql://username:password@hostname/database
Postgres            postgresql://username:password@hostname/database
SQLite (Unix)       sqlite:////absolute/path/to/database
SQLite (Windows)    sqlite:///c:/absolute/path/to/database
```

最常用的 SQLAlchemy 列类型如下：
```
Type name       Python Type         Python type Description
---------       -------             -----------------------
Integer         int                 Integerint Regular integer, typically 32 bits
SmallInteger    int                 Short-range integer, typically 16 bits
BigInteger      int or long         Unlimited precision integer
Float           float               Floating-point number
Numeric         decimal.Decimal     Fixed-point number
String          str                 Variable-length string
Text            str                 Variable-length string, optimized for large or unbound length
Unicode         unicode             Variable-length Unicode string
UnicodeText     unicode             Variable-length Unicode string, optimized for large or unbound length
Boolean         bool                Boolean value
Date            datetime.date       Date value
Time            datetime.time       Time value
DateTime        datetime.datetime   Date and time value
Interval        datetime.timedelta  Time interval
Enum            str                 List of string values
PickleType      Any Python object   Automatic Pickle serialization
LargeBinary     str                 Binary blob
```
模型可以（没有强制要求）定义 __repr()__ 方法，返回一个具有可读性的字符串表示模型，可在调试和测试时使用。

最常见的 SQLAlchemy 选项：
```
Option name     Description
-----------     -----------
primary_key     If set to True , the column is the table’s primary key.
unique          If set to True , do not allow duplicate values for this column.
index           If set to True , create an index for this column, so that queries are more efficient.
nullable        If set to True , allow empty values for this column. If set to False , the column will not allow null values.
default         Define a default value for the column.
```


### sqlacodegen

安装
```
$ pip install sqlacodegen
```

生成 model
```
$ sqlacodegen sqlite:///flask.db --outfile app/models.py
```

参考例子：
```
$ sqlacodegen postgresql:///some_local_db
$ sqlacodegen mysql+oursql://user:password@localhost/db_name
$ sqlacodegen sqlite:///database.db
$ sqlacodegen mysql://root:root@127.0.0.1:3306/db_name > models.py
$ sqlacodegen mysql://root:root@127.0.0.1:3306/db_name --outfile models.py
```

修改 models 文件：

    from sqlalchemy.ext.declarative import declarative_base
    
    
    Base = declarative_base()

替换为：

    from flask.ext.sqlalchemy import SQLAlchemy
    from app import app
    db = SQLAlchemy(app)
    Base = db.Model


[http://docs.sqlalchemy.org/en/latest/core/engines.html](http://docs.sqlalchemy.org/en/latest/core/engines.html)


### 存入数据库中文乱码

SQLALCHEMY_DATABASE_URI = 'mysql://[用户]:[密码]@[IP]/[库名]?charset=utf8'

注意是 utf8 ，不是 utf-8
> show variables like 'character%';
mysql 里的 charset 是 utf8


### 关于分页

错误写法：
```
rows = db_session.query(Author).filter_by(**kwargs).paginate(page, per_page, False)
```

报错如下：
```
AttributeError: 'Query' object has no attribute 'paginate'
```

失败原因：
```
"Query" refers to the SQLAlchemy Query object. 
"BaseQuery" refers to the Flask-SQLALchemy BaseQuery object, which is a subclass of Query. 
This subclass includes helpers such as first_or_404() and paginate().
However, this means that a Query object does NOT have the paginate() function.
How you actually build the object you are calling your "Query" object depends on whether you are dealing with a Query or BaseQuery object.
```

参考：[http://stackoverflow.com/questions/18468887/flask-sqlalchemy-pagination-error](http://stackoverflow.com/questions/18468887/flask-sqlalchemy-pagination-error)

正确写法：
```
rows = Author.query.filter_by(**kwargs).paginate(page, per_page, False)
```

模板中遍历 item，单页 item 序号用 loop.index 表示


### 表单

WTForms 标准 HTML 表单域
```
表单域类型               描述
---------               ----
StringField             文本框
TextAreaField           多行文本框
PasswordField           密码输入框
HiddenField             隐藏文本框
DateField               接收给定格式datetime.date型的文本框
DateTimeField           接收给定格式datetime.datetime型的文本框
IntegerField            接收整型的文本框
DecimalField            接收decimal.Decimal型的文本框
FloadField              接收浮点型的文本框
BooleanField            带有True和False的复选框
RadioField              一组单选框
SelectField             下拉选择框
SelectMultipleField     下拉多选框
FieldField              文件上传框
SubmitField             表单提交按钮
FormField               将一个表单作为表单域嵌入到容器表单中
FieldList               给定类型的表单域列表
```

WTForms 验证
```
验证程序         描述
-------         ----
Email           验证邮箱地址
EqualTo         比较两个域的值；在要求输入两次密码进行确认的时候非常有用
IPAddress       验证IPv4网络地址
Length          验证输入字符串的长度
NumberRange     验证输入的值在数值范围内
Optional        允许输入为空；忽略额外的验证
Required        验证表单域包含数据
Regexp          验证输入的正则表达式
URL             验证一个URL
AnyOf           验证输入是一组可能值中的一个
NoneOf          验证输入不是一组可能值中的一个
```

自定义表单验证

参考官方文档：[http://wtforms.readthedocs.org/en/latest/validators.html#custom-validators](http://wtforms.readthedocs.org/en/latest/validators.html#custom-validators)


### Message Flashing

闪现消息 定义4种类型 success info warning danger

参考：[http://flask.pocoo.org/docs/0.10/patterns/flashing/#flashing-with-categories](http://flask.pocoo.org/docs/0.10/patterns/flashing/#flashing-with-categories)


### 关于时间

python 中：
timestamp=datetime.datetime.utcnow()

sql 模式下：
CURRENT_TIMESTAMP

均为 UTC 时间（非系统本地时间）

把时间设置为 UTC 时区，所有的存储在数据库里的时间将是 UTC 格式，用户可能在世界各地写微博，因此我们需要使用统一的时间单位。

另外，sqlite 并不支持像 mysql 有这种 DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP 触发器的简单语法。
其实更新时间完全可以在程序中控制。

若缺省值是 CURRENT_TIME、CURRENT_DATE 或 CURRENT_TIMESTAMP，则当前 UTC 日期和/或时间被插入字段。

CURRENT_TIME 的格式为 “HH:MM:SS”

CURRENT_DATE 为 “YYYY-MM-DD”

而 CURRENT_TIMESTAMP 是 “YYYY-MM-DD HH:MM:SS”


### 用户登陆

Flask-Login 扩展需要在我们 model 的 User 类里实现一些方法。：

    def is_authenticated(self):
            return True
    
    def is_active(self):
        return True
    
    def is_anonymous(self):
        return False
    
    def get_id(self):
        try:
            return unicode(self.id)  # python 2
        except NameError:
            return str(self.id)  # python 3

g.user 视图和模板都可以用

current_user 仅仅支持视图


### 用 jQuery 实现 Ajax

[http://www.pythondoc.com/flask/patterns/jquery.html](http://www.pythondoc.com/flask/patterns/jquery.html)


### Bootstrap 轮播（Carousel）插件

[http://www.runoob.com/bootstrap/bootstrap-carousel-plugin.html](http://www.runoob.com/bootstrap/bootstrap-carousel-plugin.html)


## 部署方案( Nginx + Gunicorn + Supervisor )

生产环境下，flask 自带的 服务器，无法满足性能要求。我们这里采用 gunicorn 做 wsgi 容器，用来部署 python。

Gunicorn 官网：[http://gunicorn.org/](http://gunicorn.org/)

参考：[virtualenv 环境下 Flask + Nginx + Gunicorn+ Supervisor 搭建 Python Web](http://www.ituring.com.cn/article/201045?utm_source=tuicool)

安装
```
$ pip install gunicorn
```
用 gunicorn 启动 flask
```
$ gunicorn -w4 -b0.0.0.0:8000 app:app
[2016-03-02 15:22:44 +0000] [14362] [INFO] Starting gunicorn 19.4.5
[2016-03-02 15:22:44 +0000] [14362] [INFO] Listening at: http://0.0.0.0:8000 (14362)
[2016-03-02 15:22:44 +0000] [14362] [INFO] Using worker: sync
[2016-03-02 15:22:44 +0000] [14367] [INFO] Booting worker with pid: 14367
[2016-03-02 15:22:44 +0000] [14370] [INFO] Booting worker with pid: 14370
[2016-03-02 15:22:45 +0000] [14373] [INFO] Booting worker with pid: 14373
[2016-03-02 15:22:45 +0000] [14374] [INFO] Booting worker with pid: 14374
```
此时，我们需要用 8000 的端口进行访问，原先的5000并没有启用。

安装 supervisor
```
$ pip install supervisor
$ echo_supervisord_conf > etc/supervisord.conf
```

新增如下配置
```
[program:app]
command="gunicorn -w 4 -b 0.0.0.0:8000 app:app"
startsecs=0
stopwaitsecs=0
autostart=false
autorestart=false
stdout_logfile=log/gunicorn.log
stderr_logfile=log/gunicorn.err
```

启动 supervisord 服务
```
$ supervisord -c etc/supervisord.conf
```

常用命令
```
supervisord -c etc/supervisord.conf
supervisorctl -c etc/supervisord.conf status                  查看supervisor的状态
supervisorctl -c etc/supervisord.conf reload                  重新载入 配置文件
supervisorctl -c etc/supervisord.conf start [all]|[appname]   启动指定/所有 supervisor 管理的程序进程
supervisorctl -c etc/supervisord.conf stop [all]|[appname]    关闭指定/所有 supervisor 管理的程序进程
supervisorctl -c etc/supervisord.conf restart [all]|[appname] 重启指定/所有 supervisor 管理的程序进程
```

supervisor 还有一个 web 的管理界面，可以激活。更改下配置：
```
[inet_http_server]         ; inet (TCP) server disabled by default
port=127.0.0.1:9001        ; (ip_address:port specifier, *:port for all iface)
username=admin             ; (default is no username (open server))
password=123456            ; (default is no password (open server))
```
```
[supervisorctl]
serverurl=unix:///tmp/supervisor.sock ; use a unix:// URL  for a unix socket
serverurl=http://127.0.0.1:9001       ; use an http:// url to specify an inet socket
username=admin                        ; should be same as http_username if set
password=123456                       ; should be same as http_password if set
;prompt=mysupervisor                  ; cmd line prompt (default "supervisor")
;history_file=~/.sc_history           ; use readline history if available
```
用户名 和 密码 必须一致，也可以同时注释掉。

重新加载配置 并 重启服务
```
$ supervisorctl -c etc/supervisord.conf reload
$ supervisorctl -c etc/supervisord.conf restart all
```

浏览器访问 [http://127.0.0.1:9001](http://127.0.0.1:9001) 可以得到 supervisor 的 web 管理界面，
访问 [http://127.0.0.1:8000](http://127.0.0.1:8000) 可以看见 gunicorn 启动的返回的页面。

nginx 服务
```
sudo service nginx start
sudo service nginx stop
sudo service nginx restart
```

```
进入项目目录
$ sudo ln -s `pwd`/etc/nginx.conf /etc/nginx/conf.d/flask_app_nginx.conf
$ sudo nginx -s reload  # 平滑重启
$ sudo subl /etc/hosts
# 127.0.0.1    www.flask_app.com
```

查看 ip 地址
```
$ ifconfig eth0 | grep 'inet ' | awk '{print $2}'
```

nginx 静态资源目录配置
```
$ sudo mkdir -p /data/static
$ sudo chown nginx. /data -R
$ sudo ln -s /data/static /home/zhanghe/code/flask_project/app/static
```

为了保证网站安全（避免上传漏洞），需要正确权限配置（目录755，静态文件644权限）
```
$ cd /data/
$ find ./ -type d -print | xargs chmod 755
$ find ./ -type f -print | xargs chmod 644
```

不建议以下为方便而设置的777权限
```
$ sudo chmod 777 -R /data/static/
```

新增 nginx 配置信息
```
location ~ ^/static/ {
    root /data/;
    #过期30天，静态文件不怎么更新，过期可以设大一点，如果频繁更新，则可以设置得小一点。
    expires 30d;
}
```


## 统计代码行数(包含注释)

查看项目python代码行数
```
$ find ./app -type f -name "*.py" | xargs wc -l
```

查看项目模板文件行数
```
$ find ./app -type f -name "*.html" | xargs wc -l
```


## 调试

在 Python 应用程序中设置断点
```
import pdb; pdb.set_trace()
```


## 远程调试
```
$ pip install remote-pdb
```

远程调试配置代码（添加web服务启动之前）：
```
import signal
import os


def handle_pdb(sig, frame):
    from remote_pdb import RemotePdb
    print sig, frame
    RemotePdb('0.0.0.0', 48110).set_trace()  # 如将ip地址设置为127.0.0.1，只能本机调试

signal.signal(signal.SIGUSR1, handle_pdb)
print('pid:%s' % os.getpid())
```

调试过程：

一、服务启动
```
$ ./run.py 
pid:7892
 * Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
10 <frame object at 0x7fb9010259d8>
CRITICAL:root:RemotePdb session open at 127.0.0.1:48110, waiting for connection ...
RemotePdb session open at 0.0.0.0:48110, waiting for connection ...
CRITICAL:root:RemotePdb accepted connection from ('127.0.0.1', 41497).
RemotePdb accepted connection from ('127.0.0.1', 41497).
```
终端输出的进程id 为 7892

二、给进程7892 发送终止信号
```
$ kill -10 7892
```

三、远程登陆
```
$ telnet 127.0.0.1 48110
Trying 127.0.0.1...
Connected to 127.0.0.1.
Escape character is '^]'.
--Return--
> /home/zhanghe/code/flask_project/run.py(21)handle_pdb()->None
-> RemotePdb('127.0.0.1', 48110).set_trace()
(Pdb) 
```

四、退出调试(2步)：
Ctrl + ], q
```
(Pdb) ^]

telnet> q
Connection closed.
```
此时，程序继续运行（web继续提供服务）

pdb 可以执行命令：
直接回车是重复前一条命令！
p(print) 查看一个变量值
n(next) 下一步
s(step) 单步,可进入函数
c(continue)继续前进
l(list)看源代码

查看系统支持的信号列表
```
$ kill -l
 1) SIGHUP	 2) SIGINT	 3) SIGQUIT	 4) SIGILL	 5) SIGTRAP
 6) SIGABRT	 7) SIGBUS	 8) SIGFPE	 9) SIGKILL	10) SIGUSR1
11) SIGSEGV	12) SIGUSR2	13) SIGPIPE	14) SIGALRM	15) SIGTERM
16) SIGSTKFLT	17) SIGCHLD	18) SIGCONT	19) SIGSTOP	20) SIGTSTP
21) SIGTTIN	22) SIGTTOU	23) SIGURG	24) SIGXCPU	25) SIGXFSZ
26) SIGVTALRM	27) SIGPROF	28) SIGWINCH	29) SIGIO	30) SIGPWR
31) SIGSYS	34) SIGRTMIN	35) SIGRTMIN+1	36) SIGRTMIN+2	37) SIGRTMIN+3
38) SIGRTMIN+4	39) SIGRTMIN+5	40) SIGRTMIN+6	41) SIGRTMIN+7	42) SIGRTMIN+8
43) SIGRTMIN+9	44) SIGRTMIN+10	45) SIGRTMIN+11	46) SIGRTMIN+12	47) SIGRTMIN+13
48) SIGRTMIN+14	49) SIGRTMIN+15	50) SIGRTMAX-14	51) SIGRTMAX-13	52) SIGRTMAX-12
53) SIGRTMAX-11	54) SIGRTMAX-10	55) SIGRTMAX-9	56) SIGRTMAX-8	57) SIGRTMAX-7
58) SIGRTMAX-6	59) SIGRTMAX-5	60) SIGRTMAX-4	61) SIGRTMAX-3	62) SIGRTMAX-2
63) SIGRTMAX-1	64) SIGRTMAX
```

以上程序使用的 SIGUSR1 是终止进程信号，为用户定义信号1


参考文档
[https://pypi.python.org/pypi/remote-pdb](https://pypi.python.org/pypi/remote-pdb)


## 参考资料：

[Flask 代码模式](http://docs.jinkan.org/docs/flask/patterns/index.html)


## 安全设置

- 路由参数 校验参数类型，格式

例如：
```
@app.route('/blog/edit/<int:blog_id>/', methods=['GET', 'POST'])
```
防止 XSS 漏洞

- 主键设置为整型（为方便底层操作，统一命名为 id）

好处：安全（防止因代码疏忽而导致的 XSS 漏洞），效率

- 链接中的重定向参数(next)不能为外链

防止 URL 重定向/跳转漏洞



## Todo：

- Nginx https 部署

- 第三方登陆


- 第三方支付

- 找回密码安全设置
参考：[密码找回功能可能存在的问题](http://drops.wooyun.org/web/3295)

- 接口参数签名校验的必要性
参考：[在线支付逻辑漏洞总结](http://drops.wooyun.org/papers/345)


## GitHub 操作

…or create a new repository on the command line
```
echo "# flask_project" >> README.md
git init
git add README.md
git commit -m "first commit"
git remote add origin git@github.com:zhanghe06/flask_project.git
git push -u origin master
```

…or push an existing repository from the command line
```
git remote add origin git@github.com:zhanghe06/flask_project.git
git push -u origin master
```
