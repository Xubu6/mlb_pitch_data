-- Alan Xu, Jai Bansal
-- DBMS Project 2
-- Run this SQL script to create the Schema `pitch_data` and the tables `pitch_data`, `atbats`, and `pitches`

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';


CREATE SCHEMA IF NOT EXISTS `pitch_data` DEFAULT CHARACTER SET utf8 ;
USE `pitch_data` ;

-- Create table `pitch_data`.`pitch_data`
DROP TABLE IF EXISTS `pitch_data`.`pitch_data` ;

CREATE TABLE IF NOT EXISTS `pitch_data`.`pitch_data` (
  `id` INT(11) PRIMARY KEY,
  `ab_id` INT(11) NOT NULL,
  `batter_id` INT(11) NULL,
  `batter_name` VARCHAR(55),
  `event` VARCHAR(20) NULL,
  `g_id` INT(11) NULL,
  `inning` TINYINT NULL,
  `o` TINYINT NULL,
  `p_score` TINYINT NULL,
  `p_throws` CHAR(2) NULL,
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
  `ax` DECIMAL(6,3) NULL,
  `ay` DECIMAL(6,3) NULL,
  `az` DECIMAL(6,3) NULL,
  `sz_bot` DECIMAL(4,2) NULL,
  `sz_top` DECIMAL(4,2) NULL,
  `type_confidence` DECIMAL(4,3) NULL,
  `vx0` DECIMAL(6,3) NULL,
  `vy0` DECIMAL(6,3) NULL,
  `vz0` DECIMAL(6,3) NULL,
  `x` DECIMAL(10,3) NULL,
  `x0` DECIMAL(10,3) NULL,
  `y` DECIMAL(10,3) NULL,
  `y0` DECIMAL(10,3) NULL,
  `z0` DECIMAL(10,3) NULL,
  `pfx_x` DECIMAL(6,2) NULL,
  `pfx_z` DECIMAL(6,2) NULL,
  `nasty` INT(5) NULL,
  `zone` INT(5) NULL,
  `code` CHAR(3) NULL,
  `type` CHAR(2) NULL,
  `pitch_type` CHAR(3) NULL,
  `event_num` INT(5) NULL,
  `b_score` TINYINT NULL,
  `b_count` TINYINT NULL,
  `s_count` TINYINT NULL,
  `outs` TINYINT NULL,
  `pitch_num` TINYINT NULL,
  `on_1b` TINYINT NULL,
  `on_2b` TINYINT NULL,
  `on_3b` TINYINT NULL)
ENGINE = InnoDB;

-- Create table `pitch_data`.`player_names`
DROP TABLE IF EXISTS `pitch_data`.`player_names` ;

CREATE TABLE IF NOT EXISTS `pitch_data`.`player_names` (
  `id` INT NOT NULL,
  `first_name` VARCHAR(45) NULL,
  `last_name` VARCHAR(45) NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;

-- Create table `pitch_data`.`atbats`
DROP TABLE IF EXISTS `pitch_data`.`atbats` ;

CREATE TABLE IF NOT EXISTS `pitch_data`.`atbats` (
  `ab_id` INT(11) NOT NULL,
  `batter_id` INT(11) NULL,
  `event` VARCHAR(20) NULL,
  `g_id` INT(11) NULL,
  `inning` TINYINT NULL,
  `o` TINYINT NULL,
  `p_score` TINYINT NULL,
  `p_throws` CHAR(2) NULL,
  `pitcher_id` INT(11) NULL,
  `stand` CHAR(2) NULL,
  `top` VARCHAR(10) NULL,
  PRIMARY KEY (`ab_id`),
  INDEX `fk_batter_id_idx` (`batter_id` ASC),
  INDEX `fk_pitcher_id_idx` (`pitcher_id` ASC),
  CONSTRAINT `fk_batter_id`
    FOREIGN KEY (`batter_id`)
    REFERENCES `pitch_data`.`player_names` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_pitcher_id`
    FOREIGN KEY (`pitcher_id`)
    REFERENCES `pitch_data`.`player_names` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;

-- Create table `pitch_data`.`pitches`
DROP TABLE IF EXISTS `pitch_data`.`pitches` ;

CREATE TABLE IF NOT EXISTS `pitch_data`.`pitches` (
  `px` DECIMAL(4,3) NULL,
  `pz` DECIMAL(4,3) NULL,
  `start_speed` DECIMAL(10,2) NULL,
  `end_speed` DECIMAL(10,2) NULL,
  `spin_rate` DECIMAL(10,3) NULL,
  `spin_dir` DECIMAL(10,3) NULL,
  `break_angle` DECIMAL(3,1) NULL,
  `break_length` DECIMAL(3,1) NULL,
  `break_y` DECIMAL(3,1) NULL,
  `ax` DECIMAL(6,3) NULL,
  `ay` DECIMAL(6,3) NULL,
  `az` DECIMAL(6,3) NULL,
  `sz_bot` DECIMAL(4,2) NULL,
  `sz_top` DECIMAL(4,2) NULL,
  `type_confidence` DECIMAL(4,3) NULL,
  `vx0` DECIMAL(6,3) NULL,
  `vy0` DECIMAL(6,3) NULL,
  `vz0` DECIMAL(6,3) NULL,
  `x` DECIMAL(10,3) NULL,
  `x0` DECIMAL(10,3) NULL,
  `y` DECIMAL(10,3) NULL,
  `y0` DECIMAL(10,3) NULL,
  `z0` DECIMAL(10,3) NULL,
  `pfx_x` DECIMAL(6,2) NULL,
  `pfx_z` DECIMAL(6,2) NULL,
  `nasty` INT(5) NULL,
  `zone` INT(5) NULL,
  `code` CHAR(3) NULL,
  `type` CHAR(2) NULL,
  `pitch_type` CHAR(3) NULL,
  `event_num` INT(5) NULL,
  `b_score` TINYINT NULL,
  `ab_id` INT(11) NULL,
  `b_count` TINYINT NULL,
  `s_count` TINYINT NULL,
  `outs` TINYINT NULL,
  `pitch_num` TINYINT NULL,
  `on_1b` TINYINT NULL,
  `on_2b` TINYINT NULL,
  `on_3b` TINYINT NULL,
  INDEX `fk_ab_id_idx` (`ab_id` ASC),
  CONSTRAINT `fk_ab_id`
    FOREIGN KEY (`ab_id`)
    REFERENCES `pitch_data`.`atbats` (`ab_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
