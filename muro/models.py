from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    contenido = models.TextField()
    fecha_creado = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.autor.username}: {self.contenido}'

    def get_comentarios(self):
        return Comentario.objects.filter(post=self).order_by('fecha_creado')


class Comentario(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comentarios')
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    contenido = models.TextField()
    fecha_creado = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.autor.username}: {self.contenido}'

   