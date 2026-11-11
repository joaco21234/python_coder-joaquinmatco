# Blog Consola

Siistema interactivo de blog por consola desarrollado en Python.

## Como ejecutar

Desde la carpeta raiz del proyecto, correr:

```
python main.py
```

## Estructura del proyecto

```
blog_consola/
│
├── main.py          # Archivo principal, orquesta el sistema
├── README.md        # Este archivo
│
└── blog/
    ├── __init__.py      # Indica que blog/ es un paquete de Python
    ├── datos.py         # Estructuras de datos: perfil_autor, posts, etc.
    ├── menu.py          # Muestra el menu y captura la opcion del usuario
    ├── operaciones.py   # Funciones de listado, busqueda y filtrado
    └── validaciones.py  # Reglas para validar la estructura de los posts
```

## Opciones del menu

1. **Ver todos los posts** - Lista los posts validos con titulo, autor y estado
2. **Buscar por titulo** - Busca posts que contengan una palabra en el titulo
3. **Filtrar por tag** - Muestra posts que tengan una etiqueta especifica
4. **Validar posts** - Revisa todos los posts e informa cuales tienen errores
5. **Salir** - Cierra el programa