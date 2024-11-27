import csv
from webapp.models import Producto, Categoria

with open('seeding/productos.csv', newline='', encoding='utf-8') as file:
    reader = csv.DictReader(file)
    for row in reader:
        categoria = Categoria.objects.get(id=row['categoria'])
        Producto.objects.create(
            nombre=row['nombre'],
            precio=row['precio'],
            stock=row['stock'],
            categoria=categoria
        )

"""

    datos = [
        {"nombre": "Abbey Road", "descripcion": "El último álbum de estudio de los Beatles", "precio": 25990, "stock": 50, "categoria": 1},
        {"nombre": "Dark Side of the Moon", "descripcion": "Álbum icónico de Pink Floyd", "precio": 29990, "stock": 40, "categoria": 1},
        {"nombre": "Thriller", "descripcion": "El álbum más vendido de Michael Jackson", "precio": 19990, "stock": 30, "categoria": 1},
        {"nombre": "Back in Black", "descripcion": "Uno de los mejores álbumes de AC/DC", "precio": 24990, "stock": 20, "categoria": 1},
        {"nombre": "Hotel California", "descripcion": "Álbum clásico de Eagles", "precio": 22990, "stock": 15, "categoria": 1},
        {"nombre": "Rumours", "descripcion": "Famoso álbum de Fleetwood Mac", "precio": 27990, "stock": 25, "categoria": 2},
        {"nombre": "The Wall", "descripcion": "Doble álbum conceptual de Pink Floyd", "precio": 35990, "stock": 10, "categoria": 1},
        {"nombre": "Born to Run", "descripcion": "Álbum legendario de Bruce Springsteen", "precio": 23990, "stock": 35, "categoria": 3},
        {"nombre": "Led Zeppelin IV", "descripcion": "Incluye 'Stairway to Heaven'", "precio": 26990, "stock": 50, "categoria": 1},
        {"nombre": "The Joshua Tree", "descripcion": "Álbum famoso de U2", "precio": 21990, "stock": 20, "categoria": 1},
        {"nombre": "1989", "descripcion": "Pop moderno de Taylor Swift", "precio": 19990, "stock": 45, "categoria": 3},
        {"nombre": "OK Computer", "descripcion": "Obra maestra de Radiohead", "precio": 28990, "stock": 30, "categoria": 2},
        {"nombre": "Nevermind", "descripcion": "Icono del grunge por Nirvana", "precio": 24990, "stock": 50, "categoria": 2},
        {"nombre": "Ten", "descripcion": "Álbum debut de Pearl Jam", "precio": 22990, "stock": 40, "categoria": 2},
        {"nombre": "The Eminem Show", "descripcion": "Álbum aclamado de Eminem", "precio": 18990, "stock": 30, "categoria": 4},
        {"nombre": "Graduation", "descripcion": "Álbum de Kanye West", "precio": 19990, "stock": 25, "categoria": 4},
        {"nombre": "To Pimp a Butterfly", "descripcion": "Obra maestra de Kendrick Lamar", "precio": 27990, "stock": 20, "categoria": 4},
        {"nombre": "Good Kid, M.A.A.D City", "descripcion": "Relato conceptual de Kendrick Lamar", "precio": 23990, "stock": 35, "categoria": 4},
        {"nombre": "DAMN.", "descripcion": "Álbum premiado de Kendrick Lamar", "precio": 24990, "stock": 50, "categoria": 4},
        {"nombre": "Illmatic", "descripcion": "Clásico del rap por Nas", "precio": 21990, "stock": 30, "categoria": 4},
        {"nombre": "Ready to Die", "descripcion": "Debut de The Notorious B.I.G.", "precio": 22990, "stock": 40, "categoria": 4},
        {"nombre": "My Beautiful Dark Twisted Fantasy", "descripcion": "Obra icónica de Kanye West", "precio": 26990, "stock": 20, "categoria": 4},
        {"nombre": "Rumors", "descripcion": "Famoso álbum de Fleetwood Mac", "precio": 29990, "stock": 15, "categoria": 2},
        {"nombre": "Revolver", "descripcion": "Uno de los mejores álbumes de The Beatles", "precio": 27990, "stock": 30, "categoria": 1},
        {"nombre": "A Night at the Opera", "descripcion": "Álbum icónico de Queen", "precio": 25990, "stock": 25, "categoria": 1},
        {"nombre": "Sticky Fingers", "descripcion": "Gran álbum de The Rolling Stones", "precio": 24990, "stock": 20, "categoria": 1},
        {"nombre": "Exile on Main St.", "descripcion": "Obra maestra de The Rolling Stones", "precio": 29990, "stock": 15, "categoria": 1},
        {"nombre": "Pet Sounds", "descripcion": "Álbum innovador de The Beach Boys", "precio": 27990, "stock": 10, "categoria": 1},
        {"nombre": "Purple Rain", "descripcion": "Banda sonora de Prince", "precio": 26990, "stock": 30, "categoria": 3},
        {"nombre": "Songs in the Key of Life", "descripcion": "Obra maestra de Stevie Wonder", "precio": 32990, "stock": 20, "categoria": 3},
    ]

    for dato in datos:
        categoria = Categoria.objects.get(id=dato['categoria'])  # Obtén la categoría por ID
        Producto.objects.create(
            nombre=dato['nombre'],
            descripcion=dato['descripcion'],
            precio=dato['precio'],
            stock=dato['stock'],
            categoria=categoria
        )
    print("Productos insertados correctamente.")
"""