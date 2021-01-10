/*count total copies per book:*/
SELECT COUNT(bk_id), title FROM
ThousandCopy JOIN Book ON bk_id=book_id 
GROUP BY bk_id;