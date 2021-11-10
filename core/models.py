from django.db import models
from django.db.models.fields import IntegerField

# Create your models here.

class Genero(models.Model):
    nombre= models.CharField(max_length=80)

    def __str__(self):
        return self.nombre

class Imprenta(models.Model):
    imprenta= models.CharField(max_length=100)

    def __str__(self):
        return self.imprenta

class Libro(models.Model):
    nombre= models.CharField(max_length=200)
    autor = models.CharField(max_length=100)
    genero = models.ForeignKey(Genero, on_delete=models.CASCADE)
    año= models.IntegerField()
    sinopsis = models.TextField(null=True, blank=True)
    num_pag=models.IntegerField()
    imprenta=models.ForeignKey(Imprenta, on_delete=models.CASCADE, verbose_name="editorial")
    precio=IntegerField()
    imagen = models.ImageField(null=True, blank=True)
    cantidad = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.nombre


class Extras(models.Model):
    imagen_per = models.ImageField(verbose_name="Imgen ID")
    edad = models.IntegerField()