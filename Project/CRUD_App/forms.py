from django import forms
from .models import (Product, Client, Contact_Us)

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'price', 'quantity']

class RegisterClient(forms.ModelForm):
        class Meta:
            model = Client
            fields = ['name', 'telephone', 'email', 'password']


class Contact_Us_form(forms.ModelForm):
    class Meta:
        model = Contact_Us
        fields = ['name', 'telephone', 'email', 'subject', 'message']