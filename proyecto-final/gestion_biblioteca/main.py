from db.db import get_connection
from ui.menu import main_menu

def main():
    """
    Punto de entrada principal de la aplicación.
    """
    try:
        # Crear la conexión a la base de datos
        connection = get_connection()
        if connection:
            # Asignar la conexión a los módulos
            from modules import users
            from modules import books
            from modules import loans
            from modules import search
            from modules import reports

            # Asignar la conexión a los módulos que la necesitan
            users.connection = connection
            books.connection = connection
            loans.connection = connection
            search.connection = connection
            reports.connection = connection

            # Llamar al menú principal o las funciones que requieran la conexión
            main_menu()

            # Cerrar la conexión al finalizar
            connection.close()
        else:
            print("No se pudo establecer la conexión a la base de datos. Verifica la configuración.")
    except Exception as e:
        print(f"Error inesperado: {e}")

if __name__ == "__main__":
    main()
