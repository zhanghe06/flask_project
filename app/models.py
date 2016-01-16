# coding: utf-8
from sqlalchemy import Column, Date, Integer, String, Table
from sqlalchemy.sql.sqltypes import NullType
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
metadata = Base.metadata


class Author(Base):
    __tablename__ = 'author'

    id = Column(Integer, primary_key=True)
    name = Column(String(20), nullable=False)
    email = Column(String(20), nullable=False)


class Blog(Base):
    __tablename__ = 'blog'

    id = Column(Integer, primary_key=True)
    author = Column(String(20), nullable=False)
    title = Column(String(40), nullable=False)
    pub_date = Column(Date, nullable=False)


t_sqlite_sequence = Table(
    'sqlite_sequence', metadata,
    Column('name', NullType),
    Column('seq', NullType)
)
