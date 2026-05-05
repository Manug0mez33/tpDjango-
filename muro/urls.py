from django.urls import path

from muro.views import crear_post, editar_post, eliminar_post, inicio, muro

urlpatterns = [
    path('', inicio, name='inicio'),
    path('muro/', muro, name='muro'),
    path('crear_post/', crear_post, name='crear_post'),
    path('editar_post/<int:post_id>/', editar_post, name='editar_post'),
    path('eliminar_post/<int:post_id>/', eliminar_post, name='eliminar_post'),
]