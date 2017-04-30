-- user 测试数据
INSERT INTO `user`(id, nickname, email, phone, create_time, update_time) VALUES('1', 'Admin', 'admin@gmail.com', '13800001111', '2016-01-11 11:01:05', '2016-01-11 11:01:05');
INSERT INTO `user`(id, nickname, email, phone, create_time, update_time) VALUES('2', 'Guest', 'guest@gmail.com', '13800002222', '2016-01-12 12:25:34', '2016-01-12 12:25:34');
INSERT INTO `user`(id, nickname, email, phone, create_time, update_time) VALUES('3', 'Test', 'test@gmail.com', '13800003333', '2016-01-12 01:43:42', '2016-01-12 01:43:42');

-- user_auth 测试数据
INSERT INTO `user_auth`(user_id, auth_type, auth_key, auth_secret) VALUES('1', 'email', 'admin@gmail.com', '123456');
INSERT INTO `user_auth`(user_id, auth_type, auth_key, auth_secret) VALUES('2', 'email', 'guest@gmail.com', '123456');
INSERT INTO `user_auth`(user_id, auth_type, auth_key, auth_secret, verified) VALUES('3', 'email', 'test@gmail.com', '123456', '1');

-- author 测试数据
INSERT INTO author(`name`, email) VALUES('Mark', 'mark@gmail.com');
INSERT INTO author(`name`, email) VALUES('Jacob', 'jacob@gmail.com');
INSERT INTO author(`name`, email) VALUES('Larry', 'larry@gmail.com');
INSERT INTO author(`name`, email) VALUES('Tom', 'tom@gmail.com');
INSERT INTO author(`name`, email) VALUES('Lily', 'lily@gmail.com');

-- blog 测试数据
INSERT INTO blog(author, title, pub_date) VALUES('Mark', 'The old man and the sea', '2016-01-11 11:01:05');
INSERT INTO blog(author, title, pub_date) VALUES('Jacob', 'The fault in our stars', '2016-01-11 20:23:27');
INSERT INTO blog(author, title, pub_date) VALUES('Larry', 'The Great Gatsby', '2016-01-11 23:15:18');
INSERT INTO blog(author, title, pub_date) VALUES('Tom', 'Sense and Sensibility', '2016-01-12 12:25:34');
INSERT INTO blog(author, title, pub_date) VALUES('Tom', 'Pride and Prejudice', '2016-01-12 13:17:25');
INSERT INTO blog(author, title, pub_date) VALUES('Lily', 'Game of Thrones', '2016-01-12 14:53:01');
INSERT INTO blog(author, title, pub_date) VALUES('Mark', 'Charlie and the Chocolate Factory', '2016-01-12 15:13:17');
INSERT INTO blog(author, title, pub_date) VALUES('Larry', 'Harry Potter and the Sorcerer''s Stone', '2016-01-12 19:32:15');
INSERT INTO blog(author, title, pub_date) VALUES('Larry', 'The house on mango street', '2016-01-12 01:43:42');
INSERT INTO blog(author, title, pub_date) VALUES('Jacob', 'And then there were none', '2016-01-13 16:17:32');
