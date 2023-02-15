from django.db import models
from desarrolladoras.models import Desarrolladora
from categorias.models import Categoria

# Create your models here.
class Juegos(models.Model):
    nombre = models.CharField(max_length=30)
    fecha_lanzamiento = models.DateTimeField()
    valoracion_estrellas = models.CharField(max_length=30)
    desarrolladora = models.ForeignKey(Desarrolladora, on_delete=models.CASCADE)
    genero = models.ForeignKey(Categoria, on_delete=models.CASCADE)
