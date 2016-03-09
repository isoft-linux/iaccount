"""
WSGI config for iaccount project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.9/howto/deployment/wsgi/
"""

import os, sys

from django.core.wsgi import get_wsgi_application

PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
PROJECT_NAME = os.path.basename(os.path.dirname(os.path.realpath(__file__)))

sys.path.insert(0, PROJECT_ROOT)
for i in ("apps", "modules"):
    path_dir = os.path.join(PROJECT_ROOT, i)
    if os.path.isdir(path_dir):
        sys.path.insert(0, path_dir)
sys.path.insert(0, os.path.join(PROJECT_ROOT, PROJECT_NAME))

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings")

# This application object is used by any WSGI server configured to use this
# file. This includes Django's development server, if the WSGI_APPLICATION
# setting points here.
application = get_wsgi_application()

