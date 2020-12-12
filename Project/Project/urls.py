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
    path('accounts/login/', login, name = 'login'),

]
