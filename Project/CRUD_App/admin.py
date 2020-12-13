from django.contrib import admin
from .models import (Product, Client, Contact_Us)

MODELOS = [Product, Client, Contact_Us]

# admin.site.register(Product)
# admin.site.register(Client)

for MODELO in MODELOS:
    admin.site.register(MODELO)