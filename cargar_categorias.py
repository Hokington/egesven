import csv
from webapp.models import Categoria

with open('seeding/categorias.csv', newline='', encoding='utf-8') as file:
    reader = csv.DictReader(file)
    for row in reader:
        Categoria.objects.create(nombre=row['nombre'])
        print(f"Categoría '{row['nombre']}' agregada.")
