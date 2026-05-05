from django.contrib import admin
from .models import Post, Comentario, Categoria

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('autor', 'titulo', 'categoria','fecha_creado')
    search_fields = ('autor__username', 'titulo')
    list_filter = ('fecha_creado',)
    readonly_fields = ('fecha_creado',)

@admin.register(Comentario)
class ComentarioAdmin(admin.ModelAdmin):
    list_display = ('post', 'autor', 'contenido', 'fecha_creado')
    search_fields = ('post__titulo', 'autor__username', 'contenido')
    list_filter = ('fecha_creado',)
    readonly_fields = ('fecha_creado',)

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('nombre',)
    search_fields = ('nombre',)