## Flask 项目模拟


- product 生产环境
- develop 开发环境

### 项目演示步骤

虚拟环境 部署方式
```
$ cd flask_project                  # 进入项目目录
$ virtualenv flask.env              # 新建虚拟环境
$ source flask.env/bin/activate     # 进入虚拟环境
$ pip install -r requirements.txt   # 安装环境依赖
$ python run_frontend.py            # 开启前台服务
$ python run_backend.py             # 开启后台服务
```

也可以 docker 方式部署
```
$ cd flask_project/docker           # 进入Docker脚本目录
$ sh docker/docker_build.sh         # 创建本地Docker镜像
$ sh docker/docker_run.sh           # 运行本地Docker容器
```


### 安装 flask 以及扩展

创建并进入虚拟环境
```
$ virtualenv flask.env
$ source flask.env/bin/activate
```

项目服务依赖
```
Nginx
Redis
MariaDB
RabbitMQ
MongoDB
```


项目扩展依赖
```
$ pip install Flask
$ pip install Flask-Login
$ pip install Flask-Mail
$ pip install Flask-SQLAlchemy
$ pip install Flask-WTF
$ pip install Flask-OAuthlib
$ pip install Flask-Excel
$ pip install Flask-Moment
$ pip install Flask-Uploads
$ pip install Flask-Principal
$ pip install Flask-Babel
$ pip install sqlacodegen
$ pip install gunicorn
$ pip install schedule
$ pip install supervisor
$ pip install redis
$ pip install requests
$ pip install celery
$ pip install librabbitmq
$ pip install pika
$ pip install Pillow
$ pip install sshtunnel
$ pip install MySQL-python
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

项目地址：https://github.com/twbs/bootstrap

Bootstrap 英文官网：http://getbootstrap.com/

Bootstrap 中文网：http://www.bootcss.com/

Bootstrap CDN
```
<!-- Latest compiled and minified CSS -->
<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css" integrity="sha384-BVYiiSIFeK1dGmJRAkycuHAHRg32OmUcww7on3RYdg4Va+PmSTsz/K68vbdEjh4u" crossorigin="anonymous">

<!-- Optional theme -->
<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap-theme.min.css" integrity="sha384-rHyoN1iRsVXV4nD0JutlnGaslCJuC7uwjduW9SVrLvRYooPp2bWYgmgJQIXwl/Sp" crossorigin="anonymous">

<!-- Latest compiled and minified JavaScript -->
<script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js" integrity="sha384-Tc5IQib027qvyjSMfHjOMaLkfuWVxZxUPnCJA7l2mCWNIpG9mGCD8wGNIcPD7Txa" crossorigin="anonymous"></script>
```

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

官方文档:
[SQLAlchemy 1.0 Documentation](http://docs.sqlalchemy.org/en/rel_1_0/orm/tutorial.html)

[常见的过滤器运算符 Common Filter Operators](http://docs.sqlalchemy.org/en/rel_1_0/orm/tutorial.html#common-filter-operators)

[动态获取 Model 对象的主键](http://docs.sqlalchemy.org/en/latest/orm/internals.html#sqlalchemy.orm.state.InstanceState.identity)


打开自动提交
```
from flask.ext.sqlalchemy import SQLAlchemy
db = SQLAlchemy(session_options={'autocommit': True})
后者:
SQLALCHEMY_COMMIT_ON_TEARDOWN = True  # 打开自动提交
```

联表(内联)分页查询
```
paginate = User.query.join(UserProfile, User.id == UserProfile.user_id).add_entity(UserProfile).order_by(User.id.desc()).paginate(1, 10, False)

print paginate.items
    for (user, user_profile) in paginate.items:
        print user.id, user_profile.user_id
```
如果需要外联，join 替换为 outerjoin 即可


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

注意：

添加选项 --noinflect 否则工具默认会将表名后缀s去掉


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

注意事项：
NumberRange 校验只对数值类型（IntegerField，FloadField，DecimalField）生效；字符串类型（StringField）不生效

DataRequired, InputRequired 的区别

- DataRequired 检查类型转换后的值，是否为真（即 if field.data）
- InputRequired 检查原始输入的值，是否为真


### CSRF
跨站请求伪造

攻击方式：
    利用用户身份执行非法请求（在用户浏览器端发起特定请求）
防御策略：
    通常使用csrf_token防御

http://flask-wtf.readthedocs.io/en/stable/csrf.html

Any view using FlaskForm to process the request is already getting CSRF protection. 
也就是使用FlaskForm的表单默认都会受到保护

HTML Forms
```html
<form method="post">
    {{ form.csrf_token }}
