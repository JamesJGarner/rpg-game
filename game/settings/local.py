from .production import INSTALLED_APPS


INSTALLED_APPS = INSTALLED_APPS + (
    'django_extensions',
)

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'game',
        'USER': 'rpg-game',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
    }
}

DEBUG = True
TEMPLATE_DEBUG = DEBUG
