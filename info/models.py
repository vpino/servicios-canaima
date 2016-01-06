from django.db import models

# Create your models here.
class Repositorio(models.Model):
    Nombre = models.CharField('nombre proyecto', max_length=50)
    Url = models.CharField('url repositorio del proyecto', max_length=100)

    def __str__(self):
        return self.Nombre

class PackageGeneric(models.Model):
    Nombre = models.CharField('nombre paquete', max_length=50)

    def __str__(self):
        return self.Nombre

class PackageGenericEdu(models.Model):
    Nombre = models.CharField('nombre paquete', max_length=50)

    def __str__(self):
        return self.Nombre
