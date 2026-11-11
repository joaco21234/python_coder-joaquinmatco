# ==========================================
#  blog/menu.py
#  Manejo del menu e input del usuario
# ==========================================

def mostrar_menu():
    """Muestra el menu en consola y retorna la opcion elegida por el usuario."""
    print("\n--- MENU DEL BLOG ---")
    print("1. Ver todos los posts")
    print("2. Buscar por titulo")
    print("3. Filtrar por tag")
    print("4. Validar posts")
    print("5. Salir")

    # try-except para manejar el caso en que el usuario escriba texto en lugar de un numero
    try:
        opcion = int(input("\nElegi una opcion: "))
    except ValueError:
        opcion = -1

    return opcion