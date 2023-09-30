import django_heroku

from backend.settings_common import *

DEBUG = False

# To be modified for safety
ALLOWED_HOSTS = ['*']

CORS_ALLOWED_ORIGINS = []

django_heroku.settings(locals())