from django.db import models

# Create your models here.
class Paquete(models.Model):
    empresa = models.CharField(max_length=255)
    peso = models.IntegerField()
    pais = models.CharField(max_length=255)

    def __str__(self) -> str:
        return f'Paquete {self.id} : {self.empresa}  {self.peso} {self.pais}'

class Repartidor(models.Model):
    nombre = models.CharField(max_length=255)
    apellido = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    paquete = models.ForeignKey(Paquete,on_delete=models.SET_NULL,null=True)

    def __str__(self) -> str:
        return f'Repartidor {self.id} : {self.nombre} {self.apellido} {self.email}'