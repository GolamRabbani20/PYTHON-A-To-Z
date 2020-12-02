from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return HttpResponse("Hellow world,Runserver,My name is Md Golam Rababni,I'm BSc in CSE, why I am here!")
    
