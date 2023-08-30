from django.shortcuts import render
from .models import Product

def get(request):
    product = Product.objects.all()
    return render(request, 'pages/home.html', {'product': product})
