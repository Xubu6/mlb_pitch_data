-- Alan Xu, Jai Bansal
-- DBMS Project 2
-- Run this SQL script to create the views `pitch_analysis_view` and `2018_pitch_data`

-- Create view `pitch_data`.`pitch_analysis`
-- All stored procedures will pull from this view, as it contains the minimal attributes necessary for functionality

CREATE OR REPLACE VIEW pitch_analysis_view AS
SELECT `id`, `ab_id`, `batter_id`, `batter_name`, `event`, `pitcher_id`, `pitcher_name`,
	`stand`, `top`, `px`, `pz`, `start_speed`, `end_speed`, `spin_rate`, `spin_dir`, 
    `break_angle`, `break_length`, `break_y`, `nasty`, `zone`, `code`, `type`, `pitch_type` 
FROM pitch_data
ORDER BY id;

-- Create view `pitcher_info`;
-- Average start speeds, spin rates, break lengths, and vertical breaks by all pitchers in the data
CREATE OR REPLACE VIEW `pitcher_info` AS
SELECT pitcher_name, AVG(start_speed) AS avg_start_speed, AVG(spin_rate) AS avg_spin_rate, AVG(break_length) AS avg_break_length, AVG(break_y) AS avg_break_y
FROM pitch_analysis
GROUP BY pitcher_name;

-- SELECT * FROM pitcher_info;

-- SELECT * FROM pitch_analysis_view;






