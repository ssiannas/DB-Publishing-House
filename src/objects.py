class Book():
    def __init__(self, bookid, ISBN, title, editionno, publdate, language ):
        self.bookid = bookid
        self.ISBN = ISBN
        self.title = title
        self.editionno = editionno
        self.publdate = publdate
        self.language = language
        self.keys = ['bookid','ISBN','title','editionno','publdate','language']
        self.attributes = [self.bookid,self.ISBN,self.title,self.editionno,self.publdate,self.language]
        self.json = {}
        for i in range(len(self.keys)):
            self.json[self.keys[i]] = self.attributes[i]

    def setAuthor(self, authname):
        self.__author = authname[0]
        if len(authname) > 1:
            for i in authname[1:]:
                self.__author += ', ' + i

    def setTrans(self, trname):
        if trname:
            self.__translator = trname[0]
        else:
            self.__translator = 'None'
        if len(trname) > 1:
            for i in trname[1:]:
                self.__translator += ', ' + i

    def setEditor(self, edname):
        print(edname)
        self.__editor = edname[0]
        if len(edname) > 1:
            for i in edname[1:]:
                self.__editor += ', ' + i

    def setIll(self, illname):
        self.__illustrator = illname[0]
        if len(illname) > 1:
            for i in illname[1:]:
                self.__illustrator += ', ' + i

    def setCategory(self, category):
        self.__category = category[0]
        if len(category) > 1:
            for i in category[1:]:
                self.__category += ', ' + i

    def setUI(self):
        self.uiattr = [self.ISBN, self.title, self.editionno, self.publdate, self.language, self.__author]

    def setUIfull(self):
        self.uiattrFull = [self.ISBN, self.title, self.editionno, self.publdate, self.language, self.__category, self.__author, self.__editor, self.__translator, self.__illustrator]

    def __str__(self):
        mystr = "ISBN: {}\nTitle: {} \nEdition: #{}\nPublication Date: {}\nLanguage: {}".format(*self.attributes[1:])
        return mystr

class Client():
    def __init__(self,client_id, client_name, client_phone, client_street, client_streetno, client_city, client_zipcode, client_afm):
        self.client_id = client_id
        self.client_name = client_name
        self.client_phone = client_phone
        self.client_street = client_street
        self.client_streetno = client_streetno
        self.client_city = client_city
        self.client_zipcode = client_zipcode
        self.client_afm = client_afm
        self.attributes = [self.client_id,self.client_name,
                           self.client_phone,self.client_street,
                           self.client_streetno,self.client_city,
                           self.client_zipcode, self.client_afm]

    def __str__(self):
        mystr = "Client Name: {}\nPhone: {}\nClient Address: {}, {}, {}, {}\nAFM = {}".format(*self.attributes[1:])
        return mystr

class Warehouse():
    def __init__(self, wh_id, wh_phone, wh_street, wh_streetno, wh_city, wh_zipcode, max_storage):
        self.wh_id       = wh_id
        self.wh_phone     = wh_phone
        self.wh_street      = wh_street
        self.wh_streetno  = wh_streetno
        self.wh_city      = wh_city
        self.wh_zipcode  = wh_zipcode
        self.max_storage = max_storage
        self.attributes  = [self.wh_id, self.wh_phone,
                            self.wh_street, self.wh_streetno,
                            self.wh_city, self.wh_zipcode, self.max_storage]
    def __str__(self):
        mystr = "Warehouse phone: {}\nAddress: {}, {}, {}, {}\nMax Storage: {}".format(*self.attributes[1:])
        return mystr

class Printer():
    def __init__(self, print_id, print_phone, print_street, print_streetno, print_city, print_zipcode):
        self.print_id = print_id
        self.print_phone = print_phone
        self.print_street = print_street
        self.print_streetno = print_streetno
        self.print_city = print_city
        self.print_zipcode = print_zipcode
        self.attributes = [self.print_id, self.print_phone,
                           self.print_street,self.print_streetno,
                           self.print_city, self.print_zipcode]

    def __str__(self):
        mystr = "Printhouse phone: {}\nAddress: {}, {}, {}, {}".format(*self.attributes[1:])
        return mystr

class Associate():
    def __init__(self, assoc_id, firstname, lastname, phoneno, email, afm):
        self.assoc_id = assoc_id
        self.firstname = firstname
        self.lastname = lastname
        self.phoneno = phoneno
        self.email = email
        self.afm = afm
        self.attributes = [self.assoc_id, self.firstname,
                           self.lastname, self.phoneno,
                           self.email, self.afm]

    def __str__(self):
        mystr = "Associate Name: {} {}\nPhone: {}\nEmail:  {}\nAFM: {}".format(*self.attributes[1:])
        return mystr
