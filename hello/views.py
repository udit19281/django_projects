from django.shortcuts import render
from django.http import HttpResponse
from django.urls import include
# Create your views here.
from . import templates
def index(request):
    return HttpResponse("Hello World!")

def udit(request):
    return render(request,("hello/index.html"))

def greet(request,name):
    #return render(f"Hello, {name.capitalize()}!")
    return render(request,"hello/greet.html",{
        "name":name.capitalize()
        })
