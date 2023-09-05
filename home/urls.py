from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.getHome, name='home'),
    path('product/', views.getProduct, name='product'),
    path('ad/', views.getAdmin, name='admin'),
    path('manage/', views.getManage, name='manage'),
    path('', views.getLogin, name ='login'),
    path('register/', views.createUser, name='register'),
]
  