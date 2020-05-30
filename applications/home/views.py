from django.shortcuts import render

#para importar vistas genericas hacemos:
from django.views.generic import (
TemplateView,
ListView,
CreateView)

#importamos los modelos o bases de datos:

from .models import Prueba

# Creamos nuestra vista basada en clases:

#la vita Templateview es para mostrar templates htmls:
class pruebaView(TemplateView):
    template_name = 'home/prueba.html' #indicamos en home por que alli se encuentra prueba.html


#esta vista listview es para mostrar basicamente listas de una base de datos:
class pruebaListView(ListView):

     template_name = "home/lista.html"
     context_object_name = 'listaNumeros'
     queryset = ['1','10','20','30']
   

class ListarPrueba(ListView):

    template_name = "home/lista_prueba.html"
    model = Prueba
    context_object_name = 'lista'


#este template nos sirve para organizar mi base de datos sin el admin

class PruebaCreateView(CreateView):

    template_name = "home/add.html"
    model = Prueba
    fields = ['titulo','sudtitulo','cantidad']
  

