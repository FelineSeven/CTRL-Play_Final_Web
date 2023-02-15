from django.db import models

# Create your models here.
class Desarrolladora(models.Model):
    nombre = models.CharField(max_length=100)