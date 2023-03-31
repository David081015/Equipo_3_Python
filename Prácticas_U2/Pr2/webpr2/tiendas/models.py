from django.db import models

# Create your models here.
class Frito(models.Model):
    nombre = models.CharField(max_length=255)
    marca = models.CharField(max_length=255)
    precio = models.IntegerField()
    def __str__(self) -> str:
        return f'Frito {self.id} : {self.nombre} {self.marca} {self.precio}'

class Tienda(models.Model):
    nombre = models.CharField(max_length=255)
    color = models.CharField(max_length=255)
    horario = models.CharField(max_length=255)
    frito = models.ForeignKey(Frito,on_delete=models.SET_NULL,null=True)
    def __str__(self) -> str:
        return f'Tienda {self.id} : {self.nombre} {self.color} {self.horario}'