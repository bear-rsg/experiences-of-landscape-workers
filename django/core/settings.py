import os
import sys

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATE_DIR = os.path.join(BASE_DIR, 'core/templates')
PWA_SERVICE_WORKER_PATH = os.path.join(BASE_DIR, 'core/static/js', 'serviceworker.js')

# Application definition

INSTALLED_APPS = [
    # Default Django apps
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.humanize',
    # 3rd party apps
    'rest_framework',
    'pwa',
    # Custom apps
    'accounts',
    'general',
    'journal',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'core.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [TEMPLATE_DIR],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'core.wsgi.application'


# PWA

PWA_APP_NAME = 'Landscape Workers'
PWA_APP_DESCRIPTION = "Experiences of Landscape Workers"
PWA_APP_THEME_COLOR = '#000000'
PWA_APP_BACKGROUND_COLOR = '#ffffff'
PWA_APP_DISPLAY = 'standalone'
PWA_APP_SCOPE = '/'
PWA_APP_ORIENTATION = 'any'
PWA_APP_START_URL = '/'
PWA_APP_STATUS_BAR_COLOR = 'default'
PWA_APP_ICONS = [
    {
        'src': '/static/images/pwa/icon-48.png',
        'sizes': '48x48'
    },
    {
        'src': '/static/images/pwa/icon-72.png',
        'sizes': '72x72'
    },
    {
        'src': '/static/images/pwa/icon-96.png',
        'sizes': '96x96'
    },
    {
        'src': '/static/images/pwa/icon-128.png',
        'sizes': '128x128'
    },
    {
        'src': '/static/images/pwa/icon-144.png',
        'sizes': '144x144'
    },
    {
        'src': '/static/images/pwa/icon-152.png',
        'sizes': '152x152'
    },
    {
        'src': '/static/images/pwa/icon-167.png',
        'sizes': '167x167'
    },
    {
        'src': '/static/images/pwa/icon-180.png',
        'sizes': '180x180'
    },
    {
        'src': '/static/images/pwa/icon-192.png',
        'sizes': '192x192'
    },
    {
        'src': '/static/images/pwa/icon-256.png',
        'sizes': '256x256'
    },
    {
        'src': '/static/images/pwa/icon-512.png',
        'sizes': '512x512'
    },
    {
        'src': '/static/images/pwa/icon-1024.png',
        'sizes': '1024x1024'
    }
]
PWA_APP_ICONS_APPLE = [
    {
        'src': '/static/images/pwa/icon-256.png',
        'sizes': '256x256'
    }
]
PWA_APP_SPLASH_SCREEN = [
    {
        'src': '/static/images/pwa/icon-1024.png',
        'media': '(device-width: 320px) and (device-height: 568px) and (-webkit-device-pixel-ratio: 2)'
    }
]
PWA_APP_DIR = 'ltr'
PWA_APP_LANG = 'en-US'


# Password validation

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization

LANGUAGE_CODE = 'en-gb'

TIME_ZONE = 'Europe/London'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
STATICFILES_DIRS = [os.path.join(BASE_DIR, "core/static")]
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, "static/")

# Media files (user uploaded content)
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# Default primary key field type
# https://docs.djangoproject.com/en/latest/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Authentication URLs
LOGIN_REDIRECT_URL = '/journal/'
LOGOUT_REDIRECT_URL = '/'

# Custom user model
AUTH_USER_MODEL = 'accounts.CustomUser'

# Import local_settings.py
SECRET_KEY = None
try:
    from .local_settings import *  # NOQA
except ImportError:
    sys.exit('Unable to import local_settings.py (refer to local_settings.example.py for help)')

# Ensure the SECRET_KEY is supplied in local_settings.py - and trust that the other settings are there too.
if not SECRET_KEY:  # NOQA
    sys.exit('Missing SECRET_KEY in local_settings.py')
