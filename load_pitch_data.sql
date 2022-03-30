-- Alan Xu, Jai Bansal
-- DBMS Project 2
-- Run this SQL script to load data sets into the tables `atbats` and `pitches`

USE `pitch_data`;

-- Load atbat data from atbat.csv 
LOAD DATA 
	INFILE '/Users/alanxu/mlb_pitch_data/raw_data/atbats.csv'
	INTO TABLE atbats
    FIELDS ENCLOSED BY '"' TERMINATED BY ','
	LINES TERMINATED BY '\r\n'
    IGNORE 1 LINES; -- Header Line
    
-- Load pitch data from pitches.csv 
LOAD DATA 
	INFILE '/Users/alanxu/mlb_pitch_data/raw_data/pitches.csv'
	INTO TABLE pitches
    FIELDS ENCLOSED BY '"' TERMINATED BY ','
	LINES TERMINATED BY '\r\n'
    IGNORE 1 LINES; -- Header line
    
SELECT * FROM pitches
LIMIT 50;