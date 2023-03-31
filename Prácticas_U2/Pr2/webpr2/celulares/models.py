from django.db import models

# Create your models here.
class Celular(models.Model):
    modelo = models.CharField(max_length=255)
    marca = models.CharField(max_length=255)
    ram = models.CharField(max_length=255)
    memoria = models.CharField(max_length=255)
    def __str__(self) -> str:
        return f'Celular {self.id} : {self.modelo} {self.marca} {self.ram} {self.memoria}'