from django.urls import path
from . import views



urlpatterns = [
    
    path("buscar/",views.buscar,name='buscar'),
    path("buscar/zona/<int:id>",views.buscarzona,name='buscarzona'),
    path("buscar/zona/<int:id>",views.buscarzona,name='buscarzona')
]