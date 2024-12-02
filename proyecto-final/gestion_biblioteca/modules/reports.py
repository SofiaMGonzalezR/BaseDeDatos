import mysql.connector
from db.db import get_connection
from tabulate import tabulate

def show_debtors_report():
    """
    Muestra un reporte de los usuarios morosos.
    """
    connection = None
    cursor = None
    try:
        # Obtener la conexión a la base de datos
        connection = get_connection()
        if connection is None:
            print("No se pudo establecer la conexión a la base de datos.")
            return

        cursor = connection.cursor(dictionary=True)

        # Ejecutar la consulta para obtener los morosos
        cursor.execute("""
            SELECT Usuarios.Nombre, COUNT(*) AS MesesDeuda
            FROM Pagos
            RIGHT JOIN Usuarios ON Pagos.UsuarioID = Usuarios.ID
            WHERE Pagos.FechaPago IS NULL OR Pagos.FechaPago < CURDATE()
            GROUP BY Usuarios.ID
        """)

        morosos = cursor.fetchall()

        # Verificar si se encontraron resultados
        if not morosos:
            print("No se encontraron morosos en el sistema.")
            return

        # Mostrar los resultados del reporte con tabulate
        print("Reporte de Morosos:")
        headers = ["Nombre", "Meses de deuda"]
        table = [(moroso['Nombre'], moroso['MesesDeuda']) for moroso in morosos]
        print(tabulate(table, headers=headers, tablefmt="grid"))

    except mysql.connector.Error as err:
        print(f"Error al obtener el reporte de morosos: {err}")

    finally:
        # Asegurar que se cierren correctamente los recursos
        if cursor:
            cursor.close()
        if connection:
            connection.close()


def modify_quota():
    """
    Modifica la cuota de un usuario.
    """
    connection = None
    cursor = None
    try:
        # Obtener conexión a la base de datos
        connection = get_connection()
        if connection is None:
            print("No se pudo establecer la conexión a la base de datos.")
            return

        cursor = connection.cursor()

        # Solicitar detalles para modificar la cuota
        user_id = input("Ingrese el ID del usuario: ").strip()
        month = input("Ingrese el mes (MM): ").strip()
        year = input("Ingrese el año (YYYY): ").strip()
        new_amount = input("Ingrese el nuevo monto de la cuota: ").strip()

        # Validación de datos básicos
        if not (user_id.isdigit() and month.isdigit() and year.isdigit() and new_amount.replace('.', '', 1).isdigit()):
            print("Entrada no válida. Asegúrese de ingresar valores numéricos.")
            return

        # Formatear la fecha para la consulta
        date_like = f"{year}-{month:0>2}%"  # Asegurar el formato correcto para la fecha

        # Actualizar la cuota en la base de datos
        cursor.execute("""
            UPDATE Pagos
            SET Monto = %s
            WHERE UsuarioID = %s AND FechaPago LIKE %s
        """, (new_amount, user_id, date_like))

        # Confirmar los cambios
        connection.commit()

        if cursor.rowcount > 0:
            print("Cuota modificada correctamente.")
        else:
            print("No se encontró una cuota para modificar con los datos proporcionados.")

    except mysql.connector.Error as err:
        print(f"Error al modificar la cuota: {err}")

    finally:
        # Asegurar que se cierren correctamente los recursos
        if cursor:
            cursor.close()
        if connection:
            connection.close()


def view_quotas():
    """
    Muestra las cuotas registradas en el sistema.
    """
    connection = None
    cursor = None
    try:
        # Obtener conexión a la base de datos
        connection = get_connection()
        if connection is None:
            print("No se pudo establecer la conexión a la base de datos.")
            return

        cursor = connection.cursor(dictionary=True)

        # Preguntar si desea ver cuotas de un usuario específico o todos
        user_id = input("Ingrese el ID del usuario (deje vacío para ver todos): ").strip()

        # Construir la consulta según la entrada del usuario
        if user_id.isdigit():
            cursor.execute("""
                SELECT * FROM Pagos
                WHERE UsuarioID = %s
                ORDER BY FechaPago
            """, (user_id,))
        else:
            cursor.execute("""
                SELECT * FROM Pagos
                ORDER BY UsuarioID, FechaPago
            """)

        quotas = cursor.fetchall()

        # Verificar si se encontraron cuotas
        if not quotas:
            print("No se encontraron cuotas registradas.")
            return

        # Mostrar las cuotas con tabulate
        print("Cuotas registradas:")
        headers = ["ID", "UsuarioID", "Fecha", "Monto"]
        table = [(cuota['ID'], cuota['UsuarioID'], cuota['FechaPago'], cuota['Monto']) for cuota in quotas]
        print(tabulate(table, headers=headers, tablefmt="grid"))

    except mysql.connector.Error as err:
        print(f"Error al obtener las cuotas: {err}")

    finally:
        # Asegurar que se cierren correctamente los recursos
        if cursor:
            cursor.close()
        if connection:
            connection.close()
