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
    python3 manage.py startapp blog

Register App creted in Settings.py in to Array INSTALLED_APPS
    'blog',

Creating Class defined for Migrations in db
    python3 manage.py makemigrations


