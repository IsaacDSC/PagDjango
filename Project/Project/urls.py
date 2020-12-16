from django.contrib import admin
from django.urls import include, path
from CRUD_App.views import (
    home,
    insert_products,
    admProducts,
    editing,
    searchEdit,
    upload,
    contact_us,
    list_contact_us,
    register,
    # login,
    # register,
    )


urlpatterns = [
    path('admin/', admin.site.urls, name = 'admin'),
    path('accounts/', include('allauth.urls'), name = 'accounts'),
    path('',  home, name = 'home'),
    path('insert/', insert_products, name = 'insert_products'),
    path('edit/', admProducts, name = 'admEdit'),
    path('searchEdit/', searchEdit, name = 'searchEdit'),
    path('editing/', editing, name = 'editing'),
    path('upload/', upload, name = 'upload'),
    path('contact/', contact_us, name = 'contact'),
    path('contacts/', list_contact_us, name = 'list_contacts'),
    path('accounts/signup/', register, name = 'signup')
]

#accounts/signup/
#{% url 'account_logout' %} sair
#{% url 'account_login' %}  login
#{% url 'account_signup' %} register URL = /accounts/signup/