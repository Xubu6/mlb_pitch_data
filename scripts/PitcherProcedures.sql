-- Pitcher Stored Procedures


USE `pitch_data`;

-- Pitch/Spin Rate Leaderboard

DROP PROCEDURE IF EXISTS pitch_spin_rate_leaderboard;

DELIMITER //

CREATE PROCEDURE pitch_spin_rate_leaderboard(IN pitch_type_param CHAR(3), IN sample_size INT)

BEGIN

	SELECT pitcher_name, AVG(spin_rate)
    FROM pitch_analysis
    WHERE pitch_type = pitch_type_param
    GROUP BY pitcher_name
    HAVING COUNT(spin_rate) > sample_size
    ORDER BY AVG(spin_rate) DESC;

END //


CALL pitch_spin_rate_leaderboard('FF',500);

-- Pitch / Start Speed Leaderboard

DROP PROCEDURE IF EXISTS pitch_start_speed_leaderboard;

DELIMITER //

CREATE PROCEDURE pitch_start_speed_leaderboard(IN pitch_type_param CHAR(3), IN sample_size INT)

BEGIN

	SELECT pitcher_name, AVG(start_speed)
    FROM pitch_analysis
    WHERE pitch_type = pitch_type_param
    GROUP BY pitcher_name
    HAVING COUNT(start_speed) > sample_size
    ORDER BY AVG(start_speed) DESC;

END //

CALL pitch_start_speed_leaderboard('FF',500);

-- Pitch / Break Length Leaderboard

DROP PROCEDURE IF EXISTS pitch_break_length_leaderboard;

DELIMITER //

CREATE PROCEDURE pitch_break_length_leaderboard(IN pitch_type_param CHAR(3), IN sample_size INT)

BEGIN

	SELECT pitcher_name, AVG(break_length)
    FROM pitch_analysis
    WHERE pitch_type = pitch_type_param
    GROUP BY pitcher_name
    HAVING COUNT(break_length) > sample_size
    ORDER BY AVG(break_length) DESC;

END //

CALL pitch_break_length_leaderboard('SL',500);

-- Pitch / Break Y Leaderboard

DROP PROCEDURE IF EXISTS pitch_break_y_leaderboard;

DELIMITER //

CREATE PROCEDURE pitch_break_y_leaderboard(IN pitch_type_param CHAR(3), IN sample_size INT)

BEGIN

	SELECT pitcher_name, AVG(break_y)
    FROM pitch_analysis
    WHERE pitch_type = pitch_type_param
    GROUP BY pitcher_name
    HAVING COUNT(break_y) > sample_size
    ORDER BY AVG(break_y) DESC;

END //

CALL pitch_break_y_leaderboard('FS',100);


-- Pitch / Nasty Leaderboard

DROP PROCEDURE IF EXISTS pitch_nasty_leaderboard;

DELIMITER //

CREATE PROCEDURE pitch_nasty_leaderboard(IN pitch_type_param CHAR(3), IN sample_size INT)

BEGIN

	SELECT pitcher_name, AVG(nasty)
    FROM pitch_analysis
    WHERE pitch_type = pitch_type_param
    GROUP BY pitcher_name
    HAVING COUNT(nasty) > sample_size
    ORDER BY AVG(nasty) DESC;

END //

CALL pitch_nasty_leaderboard('FF',100);


-- General Nasty Leaderboard
DROP PROCEDURE IF EXISTS nasty_leaderboard;

DELIMITER //

CREATE PROCEDURE nasty_leaderboard(IN sample_size INT)

BEGIN

	SELECT pitcher_name, AVG(nasty)
    FROM pitch_analysis
    GROUP BY pitcher_name
    HAVING COUNT(nasty) > sample_size
    ORDER BY AVG(nasty) DESC;

END //

CALL nasty_leaderboard(100);

-- General Spin Rate Leaderboard
DROP PROCEDURE IF EXISTS spin_rate_leaderboard;

DELIMITER //

CREATE PROCEDURE spin_rate_leaderboard(IN sample_size INT)

BEGIN

	SELECT pitcher_name, AVG(spin_rate)
    FROM pitch_analysis
    GROUP BY pitcher_name
    HAVING COUNT(spin_rate) > sample_size
    ORDER BY AVG(spin_rate) DESC;

END //

CALL spin_rate_leaderboard(100);

-- General Break Length Leaderboard
DROP PROCEDURE IF EXISTS break_length_leaderboard;

DELIMITER //

CREATE PROCEDURE break_length_leaderboard(IN sample_size INT)

BEGIN

	SELECT pitcher_name, AVG(break_length)
    FROM pitch_analysis
    GROUP BY pitcher_name
    HAVING COUNT(break_length) > sample_size
    ORDER BY AVG(break_length) DESC;

END //

CALL break_length_leaderboard(100);


-- General Break Y Leaderboard
DROP PROCEDURE IF EXISTS break_y_leaderboard;

DELIMITER //

CREATE PROCEDURE break_y_leaderboard(IN sample_size INT)

BEGIN

	SELECT pitcher_name, AVG(break_y)
    FROM pitch_analysis
    GROUP BY pitcher_name
    HAVING COUNT(break_y) > sample_size
    ORDER BY AVG(break_y) DESC;

END //

CALL break_y_leaderboard(100);

-- General Start Speed Leaderboard
DROP PROCEDURE IF EXISTS start_speed_leaderboard;

DELIMITER //

CREATE PROCEDURE start_speed_leaderboard(IN sample_size INT)

BEGIN

	SELECT pitcher_name, AVG(start_speed)
    FROM pitch_analysis
    GROUP BY pitcher_name
    HAVING COUNT(start_speed) > sample_size
    ORDER BY AVG(start_speed) DESC;

END //

CALL start_speed_leaderboard(100);

-- Pitcher Pitch Info
DROP PROCEDURE IF EXISTS pitcher_pitch_info;

DELIMITER //

CREATE PROCEDURE pitcher_pitch_info(IN pitch_name_param VARCHAR(55), IN pitch_type_param CHAR(3))

BEGIN

	SELECT pitcher_name, pitch_type, AVG(start_speed), AVG(spin_rate), AVG(break_length), AVG(break_y)
    FROM pitch_analysis
    WHERE pitcher_name =  pitch_name_param AND pitch_type = pitch_type_param
    GROUP BY pitch_type;

END //

CALL pitcher_pitch_info('Aroldis Chapman', 'FF');


 
    