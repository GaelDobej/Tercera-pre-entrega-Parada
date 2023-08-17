from django.db import models

# Create your models here.

class Print(models.Model):
    titulo = models.CharField(max_length=20)
    material = models.CharField(max_length=20)
    precio = models.IntegerField()
    tamaño = models.CharField(max_length=20)

class Poster(models.Model):
    titulo = models.CharField(max_length=20)
    material = models.CharField(max_length=20)
    precio = models.IntegerField()
    tamaño = models.CharField(max_length=20)

class Card(models.Model):
    titulo = models.CharField(max_length=20)
    material = models.CharField(max_length=20)
    precio = models.IntegerField()
    tamaño = models.CharField(max_length=20)   

class Libro(models.Model):
    titulo = models.CharField(max_length=20)
    precio = models.IntegerField()
    numeroDePaginas = models.CharField(max_length=20)   

class Novela(models.Model):
    titulo = models.CharField(max_length=20)
    precio = models.IntegerField()
    numeroDePaginas = models.CharField(max_length=20)

class Cancion(models.Model):
    titulo = models.CharField(max_length=100)
    precio = models.IntegerField()
    duracion = models.CharField(max_length=10)
