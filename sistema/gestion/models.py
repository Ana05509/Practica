from django.db import models

# Create your models here.
class Cliente(models.Model):
    cedula = models.CharField(max_length=10,primary_key=True)
    nombre = models.CharField(max_length=50)
    direccion = models.CharField(max_length=100)
    telefono = models.CharField(max_length=15)
    email = models.EmailField()

    def __str__(self):
        return f' su cedula es - {self.cedula} y su nombre es {self.nombre}'