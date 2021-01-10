/*count total copies of all books:*/
SELECT COUNT(bk_id) FROM `ThousandCopy` JOIN Book ON bk_id=book_id;