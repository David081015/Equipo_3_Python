from django.db import models

# Create your models here.
class Mascota(models.Model):
    apodo = models.CharField(max_length=255)
    tipo = models.CharField(max_length=255)
    color = models.CharField(max_length=255)
    def __str__(self) -> str:
        return f'Mascota {self.id} : {self.apodo} {self.tipo} {self.color}'

class Persona(models.Model):
    nombre = models.CharField(max_length=255)
    apellido = models.CharField(max_length=255)
    edad = models.IntegerField()
    mascota = models.ForeignKey(Mascota,on_delete=models.SET_NULL,null=True)
    def __str__(self) -> str:
        return f'Persona {self.id} : {self.nombre} {self.apellido} {self.edad}'