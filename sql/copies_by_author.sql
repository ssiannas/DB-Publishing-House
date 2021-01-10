/* copies by author */
SELECT COUNT(bk_id), title,firstname, lastname FROM
`ThousandCopy` JOIN (Book JOIN (Writes JOIN (Author JOIN Associate ON writer_id=assoc_id) ON writer_id=writ_id) ON book_id=wr_bookid)ON bk_id=book_id 
GROUP BY bk_id, firstname, lastname;