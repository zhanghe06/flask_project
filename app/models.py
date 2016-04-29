# coding: utf-8
from sqlalchemy import Column, Date, DateTime, Integer, String, Table, text
from sqlalchemy.sql.sqltypes import NullType
from database import db


Base = db.Model
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
    pub_date = Column(Date)
    add_time = Column(DateTime, server_default=text("CURRENT_TIMESTAMP"))
    edit_time = Column(DateTime, server_default=text("CURRENT_TIMESTAMP"))


t_sqlite_sequence = Table(
    'sqlite_sequence', metadata,
    Column('name', NullType),
    Column('seq', NullType)
)


class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    nickname = Column(String(20), nullable=False)
    avatar_url = Column(String(80))
    email = Column(String(20))
    phone = Column(String(20))
    birthday = Column(Date)
    create_time = Column(DateTime, nullable=False, server_default=text("CURRENT_TIMESTAMP"))
    update_time = Column(DateTime, nullable=False, server_default=text("CURRENT_TIMESTAMP"))
    last_ip = Column(String(15))


class UserAuth(Base):
    __tablename__ = 'user_auth'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, nullable=False)
    auth_type = Column(String(20), nullable=False)
    auth_key = Column(String(64), nullable=False)
    auth_secret = Column(String(256), nullable=False)
    verified = Column(Integer, server_default=text("0"))
