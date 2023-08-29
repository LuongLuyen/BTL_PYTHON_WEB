from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index (request):
    res = HttpResponse()
    res.writelines("<h1> Page Home </h1>")
    res.write("App home")
    return res