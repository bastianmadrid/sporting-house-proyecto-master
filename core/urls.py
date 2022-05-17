from importlib.resources import path
from django.urls import path
from .views import index, contacto
urlpatterns =  [
    path('',index,name="index"),
    path('contacto.html',contacto,name="contacto"),
    path('iniciosesion.html',contacto,name="iniciosesion"),
    path('registro.html',contacto,name="resgitro"),
    path('running.html',contacto,name="carro")
]
