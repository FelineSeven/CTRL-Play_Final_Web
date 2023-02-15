from rest_framework import serializers
from .models import Juegos

class JuegosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Juegos
        fields= ["nombre", "fecha_lanzamiento", "valoracion_estrellas", "desarrolladora", "genero"]