from django.urls import path
from . import views

urlpatterns = [
    path('', views.vista_recetas, name='lista_recetas'),
    path('receta/<int:receta_id>/', views.detalle_receta, name='detalle_receta'),
    path('receta/crear/', views.crear_receta, name='crear_receta'),
    path('receta/<int:receta_id>/editar/', views.editar_receta, name='editar_receta'),
    path('receta/<int:receta_id>/eliminar/', views.eliminar_receta, name='eliminar_receta'),
    path('receta/<int:receta_id>/comentar/', views.comentar_receta, name='comentar_receta'),
    path('comentario/<int:comentario_id>/eliminar/', views.eliminar_comentario, name='eliminar_comentario'),
    path('registrar/', views.registrar_usuario, name='registrar_usuario'),
    path('receta/<int:receta_id>/favorito/', views.toggle_favorito, name='toggle_favorito'),
    path('favoritos/', views.mis_favoritos, name='mis_favoritos'),
    path('perfil/<str:username>/', views.perfil_usuario, name='perfil_usuario'),
]