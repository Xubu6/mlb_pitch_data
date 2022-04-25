-- Create view `pitch_data`.`pitch_analysis`
DROP VIEW IF EXISTS `pitch_data`.`pitch_analysis`;

CREATE VIEW IF NOT EXISTS `pitch_data`.`pitch_analysis` (
	`id` INT(11) PRIMARY KEY, 
    `ab_id` INT(11) NOT NULL, 
    `batter_id`INT(11) NULL,
    `batter_name` VARCHAR(55), 
    `event` VARCHAR(20) NULL, 
    `pitcher_id` INT(11) NULL, 
    `pitcher_name` VARCHAR(55), 
    `stand` CHAR(2) NULL, 
    `top` VARCHAR(10) NULL, 
    `px` DECIMAL(4,3) NULL, 
    `pz` DECIMAL(4,3) NULL, 
    `start_speed` DECIMAL(10,2) NULL, 
    `end_speed` DECIMAL(10,2) NULL, 
    `spin_rate` DECIMAL(10,3) NULL, 
    `spin_dir` DECIMAL(10,3) NULL, 
    `break_angle` DECIMAL(3,1) NULL,
    `break_length` DECIMAL(3,1) NULL, 
    `break_y` DECIMAL(3,1) NULL, 
    `nasty` INT(5) NULL, 
    `zone` INT(5) NULL, 
    `code` CHAR(3) NULL, 
    `type` CHAR(2) NULL, 
    `pitch_type` CHAR(3) NULL)
ENGINE = InnoDB;


CREATE VIEW `2018_pitch_data`;