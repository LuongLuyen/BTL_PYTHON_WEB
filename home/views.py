from django.shortcuts import render
from .models import Product

def getHome(request):
    product = Product.objects.all()
    return render(request, 'pages/home.html', {'product': product})

def getLogin(request):
    return render(request, 'pages/login.html')

def getProduct(request):
    return render(request, 'pages/product.html')

def getAdmin(request):
    return render(request, 'pages/admin.html')
def getManage(request):
    return render(request, 'pages/manage.html')