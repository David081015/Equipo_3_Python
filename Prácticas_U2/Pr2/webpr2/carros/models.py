from django.db import models

# Create your models here.
class Carro(models.Model):
    modelo = models.CharField(max_length=255)
    marca = models.CharField(max_length=255)
    color = models.CharField(max_length=255)
    def __str__(self) -> str:
        return f'Carro {self.id} : {self.modelo} {self.marca} {self.color}'