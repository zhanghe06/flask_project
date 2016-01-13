## Flask 项目模拟


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
$ chmod a+x init_db.sh
$ chmod a+x dump_db.sh
$ ./init_db.sh
```


### SQLAlchemy

python 的一种 ORM 框架

ORM：Object-Relational Mapping

把关系数据库的表结构映射到对象上


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


[http://docs.sqlalchemy.org/en/latest/core/engines.html](http://docs.sqlalchemy.org/en/latest/core/engines.html)


### 存入数据库中文乱码

SQLALCHEMY_DATABASE_URI = 'mysql://[用户]:[密码]@[IP]/[库名]?charset=utf8'

注意是 utf8 ，不是 utf-8
> show variables like 'character%';
mysql 里的 charset 是 utf8


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
