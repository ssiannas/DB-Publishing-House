from src.controller import Controller, Query
from datetime import date

class Publisher(Controller):
    def __init__(self, controller):
        super(Publisher,self).__init__(controller.getDb())

    def newClient(self, c_name, c_phone, c_street, c_strn, c_cty, c_z, client_afm):

        try:
            self.insertValues('Client',
                              'client_name, client_phone, client_street, client_streetno, client_city, client_zipcode, client_afm',
                              '(%s,%s,%s,%s,%s,%s,%s)',
                              c_name, c_phone, c_street, c_strn, c_cty, c_z, client_afm)
            self.commit()
            print("Successfully added new client")
        except ValueError:
            print("Something went wrong:", ValueError)
        return

    def newPrinter(self, p_phone, p_street, p_strn, p_cty, p_z):
        self.insertValues('Printer',
                          'print_phone, print_street, print_streetno, print_city, print_zipcode',
                          '(%s,%s,%s,%s,%s)',
                          p_phone, p_street, p_strn, p_cty, p_z)
        return

    def newWH(self, wh_phone, wh_street, wh_strn, wh_cty, wh_z, storage):
        self.insertValues('Warehouse',
                          'wh_phone, wh_street, wh_streetno, wh_city, wh_zipcode, max_storage',
                          '(%s,%s,%s,%s,%s,%s)',
                          wh_phone, wh_street, wh_strn, wh_cty, wh_z, storage)

        return

    def newAuthor(self, bookid):
        print("---------Please Add Author Details -------------")
        nfirstname, nlastname, nphone, nmail, nafm = input(
            "Format: Firstname, TLastname, Phone No, Email, AFM\n").split(', ')

        sql = 'SELECT assoc_id FROM Associate WHERE afm=' + str(nafm)
        myresult = self.query2(False, sql)
        myresult.run()
        myresult = myresult.res
        # myresult = self._Controller__cursor.fetchall()
        if len(myresult):
            print("Individual Already in Database")
            sql = 'SELECT assoc_id FROM `Associate`JOIN Author ON assoc_id=writer_id WHERE afm=' + nafm
            myresult2 = self.query2(False, sql)
            myresult2.run()
            myresult2 = myresult2.res
            self.insertValues('Writes', 'writ_id, wr_bookid', "(%s, %s)", myresult2[0][0], bookid)
        else:

            self.insertValues('Associate', 'firstname, lastname, phoneno, email, afm',
                              '(%s,%s,%s,%s,%s)',
                              nfirstname, nlastname, nphone, nmail, nafm)
            nwid = self._Controller__cursor.lastrowid
            sql = "INSERT INTO Author (writer_id) SELECT assoc_id FROM Associate WHERE afm = " + nafm
            myresult3 = self.query2(False, sql)
            myresult3.run()
            self.insertValues('Writes', 'writ_id, wr_bookid', "(%s, %s)", nwid, bookid)

    def fetchISBN(self, bkid):
        sql = "SELECT * FROM Book  WHERE ISBN = " + str(bkid)
        self.query(sql)
        res = self.__cursor.fetchone()
        return res

    def newEditor(self, bookid):
        print("---------Please Add Editor Details -------------")
        nfirstname, nlastname, nphone, nmail, nafm = input(
            "Format: Firstname, TLastname, Phone No, Email, AFM\n").split(', ')
        sql = 'SELECT assoc_id FROM Associate WHERE afm=' + str(nafm)
        myresult = self.query2(False, sql)
        myresult.run()
        myresult = myresult.res
        # myresult = self._Controller__cursor.fetchall()
        if len(myresult):
            print("Individual Already in Database")
            sql = 'SELECT assoc_id FROM `Associate`JOIN Editor ON assoc_id=editor_id WHERE afm=' + nafm
            myresult2 = self.query2(False, sql)
            myresult2.run()
            myresult2 = myresult2.res
            print(myresult2)
            self.insertValues('Edits', 'edit_id, ed_bookid', "(%s, %s)", myresult2[0][0], bookid)
        else:

            self.insertValues('Associate', 'firstname, lastname, phoneno, email, afm',
                              '(%s,%s,%s,%s,%s)',
                              nfirstname, nlastname, nphone, nmail, nafm)
            nwid = self._Controller__cursor.lastrowid
            sql = "INSERT INTO Editor (editor_id) SELECT assoc_id FROM Associate WHERE afm = " + nafm
            myresult3 = self.query2(False, sql)
            myresult3.run()
            self.insertValues('Edits', 'edit_id, ed_bookid', "(%s, %s)", nwid, bookid)

    def newBook(self):
        print("---------Please Add Book Details -------------")
        nISBN, ntitle, neditionno, pubdate, lang = input(
            "Format: ISBN, Title, Edition No, Publication date, Language\n").split(', ')
        self.insertValues('Book',
                          'ISBN,title,editionno,publdate,language',
                          '(%s,%s,%s,%s,%s)',
                          nISBN, ntitle, neditionno, pubdate, lang)

        newbkid = self._Controller__cursor.lastrowid
        return newbkid

    def newIllutr(self, bookid):
        print("---------Please Add Illustrator Details -------------")
        nfirstname, nlastname, nphone, nmail, nafm = input(
            "Format: Firstname, TLastname, Phone No, Email, AFM\n").split(', ')
        sql = 'SELECT assoc_id FROM Associate WHERE afm=' + str(nafm)
        myresult = self.query2(False, sql)
        myresult.run()
        myresult = myresult.res
        # myresult = self._Controller__cursor.fetchall()
        if len(myresult):
            print("Individual Already in Database")
            sql = 'SELECT assoc_id FROM `Associate`JOIN Illustrator ON assoc_id=ill_id WHERE afm=' + nafm
            myresult2 = self.query2(False, sql)
            print(myresult2)
            myresult2.run()
            myresult2 = myresult2.res
            print(myresult2)
            self.insertValues('Illustrates', 'illustr_id, illustr_bookid', "(%s, %s)", myresult2[0][0], bookid)
        else:

            self.insertValues('Associate', 'firstname, lastname, phoneno, email, afm',
                              '(%s,%s,%s,%s,%s)',
                              nfirstname, nlastname, nphone, nmail, nafm)
            nwid = self._Controller__cursor.lastrowid
            sql = "INSERT INTO Illustrator (ill_id) SELECT assoc_id FROM Associate WHERE afm = " + nafm
            myresult3 = self.query2(False, sql)
            myresult3.run()
            self.insertValues('Illustrates', 'illustr_id, illustr_bookid', "(%s, %s)", nwid, bookid)

    def newTrans(self, bookid):
        print("---------Please Add Translator Details -------------")
        nfirstname, nlastname, nphone, nmail, nafm, olang, lang = input(
            "Format: Firstname, Lastname, Phone No, Email, AFM, Original Language, Translated Language\n").split(', ')
        sql = 'SELECT assoc_id FROM Associate WHERE afm=' + str(nafm)
        myresult = self.query2(False, sql)
        myresult.run()
        myresult = myresult.res
        # myresult = self._Controller__cursor.fetchall()
        if len(myresult):
            print("Individual Already in Database")
            sql = 'SELECT assoc_id FROM `Associate`JOIN Translator ON assoc_id=trans_id WHERE afm=' + nafm
            myresult2 = self.query2(False, sql)
            myresult2.run()
            myresult2 = myresult2.res
            self.insertValues('Translates', 'tr_id, tr_bookid, tr_original_lang, tr_translation_lang', "(%s, %s)",
                              myresult2[0][0], bookid, olang, lang)
        else:

            self.insertValues('Associate', 'firstname, lastname, phoneno, email, afm',
                              '(%s,%s,%s,%s,%s)',
                              nfirstname, nlastname, nphone, nmail, nafm)
            nwid = self._Controller__cursor.lastrowid
            sql = "INSERT INTO Translator (trans_id) SELECT assoc_id FROM Associate WHERE afm = " + nafm
            myresult3 = self.query2(False, sql)
            myresult3.run()
            self.insertValues('Translates', 'tr_id, tr_bookid, tr_original_lang, tr_translation_lang', "(%s, %s)", nwid,
                              bookid, olang, lang)

    def add2Cat(self, nbk, catid):
        self.insertValues('Belongs', 'bookid, category_id', "(%s, %s)", nbk, catid)

    def addToCategory(self, nbk, catname):
        print("-----Select a Category------")
        catname = '"' + str(catname) + '"'
        sql = 'SELECT cat_id FROM Category WHERE cat_name=' + str(catname)
        myresult = self.query2(False, sql)
        myresult.run()
        myresult = myresult.res
        self.insertValues('Belongs', 'bookid, category_id', "(%s, %s)", nbk, myresult[0][0])

    def newPublication(self):
        print("--------- Adding New Publication -------------")
        nbk = self.newBook()
        self.newAuthor(nbk)
        self.newEditor(nbk)
        self.newIllutr(nbk)
        flag = input("Is the Book translated? (Y/N)\n")
        if (flag == "Y"): self.newTrans(nbk)
        catname = input("In which Category the book primarily belongs?")
        self.addToCategory(nbk, catname)
        self.commit()
        return

    def newBookRel(self, nISBN, ntitle, neditionno, pubdate, lang, auth_id, ed_id, ill_id, tr_id, o_lang, cat_id):
        self.insertValues('Book',
                          'ISBN,title,editionno,publdate,language',
                          '(%s,%s,%s,%s,%s)',
                          nISBN, ntitle, neditionno, pubdate, lang)
        bk_id = self._Controller__cursor.lastrowid
        for i in auth_id:
            self.insertValues('Writes', 'writ_id, wr_bookid', "(%s, %s)", i, bk_id)
        self.insertValues('Edits', 'edit_id, ed_bookid', "(%s, %s)", ed_id, bk_id)

        self.insertValues('Illustrates', 'illustr_id, illustr_bookid', "(%s, %s)", ill_id, bk_id)
        if (not tr_id == 0):
            self.insertValues('Translates', 'tr_id, tr_bookid, tr_original_lang, tr_translation_lang', "(%s, %s, %s, %s)",
                              tr_id,
                              bk_id, o_lang, lang)
        for i in cat_id:
            self.insertValues('Belongs', 'bookid, category_id', "(%s, %s)", bk_id, i)

    def insertClient(self, c_name, c_phone, c_street, c_strn, c_cty, c_z, client_afm):

        try :
            self.insertValues('Client',
                              'client_name, client_phone, client_street, client_streetno, client_city, client_zipcode, client_afm',
                              '(%s,%s,%s,%s,%s,%s,%s)',
                              c_name, c_phone, c_street, c_strn, c_cty, c_z, client_afm)
            self.commit()
            print("Successfully added new client")
        except ValueError:
            print("Something went wrong:", ValueError)
        return

    def getAuthor(self, bkid):
        sql = 'SELECT DISTINCT firstname, lastname FROM Associate JOIN Author ON assoc_id=writer_id ' \
              'JOIN Writes ON writer_id = writ_id JOIN Book on wr_bookid = ' + str(bkid)
        myresult = self.query2(False,sql)
        myresult.run()
        myresult = myresult.res
        results = []
        for i in myresult:
            results.append(i[0] + ' ' + i[1])
        return results

    def getTranslator(self, bkid):
        sql = 'SELECT DISTINCT firstname, lastname,tr_original_lang, tr_translation_lang FROM Associate JOIN Translator ON assoc_id=trans_id ' \
              'JOIN Translates ON trans_id = tr_id JOIN Book on tr_bookid = ' + str(bkid)
        myresult = self.query2(False,sql)
        myresult.run()
        myresult = myresult.res
        results = []
        for i in myresult:
            results.append(i[0] + ' ' + i[1])
        return results

    def getIllustrator(self, bkid):
        sql = 'SELECT DISTINCT firstname, lastname FROM Associate JOIN Illustrator ON assoc_id=ill_id ' \
              'JOIN Illustrates ON illustr_id = ill_id JOIN Book on illustr_bookid = ' + str(bkid)
        myresult = self.query2(False,sql)
        myresult.run()
        myresult = myresult.res
        results = []
        for i in myresult:
            results.append(i[0] + ' ' + i[1])
        return results

    def getEditor(self, bkid):
        sql = 'SELECT DISTINCT firstname, lastname FROM Associate JOIN Editor ON assoc_id=editor_id ' \
              'JOIN Edits ON edit_id = editor_id JOIN Book on ed_bookid = ' + str(bkid)
        myresult = self.query2(False,sql)
        myresult.run()
        myresult = myresult.res
        results = []
        for i in myresult:
            results.append(i[0] + ' ' + i[1])
        return results

    def checkStock(self, bookid, qty):
        sql = "SELECT COUNT(bk_id) FROM ThousandCopy JOIN Book ON bk_id=book_id GROUP BY bk_id HAVING bk_id = " + str(
            bookid)
        #self.query(sql)
        myresult = self.query2(False, sql)
        myresult.run()
        myresult = myresult.res
        #myresult = self._Controller__cursor.fetchall()
        if len(myresult):
            avail = myresult[0][0]
        else:
            avail = 0
        if (avail < qty):
            print("Insufficient Available Copies, Proceeding to print the required amount")
            return False
        else:
            print("Copies Available , Please proceed with order")
            return True

    def getBookFull(self,bkid):
        sql = 'SELECT ISBN,title,editionno,publdate,language,tr_original_lang, wrfn,wrln,edfn,edln,trfn,trln,ilfn,illn FROM (((Book ' \
            'JOIN (SELECT writer_id, wr_bookid, firstname as wrfn, lastname as wrln FROM Writes ' \
            'JOIN (Author JOIN Associate ON writer_id=assoc_id) ON writer_id=writ_id) AS W ON wr_bookid = book_id) ' \
            'JOIN (SELECT editor_id, ed_bookid, firstname as edfn, lastname as edln FROM Edits ' \
            'JOIN (Editor JOIN Associate ON editor_id=assoc_id) ON editor_id=edit_id) AS E ON ed_bookid = book_id) ' \
            'JOIN (SELECT ill_id, illustr_bookid, firstname as ilfn, lastname as illn FROM Illustrates ' \
            'JOIN (Illustrator JOIN Associate ON ill_id=assoc_id) ON ill_id=illustr_id) AS I ON illustr_bookid=book_id) ' \
            'JOIN (SELECT trans_id, tr_bookid, tr_original_lang, firstname as trfn, lastname as trln FROM Translates ' \
            'JOIN (Translator JOIN Associate ON trans_id=assoc_id) ON trans_id=tr_id) AS T ON tr_bookid=book_id WHERE book_id = ' + str(bkid)
        searchres = self.query2(sql)
        searchres.run()
        searchres.result()
        return searchres.res

    def checkStorageSpace(self, qty):
        sql = "SELECT T1.max - T2.cur as Avail FROM (SELECT SUM(max_storage) AS max FROM Warehouse) AS T1 JOIN (SELECT COUNT(bk_id) AS cur FROM `ThousandCopy` JOIN Book ON bk_id=book_id) AS T2"
        # self.query(sql)
        # myresult = self._Controller__cursor.fetchall()  # a gamisou 1x1 array
        myresult = self.query2(False, sql)
        myresult.run()
        myresult = myresult.res
        avail = myresult[0][0]
        if (avail < qty):
            print("Insufficient Storage Space")
            return False
        else:
            print("Sufficient Storage Space, Please proceed with printing order")
            return True

    def getAssocName(self, associd):
        try:
            assoc = self.fetch('Associate',associd)
            fn = assoc[1]
            ln = assoc[2]
            fullname = fn + ' ' + ln
            return fullname
        except:
            pass

    def getCategory(self,bkid):
        sql = "SELECT cat_name FROM (Category JOIN Belongs ON cat_id=category_id) JOIN Book ON book_id=bookid WHERE book_id= " + str(bkid)
        searchres = self.query2(False, sql)
        searchres.run()
        searchres.result()
        cats = []
        for i in searchres.res:
            cats.append(i[0])
        return cats

    def findmaxcopy(self, bkid):
        sql = "SELECT MAX(thousand_no) FROM ThousandCopy WHERE bk_id=" + str(bkid)
        # self._Controller__cursor.execute(sql)
        # res = self._Controller__cursor.fetchall()
        myresult = self.query2(False, sql)
        myresult.run()
        res = myresult.res
        return res[0][0]
    
    def printCopies(self, bkid, no_copies, printerid, whid):
        maxcopy = self.findmaxcopy(bkid)
        if (maxcopy == None): maxcopy = 0
        for i in range(no_copies):
            maxcopy += 1
            self.insertValues('ThousandCopy',
                         'bk_id, warehouse_id, thousand_no',
                         '(%s,%s, %s)',
                         bkid, whid, maxcopy)
            lastid = self._Controller__cursor.lastrowid
            self.insertValues('Prints',
                         'printer_id, cpy_id, print_date',
                         '(%s,%s,%s)',
                         printerid, lastid, date.today().strftime("%Y-%m-%d"))
        self._Controller__cnx.commit()

    def orderBook(self, clid,bkid,qty):
        #execute order 66
        self.insertValues('Orders',
                     'cl_id, id_book, qty,order_date',
                     '(%s,%s, %s, %s)',
                     clid, bkid, qty, date.today().strftime("%Y-%m-%d"))

        self._Controller__cnx.commit()

    def searchInCat(self, keyword, catid):
        if keyword:
            print("--------- RESULTS FOR: ", keyword, " -------------")
            keyword = '"%' + keyword + '%"'
            sql = ("SElECT book_id, ISBN, title, editionno, publdate, language " +
                   'FROM (Book JOIN (Writes JOIN (Author JOIN Associate ON writer_id=assoc_id) ON writer_id=writ_id) '
                   'ON book_id=wr_bookid) JOIN (Category JOIN Belongs ON cat_id=category_id) ON book_id=bookid '
                   'WHERE (CONCAT(firstname," ", lastname) '
                   'LIKE ' + keyword + 'OR CONCAT(lastname," ", firstname) '
                    'LIKE ' + keyword + " OR title LIKE " + keyword + " OR ISBN LIKE " + keyword +" )AND cat_id=" + str(catid))

            searchres = self.query2(False, sql)
            searchres.run()
            return searchres.res
        else:
            sql = ('SElECT book_id, ISBN, title, editionno, publdate, language FROM Book ' +
                    'JOIN (Category JOIN Belongs ON cat_id=category_id) ON book_id=bookid '\
                    ' AND cat_id=' + str(catid))
            searchres = self.query2(False, sql)
            searchres.run()
            searchres.result()
            return searchres.res

    def checkStorageSpaceWH(self, qty, wh_id):
        sql = "SELECT T1.max - T2.cur as Avail FROM (SELECT SUM(max_storage) AS max FROM Warehouse WHERE wh_id=" + str(
            wh_id) + " ) AS T1 JOIN (SELECT COUNT(bk_id) AS cur FROM `ThousandCopy` JOIN Book ON bk_id=book_id WHERE warehouse_id =" + str(
            wh_id) + ") AS T2"
        # self.query(sql)
        # myresult = self._Controller__cursor.fetchall()  # a gamisou 1x1 array
        myresult = self.query2(False, sql)
        myresult.run()
        myresult = myresult.res
        avail = myresult[0][0]
        if (avail < qty):
            print("Insufficient Storage Space for selected Warehouse")
            return False
        else:
            print("Sufficient Storage Space for selected Warehouse")
            return True

    def checkStorageSpaceWH(self, qty, wh_id):
        sql = "SELECT T1.max - T2.cur as Avail FROM (SELECT SUM(max_storage) AS max FROM Warehouse WHERE wh_id=" + str(
            wh_id) + " ) AS T1 JOIN (SELECT COUNT(bk_id) AS cur FROM `ThousandCopy` JOIN Book ON bk_id=book_id WHERE warehouse_id =" + str(
            wh_id) + ") AS T2"
        # self.query(sql)
        # myresult = self._Controller__cursor.fetchall()  # a gamisou 1x1 array
        myresult = self.query2(False, sql)
        myresult.run()
        myresult = myresult.res
        avail = myresult[0][0]
        if (avail < qty):
            print("Insufficient Storage Space for selected Warehouse")
            return False
        else:
            print("Sufficient Storage Space for selected Warehouse")
            return True

    def search(self, keyword):
        if keyword:
            print("--------- RESULTS FOR: ", keyword, " -------------")
            keyword = '"%' + keyword + '%"'
            sql = ("SElECT DISTINCT book_id, ISBN, title, editionno, publdate, language " +
                   'FROM Book JOIN (Writes JOIN (Author JOIN Associate ON writer_id=assoc_id) ON writer_id=writ_id) '
                   'ON book_id=wr_bookid WHERE CONCAT(firstname," ", lastname) '
                   'LIKE ' + keyword + 'OR CONCAT(lastname," ", firstname) '
                   'LIKE ' + keyword + " OR title LIKE " + keyword + " OR ISBN LIKE " + keyword)
            #self.queryPrint(sql)
            searchres = self.query2(False, sql)
            searchres.run()
            return  searchres.res
        else:
            return self.fetchall('Book')
