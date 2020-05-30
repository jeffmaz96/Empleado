from django.contrib import admin
#primero importamos nuestro modelo
from .models import  Prueba

#luego registramos nuestro modelo:
admin.site.register(Prueba)

