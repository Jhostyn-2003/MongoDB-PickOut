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

#Definicion de esquema rigido mongodb con una clase
class logins(Document):
    ID_paralelo = StringField(required=True)
    contrasenia = StringField(required=True, min_length=8, max_length=30)
    
#Crear documento
loginParalelo1 = logins(
    ID_paralelo = "ObjectId('78sfd0889er08')",
    contrasenia = "contraseñaParaleloA"
)
loginParalelo1.save() #Insertar un nuevo login

for doc in logins.objects:
 print(doc.ID_paralelo)
