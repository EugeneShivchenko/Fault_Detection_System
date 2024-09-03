"""
Конфигурация WSGI для проекта Detection_system.

Она представляет вызываемый WSGI как переменную уровня модуля с именем ``application``.

Для получения дополнительной информации об этом файле см.
https://docs.djangoproject.com/en/4.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Detection_system.settings')

application = get_wsgi_application()
