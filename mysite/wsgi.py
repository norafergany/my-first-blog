"""
WSGI config for mysite project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")

application = get_wsgi_application()
<<<<<<< HEAD
=======

<<<<<<< HEAD
=======
from whitenoise.django import DjangoWhiteNoise
application = DjangoWhiteNoise(application)
>>>>>>> b80c38aa3ef5f6261a9557973cb5f5f33a9ab464
>>>>>>> 58708d094c0bc6ed99b4c9b38c43ff1954610752
