# ==========================================
#  blog/datos.py
#  Estructuras de datos base del sistema
# ==========================================

# Diccionario con el perfil del autor del blog
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

# Lista de posts; el ultimo tiene datos incompletos para probar validaciones
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