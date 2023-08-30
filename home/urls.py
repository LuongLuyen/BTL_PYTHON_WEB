from django.urls import path, re_path
from django.contrib import admin
from . import views
from home.views import (
  ListProduct,
)

urlpatterns = [
    path('', views.index),
    re_path(r'^product/$', ListProduct.as_view(), name='product'),
]
  