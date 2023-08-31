from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.getHome),
    path('product/', views.getProduct),
    path('ad/', views.getAdmin),
    path('manage/', views.getManage),
    path('', views.getLogin),
]
  