from django.shortcuts import render

from muro.models import Post



def inicio(request):
    return render(request, 'muro/index.html')

def muro(request):
    posteos = Post.objects.all().order_by('-fecha_creado')
    return render(request, 'muro/muro.html', {'posteos': posteos})
