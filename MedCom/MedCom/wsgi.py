"""
WSGI config for MedCom project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'MedCom.settings')

application = get_wsgi_application()


def handler(request, **kwargs):
    return app(request, **kwargs)