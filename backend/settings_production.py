import os

import django_heroku
import dj_database_url

from backend.settings_common import *  # noqa: F401,F403

DEBUG = False

# Necessary to make React front-end work with Django
CORS_ALLOWED_ORIGINS = [
    'http://localhost:8000',
]

DATABASES = {
    "default": dj_database_url.parse(os.environ.get('DATABASE_URL')),
}

django_heroku.settings(locals())
