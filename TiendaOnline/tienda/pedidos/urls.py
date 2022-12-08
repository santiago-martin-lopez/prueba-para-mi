from django.urls import path
from .views import *

urlpatterns = [
    path('',inicio,name='inicio'),
    path('clientes/',clientes,name='clientes'),
    path('articulos/',articulos,name='articulos'),
    path('pedidos/',pedidos,name='pedidos'),
    path('busquedaclientes/',busquedaclientes,name='busquedaclientes'),
    path('resultadosclientes/',resultadosclientes,name='resultadosclientes'),
    path('busquedaarticulos/',busquedaarticulos,name='busquedaarticulos'),
    path('resultadosarticulos/',resultadosarticulos,name='resultadosarticulos')
]