</form>
```

```html
<form method="post">
    <input type="hidden" name="csrf_token" value="{{ csrf_token() }}"/>
</form>
```

JavaScript Requests
```html
<script type="text/javascript">
    var csrf_token = "{{ csrf_token() }}";

    $.ajaxSetup({
        beforeSend: function(xhr, settings) {
            if (!/^(GET|HEAD|OPTIONS|TRACE)$/i.test(settings.type) && !this.crossDomain) {
                xhr.setRequestHeader("X-CSRFToken", csrf_token);
            }
        }
    });
</script>
```

### Message Flashing

闪现消息 定义4种类型 success info warning danger

参考：[http://flask.pocoo.org/docs/0.10/patterns/flashing/#flashing-with-categories](http://flask.pocoo.org/docs/0.10/patterns/flashing/#flashing-with-categories)


如果需要自动关闭
```
$("#success-alert").fadeTo(2000, 500).slideUp(500, function(){
    $("#success-alert").slideUp(500);
});
```

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

注意：
数据库表中的创建时间字段一般会设置缺省当前时间。
保存数据时，如果程序中，创建时间为空，创建时间字段存储的是数据库服务器的当前时间；
如果程序中直接设置好创建时间为当前时间，则保存的创建时间字段是代码服务器的当前时间。
生产环境通常 web 与 db 是分开的，时钟往往不同步。
不同开发人员程序中如果不统一的话，会造成麻烦。

Flask-Moment 本地化日期和时间

https://github.com/miguelgrinberg/Flask-Moment

[http://momentjs.com/](http://momentjs.com/)

例子
```
{{ moment().fromNow(refresh=True).format('LLLL') }}
```

页面配置

本地加载：
```
<script src="{{ url_for('static', filename='plugin/moment-2.18.1/min/moment-with-locales.min.js') }}"></script>
<script>
    moment.locale("zh-cn");
    function flask_moment_render(elem) {
        $(elem).text(eval('moment("' + $(elem).data('timestamp') + '").' + $(elem).data('format') + ';'));
        $(elem).removeClass('flask-moment').show();
    }
    function flask_moment_render_all() {
        $('.flask-moment').each(function () {
            flask_moment_render(this);
            if ($(this).data('refresh')) {
                (function (elem, interval) {
                    setInterval(function () {
                        flask_moment_render(elem)
                    }, interval);
                })(this, $(this).data('refresh'));
            }
        })
    }
    $(document).ready(function () {
        flask_moment_render_all();
    });
