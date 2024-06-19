from django.urls import path
from  . import views

urlpatterns = [
    path('', views.base, name='base'),
    path('info', views.info, name='info'),
    path('catalogo', views.catalogo, name = 'catalogo'),
    path('contacto', views.contacto, name = 'contacto'),
    path('carro', views.carro, name = 'carro')
]