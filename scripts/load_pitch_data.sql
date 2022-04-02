-- Alan Xu, Jai Bansal
-- DBMS Project 2
-- Run this SQL script to load data sets into the tables `atbats` and `pitches`

USE `pitch_data`;

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

-- SELECT COUNT(*) FROM atbats;
SELECT * FROM pitches JOIN atbats USING(ab_id) limit 50;




