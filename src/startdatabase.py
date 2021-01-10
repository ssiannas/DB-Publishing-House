import src.controller as controller
import src.loader as loader
import src.database as database
import src.publisher as publisher

def loadPub():
    db = database.Database()
    db.createConnection()
    db.createcursor()

    mycontroller = controller.Controller(db)
    myloader = loader.Loader(db,mycontroller)
    pub = publisher.Publisher(mycontroller)

    return db, mycontroller, myloader, pub

