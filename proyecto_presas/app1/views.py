from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .forms import notaForm
# Create your views here.
def inicio(request):
    return render(request, 'paginas/inicio.html')
def nosotros(request):
    return render(request, 'paginas/nosotros.html')
def notas(request):
    usuarios=Presa.objects.all()
    return render(request, 'usuarios/index.html',{'usuarios':usuarios})
def hacerNota(request):
    formulario=notaForm(request.POST or None,request.FILES or None)
    if formulario.is_valid():
        formulario.save()
        return redirect('usuarios')
    else: print('Error')
    return render(request, 'usuarios/formRegistrarRuptura.html',{'formulario':formulario})
def eliminarNota(request,id):
    usuarios=Presa.objects.get(id=id)
    usuarios.delete()
    return redirect('usuarios')

def editarNota(request,id):
    notas=Presa.objects.get(id=id)
    formulario=notaForm(request.POST or None,request.FILES or None,instance=notas)
    if formulario.is_valid() and request.method == 'POST':
        formulario.save()
        return redirect('usuarios')
    return render(request,'usuarios/editar.html',{'formulario':formulario})

