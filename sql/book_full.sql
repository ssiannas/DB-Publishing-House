/*Book full*/
SELECT book_id,ISBN,title,editionno,publdate,language,tr_original_lang, wrfn,wrln,edfn,edln,trfn,trln,ilfn,illn FROM (((Book
JOIN (SELECT writer_id, wr_bookid, firstname as wrfn, lastname as wrln FROM Writes JOIN (Author JOIN Associate ON writer_id=assoc_id) ON writer_id=writ_id) AS W ON wr_bookid = book_id)
JOIN (SELECT editor_id, ed_bookid, firstname as edfn, lastname as edln FROM Edits JOIN (Editor JOIN Associate ON editor_id=assoc_id) ON editor_id=edit_id) AS E ON ed_bookid = book_id)
JOIN (SELECT ill_id, illustr_bookid, firstname as ilfn, lastname as illn FROM Illustrates JOIN (Illustrator JOIN Associate ON ill_id=assoc_id) ON ill_id=illustr_id) AS I ON illustr_bookid=book_id)
JOIN (SELECT trans_id, tr_bookid, tr_original_lang, firstname as trfn, lastname as trln FROM Translates JOIN (Translator JOIN Associate ON trans_id=assoc_id) ON trans_id=tr_id) AS T ON tr_bookid=book_id;