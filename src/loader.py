from random import choice
from src.config import languages,groupA,groupB
from src.fromfile import getfromfile

class Loader():
    def __init__(self, db, ctrl):
        self.__database = db.getconnection()
        self.__controller = ctrl

    def createDB(self):
        print("=====CREATING DATABASE=======")
        self.__controller.runscript("create_db")
        print("=====DATABASE CREATED======")

    def dropDB(self):
        print("=====DROPPING DATABASE=======")
        self.__controller.runscript("drop_db")
        print("=====DATABASE DROPPED======")

    def resetDB(self):
        print("=====RESETING DATABASE=======")
        self.__controller.runscript("drop_db")
        self.__controller.runscript("create_db")
        print("=====DATABASE RESET COMPLETE======")

    def loadBelongs(self):
        cats = []
        book_id = self.__controller.fetchattr('book_id', 'Book')
        book_count = len(book_id)
        cats = self.__controller.fetchattr('cat_id', 'Category')
        cat_count = len(cats)
        for i in range(book_count):
            bkid = book_id[i]
            catid = choice(cats)
            self.__controller.insertValues("Belongs",
                         'bookid, category_id',
                         "(%s, %s)",
                         bkid, catid)
            if (i % 3 == 0):
                if (catid in groupA):
                    while (True):
                        catid2 = choice(groupA)
                        if (catid != catid2):
                            self.__controller.insertValues("Belongs",
                                         'bookid, category_id',
                                         "(%s, %s)",
                                         bkid, catid2)
                            break
                else:
                    while (True):
                        catid2 = choice(groupB)
                        if (catid != catid2):
                            self.__controller.insertValues("Belongs",
                                         'bookid, category_id',
                                         "(%s, %s)",
                                         bkid, catid2)
                            break

        self.__database.commit()

    def loadAssocRel(self,type):
        if type == "Author":
            table = "Writes"
            typeid = "writer_id"
            type_id = "writ_id"
            type_book = "wr_bookid"
        elif type == "Editor":
            table = "Edits"
            typeid = "editor_id"
            type_id = "edit_id"
            type_book = "ed_bookid"
        elif type == "Illustrator":
            table = "Illustrates"
            typeid = "ill_id"
            type_id = "illustr_id"
            type_book = "illustr_bookid"
        elif type == "Translator":
            table = "Translates"
            typeid = "trans_id"
            type_id = "tr_id"
            type_book = "tr_bookid"
        else:
            print("Wrong Associate Type")
            return
        assoc_id = self.__controller.fetchattr(typeid, type)
        assoc_count = len(assoc_id)
        book_id = self.__controller.fetchattr('book_id', 'Book')
        book_count = len(book_id)
        book_langs = self.__controller.fetchattr('language', 'Book')
        cnt = 0
        for i in range(book_count):
            bkid = book_id[i]
            associd = assoc_id[cnt]
            if (type != "Translator"):
                self.__controller.insertValues(table, type_id + ", " + type_book, "(%s, %s)", associd, bkid)
            else:
                bklang = book_langs[i][0]
                language = choice(languages)
                self.__controller.insertValues(table, type_id + ", " + type_book + ",tr_original_lang, tr_translation_lang",
                             "(%s, %s, %s, %s)",
                             associd, bkid, language, bklang)
            cnt += 1
            if cnt == assoc_count:
                cnt = 0
        self.__database.commit()

    def loadBooks(self):
        data = getfromfile("books.txt")
        for item in data:
            self.__controller.insertValues('Book',
                         'ISBN,title,editionno,publdate,language',
                         '(%s,%s,%s,%s,%s)',
                         *item)
        self.__database.commit()

    def loadDatabase(self):
        print("Loading database...")
        print("Loading Associates...")
        self.loadAssoc()
        print("Loading Books...")
        self.loadBooks()
        print("Loading Categories...")
        self.loadCategories()
        print("Loading Clients...")
        self.loadClient()
        print("Loading Printhouses...")
        self.loadPrinter()
        print("Loading Warehouses...")
        self.loadWarehouse()
        print("Loading Relationships...")
        self.loadAssocRel('Author')
        self.loadAssocRel('Illustrator')
        self.loadAssocRel('Editor')
        self.loadAssocRel('Translator')
        self.loadBelongs()
        print("========Loading Database Complete =========")

    def loadAssoc(self):
        data = getfromfile("dudes.txt")
        count = 0
        for item in data:
            if (count < 25):
                self.__controller.insertAssoc("Author", *item)
            elif (count < 30 and count >= 25):
                self.__controller.insertAssoc("Editor", *item)
            elif (count >= 30 and count < 35):
                self.__controller.insertAssoc("Illustrator", *item)
            elif (count >= 35 and count < 40):
                self.__controller.insertAssoc("Translator", *item)
            count += 1
        self.__database.commit()

    def loadClient(self):
        data = getfromfile("companies.txt")
        for item in data:
            self.__controller.insertValues('Client',
                         'client_name, client_phone, client_street, client_streetno, client_city, client_zipcode, client_afm',
                         '(%s,%s,%s,%s,%s,%s,%s)',
                         *item)
        self.__database.commit()

    def loadPrinter(self):
        data = getfromfile("printhouse.txt")
        for item in data:
            self.__controller.insertValues('Printer', 'print_id, print_phone, print_street, print_streetno, print_city, print_zipcode',
                         '(%s,%s,%s,%s,%s,%s)',
                         *item)
        self.__database.commit()

    def loadWarehouse(self):
        data = getfromfile("storage.txt")
        for item in data:
            self.__controller.insertValues('Warehouse', 'wh_id, wh_phone, wh_street, wh_streetno, wh_city, wh_zipcode',
                         '(%s,%s,%s,%s,%s,%s)',
                         *item)
        self.__database.commit()

    def loadCategories(self):
        data = getfromfile("categories.txt")
        for item in data:
            self.__controller.insertValues('Category', 'cat_name',
                         '(%s)',
                         *item)
        self.__database.commit()