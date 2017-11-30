from django.db import models


# Create your models here.

class Categoria(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre


class Producto(models.Model):
    categoria = models.ForeignKey(Categoria)
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre
