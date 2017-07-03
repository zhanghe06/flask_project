ALTER TABLE `score_item` MODIFY `amount` DECIMAL(8, 2) NOT NULL DEFAULT '0' COMMENT '积分分值';
ALTER TABLE `score_charity_item` MODIFY `amount` DECIMAL(8, 2) NOT NULL DEFAULT '0' COMMENT '积分分值';
ALTER TABLE `score_digital_item` MODIFY `amount` DECIMAL(8, 2) NOT NULL DEFAULT '0' COMMENT '积分分值';
ALTER TABLE `score_expense_item` MODIFY `amount` DECIMAL(8, 2) NOT NULL DEFAULT '0' COMMENT '积分分值';
ALTER TABLE `bonus_item` MODIFY `amount` DECIMAL(8, 2) NOT NULL DEFAULT '0' COMMENT '奖金金额';
ALTER TABLE `scheduling_item` MODIFY `amount` DECIMAL(8, 2) NOT NULL DEFAULT '0' COMMENT '排单分值';
