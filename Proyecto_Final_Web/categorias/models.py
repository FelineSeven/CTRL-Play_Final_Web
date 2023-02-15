from django.db import models

# Create your models here.
class Categoria(models.Model):
    nameCat = models.CharField(max_length=30)
