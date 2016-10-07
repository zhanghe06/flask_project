## SQLAlchemy

[SQLAlchemy Documentation](http://docs.sqlalchemy.org/en/latest)


### Conjunctions

[Conjunctions](http://docs.sqlalchemy.org/en/latest/core/tutorial.html#conjunctions)

- and_()
- or_()
- not_()


### Common Filter Operators

[Common Filter Operators](http://docs.sqlalchemy.org/en/latest/orm/tutorial.html#common-filter-operators)

- User.name == 'ed'
- User.name != 'ed'
- User.name.like('%ed%')
- User.name.in_(['ed', 'wendy', 'jack'])
- ~User.name.in_(['ed', 'wendy', 'jack'])
- User.name == None
- User.name.is_(None)
- User.name != None
- User.name.isnot(None)


### Functions

[Functions](http://docs.sqlalchemy.org/en/latest/core/tutorial.html#functions)

from sqlalchemy.sql import func

- func.now()
- func.current_timestamp()
- func.concat('x', 'y')


### Transtraction

基本结构：
```
try:
    db.session.add(model_obj_01)
    db.session.flush()
    print inspect(model_obj_01).identity[0]
    
    db.session.add(model_obj_02)
    db.session.flush()
    print inspect(model_obj_02).identity[0]

    db.session.commit()
except Exception as e:
    db.session.rollback()
    raise e
```

db.session.flush() 是将数据修改刷入内存
db.session.commit() 将修改存入数据库


连接 URI 格式

[支持的数据库](http://www.sqlalchemy.org/docs/core/engines.html)

Postgres:

postgresql://scott:tiger@localhost/mydatabase

MySQL:

mysql://scott:tiger@localhost/mydatabase

Oracle:

oracle://scott:tiger@127.0.0.1:1521/sidname

SQLite (注意开头的四个斜线):

sqlite:////absolute/path/to/foo.db
