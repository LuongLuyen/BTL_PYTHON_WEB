from django.shortcuts import render,redirect
from .models import Product,User
from .forms import UserForm,ProductForm

def getHome(request):
    if request.method == 'POST':
        category = request.POST.get('data') 
        id = request.POST.get('id_product')
        if(id!=None):
            product = Product.objects.get(id=id)
            return render(request, 'pages/product.html', {'product': product})
        product = Product.objects.filter(category=category)
        return render(request, 'pages/home.html', {'product': product})
    else:
        product = Product.objects.all()
        return render(request, 'pages/home.html', {'product': product})


def getLogin(request):
    if request.method == 'POST':
        userName = request.POST.get('userName') 
        password = request.POST.get('password') 
        if(userName== "admin123" and password== "admin123"):
            product = Product.objects.all()
            return render(request, 'pages/home.html', {'product': product})
        return render(request, 'pages/login.html')
    else:
        return render(request, 'pages/login.html')

def getProduct(request):
    if request.method == 'POST':
        id = request.POST.get('id_product')
        if(id!=None):
            product = Product.objects.get(id=id)
            return render(request, 'pages/manage.html', {'product': product})
    else:
        return render(request, 'pages/manage.html')

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