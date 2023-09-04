from django.shortcuts import render,redirect
from .models import Product,User
from .forms import UserForm,ProductForm

def getHome(request):
    if request.method == 'POST':
        category = request.POST.get('data') 
        product = Product.objects.filter(category=category)
        return render(request, 'pages/home.html', {'product': product})
    else:
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



def createUser(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = UserForm()
    return render(request, 'pages/register.html', {'form': form})