# ==========================================
#  blog/operaciones.py
#  Funciones principales: listar, buscar y filtrar posts
# ==========================================

def listar_posts(lista):
    """Recorre la lista de posts y muestra titulo, autor y estado de cada uno."""
    if not lista:
        print("No hay posts disponibles.")
        return

    print("\nPosts disponibles:")
    for post in lista:
        # Acceso al nombre del autor dentro del diccionario anidado
        nombre_autor = post["autor"]["nombre"]
        print(f"- {post['titulo']} | Autor: {nombre_autor} | Estado: {post['estado']}")


def buscar_por_titulo(lista, termino):
    """
    Busca posts cuyo titulo contenga el termino indicado.
    Retorna una lista con los posts que coinciden.
    Ignora diferencias de mayusculas y minusculas con .lower()
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
    Ignora diferencias de mayusculas y minusculas con .lower()
    """
    tag = tag.lower()
    resultados = []

    for post in lista:
        for t in post["tags"]:
            if tag == t.lower():
                resultados.append(post)
                break  # evitar duplicados si el tag aparece mas de una vez

    return resultados