</script>
```

cdn方案：
```
{{ moment.include_moment() }}
{{ moment.locale('zh-cn') }}
```


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


[https://flask-login.readthedocs.io/en/latest/](https://flask-login.readthedocs.io/en/latest/)


### 用 jQuery 实现 Ajax

[http://www.pythondoc.com/flask/patterns/jquery.html](http://www.pythondoc.com/flask/patterns/jquery.html)


### Bootstrap 轮播（Carousel）插件

[http://www.runoob.com/bootstrap/bootstrap-carousel-plugin.html](http://www.runoob.com/bootstrap/bootstrap-carousel-plugin.html)


### 轮播大图样式

- 选择 宽度1920 高度610 的高画质图片
- 主要图像内容信息集中在中间1024的区域


### Swiper 移动端触摸滑动插件

[http://www.swiper.com.cn/](http://www.swiper.com.cn/)


### Slideout.js 侧滑插件

[https://github.com/mango/slideout](https://github.com/mango/slideout)


### LightBox 插件

参考: [LightBox.md](doc/LightBox.md)


### Chart.js 图表插件

[http://www.bootcss.com/p/chart.js/docs/](http://www.bootcss.com/p/chart.js/docs/)

响应式辅助参数：
responsive: true


## clipboard.js 剪贴板插件

https://github.com/zenorocha/clipboard.js/


## Flask-Excel

http://flask-excel.readthedocs.io/en/latest/

支持 csv tsv 导出
如果需要导出 xls 格式，需要安装 pyexcel-xls


## Flask-Uploads

https://pythonhosted.org/Flask-Uploads/


## Flask-Principal

http://pythonhosted.org/Flask-Principal/
http://flask-principal-cn.readthedocs.io/zh_CN/latest/



## Flask-DebugToolbar
https://flask-debugtoolbar.readthedocs.io/en/latest/


## 部署方案( Nginx + Gunicorn + Supervisor )

生产环境下，flask 自带的 服务器，无法满足性能要求。我们这里采用 gunicorn 做 wsgi 容器，用来部署 python。

Gunicorn 官网：[http://gunicorn.org/](http://gunicorn.org/)

参考：[virtualenv 环境下 Flask + Nginx + Gunicorn+ Supervisor 搭建 Python Web](http://www.ituring.com.cn/article/201045?utm_source=tuicool)

Supervisor 重启 Gunicorn 时，有时会碰到 Gunicorn 起不来的情况
查看端口占用情况
```
# netstat -tulpn
Active Internet connections (only servers)
Proto Recv-Q Send-Q Local Address           Foreign Address         State       PID/Program name
tcp        0      0 0.0.0.0:8000            0.0.0.0:*               LISTEN      1722/python
tcp        0      0 127.0.0.1:9001          0.0.0.0:*               LISTEN      1/python
tcp        0      0 0.0.0.0:8010            0.0.0.0:*               LISTEN      647/python
# kill -9 PID
```

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

进程数的推荐配置：
workers = multiprocessing.cpu_count() * 2 + 1

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
# 127.0.0.1    www.flask-app.com
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

Nginx https 部署

参考: [https.md](doc/https.md)


## 上传目录权限设置
```
$ chmod 777 /data/uploads
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
redirect=<script>alert('XSS')</script>


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


## Fix SNIMissingWarning

机器环境:
```
$ python --version
Python 2.7.6
```

虚拟环境:
```
$ pip freeze | grep requests
requests==2.9.1
requests-oauthlib==0.6.1
```

