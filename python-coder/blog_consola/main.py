# ==========================================
#  main.py
#  Archivo principal: orquesta el sistema del blog
# ==========================================

from blog.datos import posts
from blog.menu import mostrar_menu
from blog.operaciones import listar_posts, buscar_por_titulo, filtrar_por_tag
from blog.validaciones import validar_post


if __name__ == "__main__":

    # Separar posts validos de los que tienen datos incompletos al iniciar
    posts_validos = [post for post in posts if validar_post(post) == True]
    posts_invalidos = [post for post in posts if validar_post(post) != True]

    if posts_invalidos:
        print(f"Aviso: {len(posts_invalidos)} post(s) con datos incompletos no se mostraran en el listado.")

    # Bucle principal: se mantiene activo hasta que el usuario elija salir
    while True:

        opcion = mostrar_menu()

        # Opcion 1: Ver todos los posts validos
        if opcion == 1:
            listar_posts(posts_validos)

        # Opcion 2: Buscar por titulo
        elif opcion == 2:
            termino = input("Buscar por titulo: ")
            if not termino.strip():
                print("Debes ingresar un termino para buscar.")
            else:
                resultados = buscar_por_titulo(posts_validos, termino)
                if resultados:
                    print(f"\nResultados para '{termino}':")
                    listar_posts(resultados)
                else:
                    print("No se encontraron posts con ese titulo.")

        # Opcion 3: Filtrar por tag
        elif opcion == 3:
            tag = input("Filtrar por tag: ")
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

        # Opcion 4: Validar todos los posts
        elif opcion == 4:
            print("\nValidando posts:")
            for post in posts:
                resultado = validar_post(post)
                id_post = post.get("id", "?")
                if resultado == True:
                    print(f"  Post {id_post}: valido")
                else:
                    print(f"  Post {id_post}: error - {resultado}")

        # Opcion 5: ssalir
        elif opcion == 5:
            print("\nGracias por usar el sistema del blog.")
            break

        # Opcion invalida
        else:
            print("Opcion invalida, intenta de nuevo")