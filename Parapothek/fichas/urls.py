from django.urls import path
from .views import *

urlpatterns = [
    #path modelo ficha
    path('fichas/',FichasViews.as_view(), name= 'fichas'),
    path('fichaupdate/<int:pk>',FichaUpdate.as_view(),name='fichaupdate'),
    path('buscarficha',buscadorfichas,name='buscarficha'),
    path('fichaspuntuacion/',FichasViewsPuntuacion.as_view(), name= 'fichaspuntuacion'),
    #path añadir indicaciones
    path('fichas/indicaciones/<int:pk>',views.indicacioneschoose, name= 'indicacioneschoose'),
    #path modelo zona
    path('zonasaplicacion/',ZonasViews.as_view(),name='zonas'),
    path('zonacreate/',ZonaCreate.as_view(), name= 'zonacreate'),
    path('zonaupdate/<int:pk>',ZonaUpdate.as_view(),name='zonaupdate'),
    path('zonadelete/<int:pk>',ZonaDelete.as_view(),name='zonadelete'),
    #path modelo indicaciones
    path('indicaciones/',IndicacionesViews.as_view(),name='indicaciones'),
    path('indicacioncreate/',IndicacionCreate.as_view(), name= 'indicacioncreate'),
    path('indicacionupdate/<int:pk>',IndicacionUpdate.as_view(),name='indicacionupdate'),
    path('indicaciondelete/<int:pk>',IndicacionDelete.as_view(),name='indicaciondelete'),
    #path puntuar
    path ('fichas/puntuar/<int:id>', views.puntuar,name='puntuar')
    
    
]
    