执行 pip freeze 命令后有报错信息:
```
/home/zhanghe/code/flask_project/flask.env/local/lib/python2.7/site-packages/pip/_vendor/requests/packages/urllib3/util/ssl_.py:315: SNIMissingWarning: An HTTPS request has been made, but the SNI (Subject Name Indication) extension to TLS is not available on this platform. This may cause the server to present an incorrect TLS certificate, which can cause validation failures. For more information, see https://urllib3.readthedocs.org/en/latest/security.html#snimissingwarning.
```
原因: [requests 2.6 以后的版本, pyopenssl.inject_into_urllib3()](https://github.com/kennethreitz/requests/blob/a57c87a459d51c5b17d20285109e901b8aa95752/requests/__init__.py#L54)

python-2.7.9 以前的版本都会有这个问题

如果不想升级 python 版本, 可以选择降级 requests 版本, 例如: requests==2.5.3

最佳解决方案:
```
$ sudo apt-get install python-dev libffi-dev libssl-dev
$ pip install 'requests[security]'
```
相应的依赖都会被装上:
```
Installing collected packages: idna, pyasn1, six, enum34, ipaddress, pycparser, cffi, cryptography, pyOpenSSL, ndg-httpsclient
Successfully installed cffi-1.5.2 cryptography-1.3.1 enum34-1.1.3 idna-2.1 ipaddress-1.0.16 ndg-httpsclient-0.4.0 pyOpenSSL-16.0.0 pyasn1-0.1.9 pycparser-2.14 six-1.10.0
```


## UUID

[https://docs.python.org/2/library/uuid.html#example](https://docs.python.org/2/library/uuid.html#example)


## SendCloud

[http://sendcloud.sohu.com/](http://sendcloud.sohu.com/)

## QiNiu

安装
```
$ pip install qiniu
```

[http://www.qiniu.com/](http://www.qiniu.com/)

[python SDK 官方版](https://github.com/qiniu/python-sdk)

[python SDK 社区版](https://github.com/yueyoum/seven-cow)

[Flask 扩展](https://github.com/csuzhangxc/Flask-QiniuStorage)


## 注册邮箱验证

主要验证两点：
- 邮箱是否可达
- 是否本人操作

验证方式：
- 一、验证 token：https://www.***.com/email/signup/token
- 二、验证签名：https://www.***.com/email/signup/sign

显然第二种方式更好，不需要生成一个一次性的 token 并把它们存到数据库中

参考：[http://itsdangerous.readthedocs.io/en/latest/](http://itsdangerous.readthedocs.io/en/latest/)


## 签名模块

中文文档：[http://itsdangerous.readthedocs.io/en/latest/](http://itsdangerous.readthedocs.io/en/latest/)


## 常用链接的处理

添加锚点： url_for('end_points', _anchor='part_id')

_external=True 绝对路径


## 编码规范（建议）

新增表单
```
@app.route('/add/', methods=['GET', 'POST'])
@login_required
def add():
    """
    添加
    """
    form = AddForm(request.form)
    if request.method == 'POST':
        if form.validate_on_submit():
            from datetime import datetime
            current_time = datetime.utcnow()
            info = {
                'author': form.author.data,
                'title': form.title.data,
                'pub_date': form.pub_date.data,
                'add_time': current_time,
                'edit_time': current_time,
            }
            result = add(info)
            if result:
                flash(u'Add Success', 'success')
            else:
                flash(u'Add Failed', 'warning')
    return render_template('add.html', form=form)
```

编辑表单
```
@app.route('/edit/<int:id>/', methods=['GET', 'POST'])
@login_required
def edit(id):
    """
    编辑
    """
    form = EditForm(request.form)
    if request.method == 'GET':
        info = get_info(id)
        if blog_info:
            form.author.data = info.author
            form.title.data = info.title
            form.pub_date.data = info.pub_date
        else:
            return redirect(url_for('index'))
    if request.method == 'POST':
        if form.validate_on_submit():
            from datetime import datetime
            info = {
                'author': form.author.data,
                'title': form.title.data,
                'pub_date': form.pub_date.data,
                'edit_time': datetime.utcnow(),
            }
            result = edit(id, info)
            if result:
                flash(u'Edit Success', 'success')
            else:
                flash(u'Edit Failed', 'warning')
    return render_template('edit.html', id=id, form=form)
```


## 模板引擎

[https://github.com/aui/artTemplate](https://github.com/aui/artTemplate)

[https://github.com/wycats/handlebars.js](https://github.com/wycats/handlebars.js)

模板引擎与jinja结合
```
{% raw %}
...
{% endraw %}
```


## 模块导入更新

旧模块 | 新模块
| --- | --- |
flask.ext.login | flask_login
flask.ext.wtf | flask_wtf
flask.ext.sqlalchemy | flask_sqlalchemy
flask.ext.mail | flask_mail

表单里，用 FlaskForm 替代历史版本 Form
```
from flask.ext.wtf import Form
替换为
from flask_wtf import FlaskForm
```


## 过滤器

注册自定义过滤器
```
方式一：
@app.template_filter('reverse')
def reverse_filter(s):
    return s[::-1]

方式二：
def reverse_filter(s):
    return s[::-1]
app.jinja_env.filters['reverse'] = reverse_filter
```

过滤器使用
```
{% for x in mylist | reverse %}
{% endfor %}
```


## 用户注册

注册方式 | 校验方式
| --- | --- |
手机号码 | 短信验证码
邮箱 | 发送带身份信息加密的链接，点击校验通过后即确认身份
第三方 | oauth

注意：如果需要兼容国际手机号码注册，需要添加国家区号

平台内先注册，后绑定第三方账号


## 手机注册

检查手机号码
检查图形码
获取短信验证码
    1、前台页面60S倒计时，60S后恢复
    2、后台生成短信码 session存储
    3、发送短信
提交注册（校验 表单与session 短信验证码）


## 忘记密码


## 页面全选功能设计
```
$("#check_all").change(function(){ 
    $('.check_children').prop("checked",this.checked); 
}); 
```


## 业务逻辑确认外键还是数据库设置外键

效率与一致性的权衡

主外键只是一种保持数据一致性的手段之一，如果有别的方式来保持数据一致性（业务逻辑保持数据一致性），那么数据库不设置主外键也是可以的。


## 数据库设计 NOT NULL 与 DEFAULT(默认非null值)

1、NOT NULL DEFAULT 同时设置，可以不插入字段，但是不能插入 null 值
2、仅仅设置 DEFAULT，可以不插入字段，也可插入 null 值
3、仅仅设置 NOT NULL，可以不插入字段，不可插入 null 值

通常，DEFAULT 的设置会简化代码的设计，
同时考虑索引效率，会将需要建立索引的字段添加 DEFAULT，因为 null是无法比较的
```
MariaDB [(none)]> select 2=2, 'a'='a', NULL=NULL;
+-----+---------+-----------+
| 2=2 | 'a'='a' | NULL=NULL |
+-----+---------+-----------+
|   1 |       1 |      NULL |
+-----+---------+-----------+
1 row in set (0.00 sec)
```

## 关于数据库索引优化

索引的类型

索引名称 | 定义 | 描述
| --- | --- | --- |
普通索引 | key | 唯一的作用就是加快查询的速度
主键索引 | primary key | 字段具备唯一性 一张数据表中只有一个
唯一索引 | unique key | 保证数据唯一性
联合索引 | key(a,b,c) | 实际上是建立3个索引(a,b,c;a,b;a)，每个索引都包含a
外键索引 | - | 就是用来维护数据表之间的相关性的，并且会导致数据的写入等操作的速度过慢，所以好像没啥用（对于较大的项目）
全文索引 | FULLTEXT(column1, column2) | mysql5.6以前的InnoDB表不支持。使用：WHERE MATCH(column) AGAINST('search_content')


能否用到索引 | 操作符
| --- | --- |
可以用到 | <, <=, =, >, >=, BETWEEN, IN, LIKE _%
不能用到 | <>, !=, not in, LIKE %_

对于比较长的字符串比如varchar(255)类型字段，可为该字段的前n个值建立索引，可用以下语句确定索引的长度
```
select count(distinct substring(字段,1,结束位置)) from 表
```

EXPLAIN 测试SQL执行计划


## 基于 redisde 会话管理

登陆成功后，即可看到session信息
```
127.0.0.1:6379> keys *
1) "session:.eJw9kF1vgjAYhf_K0msvsOASTbww1jkMbwmk1bU3RD5caWUoyNAa__uIS8y5PMnz5Jw7Sg5N0So0uzRdMUJJmaPZHb2laIbAZhMgEYZqY8CKnla8D5nxQGc3uhYerMEBZjDV2VhYvwcilcDcBcxxSGJDdV5KkpchiVzBVi7stlpqH0vmX0PiO0C4pYxWYI0n7JAq1oPHEXp1kyxWIVGGDsxwxz2h1VGyaHBFPeBoAhZcsaNHqmHosjl6jFDWNofkUpvi5zVBEo6BDWjsD6rMk-x7TK1UgGMDjA_z-I3q1QS070itNCXGkYv5E3c-J_W-u6imyMvmRdx_xk5G6t_ALjpYen2gF-8hWfSwnLYpzk9pOVX5V1yn7uZUVFsTuB_XoP8ndm3RPA9GLnr8AWDyey8.C58cvw._6DL2RmlQ9oqsw8IlGuX0FvLGts"
127.0.0.1:6379> type "session:.eJw9kF1vgjAYhf_K0msvsOASTbww1jkMbwmk1bU3RD5caWUoyNAa__uIS8y5PMnz5Jw7Sg5N0So0uzRdMUJJmaPZHb2laIbAZhMgEYZqY8CKnla8D5nxQGc3uhYerMEBZjDV2VhYvwcilcDcBcxxSGJDdV5KkpchiVzBVi7stlpqH0vmX0PiO0C4pYxWYI0n7JAq1oPHEXp1kyxWIVGGDsxwxz2h1VGyaHBFPeBoAhZcsaNHqmHosjl6jFDWNofkUpvi5zVBEo6BDWjsD6rMk-x7TK1UgGMDjA_z-I3q1QS070itNCXGkYv5E3c-J_W-u6imyMvmRdx_xk5G6t_ALjpYen2gF-8hWfSwnLYpzk9pOVX5V1yn7uZUVFsTuB_XoP8ndm3RPA9GLnr8AWDyey8.C58cvw._6DL2RmlQ9oqsw8IlGuX0FvLGts"
string
127.0.0.1:6379> get "session:.eJw9kF1vgjAYhf_K0msvsOASTbww1jkMbwmk1bU3RD5caWUoyNAa__uIS8y5PMnz5Jw7Sg5N0So0uzRdMUJJmaPZHb2laIbAZhMgEYZqY8CKnla8D5nxQGc3uhYerMEBZjDV2VhYvwcilcDcBcxxSGJDdV5KkpchiVzBVi7stlpqH0vmX0PiO0C4pYxWYI0n7JAq1oPHEXp1kyxWIVGGDsxwxz2h1VGyaHBFPeBoAhZcsaNHqmHosjl6jFDWNofkUpvi5zVBEo6BDWjsD6rMk-x7TK1UgGMDjA_z-I3q1QS070itNCXGkYv5E3c-J_W-u6imyMvmRdx_xk5G6t_ALjpYen2gF-8hWfSwnLYpzk9pOVX5V1yn7uZUVFsTuB_XoP8ndm3RPA9GLnr8AWDyey8.C58cvw._6DL2RmlQ9oqsw8IlGuX0FvLGts"
"(dp0\nS'csrf_token'\np1\nS'c44590d3e1d7be4250ff8c88e1b807832939b8ab'\np2\nsS'_fresh'\np3\nI01\nsS'user_id'\np4\nV3\np5\nsS'_id'\np6\nS'3790462bd3606e09982724f80c4196675c2006ace73e684d67bd7b847a171ecf26e2182405353f398c63bdc364b12e4a88d46a9e8b8ee466403d9337ace638b7'\np7\ns."
127.0.0.1:6379>
```


## 并发测试

flask 自带的 BaseHTTPServer 性能太差，测试过程中，连续刷新10次左右竟然报错
```
IOError: [Errno 32] Broken pipe
```

测试图形验证码并发
```
✗ ab -n 1000 -c 100 http://127.0.0.1:8000/captcha/get_code/reg/
```


## 事务一致性

分布式架构下，无法做到跨服务事务，只能通过逻辑事务，回滚采用补偿方案处理


## ajax 前后端规范

后端返回结构
```
json.dumps({'result': True})
json.dumps({'result': False, 'msg': u'错误消息'})
json.dumps({'result': False, 'msg': u'错误消息', 'location': 'http://www.baidu.com'})
```

前端处理逻辑
```

```

## sqlalchemy.exc.OperationalError
OperationalError: (_mysql_exceptions.OperationalError) (2006, 'MySQL server has gone away')


## sqlalchemy.exc.InvalidRequestError
StatementError: (sqlalchemy.exc.InvalidRequestError) Can't reconnect until invalid transaction is rolled back

检查配置
```
MariaDB [flask_project]> show global variables like "%timeout%";
+-----------------------------+----------+
| Variable_name               | Value    |
+-----------------------------+----------+
| connect_timeout             | 5        |
| deadlock_timeout_long       | 50000000 |
| deadlock_timeout_short      | 10000    |
| delayed_insert_timeout      | 300      |
| innodb_flush_log_at_timeout | 1        |
| innodb_lock_wait_timeout    | 50       |
| innodb_rollback_on_timeout  | OFF      |
| interactive_timeout         | 28800    |
| lock_wait_timeout           | 31536000 |
| net_read_timeout            | 30       |
| net_write_timeout           | 60       |
| slave_net_timeout           | 3600     |
| thread_pool_idle_timeout    | 60       |
| wait_timeout                | 600      |
+-----------------------------+----------+
14 rows in set (0.00 sec)
```

查看连接情况
```
MariaDB [flask_project]> show processlist;
+-----+------+------------------+---------------+---------+------+-------+------------------+----------+
| Id  | User | Host             | db            | Command | Time | State | Info             | Progress |
+-----+------+------------------+---------------+---------+------+-------+------------------+----------+
| 176 | root | 172.17.0.5:46672 | flask_project | Query   |    0 | init  | show processlist |    0.000 |
| 180 | root | 172.17.0.1:39592 | flask_project | Sleep   |  284 |       | NULL             |    0.000 |
+-----+------+------------------+---------------+---------+------+-------+------------------+----------+
2 rows in set (0.00 sec)
```

查看当前打开的连接的数量
```
MariaDB [flask_project]> show status like '%Threads_connected%';
+-------------------+-------+
| Variable_name     | Value |
+-------------------+-------+
| Threads_connected | 2     |
+-------------------+-------+
1 row in set (0.01 sec)
```

修改连接超时时间（测试）
```
MariaDB [flask_project]> set global wait_timeout=6;
```

```
MariaDB [flask_project]> show global variables like 'wait_timeout';
+---------------+-------+
| Variable_name | Value |
+---------------+-------+
| wait_timeout  | 600   |
+---------------+-------+
1 row in set (0.00 sec)
MariaDB [flask_project]> show variables like 'wait_timeout';
+---------------+-------+
| Variable_name | Value |
+---------------+-------+
| wait_timeout  | 28800 |
+---------------+-------+
1 row in set (0.00 sec)
MariaDB [flask_project]> show global status like 'uptime';
+---------------+--------+
| Variable_name | Value  |
+---------------+--------+
| Uptime        | 204519 |
+---------------+--------+
1 row in set (0.00 sec)

MariaDB [flask_project]> show global variables like 'max_allowed_packet';
+--------------------+----------+
| Variable_name      | Value    |
+--------------------+----------+
| max_allowed_packet | 16777216 |
+--------------------+----------+
1 row in set (0.00 sec)
```


错误重现:

当有事务没有提交或者没有回滚时，sqlalchemy 的连接回收时间（SQLALCHEMY_POOL_RECYCLE）大于数据库关闭等待连接时间（global wait_timeout）；

一旦数据库连接超时自动断开，此时 sqlalchemy 尝试连接数据库，会出现 OperationalError: (_mysql_exceptions.OperationalError) (2006, 'MySQL server has gone away')

处理方案:
1. sqlalchemy 的超时时间 小于 数据库的超时时间
2. 代码操作数据库，立即提交事务，错误回滚

官方说明:

http://flask-sqlalchemy.pocoo.org/2.2/config/#timeouts


## gunicorn [CRITICAL] WORKER TIMEOUT


## jinja 模板递归

关键词 recursive

```
{% for item in [8,[[10,11,34],2],[3,4,5,[6,7,8]]] recursive %}
    {% if loop.first %}
        <br/>{{ '----'*loop.depth }}开始{{ loop.depth }}<br/>
    {% endif %}
    {{ '----'*loop.depth }}Depth: {{ loop.depth }}
    {% if item[0] %}
        {{ loop(item) }}
    {% else %}
        Number: {{ item }} ;<br/>
    {% endif %}
    {% if loop.last %}
        {{ '----'*loop.depth }}结束{{ loop.depth }}<br/>
    {% endif %}
{% endfor %}
```

递归循环结果：
```
----开始1
----Depth: 1 Number: 8 ;
----Depth: 1
--------开始2
--------Depth: 2
------------开始3
------------Depth: 3 Number: 10 ;
------------Depth: 3 Number: 11 ;
------------Depth: 3 Number: 34 ;
------------结束3
--------Depth: 2 Number: 2 ;
--------结束2
----Depth: 1
--------开始2
--------Depth: 2 Number: 3 ;
--------Depth: 2 Number: 4 ;
--------Depth: 2 Number: 5 ;
--------Depth: 2
------------开始3
------------Depth: 3 Number: 6 ;
------------Depth: 3 Number: 7 ;
------------Depth: 3 Number: 8 ;
------------结束3
--------结束2
----结束1
```

## 在 jinja2 macro 使用 current_user

需要带使用上下文参数（with context）
```
{% from "macros/comments.html" import comment_form with context %}
```


## 银行卡验证接口

http://www.apistore.cn/

http://v.gotoway.com/api/v4/bankCard?key=0341749f1adc9e4f47f6a936e7ed9b46&bankcard=123456


```
{
"error_code": 0,
"reason": "Succes",
"result": {
    "abbreviation": "ABC",
    "bankimage": "http://auth.apis.la/bank/3_ABC.png",
    "bankname": "农业银行",
    "banknum": "1030000",
    "bankurl": "http://www.abchina.com/",
    "cardlength": "19",
    "cardname": "金穗通宝卡(银联卡)",
    "cardprefixlength": "6",
    "cardprefixnum": "622848",
    "cardtype": "银联借记卡",
    "enbankname": "Agricultural Bank of China",
    "isLuhn": true,
    "iscreditcard": 1,
    "servicephone": "95599"
},
"ordersign": "20170621091044215952509756"
}
```

认证类型：
- 实名认证 （姓名、身份证号码）
- 银行卡三要素认证 （银行卡姓名/卡号/身份证）
- 银行卡四要素认证 （银行卡姓名/卡号/身份证/手机号）


## 参数优化

连接池大小 == web进程数 == CPU核心数

SQLALCHEMY_POOL_RECYCLE < wait_timeout


```
MariaDB [flask_project]> show global variables like 'max_connections';
+-----------------+-------+
| Variable_name   | Value |
+-----------------+-------+
| max_connections | 100   |
+-----------------+-------+
1 row in set (0.00 sec)
MariaDB [flask_project]> set global max_connections=1000;
```
set global max_connections=1000;


## 流式处理的几种方式

- HTML5 Server-Sent Events
- Flask-SSE

http://dormousehole.readthedocs.io/en/latest/patterns/streaming.html

http://flask.pocoo.org/snippets/118/

http://www.python-requests.org/en/master/user/advanced/#streaming-requests

http://flask-sse.readthedocs.io/en/latest/quickstart.html


## 日志

使用 supervisor 管理进程，终端输出的日志信息，被supervisor截获后，写入stderr_logfile，一直想不通

查看 logging 模块源码

```
class StreamHandler(Handler):
    """
    A handler class which writes logging records, appropriately formatted,
    to a stream. Note that this class does not close the stream, as
    sys.stdout or sys.stderr may be used.
    """

    def __init__(self, stream=None):
        """
        Initialize the handler.

        If stream is not specified, sys.stderr is used.
        """
        Handler.__init__(self)
        if stream is None:
            stream = sys.stderr
        self.stream = stream
```

StreamHandler 默认是按照标准错误输出处理

print 则使用的是标准输出


## 分库分表

垂直分库

水平分表

- 分库

http://flask-sqlalchemy.pocoo.org/2.1/binds/
```
SQLALCHEMY_DATABASE_URI = 'postgres://localhost/main'
SQLALCHEMY_BINDS = {
    'users':        'mysqldb://localhost/users',
    'appmeta':      'sqlite:////path/to/appmeta.db'
}
```

```
class User(db.Model):
    __bind_key__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
```

使用 SQLALCHEMY_BINDS（） 和 **\_\_bind_key__**

- 分表

网友方案，先拿来
```
class GoodsDesc(object):

    _mapper = {}

    @staticmethod
    def model(goods_id):
        table_index = goods_id%100
        class_name = 'GoodsDesc_%d' % table_index

        ModelClass = GoodsDesc._mapper.get(class_name, None)
        if ModelClass is None:
            ModelClass = type(class_name, (db.Model,), {
                '__module__' : __name__,
                '__name__' : class_name,
                '__tablename__' : 'goods_desc_%d' % table_index,

                'goods_id' : db.Column(db.Integer, primary_key=True),
                'goods_desc' : db.Column(db.Text, default=None),
            })
            GoodsDesc._mapper[class_name] = ModelClass

        cls = ModelClass()
        cls.goods_id = goods_id
        return cls

# 外部代码调用如例如下：
# -----------------------

# 新增插入
gdm = GoodsDesc.model(goods_id)
gdm.goods_desc = 'desc'
db.session.add(gd)

# 查询
gdm = GoodsDesc.model(goods_id)
gd = gdm.query.filter_by(goods_id=goods_id).first()
```

待改进
```
_mapper = {}


def shard(self, pk_id):
    """
    分表
    :param self:
    :param pk_id:
    :return:
    """
    table_index = pk_id % 16
    class_name = '%s_%02d' % (self.name, table_index)

    model_class = _mapper.get(class_name, None)
    if model_class is None:
        model_class = type(class_name, (Base,), {
            '__module__': __name__,
            '__name__': class_name,
            '__tablename__': '%s_%d' % (self.__table__.name, table_index),

            'goods_id': db.Column(db.Integer, primary_key=True),
            'goods_desc': db.Column(db.Text, default=None),
        })
        _mapper[class_name] = model_class

    cls = model_class()
    cls.id = pk_id
    return cls
```


## 单一架构 VS 微服务架构


## 信息修改
账号修改
密码修改


## Todo：

- 第三方登陆

- 第三方支付

- 邮件列表的绑定和解绑

- 找回密码安全设置
参考：[密码找回功能可能存在的问题](http://drops.wooyun.org/web/3295)

- 接口参数签名校验的必要性
参考：[在线支付逻辑漏洞总结](http://drops.wooyun.org/papers/345)

- 检查数据重复, 处理效率问题

- 页面导出csv

- 各大搜索引擎提交入口

- 用户推广，注册邀请
