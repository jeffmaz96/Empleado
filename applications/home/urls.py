from django.contrib import admin
from django.urls import path

#para utilizar la vista la tenemos que importar:
from.import views

urlpatterns = [
    path('prueba/',views.pruebaView.as_view() ),
    path('lista/',views.pruebaListView.as_view() ),
    path('lista_prueba/',views.ListarPrueba.as_view() ),
    path('add/',views.PruebaCreateView.as_view() ),
]

