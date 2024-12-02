import mysql.connector
from tabulate import tabulate
from db.db import get_connection


def get_cursor():
    """
    Establece la conexión a la base de datos y devuelve un cursor.
    """
    connection = get_connection()
    if connection is None:
        print("No se pudo establecer la conexión a la base de datos.")
        return None, None
    return connection, connection.cursor(dictionary=True)


def view_books():
    """
    Muestra todos los libros almacenados en la base de datos en formato de tabla.
    """
    connection, cursor = get_cursor()
    if cursor is None:
        return

    try:
        cursor.execute("SELECT * FROM Libros")
        libros = cursor.fetchall()
        if libros:
            headers = ["ID", "Título", "Autor", "Género", "Año de Publicación"]
            data = [[libro["ID"], libro["Titulo"], libro["Autor"], libro["Genero"], libro["AnioPublicacion"]]
                    for libro in libros]
            print(tabulate(data, headers=headers, tablefmt="fancy_grid"))
        else:
            print("No se encontraron libros.")
    except mysql.connector.Error as err:
        print(f"Error al consultar los libros: {err}")
    finally:
        cursor.close()
        connection.close()


def add_book():
    """
    Función para agregar un nuevo libro a la base de datos.
    """
    connection, cursor = get_cursor()
    if cursor is None:
        return

    try:
        # Solicitar los datos del libro
        titulo = input("Ingrese el título del libro: ").strip()
        autor = input("Ingrese el autor del libro: ").strip()
        genero = input("Ingrese el género del libro: ").strip()
        anio_publicacion = input("Ingrese el año de publicación: ").strip()

        # Validación básica
        if not titulo or not autor or not genero or not anio_publicacion:
            print("Todos los campos son obligatorios.")
            return

        # Validar que el año de publicación sea un número
        if not anio_publicacion.isdigit():
            print("El año de publicación debe ser un número válido.")
            return

        # Intentar insertar el nuevo libro en la base de datos
        cursor.execute("INSERT INTO Libros (Titulo, Autor, Genero, AnioPublicacion) VALUES (%s, %s, %s, %s)",
                       (titulo, autor, genero, anio_publicacion))
        connection.commit()
        print("Libro agregado exitosamente.")
    except mysql.connector.Error as err:
        print(f"Error al agregar el libro: {err}")
    finally:
        cursor.close()
        connection.close()


def update_book():
    connection, cursor = get_cursor()
    if cursor is None:
        return

    try:
        book_id = input("Ingrese el ID del libro a actualizar: ").strip()

        if not book_id:
            print("El ID del libro no puede estar vacío.")
            return

        # Obtener los nuevos valores del libro
        nuevo_titulo = input("Ingrese el nuevo título (dejar vacío para no cambiar): ").strip()
        nuevo_autor = input("Ingrese el nuevo autor (dejar vacío para no cambiar): ").strip()
        nuevo_genero = input("Ingrese el nuevo género (dejar vacío para no cambiar): ").strip()
        nuevo_anio = input("Ingrese el nuevo año de publicación (dejar vacío para no cambiar): ").strip()

        # Comprobar si al menos un campo ha sido proporcionado
        if not any([nuevo_titulo, nuevo_autor, nuevo_genero, nuevo_anio]):
            print("Debe ingresar al menos un campo para actualizar.")
            return

        # Actualizar los campos que no están vacíos
        if nuevo_titulo:
            cursor.execute("UPDATE Libros SET Titulo = %s WHERE ID = %s", (nuevo_titulo, book_id))
        if nuevo_autor:
            cursor.execute("UPDATE Libros SET Autor = %s WHERE ID = %s", (nuevo_autor, book_id))
        if nuevo_genero:
            cursor.execute("UPDATE Libros SET Genero = %s WHERE ID = %s", (nuevo_genero, book_id))
        if nuevo_anio:
            if not nuevo_anio.isdigit():
                print("El año de publicación debe ser un número válido.")
                return
            cursor.execute("UPDATE Libros SET AnioPublicacion = %s WHERE ID = %s", (nuevo_anio, book_id))

        connection.commit()
        print("Libro actualizado exitosamente.")
    except mysql.connector.Error as err:
        print(f"Error al actualizar el libro: {err}")
    finally:
        cursor.close()
        connection.close()


def delete_book():
    connection, cursor = get_cursor()
    if cursor is None:
        return

    try:
        book_id = input("Ingrese el ID del libro a eliminar: ").strip()

        if not book_id:
            print("El ID del libro no puede estar vacío.")
            return

        cursor.execute("DELETE FROM Libros WHERE ID = %s", (book_id,))
        connection.commit()

        if cursor.rowcount > 0:
            print("Libro eliminado exitosamente.")
        else:
            print("No se encontró un libro con ese ID.")
    except mysql.connector.Error as err:
        print(f"Error al eliminar el libro: {err}")
    finally:
        cursor.close()
        connection.close()
