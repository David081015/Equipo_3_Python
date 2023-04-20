from django.db import models

# Create your models here.
class Mascota(models.Model):
    nombre = models.CharField(max_length=255)
    edad = models.IntegerField()
    raza = models.CharField(max_length=255)

    def __str__(self) -> str:
        return f'Mascota {self.id} : {self.nombre}  {self.edad} {self.raza}'

class Dueño(models.Model):
    nombre = models.CharField(max_length=255)
    apellido = models.CharField(max_length=255)
    numtelefono = models.CharField(max_length=255)
    mascota = models.ForeignKey(Mascota,on_delete=models.SET_NULL,null=True)

    def __str__(self) -> str:
        return f'Dueño {self.id} : {self.nombre} {self.apellido} {self.numtelefono}'