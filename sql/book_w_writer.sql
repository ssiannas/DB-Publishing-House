/*book with writer*/
SElECT title,firstname, lastname FROM Book JOIN (Writes JOIN (Author JOIN Associate ON writer_id=assoc_id) ON writer_id=writ_id) ON book_id=wr_bookid;