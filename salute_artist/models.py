from django.db import models

# Create your models here.

class Pintor(models.Model):
    nombre = models.CharField(max_length=50)
    edad = models.IntegerField()
    gmail = models.EmailField()
    portfolio = models.URLField()
    activo = models.CharField(max_length=10)

    class Meta:
        verbose_name = "Pintor"
        verbose_name_plural = "Pintores"

    def __str__(self):
        return f"{self.nombre}"

class Escritor(models.Model):
    nombre = models.CharField(max_length=50)
    edad = models.IntegerField()
    gmail = models.EmailField()
    portfolio = models.URLField()
    activo = models.CharField(max_length=10)

    class Meta:
        verbose_name = "Escritor"
        verbose_name_plural = "Escritores"

    def __str__(self):
        return f"{self.nombre}"

class Musico(models.Model):
    nombre = models.CharField(max_length=50)
    edad = models.IntegerField()
    gmail = models.EmailField()
    portfolio = models.URLField()
    activo = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.nombre}"