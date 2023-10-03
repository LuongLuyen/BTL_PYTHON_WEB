from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.getHome, name='home'),
    path('add/', views.getAdd, name='add'),
    path('product/', views.getProduct, name='product'),
    path('admins/', views.getAdmin, name='admins'),
    path('manage/', views.getManage, name='manage'),
    path('', views.getLogin, name ='login'),
    path('register/', views.createUser, name='register'),
]
  