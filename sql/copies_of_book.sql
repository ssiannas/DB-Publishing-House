/*count total copies for single book:*/
SELECT COUNT(bk_id), title FROM
ThousandCopy JOIN Book ON bk_id=book_id
WHERE bk_id = 1
GROUP BY bk_id;