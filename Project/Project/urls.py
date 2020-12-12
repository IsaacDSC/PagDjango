"""Project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from CRUD_App.views import (home, insert_products, admProducts, editing, searchEdit, upload, login)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name = 'home'),
    path('insert/', insert_products, name = 'insert_products'),
    path('edit/', admProducts, name = 'admEdit'),
    path('searchEdit/', searchEdit, name = 'searchEdit'),
    path('editing/', editing, name = 'editing'),
    path('upload/', upload, name = 'upload'),
    path('login/', login, name = 'login'),

]