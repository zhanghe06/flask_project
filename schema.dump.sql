PRAGMA foreign_keys=OFF;
BEGIN TRANSACTION;
CREATE TABLE author (
  id integer primary key autoincrement,
  name varchar(20) not null,
  email varchar(20) not null
);
INSERT INTO "author" VALUES(1,'Mark','mark@gmail.com');
INSERT INTO "author" VALUES(2,'Jacob','jacob@gmail.com');
INSERT INTO "author" VALUES(3,'Larry','larry@gmail.com');
INSERT INTO "author" VALUES(4,'Tom','tom@gmail.com');
INSERT INTO "author" VALUES(5,'Lily','lily@gmail.com');
CREATE TABLE blog (
  id integer primary key autoincrement,
  author varchar(20) not null,
  title varchar(40) not null,
  pub_date date not null
);
INSERT INTO "blog" VALUES(1,'Mark','The old man and the sea','2016-01-11 11:01:05');
INSERT INTO "blog" VALUES(2,'Jacob','The fault in our stars','2016-01-11 20:23:27');
INSERT INTO "blog" VALUES(3,'Larry','The Great Gatsby','2016-01-11 23:15:18');
INSERT INTO "blog" VALUES(4,'Tom','Sense and Sensibility','2016-01-12 12:25:34');
INSERT INTO "blog" VALUES(5,'Tom','Pride and Prejudice','2016-01-12 13:17:25');
INSERT INTO "blog" VALUES(6,'Lily','Game of Thrones','2016-01-12 14:53:01');
INSERT INTO "blog" VALUES(7,'Mark','Charlie and the Chocolate Factory','2016-01-12 15:13:17');
INSERT INTO "blog" VALUES(8,'Larry','Harry Potter and the Sorcerer''s Stone','2016-01-12 19:32:15');
INSERT INTO "blog" VALUES(9,'Larry','The house on mango street','2016-01-12 01:43:42');
INSERT INTO "blog" VALUES(10,'Jacob','And then there were none','2016-01-13 16:17:32');
DELETE FROM sqlite_sequence;
INSERT INTO "sqlite_sequence" VALUES('author',5);
INSERT INTO "sqlite_sequence" VALUES('blog',10);
COMMIT;
