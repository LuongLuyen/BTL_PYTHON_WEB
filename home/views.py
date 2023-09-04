from django.shortcuts import render,redirect
from .models import Product
from .forms import ProductForm
from .models import User
from .forms import UserForm

def getHome(request):
    product = Product.objects.all()
    return render(request, 'pages/home.html', {'product': product})

def postHome(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('item-list')
    else:
        form = ProductForm()
    return render(request, 'pages/home.html', {'form': form})


def getLogin(request):
    return render(request, 'pages/login.html')

def getProduct(request):
    return render(request, 'pages/product.html')

def getAdmin(request):
    return render(request, 'pages/admin.html')
def getManage(request):
    return render(request, 'pages/manage.html')



def createUser(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = UserForm()
    return render(request, 'pages/register.html', {'form': form})