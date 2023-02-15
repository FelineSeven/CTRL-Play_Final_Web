from django.urls import path
from . import views

urlpatterns = [
    #ruta, vista, nombre interno
    path('',views.index, name='index'),
    path('juegos/api/', views.JuegosListApiView.as_view()),
    
    path('juegos/', views.listarJuegos, name='juegos'),
    path('juegos/new', views.crear_juegos, name='nuevo_juego'),
    path('juegos/<id>/',views.juegos_view, name='juegos_view'),
    path('juegos/delete/<id>/', views.delete_view, name='juego_eliminar')
]