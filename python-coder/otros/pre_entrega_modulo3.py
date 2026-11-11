# ==========================================
#  Módulo 3 | Pre-entrega 3
# ==========================================


# Diccionario con el perfil del autor del blog
perfil_autor = {
    "nombre": "joaquin matcovich",
    "bio": "Desarrollador apasionado por Python y las tecnologías web.",
    "especialidad": "Python y Django",
    "redes_sociales": [
        "https://twitter.com/joaquin",
        "https://linkedin.com/in/joaquin"
        "https://github.com/joaquin",
    ]
}

# Tupla de estados posibles para un post (inmutable, actúa como constante)
estados_post = ("borrador", "publicado", "archivado")

# Set de etiquetas del blog (los duplicados se eliminan automáticamente)
etiquetas_blog = {
    "Python",
    "Django",
    "Web",
    "Backend",
    "APIs",
    "Python",     # duplicado intencional
    "Backend"     # duplicado intencional
}

# Lista de posts; cada post es un diccionario con la estructura requerida
posts = [
    {
        "id": 1,
        "titulo": "Primeros pasos con Python",
        "contenido": "En este post veremos cómo empezar a programar con Python: instalación, variables y tu primer script.",
        "autor": perfil_autor,
        "tags": ["Python", "Principiantes"],
        "estado": estados_post[1]   # "publicado"
    },
    {
        "id": 2,
        "titulo": "Construyendo una API REST con Django",
        "contenido": "Django REST Framework nos permite crear APIs robustas de forma rápida. Repasamos los conceptos clave.",
        "autor": perfil_autor,
        "tags": ["Python", "Django", "APIs", "Backend"],
        "estado": estados_post[1]   # "publicado"
    },
    {
        "id": 3,
        "titulo": "Organizando datos con listas y diccionarios",
        "contenido": "Las estructuras de datos en Python son la base de cualquier programa. Aprendemos listas, diccionarios, tuplas y sets.",
        "autor": perfil_autor,
        "tags": ["Python", "Principiantes"],
        "estado": estados_post[0]   # "borrador"
    },
    {
        "id": 4,
        "titulo": "Deploy de una app web en la nube",
        "contenido": "Repasamos las opciones para llevar tu aplicación Django a producción: Railway, Render y VPS.",
        "autor": perfil_autor,
        "tags": ["Django", "Web", "Backend"],
        "estado": estados_post[2]   # "archivado"
    }
]


# --- Bucle principal del sistema ---

# El programa se mantiene activo hasta que el usuario elija salir (opcion 4)
while True:

    # Mostrar el menu en caada iteracion
    print("\n--- MENU DEL BLOG ---")
    print("1. Ver todos los posts")
    print("2. Buscar por titulo")
    print("3. Filtrar por tag")
    print("4. Salir")

    # Capturar la opcion elegida por el usuario (input() siempre devuelvve texto)
    opcion = input("\nElegí una opción: ")

    # --- Opcion 1: Ver todos los posts ---
    if opcion == "1":
        print("\nPosts disponibles:")
        # Recorrer la lista e imprimir titulo y nombre del autor (dato anidado)
        for post in posts:
            print(f"- {post['titulo']} | Autor: {post['autor']['nombre']}")

    # --- Opcion 2: Buscar por titulo ---
    elif opcion == "2":
        # . lower para Convertir a minusculas para ignorar diferencias de capitalizacion
        busqueda = input("Buscar por titulo: ").lower()
        encontrados = 0

        for post in posts:
            # Comparar la busqueda contra el titulo en minusculas
            if busqueda in post["titulo"].lower():
                print(f"- {post['titulo']} | Autor: {post['autor']['nombre']}")
                encontrados += 1

        # Informar si no hubo resultados
        if encontrados == 0:
            print("No se encontraron posts con ese titulo.")

    # --- Opcion 3: Filtrar por tag ---
    elif opcion == "3":
        tag_buscado = input("Filtrar por tag: ").lower()
        encontrados = 0

        for post in posts:
            # Recorrer la lista de tags de cada post
            for tag in post["tags"]:
                if tag_buscado == tag.lower():
                    # Mostrar el post solo si coincide el tag
                    if encontrados == 0:
                        print(f"\nPosts con el tag '{tag_buscado.capitalize()}':")
                    print(f"- {post['titulo']}")
                    encontrados += 1
                    break  # Evitar duplicados si el tag aparece mas de una vez

        if encontrados == 0:
            print(f"No se encontraron posts con el tag '{tag_buscado}'.")

    # --- Opcion 4: Salir del programa ---
    elif opcion == "4":
        print("\nGracias por usar el sistema del blog.")
        break   # Termina el bucle while y cierra el programa

    # --- Opcion invalida ---
    else:
        print("Opción invalida, intenta de nuevo")