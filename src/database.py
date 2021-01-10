import mysql.connector
import src.config as cfg
    
class Database:
    def __init__(self):
        self.__database_name = cfg.dbname
        self.__host = cfg.host
        self.__username = cfg.username
        self.__password = cfg.password
        self.__isconnected = False

    def createcursor(self):
        self.__cursor = self.__cnx.cursor(buffered=True)
        self.__dictcursor = self.__cnx.cursor(dictionary=True, buffered=True)

    def createConnection(self):
        try:
            print("Establishing connection to: ", self.__database_name)
            cnx = mysql.connector.connect(
                user=self.__username,
                password=self.__password,
                host=self.__host,
                database=self.__database_name)
            print("Connection established!")
            self.__cnx = cnx
            self.__isconnected = True
        except mysql.connector.Error as err:
            print("Something went wrong: {}".format(err))

    def getconnection(self):
        return self.__cnx

    def getCursors(self):
        return self.__cursor, self.__dictcursor

    def close(self):
        self.__cnx.close()
        self.__isconnected = False

    def isconnected(self):
        return self.__isconnected