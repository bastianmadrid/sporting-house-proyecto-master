from django.contrib import admin
from .models import producto, usuario, zapatillas, bicileta, equipo
# Register your models here.

admin.site.register(zapatillas)
admin.site.register(bicileta)
admin.site.register(equipo)
admin.site.register(usuario)
admin.site.register(producto)