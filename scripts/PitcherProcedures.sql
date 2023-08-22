-- Pitcher Stored Procedures

USE `pitch_data`;

-- Pitch/Spin Rate Leaderboard
-- this SP takes in a parameter that represents the pitch type and returns 
-- a leaderboard of pitchers with the highest average spin rates for that pitch
DROP PROCEDURE IF EXISTS pitch_spin_rate_leaderboard;

DELIMITER //

CREATE PROCEDURE pitch_spin_rate_leaderboard(IN pitch_type_param CHAR(5))

BEGIN

	SELECT pitcher_name, AVG(spin_rate)
    FROM pitch_analysis_view
    WHERE pitch_type = pitch_type_param
    GROUP BY pitcher_name
    ORDER BY AVG(spin_rate) DESC;

END //

-- Test the above SP
CALL pitch_spin_rate_leaderboard('FF');

-- Pitch / Start Speed Leaderboard
-- this SP takes in a parameter that represents the pitch type and returns 
-- a leaderboard of pitchers with the highest average velocities for that pitch
DROP PROCEDURE IF EXISTS pitch_start_speed_leaderboard;

DELIMITER //

CREATE PROCEDURE pitch_start_speed_leaderboard(IN pitch_type_param CHAR(5))

BEGIN

	SELECT pitcher_name, AVG(start_speed)
    FROM pitch_analysis_view
    WHERE pitch_type = pitch_type_param
    GROUP BY pitcher_name
    ORDER BY AVG(start_speed) DESC;

END //

DELIMITER ;

-- Test the above SP
CALL pitch_start_speed_leaderboard('FF');

-- Pitch / Break Length Leaderboard
-- this SP takes in a parameter that represents the pitch type and returns 
-- a leaderboard of pitchers with the highest average break length for that pitch
DROP PROCEDURE IF EXISTS pitch_break_length_leaderboard;

DELIMITER //

CREATE PROCEDURE pitch_break_length_leaderboard(IN pitch_type_param CHAR(5))

BEGIN

	SELECT pitcher_name, AVG(break_length)
    FROM pitch_analysis_view
    WHERE pitch_type = pitch_type_param
    GROUP BY pitcher_name
    ORDER BY AVG(break_length) DESC;

END //

DELIMITER ;

-- Test the above SP
CALL pitch_break_length_leaderboard('SL');

-- Pitch / Break Y Leaderboard
-- this SP takes in a parameter that represents the pitch type and returns 
-- a leaderboard of pitchers with the highest average break (y) for that pitch
DROP PROCEDURE IF EXISTS pitch_break_y_leaderboard;

DELIMITER //

CREATE PROCEDURE pitch_break_y_leaderboard(IN pitch_type_param CHAR(5))

BEGIN

	SELECT pitcher_name, AVG(break_y)
    FROM pitch_analysis_view
    WHERE pitch_type = pitch_type_param
    GROUP BY pitcher_name
    ORDER BY AVG(break_y) DESC;

END //

DELIMITER ;

-- Test the above SP
CALL pitch_break_y_leaderboard('FS');


-- Pitch / Nasty Leaderboard
-- this SP takes in a parameter that represents the pitch type and returns 
-- a leaderboard of pitchers with the nastiest stuff for that pitch
DROP PROCEDURE IF EXISTS pitch_nasty_leaderboard;

DELIMITER //

CREATE PROCEDURE pitch_nasty_leaderboard(IN pitch_type_param CHAR(5))

BEGIN

	SELECT pitcher_name, AVG(nasty)
    FROM pitch_analysis_view
    WHERE pitch_type = pitch_type_param
    GROUP BY pitcher_name
    ORDER BY AVG(nasty) DESC;

END //

DELIMITER ;

-- Test the above SP
CALL pitch_nasty_leaderboard('FF');


-- General Nasty Leaderboard
-- this SP takes in a parameter that represents the min pitches to be qualified and returns
-- a leaderboard of pitchers with the nastiest stuff as long as they have that number of pitches
DROP PROCEDURE IF EXISTS nasty_leaderboard;

DELIMITER //

CREATE PROCEDURE nasty_leaderboard(IN sample_size CHAR(5))

