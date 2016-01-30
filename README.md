## Flask 项目模拟

### 项目演示步骤
```
$ cd flask_project
$ virtualenv flask.env
$ source flask.env/bin/activate
$ pip install -r requirements.txt
$ chmod a+x ./etc/db_init.sh
$ ./etc/db_init.sh
$ ./run.py
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
$ pip install sqlacodegen
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
rows = db_session.query(Author).filter(eval(condition)).paginate(page, per_page, False)
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
rows = Author.query.filter(eval(condition)).paginate(page, per_page, False)
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

Gunicorn 官网：[http://gunicorn.org/](http://gunicorn.org/)



## 部署方案( Nginx + Uwsgi + Supervisor )



## 参考资料：

[Flask 代码模式](http://docs.jinkan.org/docs/flask/patterns/index.html)


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
