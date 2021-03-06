-- Alan Xu, Jai Bansal
-- DBMS Project 2
-- Run this SQL script to load data sets into the tables `atbats` and `pitches` and `pitch_data`
-- You may have to adjust the locations of the files depending on where they are in your directories

USE `pitch_data`;

-- Load atbat data from player_names.csv 
LOAD DATA 
	INFILE '/Users/alanxu/mlb_pitch_data/raw_data/player_names.csv' 
	INTO TABLE player_names
    FIELDS TERMINATED BY ','
    ENCLOSED BY '"' 
	LINES TERMINATED BY '\n'
    IGNORE 1 ROWS; -- Header Line

-- Should be 2218 lines

-- Load atbat data from atbat.csv 
LOAD DATA 
	INFILE '/Users/alanxu/mlb_pitch_data/raw_data/atbats.csv' 
	INTO TABLE atbats
    FIELDS TERMINATED BY ','
    ENCLOSED BY '"' 
	LINES TERMINATED BY '\n'
    IGNORE 1 ROWS; -- Header Line

-- Should be 740389 lines

    
-- Load pitch data from pitches.csv 
LOAD DATA 
	INFILE '/Users/alanxu/mlb_pitch_data/raw_data/pitches.csv' IGNORE
	INTO TABLE pitches
    FIELDS TERMINATED BY ','
    ENCLOSED BY '"' 
	LINES TERMINATED BY '\n'
    IGNORE 1 ROWS; -- Header line
    
-- Should be 2867154 lines (certain rows truncated because bad data)

-- Need to run this after pitches creation, as the original data set does not have a pk and Pythons MySQL API requires that there is a pk
ALTER TABLE pitches ADD id INT PRIMARY KEY AUTO_INCREMENT;

-- Populate Megatable (pitch_data)
INSERT INTO pitch_data (`id`,`ab_id`, `batter_id`, `batter_name`, `event`, `g_id`, `inning`, `o`,`p_score`,`p_throws`, `pitcher_id`, `pitcher_name`,
  `stand`,`top`,`px`,`pz`,`start_speed`,`end_speed`,`spin_rate`,`spin_dir`,`break_angle`,`break_length`, `break_y`, `ax`, `ay`,
  `az`, `sz_bot`,  `sz_top`,  `type_confidence`,  `vx0`,  `vy0`,  `vz0`,  `x`,  `x0`,`y`,`y0`,`z0`,`pfx_x`, `pfx_z`, `nasty`,`zone`,
  `code`,`type`,`pitch_type`,`event_num`,`b_score`, `b_count`, `s_count`, `outs`, `pitch_num`, `on_1b`, `on_2b`, `on_3b`)
SELECT 
  p.`id`, a.`ab_id`, a.`batter_id`, CONCAT(pn1.`first_name`, ' ', pn1.`last_name`), a.`event`, a.`g_id`, 
  a.`inning`, a.`o`,a.`p_score`,a.`p_throws`, a.`pitcher_id`, CONCAT(pn2.`first_name`, ' ', pn2.`last_name`), a.`stand`,a.`top`,p.`px`,p.`pz`,
  p.`start_speed`,p.`end_speed`,p.`spin_rate`,p.`spin_dir`, p.`break_angle`,p.`break_length`, p.`break_y`,p.`ax`, p.`ay`, p.`az`,
  p.`sz_bot`,  p.`sz_top`,  p.`type_confidence`,  p.`vx0`,  p.`vy0`,  p.`vz0`, p.`x`, p.`x0`,p.`y`,p.`y0`,p.`z0`,p.`pfx_x`,
  p.`pfx_z`,p.`nasty`,p.`zone`,p.`code`,p.`type`,p.`pitch_type`,p.`event_num`,p.`b_score`, p.`b_count`, p.`s_count`, p.`outs`,
  p.`pitch_num`, p.`on_1b`, p.`on_2b`, p.`on_3b`
FROM pitches p 
JOIN atbats a USING (ab_id)
JOIN player_names pn1 ON (a.batter_id = pn1.id)
JOIN player_names pn2 ON (a.pitcher_id = pn2.id);


-- Load Data into decomoposed pitch_analysis table
INSERT INTO pitch_analysis (`id`, `ab_id`, `batter_id`, `batter_name`, `event`, `pitcher_id`, `pitcher_name`, `stand`, `top`, `px`, `pz`, `start_speed`, `end_speed`, `spin_rate`, `spin_dir`, `break_angle`, `break_length`, `break_y`, `nasty`, `zone`, `code`, `type`, `pitch_type` )
SELECT `id`, `ab_id`, `batter_id`, `batter_name`, `event`, `pitcher_id`, `pitcher_name`, `stand`, `top`, `px`, `pz`, `start_speed`, `end_speed`, `spin_rate`, `spin_dir`, `break_angle`, `break_length`, `break_y`, `nasty`, `zone`, `code`, `type`, `pitch_type` 
FROM pitch_data;


-- SELECT statements
-- --------------------- --
-- SELECT COUNT(*) FROM atbats;
-- SELECT * FROM pitches JOIN atbats USING(ab_id) limit 50;
-- SELECT * FROM pitch_data LIMIT 100;

SELECT * FROM pitch_data LIMIT 50;

SELECT * FROM pitch_analysis LIMIT 50;




