from rich.console import Console
from rich.table import Table
from rich.prompt import Prompt
from rich.panel import Panel
from rich.color import Color
from rich.text import Text
from tabulate import tabulate
from modules import books, loans, reports, search, users
from modules.books import view_books, add_book, update_book, delete_book
from modules.reports import show_debtors_report, modify_quota, view_quotas
from modules.search import search_books, search_users

console = Console()


def show_menu(title, options):
    """
    Muestra un menú con opciones estilizadas utilizando Rich.
    """
    console.clear()
    console.print(Panel(f"[bold yellow]{title}[/bold yellow]", style="bold magenta"))

    for key, value in options.items():
        # Añadir color a las opciones y un icono para hacerlas más atractivas
        console.print(f"[bold green]{key}.[/bold green] {value}", style="bold cyan")

    choice = Prompt.ask(f"Seleccione una opción", choices=list(options.keys()))
    return choice


def display_table(headers, data):
    """
    Muestra una tabla estilizada utilizando Tabulate.
    """
    table = tabulate(data, headers=headers, tablefmt="fancy_grid")
    console.print(table)


def main_menu():
    """
    Menú principal del sistema.
    """
    while True:
        options = {
            "1": "Gestión de Usuarios",
            "2": "Gestión de Libros",
            "3": "Préstamos",
            "4": "Búsqueda",
            "5": "Reportes",
            "6": "Salir"
        }
        choice = show_menu("Biblioteca Virtual", options)
        if choice == "1":
            user_menu()
        elif choice == "2":
            book_menu()
        elif choice == "3":
            loans_menu()
        elif choice == "4":
            search_menu()
        elif choice == "5":
            reports_menu()
        elif choice == "6":
            console.print("[bold red]Saliendo del sistema. ¡Hasta luego![/bold red]")
            break


def user_menu():
    """
    Menú de gestión de usuarios.
    """
    while True:
        options = {
            "1": "Ver usuarios",
            "2": "Actualizar usuario",
            "3": "Eliminar usuario",
            "4": "Regresar al menú principal"
        }
        choice = show_menu("Gestión de Usuarios", options)
        if choice == "1":
            users.view_users()
        elif choice == "2":
            users.update_user()
        elif choice == "3":
            users.delete_user()
        elif choice == "4":
            break


def book_menu():
    """
    Menú de gestión de libros.
    """
    while True:
        options = {
            "1": "Ver libros",
            "2": "Agregar libro",
            "3": "Actualizar libro",
            "4": "Eliminar libro",
            "5": "Regresar al menú principal"
        }
        choice = show_menu("Gestión de Libros", options)
        if choice == "1":
            view_books()
        elif choice == "2":
            add_book()
        elif choice == "3":
            update_book()
        elif choice == "4":
            delete_book()
        elif choice == "5":
            break


def loans_menu():
    """
    Menú de préstamos.
    """
    while True:
        options = {
            "1": "Calcular multa por demora",
            "2": "Regresar al menú principal"
        }
        choice = show_menu("Préstamos", options)
        if choice == "1":
            loans.calculate_late_fee()
        elif choice == "2":
            break


def search_menu():
    """
    Menú de búsqueda.
    """
    while True:
        options = {
            "1": "Buscar libros",
            "2": "Buscar usuarios",
            "3": "Regresar al menú principal"
        }
        choice = show_menu("Búsqueda", options)
        if choice == "1":
            search_books()
        elif choice == "2":
            search_users()
        elif choice == "3":
            break


def reports_menu():
    """
    Menú de reportes.
    """
    while True:
        options = {
            "1": "Reporte de morosos",
            "2": "Modificar cuota",
            "3": "Ver cuotas",
            "4": "Regresar al menú principal"
        }
        choice = show_menu("Gestión de Pagos y Reportes", options)
        if choice == "1":
            show_debtors_report()
        elif choice == "2":
            modify_quota()
        elif choice == "3":
            view_quotas()
        elif choice == "4":
            break


if __name__ == "__main__":
    main_menu()
