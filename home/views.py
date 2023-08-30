from django.shortcuts import render
from .models import Product

def getHome(request):
    product = Product.objects.all()
    return render(request, 'pages/home.html', {'product': product})

def getLogin(request):
    return render(request, 'pages/login.html')
