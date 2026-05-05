from django.shortcuts import render, redirect, get_object_or_404

from muro.models import Post
from muro.forms import PostForm


def inicio(request):
    return render(request, 'muro/index.html')

def muro(request):
    posteos = Post.objects.all().order_by('-fecha_creado')
    return render(request, 'muro/muro.html', {'posteos': posteos})

def crear_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.autor = request.user
            post.save()
            return redirect('muro')
    else:
        form = PostForm()

    return render(request, 'muro/crear_post.html', {'form': form})

def editar_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)

    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('muro')
    else:
        form = PostForm(instance=post)

    return render(request, 'muro/editar_post.html', {'form': form, 'post': post})

def eliminar_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)

    if request.method == 'POST':
        post.delete()
        return redirect('muro')

    return render(request, 'muro/eliminar_post.html', {'post': post})