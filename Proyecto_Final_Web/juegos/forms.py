from django import forms
from .models import Juegos

#Crear formulario
class JuegoForm(forms.ModelForm):

    #metaclase
    class Meta:
        model = Juegos

        #especificar los campos
        fields = [
            'nombre',
            'fecha_lanzamiento',
            'valoracion_estrellas',
            'desarrolladora',
            'genero'
        ]