from rest_framework import serializers
from core.models import usuario

class usuarioSerializers(serializers.ModelSerializer):
    class Meta:
        model = usuario
        fields = ['nombre','contrasena','correo']