"""
WSGI config for config project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/wsgi/
"""


import os
import sys
import traceback

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

try:
	from django.core.wsgi import get_wsgi_application
	application = get_wsgi_application()
except Exception as e:
	print('WSGI import error:', e, file=sys.stderr)
	traceback.print_exc()
	raise
