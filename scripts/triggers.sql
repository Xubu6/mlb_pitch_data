USE `pitch_data`;

-- Triggers
DROP TRIGGER IF EXISTS pitches_before_delete;

DELIMITER //

CREATE TRIGGER pitches_before_delete
AFTER UPDATE
ON pitches
FOR EACH ROW
BEGIN
	INSERT INTO atbats(
		product_id,
		category_id,
		product_code,
		product_name,
		list_price,
		discount_percent,
		date_updated)
	VALUES(NEW.product_id, NEW.category_id, NEW.product_code, NEW.product_name, NEW.list_price, NEW.discount_percent, NOW());
END //

-- Atbats
DROP TRIGGER IF EXISTS atbats_before_delete;

DELIMITER //

CREATE TRIGGER atbats_before_delete
AFTER UPDATE
ON atbats
FOR EACH ROW
BEGIN
	IF NEW.discount_percent > 100 THEN
		SIGNAL SQLSTATE '22003'
		SET MESSAGE_TEXT = 'The discount percent is more than 100.',
        MYSQL_ERRNO = 1264;
	ELSEIF NEW.discount_percent < 0 THEN
		SIGNAL SQLSTATE '22003'
		SET MESSAGE_TEXT = 'The discount percent cannot be a negative value.',
        MYSQL_ERRNO = 1264;	
	ELSEIF NEW.discount_percent < 1 THEN
		SET NEW.discount_percent = NEW.discount_percent * 100;
	END IF;
END //