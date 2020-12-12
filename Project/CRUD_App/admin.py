from django.contrib import admin
from .models import (Product, Client)

MODELOS = [Product, Client]

# admin.site.register(Product)
# admin.site.register(Client)

for MODELO in MODELOS:
    admin.site.register(MODELO)