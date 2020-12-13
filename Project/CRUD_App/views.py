from django.shortcuts import render, redirect
from .models import (Product, Client)
from .forms import (ProductForm, RegisterClient)

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


def login(req):
    return render(req, 'registration/login.html')

def register(req):
    if req.method == 'POST':
        form = RegisterClient(req.POST or None)
        pwd = req.POST['password']

        # if form.is_valid():
        #     form.save()
        # return redirect('home')

    form = RegisterClient()
    return render(req, 'register.html', {'form': form})