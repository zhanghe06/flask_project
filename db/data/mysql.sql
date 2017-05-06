USE flask;

-- 插入用户全局注册信息
TRUNCATE TABLE `user`;
INSERT INTO `user` VALUES (1, '1', '0', '0', '2016-01-11 11:01:10', NULL, NULL, '127.0.0.1', NULL, '2016-01-11 11:01:10', '2016-01-11 11:01:05', '2016-01-11 11:01:05');
INSERT INTO `user` VALUES (2, '1', '0', '0', '2016-02-11 11:01:10', NULL, NULL, '127.0.0.1', NULL, '2016-02-11 11:01:10', '2016-02-11 11:01:05', '2016-02-11 11:01:05');
INSERT INTO `user` VALUES (3, '1', '0', '0', '2016-03-11 11:01:10', NULL, NULL, '127.0.0.1', NULL, '2016-03-11 11:01:10', '2016-03-11 11:01:05', '2016-03-11 11:01:05');

-- 插入用户认证信息
TRUNCATE TABLE `user_auth`;
INSERT INTO `user_auth` VALUES (1, 1, 0, 'Admin', 'e10adc3949ba59abbe56e057f20f883e', '1', '2016-01-11 11:01:05', '2016-01-11 11:01:05');
INSERT INTO `user_auth` VALUES (2, 2, 0, 'Guest', 'e10adc3949ba59abbe56e057f20f883e', '1', '2016-01-12 12:25:34', '2016-01-12 12:25:34');
INSERT INTO `user_auth` VALUES (3, 3, 0, 'Test', 'e10adc3949ba59abbe56e057f20f883e', '1', '2016-01-12 01:43:42', '2016-01-12 01:43:42');
INSERT INTO `user_auth` VALUES (4, 1, 1, 'admin@gmail.com', 'e10adc3949ba59abbe56e057f20f883e', '1', '2016-01-11 11:01:05', '2016-01-11 11:01:05');
INSERT INTO `user_auth` VALUES (5, 2, 1, 'guest@gmail.com', 'e10adc3949ba59abbe56e057f20f883e', '1', '2016-01-12 12:25:34', '2016-01-12 12:25:34');
INSERT INTO `user_auth` VALUES (6, 3, 1, 'test@gmail.com', 'e10adc3949ba59abbe56e057f20f883e', '1', '2016-01-12 01:43:42', '2016-01-12 01:43:42');
INSERT INTO `user_auth` VALUES (7, 1, 2, '8613800001111', 'e10adc3949ba59abbe56e057f20f883e', '1', '2016-01-11 11:01:05', '2016-01-11 11:01:05');
INSERT INTO `user_auth` VALUES (8, 2, 2, '8613800002222', 'e10adc3949ba59abbe56e057f20f883e', '1', '2016-01-12 12:25:34', '2016-01-12 12:25:34');
INSERT INTO `user_auth` VALUES (9, 3, 2, '8613800003333', 'e10adc3949ba59abbe56e057f20f883e', '1', '2016-01-12 01:43:42', '2016-01-12 01:43:42');

-- 插入用户基本信息
TRUNCATE TABLE `user_profile`;
INSERT INTO `user_profile` VALUES (1, 0, 'Admin', 0, NULL, 'admin@gmail.com', 0, '86', '13800001111', '1900-01-01', '123456789098765432', '2016-01-11 11:01:05', '2016-01-11 11:01:05');
INSERT INTO `user_profile` VALUES (2, 1, 'Guest', 0, NULL, 'guest@gmail.com', 0, '86', '13800002222', '1900-01-01', '123456789098765433', '2016-01-12 12:25:34', '2016-01-12 12:25:34');
INSERT INTO `user_profile` VALUES (3, 1, 'Test', 0, NULL, 'test@gmail.com', 0, '86', '13800003333', '1900-01-01', '123456789098765434', '2016-01-12 01:43:42', '2016-01-12 01:43:42');

-- 插入用户银行信息
TRUNCATE TABLE `user_bank`;
INSERT INTO `user_bank` VALUES (1, 'Admin', '建行', '上海分行', '1234567890', 0, 0, '2016-01-11 11:01:05', '2016-01-11 11:01:05');
INSERT INTO `user_bank` VALUES (2, 'Guest', '农行', '上海分行', '1234567891', 0, 0, '2016-01-11 11:01:05', '2016-01-11 11:01:05');

-- 插入管理员基本信息
TRUNCATE TABLE `admin`;
INSERT INTO `admin` VALUES (1, 'admin', 'e10adc3949ba59abbe56e057f20f883e', 0, '86', '13800002222', '0', '0', NULL, NULL, NULL, '2016-01-12 12:25:34', '2016-01-12 12:25:34');

-- 插入用户声望
TRUNCATE TABLE `credit`;
INSERT INTO `credit` VALUES (1, 85, 30, 62, 50, 67, 360, '2016-01-12 12:25:34', '2016-01-12 12:25:34');
INSERT INTO `credit` VALUES (2, 75, 40, 72, 41, 66, 360, '2016-01-12 12:25:34', '2016-01-12 12:25:34');

