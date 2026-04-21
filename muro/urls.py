from django.urls import path

from muro.views import inicio, muro

urlpatterns = [
    path('', inicio, name='inicio'),
    path('muro/', muro, name='muro'),
]