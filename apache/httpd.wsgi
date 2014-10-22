import os
import sys

sys.path.append('/home/dmitry/projects/it_book')
os.environ['DJANGO_SETTINGS_MODULE'] = 'it_book.settings'
import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()
