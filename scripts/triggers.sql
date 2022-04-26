USE `pitch_data`;

-- Pitches
-- This trigger protects against deletion of original, raw data that is important to the site's functionality 
DROP TRIGGER IF EXISTS pitches_before_delete;

DELIMITER //

CREATE TRIGGER pitches_before_delete
BEFORE DELETE
ON pitches
FOR EACH ROW
BEGIN
	IF OLD.id IN (SELECT id FROM pitch_data) THEN
		SIGNAL SQLSTATE '45000'
		SET MESSAGE_TEXT = 'This row cannot be deleted',
        MYSQL_ERRNO = 1045;
	END IF;
END //

-- DELETE FROM pitches WHERE id = 100;

-- Atbats
-- This trigger protects against deletion of original, raw data that is important to the site's functionality 
DROP TRIGGER IF EXISTS atbats_before_delete;

DELIMITER //

CREATE TRIGGER atbats_before_delete
BEFORE DELETE
ON atbats
FOR EACH ROW
BEGIN
	IF OLD.ab_id IN (SELECT ab_id FROM pitch_data) THEN
		SIGNAL SQLSTATE '45000'
		SET MESSAGE_TEXT = 'This row cannot be deleted',
        MYSQL_ERRNO = 1045;
	END IF;
END //

-- DELETE FROM atbats WHERE ab_id = 2015001397;