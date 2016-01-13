# coding: utf-8
from sqlalchemy import Column, Date, Integer, Numeric, Table
from sqlalchemy.sql.sqltypes import NullType
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
metadata = Base.metadata


class Author(Base):
    __tablename__ = 'author'

    id = Column(Integer, primary_key=True)
    name = Column(Numeric, nullable=False)
    email = Column(Numeric, nullable=False)


class Blog(Base):
    __tablename__ = 'blog'

    id = Column(Integer, primary_key=True)
    author = Column(Numeric, nullable=False)
    title = Column(Numeric, nullable=False)
    pub_date = Column(Date, nullable=False)


t_sqlite_sequence = Table(
    'sqlite_sequence', metadata,
    Column('name', NullType),
    Column('seq', NullType)
)
