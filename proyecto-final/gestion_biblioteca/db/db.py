import os

import mysql.connector
from dotenv import load_dotenv
from mysql.connector import Error

# Cargar variables desde el archivo .env
load_dotenv()

def get_connection():
    """Obtiene la conexión a la base de datos."""
    try:
        connection = mysql.connector.connect(
            host=os.getenv("DB_HOST"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
            database=os.getenv("DB_NAME"),
            port=os.getenv("DB_PORT")
        )
        if connection.is_connected():
            print("Conexión exitosa a la base de datos.")
            return connection
        else:
            print("No se pudo conectar a la base de datos.")
            return None
    except Error as e:
        print(f"Error al conectar a la base de datos: {e}")
        return None
