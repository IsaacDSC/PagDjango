from django.shortcuts import render, redirect
from .models import (Product, Client, Contact_Us)
from .forms import (ProductForm, RegisterClient, Contact_Us_form)

def home(req):
    products = Product.objects.all()
    return render(req, 'home.html', {'products': products})


def insert_products(req):
    form = ProductForm(req.POST or None)

    if form.is_valid():
        form.save()
        return redirect('home')

    else:
        return render(req, 'products_form.html', {'form': form})


def admProducts(req):
    products = Product.objects.all()
    return render(req, 'edit.html', {'products': products})


def searchEdit(req):
    print(req.POST['id'])
    product = Product.objects.filter(id=req.POST['id'])
    return render(req, 'formEditing.html', {'product': product[0]})


def editing(req):
    product = Product.objects.get(id=req.POST['id'])
    form = ProductForm(req.POST or None, instance = product)

    if form.is_valid():
        form.save()
        return redirect('home')
        # print(req.GET)
        # #print(product[0].name)


def upload(req):
    return render(req, 'formUpload.html')


def contact_us(req):
    if req.method == 'GET':
        form = Contact_Us_form
        return render(req, 'contact.html', {'form': form})
    if req.method == 'POST':
        form = Contact_Us_form(req.POST or None)
        if form.is_valid():
            form.save()
            return redirect('home')


def list_contact_us(req):
    contact = Contact_Us.objects.all()
    print(contact)
    return render(req, 'listContact.html', {'contacts': contact})

# def login(req):
#     return render(req, 'account/login.html')

# def register(req):
#     if req.method == 'POST':
#         form = RegisterClient(req.POST or None)
#         pwd = req.POST['password']

#         # if form.is_valid():
#         #     form.save()
#         # return redirect('home')

#     form = RegisterClient()
#     return render(req, 'register.html', {'form': form})