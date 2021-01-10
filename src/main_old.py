from fromfile import getfromfile
from random import choice
from datetime import date
import database




def orderBook(clid,bkid,qty):
    #execute order 66
    insertValues('Orders',
                 'cl_id, id_book, qty,order_date',
                 '(%s,%s, %s, %s)',
                 clid, bkid, qty, date.today().strftime("%Y-%m-%d"))

    mydb.commit()

def processOrder():
    #to do check stock -> if not enough : print more -> delete from warehouses
    return

def checkStock():
    #to do
    return

def checkStorageSpace(whid):
    #returns available storage space
    return

def loadBelongs():
    cats = []
    groupA = [1, 2, 4, 6, 8, 9]
    groupB = [3, 5, 7, 10]
    book_id = fetchattr('book_id', 'Book')
    book_count = len(book_id)
    cats = fetchattr('cat_id', 'Category')
    cat_count = len(cats)
    for i in range(book_count):
        bkid = book_id[i]
        catid = choice(cats)
        insertValues("Belongs",
                     'bookid, category_id',
                     "(%s, %s)",
                     bkid, catid)
        if (i % 3 == 0):
            if (catid in groupA):
                while (True):
                    catid2 = choice(groupA)
                    if (catid != catid2):
                        insertValues("Belongs",
                                     'bookid, category_id',
                                     "(%s, %s)",
                                     bkid, catid2)
                        break
            else:
                while (True):
                    catid2 = choice(groupB)
                    if (catid != catid2):
                        insertValues("Belongs",
                                     'bookid, category_id',
                                     "(%s, %s)",
                                     bkid, catid2)
                        break

    mydb.commit()


def loadAssocRel(type):
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
    assoc_id = fetchattr(typeid, type)
    assoc_count = len(assoc_id)
    book_id = fetchattr('book_id', 'Book')
    book_count = len(book_id)
    book_langs = fetchattr('language','Book')
    cnt = 0
    for i in range(book_count):
        bkid = book_id[i]
        associd = assoc_id[cnt]
        if (type != "Translator"):
            insertValues(table,type_id + ", " + type_book,"(%s, %s)",associd, bkid)
        else:
            bklang = book_langs[i][0]
            language = choice(languages)
            insertValues(table, type_id + ", " + type_book + ",tr_original_lang, tr_translation_lang",
                         "(%s, %s, %s, %s)",
                          associd,bkid,language, bklang)
        cnt += 1
        if cnt == assoc_count:
            cnt = 0
    mydb.commit()


def printCopies(bkid,no_copies,printerid,whid):
    maxcopy = findmaxcopy(bkid)
    if (maxcopy == None): maxcopy = 0
    for i in range(no_copies):
        maxcopy += 1
        insertValues('ThousandCopy',
                     'bk_id, warehouse_id, thousand_no',
                     '(%s,%s, %s)',
                     bkid, whid, maxcopy)
        lastid = mycursor.lastrowid
        insertValues('Prints',
                     'printer_id, cpy_id, print_date',
                     '(%s,%s,%s)',
                     printerid, lastid, date.today().strftime("%Y-%m-%d"))
    mydb.commit()

def countRows(table):
    mycursor.execute("SELECT COUNT(*) FROM " + table)
    res = mycursor.fetchall()

    return res[0][0]


def loadBooks():
    data = getfromfile("books.txt")
    for item in data:
        insertValues('Book',
                     'ISBN,title,editionno,publdate,language',
                     '(%s,%s,%s,%s,%s)',
                     *item)
    mydb.commit()

def loadDatabase():
    print("Loading database...")
    print("Loading Associates...")
    loadAssoc()
    print("Loading Books...")
    loadBooks()
    print("Loading Categories...")
    loadCategories()
    print("Loading Clients...")
    loadClient()
    print("Loading Printhouses...")
    loadPrinter()
    print("Loading Warehouses...")
    loadWarehouse()
    print("Loading Relationships...")
    loadAssocRel('Author')
    loadAssocRel('Illustrator')
    loadAssocRel('Editor')
    loadAssocRel('Translator')
    loadBelongs()
    print("========Loading Database Complete =========")
    print("Execute Command: ")

