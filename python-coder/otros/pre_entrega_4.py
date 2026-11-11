# ==========================================
#  Modulo 4 | Pre-entrega 4
# ==========================================


# --- Estructuras de datos (continuacion del Modulo 3) ---

perfil_autor = {
    "nombre": "joaquin matcovich",
    "bio": "Desarrollador apasionado por Python y las tecnologias web.",
    "especialidad": "Python y Django",
    "redes_sociales": [
        "https://twitter.com/joaquin",
        "https://linkedin.com/in/joaquin",
        "https://github.com/joaquin",
    ]
}

# Tupla de estados posibles (inmutable, actua como constante)
estados_post = ("borrador", "publicado", "archivado")

# Set de etiquetas (duplicados se eliminan automaticamente)
etiquetas_blog = {
    "Python",
    "Django",
    "Web",
    "Backend",
    "APIs",
    "Python",    # duplicado intencional
    "Backend"    # duplicado intencional
}

# Lista de posts
posts = [
    {
        "id": 1,
        "titulo": "Primeros pasos con Python",
        "contenido": "En este post veremos como empezar a programar con Python: instalacion, variables y tu primer script.",
        "autor": perfil_autor,
        "tags": ["Python", "Principiantes"],
        "estado": estados_post[1]
    },
    {
        "id": 2,
        "titulo": "Construyendo una API REST con Django",
        "contenido": "Django REST Framework nos permite crear APIs robustas de forma rapida. Repasamos los conceptos clave.",
        "autor": perfil_autor,
        "tags": ["Python", "Django", "APIs", "Backend"],
        "estado": estados_post[1]
    },
    {
        "id": 3,
        "titulo": "Organizando datos con listas y diccionarios",
        "contenido": "Las estructuras de datos en Python son la base de cualquier programa.",
        "autor": perfil_autor,
        "tags": ["Python", "Principiantes"],
        "estado": estados_post[0]
    },
    {
        "id": 4,
        "titulo": "Deploy de una app web en la nube",
        "contenido": "Repasamos las opciones para llevar tu aplicacion Django a produccion.",
        "autor": perfil_autor,
        "tags": ["Django", "Web", "Backend"],
        "estado": estados_post[2]
    },
    {
        # Post con datos incompletos para probar validar_post()
        "id": 5,
        "titulo": "",
        "contenido": "Contenido sin titulo.",
        "autor": "joaquin matcovich",   # autor como texto, no como diccionario
        "tags": [],
        "estado": estados_post[0]
    }
]


# --- Funciones del sistema ---

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
        # Si input() no puede convertirse a int, se devuelve -1 como valor invalido
        opcion = -1

    return opcion


def listar_posts(lista):
    """Recorre la lista de posts y muestra titulo y nombre del autor."""
    if not lista:
        print("No hay posts disponibles.")
        return

    print("\nPosts disponibles:")
    for post in lista:
        # Acceso al nombre del autor dentro del diccionario anidado
        nombre_autor = post["autor"]["nombre"]
        print(f"- {post['titulo']} | Autor: {nombre_autor}")


def buscar_por_titulo(lista, termino):
    """
    Busca posts cuyo titulo contenga el termino indicado.
    Retorna una lista con los posts que coinciden.
    """
    termino = termino.lower()
    resultados = []

    for post in lista:
        if termino in post["titulo"].lower():
            resultados.append(post)

    return resultados


def filtrar_por_tag(lista, tag):
    """
    Filtra posts que contengan el tag indicado.
    Retorna una lista con los posts que coinciden.
    """
    tag = tag.lower()
    resultados = []

    for post in lista:
        for t in post["tags"]:
            if tag == t.lower():
                resultados.append(post)
                break  # evitar duplicados si el tag aparece mas de una vez

    return resultados


def validar_post(post):
    """
    Verifica que un post tenga la estructura correcta.
    Retorna True si es valido, o un string con el mensaje de error si no lo es.
    Reglas: claves existentes, campos no vacios, autor como diccionario con clave nombre,
    tags como lista, estado dentro de estados_post.
    """
    # Verificar que el post sea un diccionario
    if not isinstance(post, dict):
        return "el post no es un diccionario"

    claves_requeridas = ["id", "titulo", "contenido", "autor", "tags", "estado"]

    # Verificar que existan todas las claves requeridas
    for clave in claves_requeridas:
        if clave not in post:
            return f"falta la clave '{clave}'"

    # Verificar que titulo y contenido no esten vacios
    if not post.get("titulo"):
        return "el campo 'titulo' esta vacio"

    if not post.get("contenido"):
        return "el campo 'contenido' esta vacio"

    # Verificar que el autor sea un diccionario con la clave nombre
    if not isinstance(post.get("autor"), dict):
        return "el campo 'autor' debe ser un diccionario"

    if "nombre" not in post["autor"]:
        return "el autor no tiene la clave 'nombre'"

    # Verificar que tags sea una lista
    if not isinstance(post.get("tags"), list):
        return "el campo 'tags' debe ser una lista"

    # Verificar que el estado sea uno de los valores validos
    if post.get("estado") not in estados_post:
        return f"el estado '{post.get('estado')}' no es valido"

    return True


# --- Bloque principal ---

if __name__ == "__main__":

    # Separar posts validos de los que tienen datos incompletos
    # validar_post retorna True si es valido, o un string con el error si no lo es
    posts_validos = [post for post in posts if validar_post(post) == True]
    posts_invalidos = [post for post in posts if validar_post(post) != True]

    if posts_invalidos:
        print(f"Aviso: {len(posts_invalidos)} post(s) con datos incompletos no se mostraran.")

    # Bucle principal: se mantiene activo hasta que el usuario elija salir
    while True:

        opcion = mostrar_menu()

        if opcion == 1:
            listar_posts(posts_validos)

        elif opcion == 2:
            termino = input("Buscar por titulo: ")
            # Validar que el usuario no haya dejado la busqueda vacia
            if not termino.strip():
                print("Debes ingresar un termino para buscar.")
            else:
                resultados = buscar_por_titulo(posts_validos, termino)
                if resultados:
                    print(f"\nResultados para '{termino}':")
                    listar_posts(resultados)
                else:
                    print("No se encontraron posts con ese titulo.")

        elif opcion == 3:
            tag = input("Filtrar por tag: ")
            # Validar que el usuario no haya dejado el tag vacio
            if not tag.strip():
                print("Debes ingresar un tag para filtrar.")
            else:
                resultados = filtrar_por_tag(posts_validos, tag)
                if resultados:
                    print(f"\nPosts con el tag '{tag.capitalize()}':")
                    for post in resultados:
                        print(f"- {post['titulo']}")
                else:
                    print(f"No se encontraron posts con el tag '{tag}'.")

        elif opcion == 4:
            # Recorrer todos los posts y mostrar cuales son validos y cuales no
            print("\nValidando posts:")
            for post in posts:
                resultado = validar_post(post)
                id_post = post.get("id", "?")
                if resultado == True:
                    print(f"  Post {id_post}: valido")
                else:
                    print(f"  Post {id_post}: error - {resultado}")

        elif opcion == 5:
            print("\nGracias por usar el sistema del blog.")
            break

        else:
            print("Opcion invalida, intenta de nuevo")