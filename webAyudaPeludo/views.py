from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,"index.html")

def perros(request):
    return render(request,"perros.html")

def gatos(request):
    return render(request,"gatos.html")

def scooby(request):
    return render(request,"scooby.html")

def patan(request):
    return render(request,"patan.html")

def coraje(request):
    return render(request,"coraje.html")
##################################################################

def doraemon(request):
    return render(request,"doraemon.html")

def tom(request):
    return render(request,"tom.html")

def garfield(request):
    return render(request,"garfield.html")