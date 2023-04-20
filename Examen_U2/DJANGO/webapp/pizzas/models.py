from django.db import models

# Create your models here.
class Pizza(models.Model):
    ingredientes = models.CharField(max_length=255)
    tamaño = models.CharField(max_length=255)
    precio = models.IntegerField()

    def __str__(self) -> str:
        return f'Pizza {self.id} : {self.ingredientes} {self.tamaño} {self.precio}'