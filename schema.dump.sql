PRAGMA foreign_keys=OFF;
BEGIN TRANSACTION;
CREATE TABLE user (
  id          INTEGER PRIMARY KEY  AUTOINCREMENT,
  nickname    VARCHAR(20),
  avatar_url  VARCHAR(80),
  email       VARCHAR(20),
  phone       VARCHAR(20),
  birthday    DATE,
  create_time DATETIME    NOT NULL DEFAULT CURRENT_TIMESTAMP,
  update_time DATETIME    NOT NULL DEFAULT CURRENT_TIMESTAMP,
  last_ip     VARCHAR(15)
);
INSERT INTO "user" VALUES(1,'Admin',NULL,'admin@gmail.com','13800001111',NULL,'2016-01-11 11:01:05','2016-01-11 11:01:05',NULL);
INSERT INTO "user" VALUES(2,'Guest',NULL,'guest@gmail.com','13800002222',NULL,'2016-01-12 12:25:34','2016-01-12 12:25:34',NULL);
INSERT INTO "user" VALUES(3,'Test',NULL,'test@gmail.com','13800003333',NULL,'2016-01-12 01:43:42','2016-01-12 01:43:42','127.0.0.1');
CREATE TABLE user_auth (
  id           INTEGER PRIMARY KEY   AUTOINCREMENT,
  user_id      INTEGER      NOT NULL,
  auth_type    VARCHAR(20)  NOT NULL,
  auth_key     VARCHAR(64)  NOT NULL,
  auth_secret  VARCHAR(256) NOT NULL,
  verified     TINYINT      DEFAULT 0
);
INSERT INTO "user_auth" VALUES(1,1,'email','admin@gmail.com','123456',0);
INSERT INTO "user_auth" VALUES(2,2,'email','guest@gmail.com','123456',0);
INSERT INTO "user_auth" VALUES(3,3,'email','test@gmail.com','123456',1);
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
  pub_date  DATE,
  add_time  DATETIME             DEFAULT CURRENT_TIMESTAMP,
  edit_time DATETIME             DEFAULT CURRENT_TIMESTAMP
);
INSERT INTO "blog" VALUES(1,'Mark','The old man and the sea','2016-01-11 11:01:05','2016-05-26 05:26:08','2016-05-26 05:26:08');
INSERT INTO "blog" VALUES(2,'Jacob','The fault in our stars','2016-01-11 20:23:27','2016-05-26 05:26:08','2016-05-26 05:26:08');
INSERT INTO "blog" VALUES(3,'Larry','The Great Gatsby','2016-01-11 23:15:18','2016-05-26 05:26:08','2016-05-26 05:26:08');
INSERT INTO "blog" VALUES(4,'Tom','Sense and Sensibility','2016-01-12 12:25:34','2016-05-26 05:26:08','2016-05-26 05:26:08');
INSERT INTO "blog" VALUES(5,'Tom','Pride and Prejudice','2016-01-12 13:17:25','2016-05-26 05:26:08','2016-05-26 05:26:08');
INSERT INTO "blog" VALUES(6,'Lily','Game of Thrones','2016-01-12 14:53:01','2016-05-26 05:26:08','2016-05-26 05:26:08');
INSERT INTO "blog" VALUES(7,'Mark','Charlie and the Chocolate Factory','2016-01-12 15:13:17','2016-05-26 05:26:08','2016-05-26 05:26:08');
INSERT INTO "blog" VALUES(8,'Larry','Harry Potter and the Sorcerer''s Stone','2016-01-12 19:32:15','2016-05-26 05:26:09','2016-05-26 05:26:09');
INSERT INTO "blog" VALUES(9,'Larry','The house on mango street','2016-01-12 01:43:42','2016-05-26 05:26:09','2016-05-26 05:26:09');
INSERT INTO "blog" VALUES(10,'Jacob','And then there were none','2016-01-13 16:17:32','2016-05-26 05:26:09','2016-05-26 05:26:09');
DELETE FROM sqlite_sequence;
INSERT INTO "sqlite_sequence" VALUES('user',3);
INSERT INTO "sqlite_sequence" VALUES('user_auth',3);
INSERT INTO "sqlite_sequence" VALUES('author',5);
INSERT INTO "sqlite_sequence" VALUES('blog',10);
COMMIT;
