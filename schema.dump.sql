PRAGMA foreign_keys=OFF;
BEGIN TRANSACTION;
CREATE TABLE user (
  id          INTEGER PRIMARY KEY  AUTOINCREMENT,
  email       VARCHAR(20) NOT NULL,
  password    VARCHAR(20) NOT NULL,
  nickname    VARCHAR(20) NOT NULL,
  birthday    DATE                 DEFAULT '0000-00-00',
  create_time DATETIME    NOT NULL DEFAULT CURRENT_TIMESTAMP,
  update_time DATETIME    NOT NULL DEFAULT CURRENT_TIMESTAMP,
  last_ip     VARCHAR(15)
);
INSERT INTO "user" VALUES(1,'admin@gmail.com','123456','Admin','0000-00-00','2016-01-11 11:01:05','2016-01-11 11:01:05',NULL);
INSERT INTO "user" VALUES(2,'guest@gmail.com','123456','Guest','0000-00-00','2016-01-12 12:25:34','2016-01-12 12:25:34',NULL);
INSERT INTO "user" VALUES(3,'test@gmail.com','123456','Test','0000-00-00','2016-01-12 01:43:42','2016-01-12 01:43:42',NULL);
CREATE TABLE author (
  id    INTEGER PRIMARY KEY AUTOINCREMENT,
  name  VARCHAR(20) NOT NULL,
  email VARCHAR(20) NOT NULL
);
INSERT INTO "author" VALUES(1,'Mark','mark@gmail.com');
INSERT INTO "author" VALUES(2,'Jacob','jacob@gmail.com');
INSERT INTO "author" VALUES(3,'Larry','larry@gmail.com');
INSERT INTO "author" VALUES(4,'Tom','tom@gmail.com');
INSERT INTO "author" VALUES(5,'Lily','lily@gmail.com');
CREATE TABLE blog (
  id        INTEGER PRIMARY KEY  AUTOINCREMENT,
  author    VARCHAR(20) NOT NULL,
  title     VARCHAR(40) NOT NULL,
  pub_date  DATE        NOT NULL DEFAULT '0000-00-00',
  add_time  DATETIME             DEFAULT CURRENT_TIMESTAMP,
  edit_time DATETIME             DEFAULT CURRENT_TIMESTAMP
);
INSERT INTO "blog" VALUES(1,'Mark','The old man and the sea','2016-01-11 11:01:05','2016-01-30 20:26:24','2016-01-30 20:26:24');
INSERT INTO "blog" VALUES(2,'Jacob','The fault in our stars','2016-01-11 20:23:27','2016-01-30 20:26:24','2016-01-30 20:26:24');
INSERT INTO "blog" VALUES(3,'Larry','The Great Gatsby','2016-01-11 23:15:18','2016-01-30 20:26:24','2016-01-30 20:26:24');
INSERT INTO "blog" VALUES(4,'Tom','Sense and Sensibility','2016-01-12 12:25:34','2016-01-30 20:26:25','2016-01-30 20:26:25');
INSERT INTO "blog" VALUES(5,'Tom','Pride and Prejudice','2016-01-12 13:17:25','2016-01-30 20:26:25','2016-01-30 20:26:25');
INSERT INTO "blog" VALUES(6,'Lily','Game of Thrones','2016-01-12 14:53:01','2016-01-30 20:26:25','2016-01-30 20:26:25');
INSERT INTO "blog" VALUES(7,'Mark','Charlie and the Chocolate Factory','2016-01-12 15:13:17','2016-01-30 20:26:25','2016-01-30 20:26:25');
INSERT INTO "blog" VALUES(8,'Larry','Harry Potter and the Sorcerer''s Stone','2016-01-12 19:32:15','2016-01-30 20:26:25','2016-01-30 20:26:25');
INSERT INTO "blog" VALUES(9,'Larry','The house on mango street','2016-01-12 01:43:42','2016-01-30 20:26:25','2016-01-30 20:26:25');
INSERT INTO "blog" VALUES(10,'Jacob','And then there were none','2016-01-13 16:17:32','2016-01-30 20:26:25','2016-01-30 20:26:25');
DELETE FROM sqlite_sequence;
INSERT INTO "sqlite_sequence" VALUES('user',3);
INSERT INTO "sqlite_sequence" VALUES('author',5);
INSERT INTO "sqlite_sequence" VALUES('blog',10);
COMMIT;
