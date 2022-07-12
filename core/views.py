from email import message
from pyexpat.errors import messages
from django.shortcuts import render, redirect
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.forms import AuthenticationForm
from pip import main
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
    
def carrito(request):
    return render(request,'core/carrito.html')

def carritoo(request):
    return render(request,'core/carritoo.html')

def bicicleta(request):
    return render(request,'core/bicicleta.html')
    
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


def logout_request(request):
    logout(request)
    message.info(request,"saliste exitosamente")
    return redirect("core:index")

def login_request(request):
    
    if request.method =="POST":
        form= AuthenticationForm(request,data=request.POST)
        if form.is_valid():
            correoe = form.cleaned_data.get('emailini')
            contraseña= form.cleaned_data.get('password')
            user = authenticate(emailini=correoe,password=contraseña)
            if user is not None:
                login(request,user)
                messages.info(request,f"estas logueado como {correoe} ")
                return redirect("core:index")
            else:
             messages.error(request,"correo o contraseña equivocada")
    

    
    form = AuthenticationForm()
    return render(request, "core/iniciosesion.html",{"form": form})