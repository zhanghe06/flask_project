DROP TABLE IF EXISTS user;
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

DROP TABLE IF EXISTS user_auth;
CREATE TABLE user_auth (
  id           INTEGER PRIMARY KEY   AUTOINCREMENT,
  user_id      INTEGER      NOT NULL,
  auth_type    VARCHAR(20)  NOT NULL,
  auth_key     VARCHAR(64)  NOT NULL,
  auth_secret  VARCHAR(256) NOT NULL,
  verified     TINYINT      DEFAULT 0
);

DROP TABLE IF EXISTS author;
CREATE TABLE author (
  id    INTEGER PRIMARY KEY AUTOINCREMENT,
  name  VARCHAR(20) NOT NULL,
  email VARCHAR(20) NOT NULL
);

DROP TABLE IF EXISTS blog;
CREATE TABLE blog (
  id        INTEGER PRIMARY KEY  AUTOINCREMENT,
  author    VARCHAR(20) NOT NULL,
  title     VARCHAR(40) NOT NULL,
  pub_date  DATE,
  add_time  DATETIME             DEFAULT CURRENT_TIMESTAMP,
  edit_time DATETIME             DEFAULT CURRENT_TIMESTAMP
);
