from flask import Flask
from src.startdatabase import  loadPub

app = Flask(__name__)
mydb, mycontroller, myloader, pub = loadPub()

from app import routes