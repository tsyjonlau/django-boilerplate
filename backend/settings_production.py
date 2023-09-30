import django_heroku
import dj_database_url

from backend.settings_common import *  # noqa: F401,F403

DEBUG = False

# To be modified for safety
ALLOWED_HOSTS = ['*']

DATABASES = {
	"default": dj_database_url.parse(os.environ.get('DATABASE_URL'))
}

CORS_ALLOWED_ORIGINS = []

django_heroku.settings(locals())
