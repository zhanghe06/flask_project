USE flask;

-- 插入用户全局注册信息
TRUNCATE TABLE `user`;
INSERT INTO `user` VALUES
  (1, '0', '0', NULL, NULL, '127.0.0.1', NULL, '2016-01-11 11:01:10', '2016-01-11 11:01:05', '2016-01-11 11:01:05');
INSERT INTO `user` VALUES
  (2, '0', '0', NULL, NULL, '127.0.0.1', NULL, '2016-01-11 11:01:10', '2016-01-11 11:01:05', '2016-01-11 11:01:05');
INSERT INTO `user` VALUES
  (3, '0', '0', NULL, NULL, '127.0.0.1', NULL, '2016-01-11 11:01:10', '2016-01-11 11:01:05', '2016-01-11 11:01:05');

-- 插入用户认证信息
TRUNCATE TABLE `user_auth`;
INSERT INTO `user_auth`
VALUES (1, 1, 0, 'Admin', 'e10adc3949ba59abbe56e057f20f883e', '1', '2016-01-11 11:01:05', '2016-01-11 11:01:05');
INSERT INTO `user_auth`
VALUES (2, 2, 0, 'Guest', 'e10adc3949ba59abbe56e057f20f883e', '1', '2016-01-12 12:25:34', '2016-01-12 12:25:34');
INSERT INTO `user_auth`
VALUES (3, 3, 0, 'Test', 'e10adc3949ba59abbe56e057f20f883e', '1', '2016-01-12 01:43:42', '2016-01-12 01:43:42');
INSERT INTO `user_auth` VALUES
  (4, 1, 1, 'admin@gmail.com', 'e10adc3949ba59abbe56e057f20f883e', '1', '2016-01-11 11:01:05', '2016-01-11 11:01:05');
INSERT INTO `user_auth` VALUES
  (5, 2, 1, 'guest@gmail.com', 'e10adc3949ba59abbe56e057f20f883e', '1', '2016-01-12 12:25:34', '2016-01-12 12:25:34');
INSERT INTO `user_auth` VALUES
  (6, 3, 1, 'test@gmail.com', 'e10adc3949ba59abbe56e057f20f883e', '1', '2016-01-12 01:43:42', '2016-01-12 01:43:42');
INSERT INTO `user_auth` VALUES
  (7, 1, 2, '8613800001111', 'e10adc3949ba59abbe56e057f20f883e', '1', '2016-01-11 11:01:05', '2016-01-11 11:01:05');
INSERT INTO `user_auth` VALUES
  (8, 2, 2, '8613800002222', 'e10adc3949ba59abbe56e057f20f883e', '1', '2016-01-12 12:25:34', '2016-01-12 12:25:34');
INSERT INTO `user_auth` VALUES
  (9, 3, 2, '8613800003333', 'e10adc3949ba59abbe56e057f20f883e', '1', '2016-01-12 01:43:42', '2016-01-12 01:43:42');

-- 插入用户基本信息
TRUNCATE TABLE `user_profile`;
INSERT INTO `user_profile` VALUES
  (1, 0, 'Admin', NULL, 'admin@gmail.com', 0, '86', '13800001111', NULL, '123456789098765432', '2016-01-11 11:01:05',
   '2016-01-11 11:01:05');
INSERT INTO `user_profile` VALUES
  (2, 1, 'Guest', NULL, 'guest@gmail.com', 0, '86', '13800002222', NULL, '123456789098765433', '2016-01-12 12:25:34',
   '2016-01-12 12:25:34');
INSERT INTO `user_profile` VALUES
  (3, 1, 'Test', NULL, 'test@gmail.com', 0, '86', '13800003333', NULL, '123456789098765434', '2016-01-12 01:43:42',
   '2016-01-12 01:43:42');

-- 插入用户银行信息
TRUNCATE TABLE `user_bank`;
INSERT INTO `user_bank`
VALUES (1, 'Admin', '建行', '上海分行', '1234567890', 0, 0, '2016-01-11 11:01:05', '2016-01-11 11:01:05');
INSERT INTO `user_bank`
VALUES (2, 'Guest', '农行', '上海分行', '1234567891', 0, 0, '2016-01-11 11:01:05', '2016-01-11 11:01:05');

-- 插入管理员基本信息
TRUNCATE TABLE `admin`;
INSERT INTO `admin` VALUES
  (1, 'admin', 'e10adc3949ba59abbe56e057f20f883e', 0, '86', '13800002222', '0', '0', NULL, NULL, NULL,
   '2016-01-12 12:25:34', '2016-01-12 12:25:34');

-- 插入用户声望
TRUNCATE TABLE `credit`;
INSERT INTO `credit` VALUES (1, 85, 30, 62, 50, 67, 360, '2016-01-12 12:25:34', '2016-01-12 12:25:34');
INSERT INTO `credit` VALUES (2, 75, 40, 72, 41, 66, 360, '2016-01-12 12:25:34', '2016-01-12 12:25:34');

-- 插入投资申请记录
TRUNCATE TABLE `apply_put`;
INSERT INTO `apply_put` VALUES (1, 1, 0, 2000.00, 1, 0, 0, NULL, '2016-01-12 12:25:34', '2016-01-12 12:25:34');

-- 插入提现申请记录
TRUNCATE TABLE `apply_get`;
INSERT INTO `apply_get` VALUES (1, 2, 0, 2000.00, 1, 0, 0, NULL, '2016-01-12 12:25:34', '2016-01-12 12:25:34');

-- 插入付款单记录
TRUNCATE TABLE `ticket_put`;
INSERT INTO `ticket_put` VALUES (1, 1, 1, 2000.00, 0, NULL, '2016-01-12 12:25:34', '2016-01-12 12:25:34');

-- 插入收款单记录
TRUNCATE TABLE `ticket_get`;
INSERT INTO `ticket_get` VALUES (1, 2, 1, 2000.00, 0, NULL, '2016-01-12 12:25:34', '2016-01-12 12:25:34');

-- 插入订单记录
TRUNCATE TABLE `order`;
INSERT INTO `order`
VALUES (1, 1, 1, 1, 2, 1, 1, 0, 2000.00, 0, 0, 0, NULL, NULL, NULL, '2016-01-12 12:25:34', '2016-01-12 12:25:34');
