# ==========================================
#  Pre entrega 2 blog
# ==========================================

# 1. Diccionario del perfil de autor
perfil_autor = {
    "nombre": "joaquin matcovich",
    "email": "joaqmat@gmail.com",
    "bio": "Desarrollador apasionado por Python y las tecnologias web.",
    "redes_sociales": [
        "https://twitter.com/joaquin",
        "https://github.com/joaquin",
        "https://linkedin.com/in/joaquin"
    ]
}

# 2. Tupla de estados posibles de un post (inmutable)
estados_post = ("borrador", "publicado", "archivado")

# 3. Set de etiquetas del blog (los duplicados se eliminan automáticamente)
etiquetas_blog = {
    "python",
    "inteligencia artificial",
    "desarrollo web",
    "machine learning",
    "backend",
    "apis",

}

# 4. Lista de posts
posts = [
    {
        "titulo": "Introducción a Python: por que es el lenguaje del momento",
        "autor": perfil_autor,
        "estado": estados_post[1],  # "publicado"
        "etiquetas": ["python", "backend"],
        "vistas": 1240
    },
    {
        "titulo": "Como construir una API REST con FastAPI",
        "autor": perfil_autor,
        "estado": estados_post[1],  # "publicado"
        "etiquetas": ["python", "apis", "backend"],
        "vistas": 876
    },
    {
        "titulo": "Machine Learning para principiantes: conceptos clave",
        "autor": perfil_autor,
        "estado": estados_post[0],  # "borrador"
        "etiquetas": ["machine learning", "inteligencia artificial"],
        "vistas": 0
    }
]

# 5. Verificacion de acceso a datos
print("Nombre del autor del segundo post:", posts[1]["autor"]["nombre"])

print("Lista completa de posts guardados:", posts)