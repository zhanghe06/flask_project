drop table if exists author;
create table author (
  id integer primary key autoincrement,
  name varchar(20) not null,
  email varchar(20) not null
);

drop table if exists blog;
create table blog (
  id integer primary key autoincrement,
  author varchar(20) not null,
  title varchar(40) not null,
  pub_date date not null
);
