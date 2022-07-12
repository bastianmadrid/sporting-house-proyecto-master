from cgitb import html
from importlib.resources import path
from unicodedata import name
from django import views
from . import views
from django.urls import path
from .views import editarusuario, index, contacto, iniciosesion, registro, contacto, admin, carrito, carritoo, bicicleta
urlpatterns =  [
    path('',index,name="index"),
    path('carrito.html',carrito, name="carrito"),
    path('carritoo.html',carritoo, name="carritoo"),
    path('bicicleta.html',bicicleta, name="bicicleta"),
    path('contacto.html',contacto,name="contacto"),
    path('iniciosesion.html',iniciosesion,name="iniciosesion"),
    path('registro.html', registro,name="registro"),
    path('running.html',contacto,name="carro"),
    path('POVadmin.html',admin, name="admin"),
    path('editarusuario.html',editarusuario, name="editarusuario"),
    path('registrarusuario/',views.registrarusuario),
    path('eliminarusuario/<nombre>',views.eliminarusuario),
    path('edicionusuario/<nombre>',views.edicionusuario),
    path('editarusuario/',views.editarusuairo),
    path('agregarrusuario/',views.agregarrusuario),
    path('registrarusuarioadmin/',views.registrarusuarioadmin),
    path('logout/',views.logout_request,name="logout"),
    path('login/',views.login_request,name="login"),
]

