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

可以通过管道把 schema.sql 作为 sqlite3 命令的输入来创建这个模式，命令为如下:
```
$ sqlite3 /tmp/flaskr.db < schema.sql
```


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
