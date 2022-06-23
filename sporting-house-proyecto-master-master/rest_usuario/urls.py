from django.urls import path
from rest_usuario.views import lista_usuarios, detalle_usuarios
from rest_usuario.viewsLogin import login

urlpatterns = [
    path('lista_usuario',lista_usuarios,name="lista_usuario"),
    path('detalle_usuario/<nombre>',detalle_usuarios,name="detalle_usuario"),
    path('login',login,name="login_html"),
]