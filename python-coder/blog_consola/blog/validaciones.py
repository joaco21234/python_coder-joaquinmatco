# ==========================================
#  blog/validaciones.py
#  Reglas logicas para validar la estructura de los posts
# ==========================================

from blog.datos import estados_post


def validar_post(post):
    """
    Verifica que un post tenga la estructura correcta.
    Retorna True si es valido, o un string con el mensaje de error si no lo es.
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