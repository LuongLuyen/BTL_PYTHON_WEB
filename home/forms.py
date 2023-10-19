from django import forms
from .models import Product
from .models import User

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['thumbnail', 'shortDescription', 'status','category','price']


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['userName', 'password', 'email','role']