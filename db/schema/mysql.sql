DROP DATABASE IF EXISTS `flask`;
CREATE DATABASE `flask` /*!40100 DEFAULT CHARACTER SET utf8 */;


use flask;


DROP TABLE IF EXISTS `user`;
CREATE TABLE `user` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `status_active` TINYINT NOT NULL DEFAULT '0' COMMENT '激活状态（0未激活，1已激活）',
  `status_lock` TINYINT NOT NULL DEFAULT '0' COMMENT '锁定状态（0未锁定，1已锁定）',
  `status_delete` TINYINT NOT NULL DEFAULT '0' COMMENT '删除状态（0未删除，1已删除）',
  `active_time` TIMESTAMP NULL COMMENT '激活时间',
  `lock_time` TIMESTAMP NULL COMMENT '锁定时间',
  `delete_time` TIMESTAMP NULL COMMENT '删除时间',
  `reg_ip` VARCHAR(20) COMMENT '注册IP',
  `login_ip` VARCHAR(20) COMMENT '最后一次登录IP',
  `login_time` TIMESTAMP NULL COMMENT '最后一次登录时间',
  `create_time` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
  `update_time` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT '更新时间',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='用户全局注册表';


DROP TABLE IF EXISTS `user_auth`;
CREATE TABLE `user_auth` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `user_id` INT NOT NULL DEFAULT '0' COMMENT '用户ID',
  `type_auth` TINYINT NOT NULL DEFAULT '0' COMMENT '认证类型（0账号，1邮箱，2手机，3qq，4微信，5微博）',
  `auth_key` VARCHAR(60) NOT NULL DEFAULT '' COMMENT '授权账号（如果是手机，国家区号+手机号码;第三方登陆，这里是openid）',
  `auth_secret` VARCHAR(60) NOT NULL DEFAULT '' COMMENT '密码凭证（密码;token）',
  `status_verified` TINYINT NOT NULL DEFAULT '0' COMMENT '认证状态（0未认证，1已认证）',
  `create_time` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
  `update_time` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT '更新时间',
  PRIMARY KEY (`id`),
  KEY (`user_id`),
  UNIQUE (`type_auth`, `auth_key`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='用户认证表';


DROP TABLE IF EXISTS `user_profile`;
CREATE TABLE `user_profile` (
  `user_id` INT NOT NULL COMMENT '用户ID',
  `user_pid` INT NOT NULL DEFAULT '0' COMMENT '推荐人用户ID',
  `nickname` VARCHAR(20) NOT NULL DEFAULT '' COMMENT '用户名称',
  `type_level` TINYINT NOT NULL DEFAULT '0' COMMENT '等级类型（0普通，1铜牌，2银牌，3金牌，4钻石）',
  `avatar_url` VARCHAR(60) COMMENT '用户头像',
  `email` VARCHAR(60) NOT NULL DEFAULT '' COMMENT '电子邮箱',
  `area_id` INT(4) NOT NULL DEFAULT '0' COMMENT '国家区号id',
  `area_code` VARCHAR(4) NOT NULL DEFAULT '' COMMENT '国家区号',
  `phone` VARCHAR(20) NOT NULL DEFAULT '' COMMENT '手机号码',
  `birthday` DATE NOT NULL DEFAULT '1900-01-01' COMMENT '生日',
  `id_card` VARCHAR(32) NOT NULL DEFAULT '' COMMENT '身份证号',
  `create_time` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
  `update_time` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT '更新时间',
  PRIMARY KEY (`user_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='用户基本信息表';


DROP TABLE IF EXISTS `user_bank`;
CREATE TABLE `user_bank` (
  `user_id` INT NOT NULL COMMENT '用户ID',
  `account_name` VARCHAR(60) NOT NULL DEFAULT '0' COMMENT '开户人姓名',
  `bank_name` VARCHAR(60) NOT NULL DEFAULT '' COMMENT '开户银行',
  `bank_address` VARCHAR(60) NOT NULL DEFAULT '' COMMENT '开户网点',
  `bank_account` VARCHAR(32) NOT NULL DEFAULT '' COMMENT '银行账号',
  `status_verified` TINYINT NOT NULL DEFAULT '0' COMMENT '认证状态（0未认证，1已认证）',
  `status_delete` TINYINT NOT NULL DEFAULT '0' COMMENT '删除状态（0未删除，1已删除）',
  `create_time` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
  `update_time` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT '更新时间',
  PRIMARY KEY (`user_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='用户银行账号信息';


DROP TABLE IF EXISTS `apply_put`;
CREATE TABLE `apply_put` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `user_id` INT NOT NULL COMMENT '用户Id',
  `type_apply` TINYINT(1) NOT NULL DEFAULT '0' COMMENT '申请类型:0:自主添加，1:后台添加',
  `money_apply` DECIMAL(8, 2) NOT NULL DEFAULT '0.00' COMMENT '申请金额',
  `money_order` DECIMAL(8, 2) NOT NULL DEFAULT '0.00' COMMENT '订单金额',
  `status_apply` TINYINT(1) NOT NULL DEFAULT '0' COMMENT '申请状态:0:待生效，1:已生效，2:取消',
  `status_order` TINYINT(1) NOT NULL DEFAULT '0' COMMENT '订单状态:0:待匹配，1:部分匹配，2:完全匹配',
  `status_delete` TINYINT(1) NOT NULL DEFAULT '0' COMMENT '删除状态:0:未删除，1:已删除',
  `delete_time` TIMESTAMP NULL COMMENT '删除时间',
  `create_time` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
  `update_time` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT '更新时间',
  PRIMARY KEY (`id`),
  KEY `ind_user_id` (`user_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='投资申请表';


DROP TABLE IF EXISTS `apply_get`;
CREATE TABLE `apply_get` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `user_id` INT NOT NULL COMMENT '用户Id',
  `type_apply` TINYINT(1) NOT NULL DEFAULT '0' COMMENT '申请类型:0:自主添加，1:后台生成',
  `money_apply` DECIMAL(8, 2) NOT NULL DEFAULT '0.00' COMMENT '申请金额',
  `money_order` DECIMAL(8, 2) NOT NULL DEFAULT '0.00' COMMENT '订单金额',
  `status_apply` TINYINT(1) NOT NULL DEFAULT '0' COMMENT '申请状态:0:待生效，1:生效，2:取消',
  `status_order` TINYINT(1) NOT NULL DEFAULT '0' COMMENT '匹配状态:0:待匹配，1:部分匹配，2:完全匹配',
  `status_delete` TINYINT(1) NOT NULL DEFAULT '0' COMMENT '删除状态:0:未删除，1:已删除',
  `delete_time` TIMESTAMP NULL COMMENT '删除时间',
  `create_time` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
  `update_time` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT '更新时间',
  PRIMARY KEY (`id`),
  KEY `ind_user_id` (`user_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='提现申请表';


DROP TABLE IF EXISTS `order`;
CREATE TABLE `order` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `apply_put_id` INT NOT NULL COMMENT '申请投资Id',
  `apply_get_id` INT NOT NULL COMMENT '申请提现Id',
  `apply_put_uid` INT NOT NULL COMMENT '申请投资用户Id',
  `apply_get_uid` INT NOT NULL COMMENT '申请提现用户Id',
  `type` TINYINT(1) NOT NULL DEFAULT '0' COMMENT '订单类型0:正常订单，1:流转订单',
  `money` DECIMAL(8, 2) NOT NULL DEFAULT '0.00' COMMENT '订单金额',
  `status_audit` TINYINT(1) NOT NULL DEFAULT '0' COMMENT '审核状态:0:待审核，1:审核通过，2:审核失败',
  `status_flow` TINYINT(1) NOT NULL DEFAULT '0' COMMENT '流转状态:0:未流转，1:已流转',
  `status_pay` TINYINT(1) NOT NULL DEFAULT '0' COMMENT '支付状态:0:待支付，1:支付成功，2:支付失败',
  `status_rec` TINYINT(1) NOT NULL DEFAULT '0' COMMENT '收款状态:0:待收款，1:收款成功，2:收款失败',
  `status_delete` TINYINT(1) NOT NULL DEFAULT '0' COMMENT '删除状态:0:未删除，1:已删除',
  `audit_time` TIMESTAMP NULL COMMENT '审核时间（通过、失败）',
  `pay_time` TIMESTAMP NULL COMMENT '支付时间（成功、失败）',
  `receipt_time` TIMESTAMP NULL COMMENT '收款时间（成功、失败）',
  `delete_time` TIMESTAMP NULL COMMENT '删除时间',
  `create_time` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
  `update_time` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT '更新时间',
  PRIMARY KEY (`id`),
  KEY `ind_apply_put_id` (`apply_put_id`),
  KEY `ind_apply_get_id` (`apply_get_id`),
  KEY `ind_apply_put_uid` (`apply_put_uid`),
  KEY `ind_apply_get_uid` (`apply_get_uid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='订单总表';


DROP TABLE IF EXISTS `order_flow`;
CREATE TABLE `order_flow` (
  `order_id` INT NOT NULL COMMENT '订单Id',
  `flow_order_id` INT NOT NULL COMMENT '流转来源订单Id',
  `apply_put_id` INT NOT NULL COMMENT '申请投资Id',
  `apply_get_id` INT NOT NULL COMMENT '申请提现Id',
  `apply_put_uid` INT NOT NULL COMMENT '申请投资用户Id',
  `apply_get_uid` INT NOT NULL COMMENT '申请提现用户Id',
  `create_time` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
  `update_time` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT '更新时间',
  PRIMARY KEY (`order_id`),
  KEY `ind_flow_order_id` (`flow_order_id`),
  KEY `ind_apply_put_id` (`apply_put_id`),
  KEY `ind_apply_get_id` (`apply_get_id`),
  KEY `ind_apply_put_uid` (`apply_put_uid`),
  KEY `ind_apply_get_uid` (`apply_get_uid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='订单流转记录';


DROP TABLE IF EXISTS `wallet`;
CREATE TABLE `wallet` (
  `user_id` INT NOT NULL COMMENT '用户Id',
  `amount_initial` DECIMAL(10, 2) NOT NULL DEFAULT '0.00' COMMENT '初始总金额',
  `amount_current` DECIMAL(10, 2) NOT NULL DEFAULT '0.00' COMMENT '当前总金额',
  `amount_lock` DECIMAL(10, 2) NOT NULL DEFAULT '0.00' COMMENT '锁定的金额',
  `create_time` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
  `update_time` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT '更新时间',
  PRIMARY KEY (`user_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='钱包总表';


DROP TABLE IF EXISTS `wallet_item`;
CREATE TABLE `wallet_item` (
  `id` INT NOT NULL AUTO_INCREMENT COMMENT '钱包明细id',
  `user_id` INT NOT NULL COMMENT '用户Id',
  `type` TINYINT(1) NOT NULL DEFAULT '0' COMMENT '钱包类型（1：收、2：支）',
  `money` DECIMAL(8, 2) NOT NULL DEFAULT '0.00' COMMENT '金额',
  `sc_id` INT NOT NULL DEFAULT '0' COMMENT '关联id',
  `note` VARCHAR(256) NOT NULL DEFAULT '' COMMENT '备注',
  `status` TINYINT(1) NOT NULL DEFAULT '0' COMMENT '状态:0:待生效，1:已生效，2:作废',
  `create_time` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
  `update_time` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT '更新时间',
  PRIMARY KEY (`id`),
  KEY `ind_user_id` (`user_id`),
  KEY `ind_sc_id` (`sc_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='钱包明细表';


DROP TABLE IF EXISTS `score`;
CREATE TABLE `score` (
  `user_id` INT NOT NULL COMMENT '用户Id',
  `amount` DECIMAL(10, 0) NOT NULL DEFAULT '0' COMMENT '总积分',
  `create_time` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
  `update_time` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT '更新时间',
  PRIMARY KEY (`user_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='积分总表';


DROP TABLE IF EXISTS `score_item`;
CREATE TABLE `score_item` (
  `id` INT NOT NULL AUTO_INCREMENT COMMENT '积分明细id',
  `user_id` INT NOT NULL COMMENT '用户Id',
  `type` TINYINT(1) NOT NULL DEFAULT '0' COMMENT '积分类型（1：加、2：减）',
  `amount` DECIMAL(8, 0) NOT NULL DEFAULT '0' COMMENT '积分分值',
  `note` VARCHAR(256) NOT NULL DEFAULT '' COMMENT '备注',
  `status` TINYINT(1) NOT NULL DEFAULT '0' COMMENT '状态:0:待生效，1:已生效，2:作废',
  `create_time` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
  `update_time` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT '更新时间',
  PRIMARY KEY (`id`),
  KEY `ind_user_id` (`user_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='积分明细表';


DROP TABLE IF EXISTS `bonus`;
CREATE TABLE `bonus` (
  `user_id` INT NOT NULL COMMENT '用户Id',
  `amount` DECIMAL(10, 0) NOT NULL DEFAULT '0' COMMENT '总奖金',
  `create_time` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
  `update_time` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT '更新时间',
  PRIMARY KEY (`user_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='奖金总表';


DROP TABLE IF EXISTS `bonus_item`;
CREATE TABLE `bonus_item` (
  `id` INT NOT NULL AUTO_INCREMENT COMMENT '奖金明细id',
  `user_id` INT NOT NULL COMMENT '用户Id',
  `type` TINYINT(1) NOT NULL DEFAULT '0' COMMENT '奖金类型（1：加、2：减）',
  `amount` DECIMAL(8, 0) NOT NULL DEFAULT '0' COMMENT '奖金金额',
  `note` VARCHAR(256) NOT NULL DEFAULT '' COMMENT '备注',
  `status` TINYINT(1) NOT NULL DEFAULT '0' COMMENT '状态:0:待生效，1:已生效，2:作废',
  `create_time` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
  `update_time` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT '更新时间',
  PRIMARY KEY (`id`),
  KEY `ind_user_id` (`user_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='奖金明细表';


DROP TABLE IF EXISTS `bit_coin`;
CREATE TABLE `bit_coin` (
  `user_id` INT NOT NULL COMMENT '用户Id',
  `amount` DECIMAL(10, 0) NOT NULL DEFAULT '0' COMMENT '数字货币总额',
  `create_time` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
  `update_time` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT '更新时间',
  PRIMARY KEY (`user_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='数字货币总表';


DROP TABLE IF EXISTS `bit_coin_item`;
CREATE TABLE `bit_coin_item` (
  `id` INT NOT NULL AUTO_INCREMENT COMMENT '数字货币明细id',
  `user_id` INT NOT NULL COMMENT '用户Id',
  `type` TINYINT(1) NOT NULL DEFAULT '0' COMMENT '数字货币类型（1：加、2：减）',
  `amount` DECIMAL(8, 0) NOT NULL DEFAULT '0' COMMENT '数字货币金额',
  `note` VARCHAR(256) NOT NULL DEFAULT '' COMMENT '备注',
  `status` TINYINT(1) NOT NULL DEFAULT '0' COMMENT '状态:0:待生效，1:已生效，2:作废',
  `create_time` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
  `update_time` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT '更新时间',
  PRIMARY KEY (`id`),
  KEY `ind_user_id` (`user_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='数字货币明细表';


DROP TABLE IF EXISTS `admin`;
CREATE TABLE `admin` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `username` VARCHAR(20) NOT NULL DEFAULT '' COMMENT '用户名称',
  `password` VARCHAR(60) NOT NULL DEFAULT '' COMMENT '用户密码',
  `area_id` INT(4) NOT NULL DEFAULT '0' COMMENT '国家区号id',
  `area_code` VARCHAR(4) NOT NULL DEFAULT '' COMMENT '国家区号',
  `phone` VARCHAR(20) NOT NULL DEFAULT '' COMMENT '手机号码',
  `role` TINYINT(1) NOT NULL DEFAULT '0' COMMENT '角色:0:普通，1:高级，2:系统',
  `status_delete` TINYINT NOT NULL DEFAULT '0' COMMENT '删除状态（0未删除，1已删除）',
  `delete_time` TIMESTAMP NULL COMMENT '删除时间',
  `login_time` TIMESTAMP NULL COMMENT '最后一次登录时间',
  `login_ip` VARCHAR(20) COMMENT '最后一次登录IP',
  `create_time` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
  `update_time` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT '更新时间',
  PRIMARY KEY (`id`),
  UNIQUE (`username`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='后台用户信息表';


DROP TABLE IF EXISTS `area_code`;
CREATE TABLE `area_code` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `short_code` VARCHAR(2) NOT NULL DEFAULT '' COMMENT '国家简称',
  `area_code` VARCHAR(4) NOT NULL DEFAULT '' COMMENT '区号',
  `phone_pre` VARCHAR(7) NOT NULL DEFAULT '' COMMENT '号码前缀',
  `name_c` VARCHAR(20) NOT NULL DEFAULT '' COMMENT '国家中文名称',
  `name_e` VARCHAR(20) NOT NULL DEFAULT '' COMMENT '国家英文名称',
  `country_area` VARCHAR(20) NOT NULL DEFAULT '' COMMENT '国家板块',
  `create_time` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '留言时间',
  `update_time` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT '更新时间',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='区号';


DROP TABLE IF EXISTS `message`;
CREATE TABLE `message` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `send_user_id` INT NOT NULL COMMENT '消息发送用户Id',
  `receive_user_id` INT NOT NULL COMMENT '消息接收用户Id',
  `content_send` VARCHAR(512) NOT NULL DEFAULT '' COMMENT '留言内容',
  `status_delete` TINYINT NOT NULL DEFAULT '0' COMMENT '删除状态（0未删除，1已删除）',
  `delete_time` TIMESTAMP NULL COMMENT '删除时间',
  `create_time` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '留言时间',
  `update_time` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT '更新时间',
  PRIMARY KEY (`id`),
  KEY `ind_send_user_id` (`send_user_id`),
  KEY `ind_receive_user_id` (`receive_user_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='用户留言';


DROP TABLE IF EXISTS `complaint`;
CREATE TABLE `complaint` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `send_user_id` INT NOT NULL COMMENT '前台投诉用户Id',
  `reply_admin_id` INT NOT NULL DEFAULT '0' COMMENT '后台回复用户Id',
  `content_send` VARCHAR(512) NOT NULL DEFAULT '' COMMENT '留言内容',
  `content_reply` VARCHAR(512) NOT NULL DEFAULT '' COMMENT '回复内容',
  `status_reply` TINYINT NOT NULL DEFAULT '0' COMMENT '回复状态（0未回复，1已回复）',
  `reply_time` TIMESTAMP NULL COMMENT '回复时间',
  `status_delete` TINYINT NOT NULL DEFAULT '0' COMMENT '删除状态（0未删除，1已删除）',
  `delete_time` TIMESTAMP NULL COMMENT '删除时间',
  `create_time` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '留言时间',
  `update_time` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT '更新时间',
  PRIMARY KEY (`id`),
  KEY `ind_send_user_id` (`send_user_id`),
  KEY `ind_reply_admin_id` (`reply_admin_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='投诉';


DROP TABLE IF EXISTS `credit`;
CREATE TABLE `credit` (
  `user_id` INT NOT NULL COMMENT '用户Id',
  `behavior` DECIMAL(3, 0) NOT NULL DEFAULT '0' COMMENT '行为偏好',
  `characteristics` DECIMAL(3, 0) NOT NULL DEFAULT '0' COMMENT '身份特质',
  `connections` DECIMAL(3, 0) NOT NULL DEFAULT '0' COMMENT '人脉关系',
  `history` DECIMAL(3, 0) NOT NULL DEFAULT '0' COMMENT '信用历史',
  `performance` DECIMAL(3, 0) NOT NULL DEFAULT '0' COMMENT '履约能力',
  `credit` DECIMAL(3, 0) NOT NULL DEFAULT '0' COMMENT '整体信用',
  `create_time` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
  `update_time` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT '更新时间',
  PRIMARY KEY (`user_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='用户声望（信用）';

