from django.db import migrations


def create_categories(apps, schema_editor):
    Categoria = apps.get_model('recetas', 'Categoria')
    categories = [
        ('Desayuno', 'Platos para la mañana'),
        ('Almuerzo', 'Platos para el mediodía'),
        ('Cena', 'Platos para la noche'),
        ('Postre', 'Dulces y postres'),
        ('Aperitivo', 'Entrantes y aperitivos'),
        ('Bebida', 'Bebidas y jugos'),
        ('Snack', 'Bocadillos'),
        ('Vegetariana', 'Platos sin carne'),
        ('Vegana', 'Platos sin productos animales'),
    ]
    for nombre, descripcion in categories:
        Categoria.objects.get_or_create(nombre=nombre, defaults={'descripcion': descripcion})


def delete_categories(apps, schema_editor):
    Categoria = apps.get_model('recetas', 'Categoria')
    nombres = ['Desayuno', 'Almuerzo', 'Cena', 'Postre', 'Aperitivo', 'Bebida', 'Snack', 'Vegetariana', 'Vegana']
    Categoria.objects.filter(nombre__in=nombres).delete()


class Migration(migrations.Migration):

    dependencies = [
        ('recetas', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(create_categories, reverse_code=delete_categories),
    ]
