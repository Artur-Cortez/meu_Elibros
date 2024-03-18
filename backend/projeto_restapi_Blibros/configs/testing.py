from .configs_base import *
import os 
SECRET_KEY = 'django-insecure-lp42(2m*&&u*cxqm=%26dfp@b*_*rg81$(%*kak%)141qaaq6+'

DEBUG = True

DATABASES = {
    'default':{
    'ENGINE':'django.db.backends.sqlite3',
    'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

ALLOWED_HOSTS = ['localhost', '127.0.0.1']