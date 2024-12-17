from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME':   'demo_to_do_list',
        'USER':'postgres',
        'PASSWORD':'root',
        'HOST':'localhost',
        'PORT':'5432',
    }
}