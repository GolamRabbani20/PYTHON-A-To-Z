from django.shortcuts import render


# Create your views here.
def Cloud(request):
    return render(request,"home.html",{'name':'Monir'})