def loadAssoc():
    data = getfromfile("dudes.txt")
    count =0
    for item in data:
        if (count<25):
            insertAssoc("Author", *item)
        elif (count<30 and count>=25):
            insertAssoc("Editor", *item)
        elif (count>=30 and count <35):
            insertAssoc("Illustrator", *item)
        elif (count >=35 and count <40):
            insertAssoc("Translator", *item)
        count +=1
    mydb.commit()

def loadClient():
    data = getfromfile("companies.txt")
    for item in data:
        insertValues('Client', 'client_name, client_phone, client_street, client_streetno, client_city, client_zipcode, client_afm',
                     '(%s,%s,%s,%s,%s,%s,%s)',
                     *item)
    mydb.commit()

def loadPrinter():
    data = getfromfile("printhouse.txt")
    for item in data:
        insertValues('Printer', 'print_id, print_phone, print_street, print_streetno, print_city, print_zipcode',
                     '(%s,%s,%s,%s,%s,%s)',
                     *item)
    mydb.commit()

def loadWarehouse():
    data = getfromfile("storage.txt")
    for item in data:
        insertValues('Warehouse', 'wh_id, wh_phone, wh_street, wh_streetno, wh_city, wh_zipcode',
                     '(%s,%s,%s,%s,%s,%s)',
                     *item)
    mydb.commit()

def loadCategories():
    data = getfromfile("categories.txt")
    for item in data:
        insertValues('Category', 'cat_name',
                     '(%s)',
                     *item)
    mydb.commit()

def clearTable(*args):
    for table in args:
        sql = "SELECT * FROM " + table
        mycursor.execute(sql)
        myresult = mycursor.fetchall()
        for x in myresult:
            tableid = x[0]
            deleteData(table,tableid)
    mydb.commit()

def findmaxcopy(bkid):
    sql = "SELECT MAX(thousand_no) FROM ThousandCopy WHERE bk_id=" + str(bkid)
    mycursor.execute(sql)
    res = mycursor.fetchall()
    return res[0][0]

def deleteData(table, myid):
    sql = "SELECT * FROM " + table
    mydictcursor.execute(sql)
    myresult = mydictcursor.fetchone()
    tableid = list(myresult.keys())
    sql = "DELETE FROM " + table + " WHERE " + table + "." + tableid[0] + ' = ' + str(myid)
    mycursor.execute(sql)
    mydb.commit()

def fetchall(*args):
    for table in args:
        sql = "SELECT * FROM " + table
        mycursor.execute(sql)
        myresult = mycursor.fetchall()
        print("--------- TABLE: ", table, " -------------")
        for x in myresult:
            print(x)

def fetchattr(attr, table):
    sql = "SELECT "+ attr +" FROM " + table
    mycursor.execute(sql)
    myresult = mycursor.fetchall()
    res = []
    for i in range(len(myresult)):
        res.append(myresult[i][0])
    return res

def insertValues (table, params,format_string, *values):
    sql = "INSERT INTO " + table + '(' + params + ')' + " VALUES " +format_string
    vals = values
    mycursor.execute(sql,vals)


def insertAssoc(type, firstname,lastname,phoneno,email,afm):
    type_id = ""
    if type == "Author":
        type_id = "(writer_id)"
    elif type == "Illustrator":
        type_id = "(ill_id)"
    elif type == "Translator":
        type_id = "(trans_id)"
    elif type == "Editor":
        type_id = "(editor_id)"
    else:
        print("Error: Type of associate invalid")
        return
    insertValues('Associate', 'firstname, lastname, phoneno, email, afm',
                 '(%s,%s,%s,%s,%s)',
                 firstname, lastname, phoneno, email, afm)
    sql = "INSERT INTO " + type + type_id + " SELECT assoc_id FROM Associate WHERE afm = " + afm
    mycursor.execute(sql)
    mydb.commit()



if __name__ == "__main__":
    db = database.Database()
    db.createConnection()
    db.createcursor()
    mydb = db.getconnection()
    mycursor, mydictcursor = db.getCursors()

    while mydb.is_connected():
        command = str(input('Execute command:\n'))
        exec(command)

