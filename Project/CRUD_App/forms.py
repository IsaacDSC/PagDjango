from django import forms
from .models import (Product, Client)

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'price', 'quantity']

class RegisterClient(forms.ModelForm):
        class Meta:
            model = Client
            fields = ['name', 'telephone', 'email', 'password']