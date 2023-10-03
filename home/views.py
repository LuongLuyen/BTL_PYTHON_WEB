from django.shortcuts import render,redirect, get_object_or_404
from .models import Product,User,Cart
from .forms import UserForm,ProductForm,ProductFormU


def getHome(request):
    if request.method == 'POST':
        category = request.POST.get('data') 
        id = request.POST.get('id_product')
        search = request.POST.get('search')
        if(search!= None):
            product = Product.objects.all()
            list = []
            for x in product:
               if search in x.shortDescription:
                   list.append(x)
            return render(request, 'pages/home.html', {'product': list})
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
        try:
            userDB = User.objects.get(userName=userName)
            passDB = User.objects.get(password=password)
            if(userDB!=None and passDB!=None):
                product = Product.objects.all()
                return render(request, 'pages/home.html', {'product': product})
        except:
            return render(request, 'pages/login.html')
    else:
        return render(request, 'pages/login.html')


def getProduct(request):
    if request.method == 'POST':
        id = request.POST.get('id_product')
        if(id!=None):
            product = Product.objects.get(id=id)
            return render(request, 'pages/cart.html', {'product': product})
    else:
        return render(request, 'pages/cart.html')


def getAdmin(request):
    product = Product.objects.all()
    if request.method == 'POST':
        idU = request.POST.get('data')
        idD = request.POST.get('dataD')
        if(idD!=None):
            product = get_object_or_404(Product, pk=idD)
            product.delete()
            return redirect('/admins')
        productById = Product.objects.get(id=idU)
        return render(request, 'pages/add.html', {'product': productById})
    return render(request, 'pages/admin.html', {'product': product})

def getAdd(request):
    if request.method == 'POST':
        idD = request.POST.get('dataU')
        product = get_object_or_404(Product, pk=idD)
        form = ProductForm(request.POST, instance=product)
        print(idD)
        if form.is_valid():
            form.save()
            return redirect('/admins')
    else:
        form = ProductForm()
    return render(request, 'pages/add.html', {'form': form})


def getCart(request):
    cart = Cart.objects.all()
    return render(request, 'pages/cart.html',{'product': cart})

def createUser(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = UserForm()
    return render(request, 'pages/register.html', {'form': form})