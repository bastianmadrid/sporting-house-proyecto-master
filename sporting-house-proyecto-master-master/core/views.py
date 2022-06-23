from django.shortcuts import render, redirect
from .models import usuario


# Create your views here.
def index(request):
    return render(request,'core/index.html')
def editarusuario(request):
    return render(request,'core/editarusuario.html')

def contacto(request):
    return render(request,'core/contacto.html')
    
def iniciosesion(request):
    return render(request,'core/iniciosesion.html')
    
def registro(request):
    return render(request,'core/registro.html')
    
def carro(request):
    return render(request,'core/running.html')
    
def admin(request):
    usuarios =  usuario.objects.all()
    return render(request,"core/POVadmin.html",{"usuarios":usuarios})

def registrarusuario(request):
    
    nombre= request.POST['nombre']
    contraseña= request.POST['pass1']
    correo= request.POST['email']
    newusuario= usuario.objects.create(nombre=nombre, contrasena=contraseña, correo=correo)
    return redirect('/')

def eliminarusuario(request,nombre):
    Usuario = usuario.objects.get(nombre=nombre)
    Usuario.delete()
    return redirect('/POVadmin.html')
def edicionusuario(request,nombre):
    Usuario = usuario.objects.get(nombre=nombre)
    return render(request,"core/editarusuario.html",{"Usuario":Usuario})

def editarusuairo(request):
    Nombre= request.POST['nombre']
    contraseña= request.POST['pass1']
    correo= request.POST['email']

    Usuario = usuario.objects.get(nombre=Nombre)
    Usuario.nombre = Nombre
    Usuario.correo = correo
    Usuario.contrasena = contraseña
    Usuario.save()
    return redirect('/POVadmin.html')
def agregarrusuario(request):
    return redirect('core/registro.html')
def registrarusuarioadmin(request):
    
    nombre= request.POST['nombre']
    contraseña= request.POST['pass1']
    correo= request.POST['email']
    newusuario= usuario.objects.create(nombre=nombre, contrasena=contraseña, correo=correo)
    return redirect('/')