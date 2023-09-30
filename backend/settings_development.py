from backend.settings_common import *  # noqa: F401,F403

DEBUG = True

# Necessary to make React front-end work with Django
CORS_ALLOWED_ORIGINS = [
    'http://localhost:8000',
    'http://localhost:3000',
]
