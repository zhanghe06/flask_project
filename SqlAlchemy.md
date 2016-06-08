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
