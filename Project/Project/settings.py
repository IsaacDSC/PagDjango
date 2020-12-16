import os
import sys
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '-^*a*p8ct19yz=%2t8cjb7qdwq(xt1iur+l43^qt4p(m54s2g='

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    # django apps
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'CRUD_App',
    'bootstrapform',
    # 3rd allauth party
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'crispy_forms',

]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    # django-login-required-middleware
    # 'login_required.middleware.LoginRequiredMiddleware',
    # 'django.contrib.auth.middleware.AuthenticationMiddleware',
]

ROOT_URLCONF = 'Project.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'Project.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
        # 'ENGINE': 'django.db.backends.mysql',
        # 'NAME': 'django',
        # 'USER': 'dev',
        # 'PASSWORD': 'secret',
        # 'HOST': 'localhost',
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'pt-br'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_URL = '/static/'

# Additional locations of static files
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, '/templates/')
]
# print(BASE_DIR)
# print(STATICFILES_DIRS)


#LOGOUT_REDIRECT_URL = '/accounts/login'

AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
]

SITE_ID = 1

LOGIN_REDIRECT_URL = '/'

# Savar a Sessão por DEFAULT
#ACCOUNT_SESSION_REMEMBER = True

# Verifica se o EMAIL existe ou não ENVIANDO COD de confirmação
EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"
# Só precisa digitar a senha uma vez
ACCOUNT_SIGNUP_PASSWORD_ENTER_TWICE = False
# Não precisa de username
ACCOUNT_USERNAME_REQUIRED = True
# Método de autenticação: email
ACCOUNT_AUTHENTICATION_METHOD = "email"
# Email obrigatório
ACCOUNT_EMAIL_REQUIRED = True
# Email único
ACCOUNT_UNIQUE_EMAIL = True


# django cruspy_forms
CRISPY_TEMPLATE_PACK = 'bootstrap4'

LOGIN_REQUIRED_IGNORE_VIEW_NAMES = [
    'home',
    'login',
    'contact',
    'admin',
    'admin:index',
    'admin:login',
    'accounts',
]

LOGIN_REQUIRED_IGNORE_VIEW_URL = [
    'accounts/signup/,'

]
# LOGIN_REQUIRED_IGNORE_PATHS = [
#     r'/accounts/logout/$'
#     r'/accounts/signup/$',
#     r'/admin/$',
#     r'/admin/login/$',
#     r'/about/$'
#     r'/account_signup/$'
# ]
