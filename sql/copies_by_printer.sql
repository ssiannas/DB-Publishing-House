/*count of copies in by printer:*/
SELECT COUNT(bk_id), title 
FROM (ThousandCopy JOIN Prints ON cpy_id = thousand_id) JOIN Book ON bk_id=book_id 
GROUP BY bk_id, printer_id;