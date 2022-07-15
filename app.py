import pymongo
from mongoengine import Document, StringField, connect

MONGOHOST = "localhost"
MONGOPORT = "27017"
MONGO_TIEMPO_FUERA = 1000

MONGO_URI = "mongodb://" + MONGOHOST + ":" + MONGOPORT + "/"

MONGO_BASEDATOS = "PickOut"
MONGO_COLLECTION = "logins"

client = pymongo.MongoClient(MONGO_URI,serverSelectionTimeoutMS=MONGO_TIEMPO_FUERA)
baseDatos = client[MONGO_BASEDATOS]
coleccion = client[MONGO_COLLECTION]

connect(MONGO_BASEDATOS)

print(baseDatos.list_collection_names())


