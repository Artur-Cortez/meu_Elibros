import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'projeto_restapi_Blibros.configs.desenvolvimento')

application = get_wsgi_application()
