from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'core/index.html')

def contacto(request):
    return render(request,'core/contacto.html')
    
def iniciosesion(request):
    return render(request,'core/contacto.html')
    
def resgitro(request):
    return render(request,'core/contacto.html')
    
def carro(request):
    return render(request,'core/contacto.html')
    