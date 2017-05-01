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

DROP TABLE IF EXISTS product;
CREATE TABLE product (
  id        INTEGER PRIMARY KEY  AUTOINCREMENT,
  title     VARCHAR(40) NOT NULL,
  stock     INTEGER NOT NULL DEFAULT 0,
  create_time DATETIME             DEFAULT CURRENT_TIMESTAMP,
  update_time DATETIME             DEFAULT CURRENT_TIMESTAMP
);

DROP TABLE IF EXISTS product_order;
CREATE TABLE product_order (
  id        INTEGER PRIMARY KEY  AUTOINCREMENT,
  buyer_uid        INTEGER,
  shop_id        INTEGER,
  amount     DECIMAL(10, 2) NOT NULL DEFAULT 0.00,
  pay_status  TINYINT(1) NOT NULL DEFAULT 0,
  create_time DATETIME             DEFAULT CURRENT_TIMESTAMP,
  update_time DATETIME             DEFAULT CURRENT_TIMESTAMP
);
