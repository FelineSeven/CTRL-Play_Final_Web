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


def listarJuegos(request):
    juegos = Juegos.objects.all()
    context = {'juegos': juegos}
    template = loader.get_template('juegos/juegos.html')
    return HttpResponse(template.render(context,request))


def juegos_view(request, id):
        context = {}
        context['object'] = Juegos.objects.get(id = id)
        return render(request, 'juegos/juegos_detalles.html', context)

def crear_juegos(request):

    context = {}
    form = JuegoForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('juegos')
    context['form'] = form
    return render(request, 'juegos/crear_juegos.html', context)


def delete_view(request, id):
    context = {}
    obj = get_object_or_404(Juegos, id = id)
    if request.method == "POST":
        obj.delete()
        return redirect('juegos')    
    return render(request, "juegos/eliminar_juego.html", context)