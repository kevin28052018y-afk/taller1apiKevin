import os
from dotenv import load_dotenv
from pymongo import MongoClient
from pymongo.errors import ConnectionFailure, ServerSelectionTimeoutError

# Cargar las variables de entorno desde el archivo .env (que NO se sube al repositorio)
load_dotenv()

# Obtener la URI de conexion a tu base de datos mongoDB desde las variables de entorno
MONGO_URI = os.getenv("MONGO_URL")

if not MONGO_URI:
    raise RuntimeError("La variable MONGO_URL no esta definida. Revisa tu archivo .env")

#crear una instancia del cliente de mongoDB y asignar un tiempo de espera para la seleccion del servidor
client = MongoClient(MONGO_URI, serverSelectionTimeoutMS=3000)

#crear la base de datos y la coleccion
db = client.database_apprentice
collection = db.trainee

try: 
    #intentar obtener informacion del servidor para verificar la conexion 
    client.server_info()
    client.admin.command("ping")
    print("Conexion exitosa a MongoDB")
    
except (ConnectionFailure, ServerSelectionTimeoutError) as e:
    print(f"Error al conectar a MongoDB: {e}")
