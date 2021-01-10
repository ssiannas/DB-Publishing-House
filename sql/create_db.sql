CREATE TABLE `Printer` (
	`print_id` INT NOT NULL AUTO_INCREMENT,
	`print_phone` varchar(255) NOT NULL,
	`print_street` varchar(255) NOT NULL,
	`print_streetno` varchar(255) NOT NULL,
	`print_city` varchar(255) NOT NULL,
	`print_zipcode` varchar(255) NOT NULL,
	PRIMARY KEY (`print_id`)
);

CREATE TABLE `Warehouse` (
	`wh_id` INT NOT NULL AUTO_INCREMENT,
	`wh_phone` varchar(255) NOT NULL,
	`wh_street` varchar(255) NOT NULL,
	`wh_streetno` varchar(255) NOT NULL,
	`wh_city` varchar(255) NOT NULL,
	`wh_zipcode` varchar(255) NOT NULL,
	`max_storage` INT NOT NULL DEFAULT '100',
	PRIMARY KEY (`wh_id`)
);

CREATE TABLE `Book` (
	`book_id` INT NOT NULL AUTO_INCREMENT,
	`ISBN` varchar(255) NOT NULL UNIQUE DEFAULT '0',
	`title` varchar(255) NOT NULL,
	`editionno` varchar(255) NOT NULL,
	`publdate` varchar(255) NOT NULL,
	`language` varchar(255) NOT NULL,
	PRIMARY KEY (`book_id`)
);

CREATE TABLE `Client` (
	`client_id` INT NOT NULL AUTO_INCREMENT,
	`client_name` varchar(255) NOT NULL,
	`client_phone` varchar(255) NOT NULL,
	`client_street` varchar(255) NOT NULL,
	`client_streetno` varchar(255) NOT NULL,
	`client_city` varchar(255) NOT NULL,
	`client_zipcode` varchar(255) NOT NULL,
	`client_afm` INT NOT NULL UNIQUE,
	PRIMARY KEY (`client_id`)
);

CREATE TABLE `Category` (
	`cat_id` INT NOT NULL AUTO_INCREMENT,
	`cat_name` varchar(255) NOT NULL UNIQUE,
	PRIMARY KEY (`cat_id`)
);

CREATE TABLE `Author` (
	`writer_id` INT NOT NULL,
	PRIMARY KEY (`writer_id`)
);

CREATE TABLE `Editor` (
	`editor_id` INT NOT NULL,
	PRIMARY KEY (`editor_id`)
);

CREATE TABLE `Translator` (
	`trans_id` INT NOT NULL,
	PRIMARY KEY (`trans_id`)
);

CREATE TABLE `Illustrator` (
	`ill_id` INT NOT NULL,
	PRIMARY KEY (`ill_id`)
);

CREATE TABLE `ThousandCopy` (
	`thousand_id` INT NOT NULL AUTO_INCREMENT,
	`bk_id` INT NOT NULL,
	`warehouse_id` INT,
	`thousand_no` INT NOT NULL DEFAULT '1',
	PRIMARY KEY (`thousand_id`,`bk_id`)
);

CREATE TABLE `Associate` (
	`assoc_id` INT NOT NULL AUTO_INCREMENT,
	`firstname` varchar(255) NOT NULL,
	`lastname` varchar(255) NOT NULL,
	`phoneno` varchar(255) NOT NULL,
	`email` varchar(255) NOT NULL,
	`afm` INT(255) NOT NULL UNIQUE,
	PRIMARY KEY (`assoc_id`)
);

CREATE TABLE `Copyrights` (
	`bk_id` INT NOT NULL,
	`copyright_holder` varchar(255) NOT NULL,
	`item` varchar(255),
	PRIMARY KEY (`bk_id`)
);

CREATE TABLE `Prints` (
	`printer_id` INT NOT NULL,
	`cpy_id` INT NOT NULL,
	`print_date` DATE NOT NULL,
	PRIMARY KEY (`printer_id`,`cpy_id`)
);

CREATE TABLE `Belongs` (
	`bookid` INT NOT NULL,
	`category_id` INT NOT NULL,
	PRIMARY KEY (`bookid`,`category_id`)
);

CREATE TABLE `Orders` (
	`order_id` INT NOT NULL AUTO_INCREMENT,
	`cl_id` INT NOT NULL,
	`id_book` INT NOT NULL,
	`qty` INT NOT NULL,
	`order_date` varchar(255) NOT NULL,
	PRIMARY KEY (`order_id`,`cl_id`,`id_book`)
);

CREATE TABLE `Writes` (
	`writ_id` INT NOT NULL,
	`wr_bookid` INT NOT NULL,
	PRIMARY KEY (`writ_id`,`wr_bookid`)
);

CREATE TABLE `Translates` (
	`tr_id` INT NOT NULL,
	`tr_bookid` INT NOT NULL,
	`tr_original_lang` varchar(255) NOT NULL,
	`tr_translation_lang` varchar(255) NOT NULL,
	PRIMARY KEY (`tr_id`,`tr_bookid`)
);

CREATE TABLE `Edits` (
	`edit_id` INT NOT NULL,
	`ed_bookid` INT NOT NULL,
	PRIMARY KEY (`edit_id`,`ed_bookid`)
);

