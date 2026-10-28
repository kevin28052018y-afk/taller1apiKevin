import os

from dotenv import load_dotenv
from pymongo import MongoClient
from pymongo.errors import ConnectionFailure, ServerSelectionTimeoutError

# Cargar las variables de entorno desde el archivo .env (que NO se sube al repositorio)
load_dotenv()

# Obtener la URI de conexion a tu base de datos mongoDB desde las variables de entorno
MONGO_URI = os.getenv("MONGO_URL")

#crear una instancia del cliente de mongoDB y asignar un tiempo de espera para la seleccion del servidor
client = MongoClient(MONGO_URI, serverSelectionTimeoutMS=3000)

#crear la base de datos y la coleccion
db = client.amb703
collection = db.mesa

#modelo de datos para la conexion
nueva_mesa = {
    "name": "Joan",
    "status": "Alive",
    "species": "Human",
    "gender": "Male"
}

try: 
    #intentar obtener informacion del servidor para verificar la conexion 
    client.server_info()
    client.admin.command("ping")
    print("Conexion exitosa a MongoDB")
    
    #insertar el modelo de datos en la coleccion 
    collection.insert_one(nueva_mesa)
    print("Documento insertado en la coleccion 'mesa' de la base de datos 'amb703'")
    
except (ConnectionFailure, ServerSelectionTimeoutError) as e:
    print(f"Error al conectar a MongoDB: {e}")
finally:
    client.close()