BEGIN

	SELECT pitcher_name, AVG(nasty), COUNT(start_speed) AS pitch_count
    FROM pitch_analysis_view
    GROUP BY pitcher_name
    HAVING COUNT(nasty) > sample_size
    ORDER BY AVG(nasty) DESC;

END //

DELIMITER ;

-- Test the above SP
CALL nasty_leaderboard(100);

-- General Spin Rate Leaderboard
-- this SP takes in a parameter that represents the min pitches to be qualified and returns
-- a leaderboard of pitchers with the best spin rates as long as they have that number of pitches
DROP PROCEDURE IF EXISTS spin_rate_leaderboard;

DELIMITER //

CREATE PROCEDURE spin_rate_leaderboard(IN sample_size CHAR(5))

BEGIN

	SELECT pitcher_name, AVG(spin_rate), COUNT(start_speed) AS pitch_count
    FROM pitch_analysis_view
    GROUP BY pitcher_name
    HAVING COUNT(spin_rate) > sample_size
    ORDER BY AVG(spin_rate) DESC;

END //

DELIMITER ;

-- Test the above SP
CALL spin_rate_leaderboard(100);

-- General Break Length Leaderboard
-- this SP takes in a parameter that represents the min pitches to be qualified and returns
-- a leaderboard of pitchers with the best break length as long as they have that number of pitches
DROP PROCEDURE IF EXISTS break_length_leaderboard;

DELIMITER //

CREATE PROCEDURE break_length_leaderboard(IN sample_size CHAR(5))

BEGIN

	SELECT pitcher_name, AVG(break_length), COUNT(start_speed) AS pitch_count
    FROM pitch_analysis_view
    GROUP BY pitcher_name
    HAVING COUNT(break_length) > sample_size
    ORDER BY AVG(break_length) DESC;

END //

DELIMITER ;

-- Test the above SP
CALL break_length_leaderboard(100);


-- General Break Y Leaderboard
-- this SP takes in a parameter that represents the min pitches to be qualified and returns
-- a leaderboard of pitchers with the best break (y) as long as they have that number of pitches
DROP PROCEDURE IF EXISTS break_y_leaderboard;

DELIMITER //

CREATE PROCEDURE break_y_leaderboard(IN sample_size CHAR(5))

BEGIN

	SELECT pitcher_name, AVG(break_y), COUNT(start_speed) AS pitch_count
    FROM pitch_analysis_view
    GROUP BY pitcher_name
    HAVING COUNT(break_y) > sample_size
    ORDER BY AVG(break_y) DESC;

END //

DELIMITER ;

-- Test the above SP

CALL break_y_leaderboard(100);

-- General Start Speed Leaderboard
-- this SP takes in a parameter that represents the min pitches to be qualified and returns
-- a leaderboard of pitchers with the best velocity as long as they have that number of pitches
DROP PROCEDURE IF EXISTS start_speed_leaderboard;

DELIMITER //

CREATE PROCEDURE start_speed_leaderboard(IN sample_size CHAR(5))

BEGIN

	SELECT pitcher_name, AVG(start_speed), COUNT(start_speed) AS pitch_count
    FROM pitch_analysis_view
    GROUP BY pitcher_name
    HAVING COUNT(start_speed) > sample_size
    ORDER BY AVG(start_speed) DESC;

END //

DELIMITER ;

-- Test the above SP
CALL start_speed_leaderboard(100);

-- Pitcher Pitch Info
-- this SP takes in a parameter to signal type of pitch and another that has the pitcher's name
-- returns a row of that pitcher's average stats for that type of pitch
DROP PROCEDURE IF EXISTS pitcher_pitch_info;

DELIMITER //

CREATE PROCEDURE pitcher_pitch_info(IN pitch_type_param CHAR(3), IN pitch_name_param VARCHAR(55))

BEGIN

	SELECT pitcher_name, pitch_type, AVG(start_speed), AVG(spin_rate), AVG(break_length), AVG(break_y)
    FROM pitch_analysis_view
    WHERE pitcher_name =  pitch_name_param AND pitch_type = pitch_type_param
    GROUP BY pitch_type;

END //

DELIMITER ;
-- test the above sp
CALL pitcher_pitch_info('FF', 'Aroldis Chapman');

    