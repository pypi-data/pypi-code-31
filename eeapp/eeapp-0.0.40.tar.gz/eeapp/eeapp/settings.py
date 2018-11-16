"""
Django settings for eeapp project.

Generated by 'django-admin startproject' using Django 1.8.16.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '6*j6renk936%&xmir+^o&5e*v$i1^_3x7aifbg+!i7273t(wak'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition
# pip install django-cors-headers

# CORS_ORIGIN_WHITELIST = ()  # 或者定义允许的匹配路径正则表达式.
#
# CORS_ORIGIN_REGEX_WHITELIST = ()
#
# CORS_ALLOW_METHODS = (
# 'GET',
# 'POST',
# 'PUT',
# 'PATCH',
# 'DELETE',
# 'OPTIONS'
# )
# CORS_ALLOW_HEADERS = (
# 'x-requested-with',
# 'content-type',
# 'accept',
# 'origin',
# 'authorization',
# 'x-csrftoken'
# )
INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'location',
    'base',
    'rest_framework',
    'rest_framework.authtoken',
    # 'corsheaders',
)

MIDDLEWARE_CLASSES = (
    # 'corsheaders.middleware.CorsMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
)

ROOT_URLCONF = 'eeapp.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'eeapp.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

DATABASE_ROUTERS = ['tools.datasrouter.DatabaseAppsRouter']
DATABASE_APPS_MAPPING = {
    'location': 'location',
}



DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    },
    'location': {
        'NAME': 'location',
        'ENGINE': 'django.db.backends.mysql',
        'USER': 'tong',
        'PASSWORD': 'ZHUye1122',
        'HOST': '120.25.81.176',
        'PORT': '3306',
    },
}


# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

MEDIA_HOST = 'http://0.0.0.0:8000'

STATIC_URL = '/static/'

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

REST_FRAMEWORK = {
    'EXCEPTION_HANDLER':'rest.exception.custom_exception_handler',
    'DEFAULT_AUTHENTICATION_CLASSES': (
        # 'base.api.authentication.SellerTokenAuthentication',
        'rest_framework.authentication.BasicAuthentication',
        'rest_framework.authentication.SessionAuthentication',
        ),
    'DEFAULT_RENDERER_CLASSES':(
        'rest.response.ApiJSONRenderer',
        'rest_framework.renderers.BrowsableAPIRenderer',
    ),
    'DEFAULT_PAGINATION_CLASS': 'jsonapi.response.ListPagination',
    'PAGE_SIZE': 10,
}


#
# REST_FRAMEWORK = {
#     'EXCEPTION_HANDLER':'jsonapi.exception.custom_exception_handler',
#     'DEFAULT_AUTHENTICATION_CLASSES': (
#         # 'base.api.authentication.SellerTokenAuthentication',
#         'rest_framework.authentication.BasicAuthentication',
#         'rest_framework.authentication.SessionAuthentication',
#         ),
#     'DEFAULT_RENDERER_CLASSES':(
#         'jsonapi.response.ApiJSONRenderer',
#         'rest_framework.renderers.BrowsableAPIRenderer',
#     ),
#     'DEFAULT_PAGINATION_CLASS': 'jsonapi.response.ListPagination',
#     'PAGE_SIZE': 10,
# }
