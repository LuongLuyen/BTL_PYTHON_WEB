from django.db import models

# Create your models here.
from django.db import models

class Product(models.Model):
  userid = models.IntegerField(default=0)
  thumbnail = models.CharField(max_length=255)
  shortDescription = models.CharField(max_length=100)
  status = models.CharField(max_length=50)
  category = models.CharField(max_length=50)
  price = models.CharField(max_length=50)
  
  def __str__(self):
    return self.userid
  
class Cart(models.Model):
  userid = models.IntegerField(default=0)
  thumbnail = models.CharField(max_length=255)
  shortDescription = models.CharField(max_length=100)
  transport = models.CharField(max_length=50)
  color = models.CharField(max_length=50)
  category = models.CharField(max_length=50)
  price = models.CharField(max_length=50)
  
class User(models.Model):
  userName = models.CharField(max_length=50)
  password = models.CharField(max_length=50)
  email = models.CharField(max_length=50)
  role = models.CharField(max_length=50)
  
  def __str__(self):
    return self.userName