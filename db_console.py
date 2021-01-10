from src.startdatabase import  loadPub
import src.objects as obj
if __name__ == "__main__":
    mydb,  mycontroller, myloader, pub = loadPub()

    while mydb.isconnected():
        try:
            command = str(input('Execute command:\n'))
            exec(command)
        except Exception as err:
            print("Something went wrong: {}".format(err))
