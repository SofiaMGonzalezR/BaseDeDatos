from tabulate import tabulate
import mysql.connector
from db.db import get_connection

def calculate_late_fee():
    """
    Calcula las multas por retraso en préstamos para un usuario específico.
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

        # Solicitar y validar el ID del usuario
        user_id = input("Ingrese el ID del usuario: ").strip()
        if not user_id.isdigit():
            print("El ID del usuario debe ser un número válido.")
            return

        # Solicitar y validar la cuota mensual
        try:
            cuota_mensual = float(input("Ingrese la cuota mensual del usuario: ").strip())
            if cuota_mensual <= 0:
                print("La cuota mensual debe ser un valor positivo.")
                return
        except ValueError:
            print("La cuota mensual debe ser un número válido.")
            return

        # Consultar los préstamos atrasados
        try:
            cursor.execute("""
                SELECT ID, FechaPrestamo, FechaDevolucion, DATEDIFF(CURDATE(), FechaDevolucion) AS DiasRetraso
                FROM Prestamos 
                WHERE UsuarioID = %s AND FechaDevolucion < CURDATE() AND Estado = 'Prestado'
            """, (user_id,))
            prestamos = cursor.fetchall()

            if not prestamos:
                print("No hay préstamos atrasados para este usuario.")
                return

            # Preparar los datos para la tabla
            data = []
            total_multa = 0

            for prestamo in prestamos:
                dias_retraso = max(prestamo['DiasRetraso'], 0)  # Asegurarse de que no haya días negativos
                multa = dias_retraso * (cuota_mensual * 0.03)
                total_multa += multa
                data.append([prestamo['ID'], prestamo['FechaPrestamo'], prestamo['FechaDevolucion'], dias_retraso, f"${multa:.2f}"])

            # Mostrar tabla con detalles de multas
            headers = ["ID Préstamo", "Fecha Préstamo", "Fecha Devolución", "Días de Retraso", "Multa"]
            print(tabulate(data, headers=headers, tablefmt="fancy_grid"))

            # Mostrar la multa total
            print(f"\nTotal de multas por retraso: ${total_multa:.2f}")

        except mysql.connector.Error as err:
            print(f"Error al consultar los préstamos: {err}")

    except mysql.connector.Error as err:
        print(f"Error al conectar a la base de datos: {err}")
    finally:
        if cursor:
            cursor.close()
        if connection:
            connection.close()
