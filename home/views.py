from django.shortcuts import render, redirect
from django.views.generic import ListView
from .models import Product

# Create your views here.
def index (request):
    return render(request, 'pages/home.html')


class ListProduct(ListView):
  model = Product
  def get (self, request, *args, **kwargs):
    home = 'home/templates/pages/home.html' 
    obj = {
      'product': Product.objects.all()
    }
    return render(request, home, obj)