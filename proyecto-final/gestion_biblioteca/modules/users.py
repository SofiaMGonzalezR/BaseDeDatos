import mysql.connector
from tabulate import tabulate

from db.db import get_connection


def view_users():
    connection = None
    cursor = None
    try:
        # Obtener la conexión a la base de datos
        connection = get_connection()
        if connection is None:
            print("No se pudo establecer la conexión a la base de datos.")
            return

        cursor = connection.cursor(dictionary=True)

        # Ejecutar la consulta para obtener los usuarios
        cursor.execute("SELECT * FROM Usuarios")
        usuarios = cursor.fetchall()

        # Verificar si se encontraron usuarios
        if not usuarios:
            print("No se encontraron usuarios en la base de datos.")
            return

        # Mostrar los usuarios con tabulate
        headers = ["ID", "Nombre", "Dirección", "Fecha de Registro"]
        table = [(usuario['ID'], usuario['Nombre'], usuario['Direccion'], usuario['FechaRegistro']) for usuario in usuarios]
        print(tabulate(table, headers=headers, tablefmt="grid"))

    except mysql.connector.Error as err:
        print(f"Error al obtener los usuarios: {err}")

    finally:
        # Asegurarse de cerrar la conexión y el cursor correctamente
        if cursor:
            cursor.close()
        if connection:
            connection.close()


def update_user():
    connection = None
    cursor = None
    try:
        # Obtener la conexión a la base de datos
        connection = get_connection()
        if connection is None:
            print("No se pudo establecer la conexión a la base de datos.")
            return

        cursor = connection.cursor()

        # Solicitar el ID del usuario a actualizar
        user_id = input("Ingrese el ID del usuario a actualizar: ").strip()

        # Validar que el ID no esté vacío
        if not user_id:
            print("Por favor ingrese un ID válido.")
            return

        # Solicitar los nuevos datos para actualizar
        nuevo_nombre = input("Ingrese el nuevo nombre (dejar vacío para no cambiar): ").strip()
        nueva_direccion = input("Ingrese la nueva dirección (dejar vacío para no cambiar): ").strip()

        # Actualizar solo los campos que fueron modificados
        if nuevo_nombre:
            cursor.execute("UPDATE Usuarios SET Nombre = %s WHERE ID = %s", (nuevo_nombre, user_id))
        if nueva_direccion:
            cursor.execute("UPDATE Usuarios SET Direccion = %s WHERE ID = %s", (nueva_direccion, user_id))

        # Si se realizaron actualizaciones, hacer commit
        if nuevo_nombre or nueva_direccion:
            connection.commit()
            print("Usuario actualizado exitosamente.")
        else:
            print("No se realizaron cambios en el usuario.")

    except mysql.connector.Error as err:
        print(f"Error al actualizar el usuario: {err}")

    finally:
        # Asegurarse de cerrar la conexión y el cursor correctamente
        if cursor:
            cursor.close()
        if connection:
            connection.close()


def delete_user():
    connection = None
    cursor = None
    try:
        # Obtener la conexión a la base de datos
        connection = get_connection()
        if connection is None:
            print("No se pudo establecer la conexión a la base de datos.")
            return

        cursor = connection.cursor()

        # Solicitar el ID del usuario a eliminar
        user_id = input("Ingrese el ID del usuario a eliminar: ").strip()

        # Validar que el ID no esté vacío
        if not user_id:
            print("Por favor ingrese un ID válido.")
            return

        # Ejecutar la eliminación del usuario
        cursor.execute("DELETE FROM Usuarios WHERE ID = %s", (user_id,))
        connection.commit()

        # Verificar si se eliminó el usuario
        if cursor.rowcount > 0:
            print("Usuario eliminado exitosamente.")
        else:
            print("No se encontró un usuario con ese ID.")

    except mysql.connector.Error as err:
        print(f"Error al eliminar el usuario: {err}")

    finally:
        # Asegurarse de cerrar la conexión y el cursor correctamente
        if cursor:
            cursor.close()
        if connection:
            connection.close()
