from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from .models import Receta, Comentario
from .forms import Formulario_receta, Formulario_comentario
from .forms import Formulario_receta
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm

def vista_recetas(request):
    recetas = Receta.objects.all()
    return render(request, 'lista_recetas.html', {'recetas': recetas})

def detalle_receta(request, receta_id):
    receta = get_object_or_404(Receta, id=receta_id)
    comentarios = receta.comentario_set.all()
    formulario_comentario = Formulario_comentario()
    return render(request, 'detalle_receta.html', {
        'receta': receta,
        'comentarios': comentarios,
        'formulario_comentario': formulario_comentario
    })

@login_required
def crear_receta(request):
    if request.method == 'POST':
        formulario = Formulario_receta(request.POST)
        if formulario.is_valid():
            receta = formulario.save(commit=False)
            receta.autor = request.user
            receta.save()
            return redirect('lista_recetas')
    else:
        formulario = Formulario_receta()
    return render(request, 'crear_receta.html', {'formulario': formulario})

@login_required
def editar_receta(request, receta_id):
    receta = get_object_or_404(Receta, id=receta_id)
    if request.user != receta.autor:
        return redirect('lista_recetas')
    if request.method == 'POST':
        formulario = Formulario_receta(request.POST, instance=receta)
        if formulario.is_valid():
            formulario.save()
            return redirect('detalle_receta', receta_id=receta.id)
    else:
        formulario = Formulario_receta(instance=receta)
    return render(request, 'editar_receta.html', {'formulario': formulario})

@login_required
def eliminar_receta(request, receta_id):
    receta = get_object_or_404(Receta, id=receta_id)
    if request.user != receta.autor:
        return redirect('lista_recetas')
    if request.method == 'POST':
        receta.delete()
        return redirect('lista_recetas')
    return redirect('lista_recetas')

@login_required
def comentar_receta(request, receta_id):
    receta = get_object_or_404(Receta, id=receta_id)
    if request.method == 'POST':
        formulario = Formulario_comentario(request.POST)
        if formulario.is_valid():
            comentario = formulario.save(commit=False)
            comentario.autor = request.user
            comentario.receta = receta
            comentario.save()
    return redirect('detalle_receta', receta_id=receta.id)

@login_required
def eliminar_comentario(request, comentario_id):
    comentario = get_object_or_404(Comentario, id=comentario_id)
    if request.user != comentario.autor:
        return redirect('lista_recetas')
    if request.method == 'POST':
        receta_id = comentario.receta.id
        comentario.delete()
        return redirect('detalle_receta', receta_id=receta_id)
    return redirect('lista_recetas')

def registrar_usuario(request):
    if request.method == 'POST':
        formulario = UserCreationForm(request.POST)
        if formulario.is_valid():
            usuario = formulario.save()
            login(request, usuario)
            return redirect('lista_recetas')
    else:
        formulario = UserCreationForm()
    return render(request, 'registrar_usuario.html', {'formulario': formulario})

