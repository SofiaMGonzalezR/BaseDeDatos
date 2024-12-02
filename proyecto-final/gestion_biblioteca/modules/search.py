from tabulate import tabulate
import mysql.connector
from db.db import get_connection


def search_books():
    connection = None
    cursor = None
    try:
        # Obtener la conexión a la base de datos
        connection = get_connection()
        if connection is None:
            print("No se pudo establecer la conexión a la base de datos.")
            return

        cursor = connection.cursor(dictionary=True)

        # Solicitar al usuario qué desea buscar (por título, autor o ID de usuario)
        print("¿Qué desea buscar?")
        print("1. Título")
        print("2. Autor")
        print("3. ID de usuario")
        choice = input("Seleccione una opción (1/2/3): ").strip()

        if choice == "1":
            keyword = input("Ingrese el título del libro a buscar: ").strip()
            if not keyword:
                print("Por favor ingrese un título válido.")
                return
            query = "SELECT * FROM Libros WHERE Titulo LIKE %s"
            cursor.execute(query, (f"%{keyword}%",))

        elif choice == "2":
            keyword = input("Ingrese el autor del libro a buscar: ").strip()
            if not keyword:
                print("Por favor ingrese un autor válido.")
                return
            query = "SELECT * FROM Libros WHERE Autor LIKE %s"
            cursor.execute(query, (f"%{keyword}%",))

        elif choice == "3":
            user_id = input("Ingrese el ID del usuario: ").strip()
            if not user_id.isdigit():
                print("El ID de usuario debe ser un número válido.")
                return
            query = """
                SELECT * FROM Libros 
                WHERE UsuarioID = %s
            """
            cursor.execute(query, (user_id,))

        else:
            print("Opción no válida.")
            return

        # Ejecutar la consulta de búsqueda
        resultados = cursor.fetchall()

        # Verificar si se encontraron resultados
        if not resultados:
            print("No se encontraron resultados que coincidan con la búsqueda.")
            return

        # Mostrar los resultados de la búsqueda en formato tabulado
        headers = ["ID", "Título", "Autor", "UsuarioID"]
        print(tabulate(resultados, headers=headers, tablefmt="fancy_grid"))

    except mysql.connector.Error as err:
        print(f"Error al buscar los libros: {err}")

    finally:
        if cursor:
            cursor.close()
        if connection:
            connection.close()


def search_users():
    connection = None
    cursor = None
    try:
        # Obtener la conexión a la base de datos
        connection = get_connection()
        if connection is None:
            print("No se pudo establecer la conexión a la base de datos.")
            return

        cursor = connection.cursor(dictionary=True)

        # Solicitar al usuario qué desea buscar (por nombre o ID de usuario)
        print("¿Qué desea buscar?")
        print("1. Nombre del usuario")
        print("2. ID de usuario")
        choice = input("Seleccione una opción (1/2): ").strip()

        if choice == "1":
            keyword = input("Ingrese el nombre del usuario a buscar: ").strip()
            if not keyword:
                print("Por favor ingrese un nombre válido.")
                return
            query = "SELECT * FROM Usuarios WHERE Nombre LIKE %s"
            cursor.execute(query, (f"%{keyword}%",))

        elif choice == "2":
            user_id = input("Ingrese el ID del usuario a buscar: ").strip()
            if not user_id.isdigit():
                print("El ID de usuario debe ser un número válido.")
                return
            query = "SELECT * FROM Usuarios WHERE ID = %s"
            cursor.execute(query, (user_id,))

        else:
            print("Opción no válida.")
            return

        # Ejecutar la consulta de búsqueda
        resultados = cursor.fetchall()

        # Verificar si se encontraron resultados
        if not resultados:
            print("No se encontraron resultados que coincidan con la búsqueda.")
            return

        # Mostrar los resultados de la búsqueda en formato tabulado
        headers = ["ID", "Nombre", "Correo Electrónico", "Dirección"]
        print(tabulate(resultados, headers=headers, tablefmt="fancy_grid"))

    except mysql.connector.Error as err:
        print(f"Error al buscar los usuarios: {err}")

    finally:
        if cursor:
            cursor.close()
        if connection:
            connection.close()
