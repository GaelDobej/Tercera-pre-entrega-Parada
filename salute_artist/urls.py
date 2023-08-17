from django.urls import path, include
from .views import *
from .models import *

app_name = "salute_artist"

urlpatterns = [
    path('pintor/', pintores, name='pintor'),
    path('escritor/', escritores, name='escritor'),
    path('musico/', musicos, name='musico'),

    path('pintor_Form/', pintorForm, name='pintor_Form'),
    path('musico_Form/', musicoForm, name='musico_Form'),
    path('escritor_Form/', escritorForm, name='escritor_Form'),

    path('buscar_Musico/', buscarMusico, name='buscar_Musico'),
    path('buscar_Musico/buscar2/', buscar2, name='buscar2'),       

    path('buscar_Escritor/', buscarEscritor, name='buscar_Escritor'),
    path('buscar_Escritor/buscar3/', buscar3, name='buscar3'),    

    path('buscar_Pintor/', buscarPintor, name='buscar_Pintor'),
    path('buscar_Pintor/buscar4/', buscar4, name='buscar4'),    
]