from flask import request
import src.objects as obj
from app import pub

def fetchforUI(booklist):
    myBooks = []
    mykeys = ['ISBN', 'Title', 'Edition #', 'Publication Date', 'Language', 'Author Name']
    myids = []
    for book in booklist:
        mybook = obj.Book(*book)
        mybook.setAuthor(pub.getAuthor(mybook.bookid))
        mybook.setUI()
        myBooks.append(mybook)
        myids.append(mybook.bookid)
    return myBooks,mykeys,myids


def getCategories():
    mycats = pub.fetchall('Category')
    return mycats

def searchbooks(keyword, catid):
    if catid != 0:
        booklist = pub.searchInCat(keyword,catid)
    else:
        booklist = pub.search(keyword)
    return fetchforUI(booklist)

def searchFull(bkid):
    book = pub.fetch('Book', bkid)
    mybook = obj.Book(*book)
    mybook.setAuthor(pub.getAuthor(mybook.bookid))
    mybook.setTrans(pub.getTranslator(mybook.bookid))
    mybook.setEditor(pub.getEditor(mybook.bookid))
    mybook.setIll(pub.getIllustrator(mybook.bookid))
    mybook.setCategory(pub.getCategory(mybook.bookid))
    mykeys = ['ISBN', 'Title', 'Edition #', 'Publication Date', 'Language','Category', 'Author Name','Editor Name','Translator Name','Illustrator Name']
    mybook.setUIfull()
    mybook = mybook.uiattrFull
    return mybook,mykeys

def getAuths():
    auths = pub.fetchall('Author')
    myauths =[]
    authids = []
    for i in auths:
        authids.append(i[0])
        myauths.append(pub.getAssocName(i[0]))
    return zip(myauths,authids)

def getEds():
    eds = pub.fetchall('Editor')
    myeds = []
    edids = []
    for i in eds:
        edids.append(i[0])
        myeds.append(pub.getAssocName(i[0]))
    return zip(myeds,edids)

def getIlls():
    ills = pub.fetchall('Illustrator')
    myills =[]
    illids = []
    for i in ills:
        illids.append(i[0])
        myills.append(pub.getAssocName(i[0]))
    return zip(myills,illids)

def getTrans():
    trans = pub.fetchall('Translator')
    mytrans =[]
    transids = []
    for i in trans:
        transids.append(i[0])
        mytrans.append(pub.getAssocName(i[0]))
    return zip(mytrans,transids)

def addBook():
    try:
        isbn = request.form['isbn']
        title = request.form['title']
        editionno = request.form['editionno']
        publdate = request.form['publdate']
        language = request.form['language']
        auth = request.form.getlist('author')
        ed = request.form['editor']
        trans = request.form['translator']
        ill = request.form['illustrator']
        olang = request.form['or_lang']
        category = request.form.getlist('category')
        if not category:
            category = [1]
        pub.newBookRel(isbn,title,editionno,publdate,language,auth,ed,ill,trans,olang,category)
        pub.commit()
    except Exception as e:
        print(e)

def addWh():
    try:
        phone = request.form['phone']
        street = request.form['street']
        streetno = request.form['streetno']
        city = request.form['city']
        zipcode = request.form['zipcode']
        max_storage = request.form['max_storage']
        pub.newWH(phone,street,streetno,city,zipcode,max_storage)
        pub.commit()
    except Exception as e:
        print(e)

def addClient():
    try:
        name = request.form['name']
        phone = request.form['phone']
        street = request.form['street']
        streetno = request.form['streetno']
        city = request.form['city']
        zipcode = request.form['zipcode']
        afm = request.form['afm']
        pub.newClient(name,phone,street,streetno,city,zipcode,afm)
        pub.commit()
    except Exception as e:
        print(e)

def addPrint():
    try:
        phone = request.form['phone']
        street = request.form['street']
        streetno = request.form['streetno']
        city = request.form['city']
        zipcode = request.form['zipcode']
        pub.newPrinter(phone,street,streetno,city,zipcode)
        pub.commit()
    except Exception as e:
        print(e)


def addAssoc():
    try:
        fn = request.form['fn']
        ln = request.form['ln']
        phone = request.form['phone']
        mail = request.form['mail']
        afm = request.form['afm']
        type = request.form['type']
        print(type)
        pub.insertAssoc(type,fn,ln,phone,mail,afm)
        pub.commit()
    except Exception as e:
        print(e)
