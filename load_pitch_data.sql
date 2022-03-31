-- Alan Xu, Jai Bansal
-- DBMS Project 2
-- Run this SQL script to load data sets into the tables `atbats` and `pitches`

USE `pitch_data`;

-- Load atbat data from atbat.csv 
LOAD DATA 
	INFILE '/Applications/MAMP/tmp/atbats.csv' IGNORE
	INTO TABLE atbats
    FIELDS ENCLOSED BY '"' TERMINATED BY ','
	LINES TERMINATED BY '\n'
    IGNORE 1 LINES; -- Header Line
    
-- Load pitch data from pitches.csv 
LOAD DATA 
	INFILE '/Applications/MAMP/tmp/pitches.csv' IGNORE
	INTO TABLE pitches
    FIELDS ENCLOSED BY '"' TERMINATED BY ','
	LINES TERMINATED BY '\n';

    
SELECT * FROM atbats
LIMIT 50;

SELECT *
FROM pitches
LIMIT 50;