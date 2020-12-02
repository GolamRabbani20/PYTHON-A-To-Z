from django.shortcuts import render


# Create your views here.

def About(request10):
    return render(request10,"home.html",{'name':'Lazina'})
