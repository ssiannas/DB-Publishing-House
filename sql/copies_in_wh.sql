/*count all different copies in a single warehouse:*/
SELECT COUNT(bk_id), title, warehouse_id 
FROM `ThousandCopy` JOIN Book ON bk_id=book_id 
GROUP BY bk_id, warehouse_id;