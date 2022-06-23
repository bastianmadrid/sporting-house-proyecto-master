from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view,permission_classes
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from core.models import usuario
from rest_usuario.serializers import usuarioSerializers
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

@csrf_exempt
@api_view(['GET','POST'])
@permission_classes((IsAuthenticated,))
def lista_usuarios(request):
    if request.method == 'GET':
        listaUsuario = usuario.objects.all()
        serializ = usuarioSerializers(listaUsuario, many = True)
        return Response(serializ.data)
    elif request.method == 'POST':
        dataV = JSONParser().parse(request)
        serializ = usuarioSerializers(data = dataV)
        if serializ.is_valid():
            serializ.save()
            return Response(serializ.data, status = status.HTTP_201_CREATED)
        else:
            return Response(serializ.errors, status = status.HTTP_400_BAD_REQUEST) 

@api_view(['GET','PUT','DELETE'])
@permission_classes((IsAuthenticated,))
def detalle_usuarios(request, nombre):
    try:
        Usuario = usuario.objects.get(nombre = nombre)
    except usuario.DoesNotExist:
        return Response(status = status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        serializ = usuarioSerializers(Usuario)
        return Response(serializ.data)
    elif request.method == "PUT":
        dataV = JSONParser().parse(request)
        serializ = usuarioSerializers(Usuario, data = dataV)
        if serializ.is_valid():
            serializ.save()
            return Response(serializ.data)
        else:
            return Response(serializ.errors, status = status.HTTP_400_BAD_REQUEST) 
    elif request.method == "DELETE":
        Usuario.delete() # DELETE A LA BD
        return Response(status = status.HTTP_204_NO_CONTENT) 

