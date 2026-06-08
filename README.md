# MyRecipe

Pequeña aplicación Django para gestionar recetas: crear, editar, listar, ver detalle, marcar favoritos y gestionar perfil de usuario.

## Qué hace
- Permite a los usuarios registrarse e iniciar sesión.
- Crear, editar y eliminar recetas con imágenes.
- Buscar y listar recetas.
- Marcar recetas como favoritas y ver tu lista de favoritos.

## Ejecutar en local
1. Crear y activar un entorno virtual (recomendado):

```bash
python3 -m venv venv
source venv/bin/activate
```

2. Instalar dependencias:

```bash
pip install -r requirements.txt
```

3. Aplicar migraciones:

```bash
python manage.py migrate
```

4. (Opcional) Crear un superusuario:

```bash
python manage.py createsuperuser
```

5. Ejecutar el servidor de desarrollo:

```bash
python manage.py runserver
```

6. Abrir en el navegador:

```
http://127.0.0.1:8000/
```