from django.db import models

#aqui escribiremos nuestras bases de datos o modelos:

class Prueba(models.Model):

    titulo = models.CharField(max_length=100)
    sudtitulo = models.CharField(max_length=50)
    cantidad = models.IntegerField()

    def __str__(self):
        return self.titulo + ' - ' + self.sudtitulo 

