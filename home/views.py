from django.shortcuts import render,redirect, get_object_or_404
from .models import Product,User,Cart
from .forms import UserForm,ProductForm
from django.contrib.auth import logout


def getHome(request):
    if request.method == 'POST':
        category = request.POST.get('data') 
        id = request.POST.get('id_product')
        idG = request.POST.get('id_productG')
        idUser =  request.session['user_id']
       
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
        if(idG!=None and idUser!=None):
            cart = Cart(userid=idUser,thumbnail="",shortDescription="",transport="",color="",category="",price="")
            product = Product.objects.get(id=idG)
            cart.shortDescription = product.shortDescription
            cart.thumbnail = product.thumbnail
            cart.transport = ""
            cart.color = "None"
            cart.category = product.category
            cart.price = product.price
            cart.save()
            cart = Cart.objects.filter(id=idUser)
            return render(request, 'pages/cart.html', {'product': cart})
        product = Product.objects.filter(category=category)
        return render(request, 'pages/home.html', {'product': product})
    else:
        product = Product.objects.all()
        return render(request, 'pages/home.html', {'product': product})
 
def getLogin(request):
    if request.method == 'POST':
        userName = request.POST.get('userName') 
        password = request.POST.get('password') 
        lo = request.POST.get('dataOut') 
        try:
            userDB = User.objects.get(userName=userName)
            passDB = User.objects.get(password=password)
            if(userDB!=None and passDB!=None):
                product = Product.objects.all()
                request.session['user_id'] = userDB.id
                request.session['name'] = str(userDB)
                name =  request.session['name']
                return render(request, 'pages/home.html', {'product': product, 'name': name})
        except:
            return render(request, 'pages/login.html')
        if(lo=="dataOut"):
            if 'user_id' in request.session:
                del request.session['user_id']
                request.session.pop('name', None)
            logout(request)
        
            return render(request, 'pages/login.html')
    else:
        return render(request, 'pages/login.html')

def getProduct(request):
    name =  request.session['name']
    if request.method == 'POST':
        idUser =  request.session['user_id']
        id = request.POST.get('idP')
        color = request.POST.get('color')
        if(id!=None and idUser!=None):
            cart = Cart(userid=idUser,thumbnail="",shortDescription="",transport="",color="",category="",price="")
            product = Product.objects.get(id=id)
            cart.shortDescription = product.shortDescription
            cart.thumbnail = product.thumbnail
            cart.transport = ""
            cart.color = color
            cart.category = product.category
            cart.price = product.price
            cart.save()
            cart = Cart.objects.filter(id=idUser)
            return render(request, 'pages/cart.html',{'product': cart,'name': name})
        return render(request, 'pages/product.html')
    else:
        return render(request, 'pages/product.html')


def getAdmin(request):
    name =  request.session['name']
    product = Product.objects.all()
    if request.method == 'POST':
        idU = request.POST.get('data')
        idD = request.POST.get('dataD')
        if(idD!=None):
            product = get_object_or_404(Product, pk=idD)
            product.delete()
            return redirect('/admins')
        productById = Product.objects.get(id=idU)
        return render(request, 'pages/add.html', {'product': productById,'name': name})
    return render(request, 'pages/admin.html', {'product': product,'name': name})

def getAdd(request):
    name =  request.session['name']
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
    return render(request, 'pages/add.html', {'form': form, 'name': name})


def getCart(request):
    name =  request.session['name']
    idUser =  request.session['user_id']
    cart = Cart.objects.filter(userid=idUser)
    if request.method == 'POST':
        id = request.POST.get('dataId')
        if(id !=None):
            cart = get_object_or_404(Cart, pk=id)
            cart.delete()
            return redirect('/cart')
        status = request.POST.get('data')
        if(status != "all"):
            cart = Cart.objects.filter( transport= status,userid=idUser)
            return render(request, 'pages/cart.html',{'product': cart, 'name': name})
    return render(request, 'pages/cart.html',{'product': cart, 'name': name})

def createUser(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = UserForm()
    return render(request, 'pages/register.html', {'form': form})