CREATE TABLE `Illustrates` (
	`illustr_id` INT NOT NULL,
	`illustr_bookid` INT NOT NULL,
	PRIMARY KEY (`illustr_id`,`illustr_bookid`)
);

ALTER TABLE `Author` ADD CONSTRAINT `Author_fk0` FOREIGN KEY (`writer_id`) REFERENCES `Associate`(`assoc_id`) ON DELETE CASCADE ON UPDATE CASCADE;

ALTER TABLE `Editor` ADD CONSTRAINT `Editor_fk0` FOREIGN KEY (`editor_id`) REFERENCES `Associate`(`assoc_id`) ON DELETE CASCADE ON UPDATE CASCADE;

ALTER TABLE `Translator` ADD CONSTRAINT `Translator_fk0` FOREIGN KEY (`trans_id`) REFERENCES `Associate`(`assoc_id`) ON DELETE CASCADE ON UPDATE CASCADE;

ALTER TABLE `Illustrator` ADD CONSTRAINT `Illustrator_fk0` FOREIGN KEY (`ill_id`) REFERENCES `Associate`(`assoc_id`) ON DELETE CASCADE ON UPDATE CASCADE;

ALTER TABLE `ThousandCopy` ADD CONSTRAINT `ThousandCopy_fk0` FOREIGN KEY (`bk_id`) REFERENCES `Book`(`book_id`) ON DELETE CASCADE ON UPDATE CASCADE;

ALTER TABLE `ThousandCopy` ADD CONSTRAINT `ThousandCopy_fk1` FOREIGN KEY (`warehouse_id`) REFERENCES `Warehouse`(`wh_id`) ON DELETE CASCADE ON UPDATE CASCADE;

ALTER TABLE `Copyrights` ADD CONSTRAINT `Copyrights_fk0` FOREIGN KEY (`bk_id`) REFERENCES `Book`(`book_id`) ON DELETE CASCADE ON UPDATE CASCADE;

ALTER TABLE `Prints` ADD CONSTRAINT `Prints_fk0` FOREIGN KEY (`printer_id`) REFERENCES `Printer`(`print_id`) ON DELETE CASCADE ON UPDATE CASCADE;

ALTER TABLE `Prints` ADD CONSTRAINT `Prints_fk1` FOREIGN KEY (`cpy_id`) REFERENCES `ThousandCopy`(`thousand_id`) ON DELETE CASCADE ON UPDATE CASCADE;

ALTER TABLE `Belongs` ADD CONSTRAINT `Belongs_fk0` FOREIGN KEY (`bookid`) REFERENCES `Book`(`book_id`) ON DELETE CASCADE ON UPDATE CASCADE;

ALTER TABLE `Belongs` ADD CONSTRAINT `Belongs_fk1` FOREIGN KEY (`category_id`) REFERENCES `Category`(`cat_id`) ON DELETE CASCADE ON UPDATE CASCADE;

ALTER TABLE `Orders` ADD CONSTRAINT `Orders_fk0` FOREIGN KEY (`cl_id`) REFERENCES `Client`(`client_id`) ON DELETE CASCADE ON UPDATE CASCADE;

ALTER TABLE `Orders` ADD CONSTRAINT `Orders_fk1` FOREIGN KEY (`id_book`) REFERENCES `Book`(`book_id`) ON DELETE CASCADE ON UPDATE CASCADE;

ALTER TABLE `Writes` ADD CONSTRAINT `Writes_fk0` FOREIGN KEY (`writ_id`) REFERENCES `Author`(`writer_id`) ON DELETE CASCADE ON UPDATE CASCADE;

ALTER TABLE `Writes` ADD CONSTRAINT `Writes_fk1` FOREIGN KEY (`wr_bookid`) REFERENCES `Book`(`book_id`) ON DELETE CASCADE ON UPDATE CASCADE;

ALTER TABLE `Translates` ADD CONSTRAINT `Translates_fk0` FOREIGN KEY (`tr_id`) REFERENCES `Translator`(`trans_id`) ON DELETE CASCADE ON UPDATE CASCADE;

ALTER TABLE `Translates` ADD CONSTRAINT `Translates_fk1` FOREIGN KEY (`tr_bookid`) REFERENCES `Book`(`book_id`) ON DELETE CASCADE ON UPDATE CASCADE;

ALTER TABLE `Edits` ADD CONSTRAINT `Edits_fk0` FOREIGN KEY (`edit_id`) REFERENCES `Editor`(`editor_id`) ON DELETE CASCADE ON UPDATE CASCADE;

ALTER TABLE `Edits` ADD CONSTRAINT `Edits_fk1` FOREIGN KEY (`ed_bookid`) REFERENCES `Book`(`book_id`) ON DELETE CASCADE ON UPDATE CASCADE;

ALTER TABLE `Illustrates` ADD CONSTRAINT `Illustrates_fk0` FOREIGN KEY (`illustr_id`) REFERENCES `Illustrator`(`ill_id`) ON DELETE CASCADE ON UPDATE CASCADE;

ALTER TABLE `Illustrates` ADD CONSTRAINT `Illustrates_fk1` FOREIGN KEY (`illustr_bookid`) REFERENCES `Book`(`book_id`) ON DELETE CASCADE ON UPDATE CASCADE;