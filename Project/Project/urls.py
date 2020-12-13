from django.contrib import admin
from django.urls import include, path
from CRUD_App.views import (
    home,
    insert_products,
    admProducts,
    editing,
    searchEdit,
    upload,
    Contact_Us,
    # login,
    # register,
    )


urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('', home, name = 'home'),
    path('insert/', insert_products, name = 'insert_products'),
    path('edit/', admProducts, name = 'admEdit'),
    path('searchEdit/', searchEdit, name = 'searchEdit'),
    path('editing/', editing, name = 'editing'),
    path('upload/', upload, name = 'upload'),
    path('contact/', Contact_Us, name = 'contact')
]

#accounts/signup/
#{% url 'account_logout' %} sair
#{% url 'account_login' %}  login
#{% url 'account_signup' %} register