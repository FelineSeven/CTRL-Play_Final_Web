from django.shortcuts import render

# Create your views here.
#imports
from django.template import loader
from django.http import HttpResponse

#Rest imports
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

#Modelos
from .models import Juegos
from .serializers import JuegosSerializer

def index(request):
    #Archivo HTML con template
    template = loader.get_template('index.html')
    #logica de la vista
    context = {}
    #respuesta
    return HttpResponse(template.render(context,request))

class JuegosListApiView(APIView):
    def get(self, request, *args, **kwargs):
        
        juegos = Juegos.objects.all()
        serializer = JuegosSerializer(juegos, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
