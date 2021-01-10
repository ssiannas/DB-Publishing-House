SELECT COUNT(book_id), firstname, lastname FROM 
Book JOIN (Writes JOIN (Author JOIN Associate ON writer_id=assoc_id) ON writer_id=writ_id) ON book_id=wr_bookid 
GROUP BY writer_id
HAVING COUNT(book_id)>1;