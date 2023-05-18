from django.urls import path
from . import  views

urlpatterns = [
    path('',views.inicio,name='inicio'),
    path('nosotros',views.nosotros,name='nosotros'),
    path('usuarios',views.notas,name='usuarios'),
    path('hacerNota',views.hacerNota,name='hacerNota'),
    path('eliminarNota/<int:id>',views.eliminarNota,name='eliminarNota'),
    path('editarNota/<int:id>',views.editarNota,name='editarNota'),
    
]

