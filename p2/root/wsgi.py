"""
WSGI config for p2 project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "p2.core.settings")

# Import django settings after setting DJANGO_SETTINGS_MODULE
# pylint: disable=wrong-import-position, ungrouped-imports
# from django.conf import settings # noaq isort:skip

# # pylint: disable=invalid-name
# application = None
# if settings.ERROR_REPORT_ENABLED:
#     application = Sentry(get_wsgi_application())
# else:
application = get_wsgi_application()