-- 插入投资申请记录
TRUNCATE TABLE `apply_put`;
INSERT INTO `apply_put` VALUES (1, 1, 0, 1000.00, 0.00, 1, 0, 0, null, '2017-05-06 08:43:00', '2017-05-06 08:43:00');
INSERT INTO `apply_put` VALUES (2, 1, 0, 2000.00, 2000.00, 1, 2, 0, null, '2017-05-06 08:43:05', '2017-05-06 08:47:07');
INSERT INTO `apply_put` VALUES (3, 1, 0, 3000.00, 0.00, 1, 0, 0, null, '2017-05-06 08:43:10', '2017-05-06 08:43:10');
INSERT INTO `apply_put` VALUES (4, 2, 0, 1200.00, 0.00, 1, 0, 0, null, '2017-05-06 08:43:39', '2017-05-06 08:43:39');
INSERT INTO `apply_put` VALUES (5, 2, 0, 2200.00, 0.00, 1, 0, 0, null, '2017-05-06 08:43:44', '2017-05-06 08:43:44');
INSERT INTO `apply_put` VALUES (6, 2, 0, 3200.00, 0.00, 1, 0, 0, null, '2017-05-06 08:43:48', '2017-05-06 08:43:48');
INSERT INTO `apply_put` VALUES (7, 3, 0, 400.00, 400.00, 1, 2, 0, null, '2017-05-06 08:44:13', '2017-05-06 08:47:07');
INSERT INTO `apply_put` VALUES (8, 3, 0, 600.00, 0.00, 1, 0, 0, null, '2017-05-06 08:44:17', '2017-05-06 08:44:17');
INSERT INTO `apply_put` VALUES (9, 3, 0, 800.00, 800.00, 1, 2, 0, null, '2017-05-06 08:44:21', '2017-05-06 08:47:07');

-- 插入提现申请记录
TRUNCATE TABLE `apply_get`;
INSERT INTO `apply_get` VALUES (1, 1, 0, 1000.00, 0.00, 1, 0, 0, null, '2017-05-06 08:43:15', '2017-05-06 08:43:15');
INSERT INTO `apply_get` VALUES (2, 1, 0, 2000.00, 0.00, 1, 0, 0, null, '2017-05-06 08:43:22', '2017-05-06 08:43:22');
INSERT INTO `apply_get` VALUES (3, 1, 0, 3000.00, 0.00, 1, 0, 0, null, '2017-05-06 08:43:27', '2017-05-06 08:43:27');
INSERT INTO `apply_get` VALUES (4, 2, 0, 1200.00, 0.00, 1, 0, 0, null, '2017-05-06 08:43:53', '2017-05-06 08:43:53');
INSERT INTO `apply_get` VALUES (5, 2, 0, 2200.00, 0.00, 1, 0, 0, null, '2017-05-06 08:43:58', '2017-05-06 08:43:58');
INSERT INTO `apply_get` VALUES (6, 2, 0, 3200.00, 3200.00, 1, 2, 0, null, '2017-05-06 08:44:02', '2017-05-06 08:47:07');
INSERT INTO `apply_get` VALUES (7, 3, 0, 400.00, 0.00, 1, 0, 0, null, '2017-05-06 08:44:25', '2017-05-06 08:44:25');
INSERT INTO `apply_get` VALUES (8, 3, 0, 600.00, 0.00, 1, 0, 0, null, '2017-05-06 08:44:28', '2017-05-06 08:44:28');
INSERT INTO `apply_get` VALUES (9, 3, 0, 800.00, 0.00, 1, 0, 0, null, '2017-05-06 08:44:32', '2017-05-06 08:44:32');


-- 插入订单记录
TRUNCATE TABLE `order`;
INSERT INTO `order` VALUES (1, 2, 6, 1, 2, 0, 2000.00, 1, 0, 0, 0, 0, '2017-05-06 08:47:07', null, null, null, '2017-05-06 08:47:07', '2017-05-06 08:47:07');
INSERT INTO `order` VALUES (2, 7, 6, 3, 2, 0, 400.00, 1, 0, 0, 0, 0, '2017-05-06 08:47:07', null, null, null, '2017-05-06 08:47:07', '2017-05-06 08:47:07');
INSERT INTO `order` VALUES (3, 9, 6, 3, 2, 0, 800.00, 1, 0, 0, 0, 0, '2017-05-06 08:47:07', null, null, null, '2017-05-06 08:47:07', '2017-05-06 08:47:07');

-- 插入钱包总记录
TRUNCATE TABLE `wallet`;
INSERT INTO `wallet` VALUES (1, '1000.00', '2400.00', 0, '2016-01-12 12:25:34', '2016-01-12 12:25:34');

-- 插入积分总记录
TRUNCATE TABLE `score`;
INSERT INTO `score` VALUES (1, '0.00', '2016-01-12 12:25:34', '2016-01-12 12:25:34');

-- 插入奖金总记录
TRUNCATE TABLE `bonus`;
INSERT INTO `bonus` VALUES (1, '0.00', '2016-01-12 12:25:34', '2016-01-12 12:25:34');

