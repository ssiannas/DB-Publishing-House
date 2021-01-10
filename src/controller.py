from mysql.connector import  Error as sqlError
from src.fromfile import getscript
import src.objects as obj

class Controller():
    def __init__(self, db):
        self.__cnx = db.getconnection()
        self.__cursor, self.__dictcursor = db.getCursors()
        self.__database = db

    def countRows(self, table):
        self.query("SELECT COUNT(*) FROM " + table)
        res = self.__cursor.fetchall()
        return res[0][0]

    def copiesOfBook(self, bkid):
        sql = 'SELECT COUNT(bk_id), title FROM ThousandCopy JOIN Book ON bk_id=book_id WHERE bk_id = ' + str(bkid) + ' GROUP BY bk_id;'
        self.query()

    def commit(self):
        self.__cnx.commit()


    def clearTable(self, *args):
        for table in args:
            sql = "SELECT * FROM " + table
            self.__cursor.execute(sql)
            myresult = self.__cursor.fetchall()
            for x in myresult:
                tableid = x[0]
                self.deleteData(table, tableid)
        self.__cnx.commit()

    def getTableIdName(self,table):
        sql = "SELECT * FROM " + table
        self.__dictcursor.execute(sql)
        myresult = self.__dictcursor.fetchone()
        tableid = list(myresult.keys())
        return tableid[0]

    def deleteData(self, table, myid):
        tableid = self.getTableIdName(table)
        sql = "DELETE FROM " + table + " WHERE " + table + "." + tableid + ' = ' + str(myid)
        self.query(sql)
        self.__cnx.commit()

    def update(self, table, column, value, row_id):
        tableid = self.getTableIdName(table)
        if (type(value) == type("")):
            value = "'" + value + "'"
        sql = "UPDATE " + table + " SET " + column + '=' + str(value) + " WHERE " + str(tableid) + '=' + str(row_id)
        self.query(sql)
        self.__cnx.commit()

    def fetch(self, table, id):
        tableid = self.getTableIdName(table)
        sql = "SELECT * FROM " + table + " WHERE " +  tableid +'=' + str(id)
        self.query(sql)
        res = self.__cursor.fetchone()
        return res

    def printTable(self, table):
        data = self.fetchall(table)
        print("===============Printing Table: Book ================")
        for i in data:
            print(i)

    def fetchall(self, table):
        sql = "SELECT * FROM " + table
        qr = self.query2(False, sql)
        qr.run()
        return qr.res

    def fetchattr(self, attr, table):
        sql = "SELECT " + attr + " FROM " + table
        self.__cursor.execute(sql)
        myresult = self.__cursor.fetchall()
        res = []
        for i in range(len(myresult)):
            res.append(myresult[i][0])
        return res

    def insertValues(self, table, params, format_string, *values):
        sql = "INSERT INTO " + table + '(' + params + ')' + " VALUES " + format_string
        vals = values
        self.__cursor.execute(sql, vals)

    def insertAssoc(self, type, firstname, lastname, phoneno, email, afm):
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
        self.insertValues('Associate', 'firstname, lastname, phoneno, email, afm',
                     '(%s,%s,%s,%s,%s)',
                     firstname, lastname, phoneno, email, afm)
        sql = "INSERT INTO " + type + type_id + " SELECT assoc_id FROM Associate WHERE afm = " + afm
        self.query(sql)
        self.__cnx.commit()

    def dictquery(self, *args):
        if len(args): sql = args[0]
        else: sql = input()
        try:
            self.__dictcursor.execute(sql)
        except sqlError as err:
            print("Something went wrong: {}".format(err))

    def dictqueryPrint(self, *args):
        try:
            self.query(*args)
            res = self.__dictcursor.fetchall()
            for i in res:
                print(i)
        except sqlError as err:
            print("Something went wrong: {}".format(err))

    def query2(self,dict, *args):
        if len(args): sql = args[0]
        else: sql = input()
        qr = Query(dict, self.__database, sql)
        return qr

    def query(self, *args):
        if len(args): sql = args[0]
        else: sql = input()
        try:
            self.__cursor.execute(sql)
        except sqlError as err:
            print("Something went wrong: {}".format(err))

    def queryPrint(self, *args):
        try:
            self.query(*args)
            res = self.__cursor.fetchall()
            for i in res:
                print(i)
        except sqlError as err:
            print("Something went wrong: {}".format(err))

    def runscript2(self, filename):
        commands = getscript(filename)
        print("Executing " + filename + ".sql...")
        for c in commands:
            self.query2(c)
        print("Finished running script.")
        self.__cnx.commit()

    def runscript(self, filename):
        commands = getscript(filename)
        print("Executing " + filename + ".sql...")
        for c in commands:
            self.query(c)
        print("Finished running script.")
        self.__cnx.commit()

    def runscriptPrint(self, filename):
        commands = getscript(filename)
        print("Executing " + filename + ".sql...")
        for c in commands:
            self.queryPrint(c)
        print("Finished running script.")
        self.__cnx.commit()

    def getDb(self):
        return self.__database

    def getConn(self):
        return self.__cnx


class Query():
    def __init__(self, dict, db, sql):
        self.sql = sql
        self.__cursor, self.__dictcursor = db.getCursors()
        if dict: self.cursor = self.__dictcursor
        else: self.cursor = self.__cursor
        self.__cnx = db.getconnection()
        self.__runcnt = 0

    def run(self):
        self.__runcnt += 1
        mystr = ""
        try:
            self.cursor.execute(self.sql)
            try:
                self.res = self.cursor.fetchall()
                for i in self.res:
                    mystr += str(i) + "\n"
                self.myresult = mystr
            except (sqlError, Exception) as err:
                return ("Something went wrong: {}".format(err))
        except sqlError as err:
            print("Something went wrong: {}".format(err))

    def jsonify(self):
        self.cursor = self.__dictcursor
        self.run()
        try:
            self.cursor.execute(self.sql)
            try:
                self.json = self.cursor.fetchall()
            except (sqlError, Exception) as err:
                return ("Something went wrong: {}".format(err))
        except sqlError as err:
            print("Something went wrong: {}".format(err))


    def result(self):
        try:
            print(self.myresult)
        except:
            if (self.__runcnt == 0):
                print("You must first run the Query")
            else:
                print("This query doesn't return anything")

    def __str__(self):
        return self.sql


