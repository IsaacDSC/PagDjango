# PagDjango

Criar Virtual ENV
    python3 -m venv myEnv

Ativar Virtual ENV
    source myEnv/bin/activate

Install django
    python3 -m pip install Django

Created to project init
    django-admin startproject WebPage

Created migrations in db
#access in folder project
    python3 manage.py migrate
    {db created in class}

Created superUser access Admin router
    python3 manage.py createsuperuser
#insert  datas superUser

Start Run Server
    python3 manage.py runserver

Creating  primary model app
    python3 manage.py startapp 'nameApp'

Register App creted in Settings.py in to Array INSTALLED_APPS
    'nome do App',

Creating Class defined for Migrations in db
    python3 manage.py makemigrations

dependencies for using bootrap form django
    #pip install django-bootstrap-form
    #include INSTALLED_APPS = ['bootstrapform',]

denpendecies login/register/logout from django
    #pip install django-crispy-forms
    #include INSTALLED_APPS = ['cruspy_forms',]


add django-login-required-middleware
    #pip install django-login-required-middleware
    documnentation: https://pypi.org/project/django-login-required-middleware/