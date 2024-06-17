from django.urls import path
from  . import views

urlpatterns = [
    path('', views.base, name='base'),
    path('info', views.info, name='info'),
    path('login', views.login, name='login'),
    path('catalogo', views.catalogo, name = 'catalogo'),
    path('contacto', views.contacto, name = 'contacto')
]