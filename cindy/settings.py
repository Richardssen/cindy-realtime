"""
Django settings for cindy project.

Generated by 'django-admin startproject' using Django 1.11.5.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

import os

from django.utils.translation import ugettext_lazy as _

from .security import *

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

ALLOWED_HOSTS = [
    'localhost',
    '127.0.0.1',
] + HOSTS

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'graphene_django',
    'sui_hei',
] # yapf: disable

if ENABLE_OPEN:
    INSTALLED_APPS += ['open']

INSTALLED_APPS += [
    "channels",
    "webpack_loader",
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    #'sui_hei.middleware.GraphQLLocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'cindy.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'cindy.wsgi.application'

# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
    'default': POSTGREDB_SETTINGS,
}

# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME':
        'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME':
        'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME':
        'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME':
        'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Internationalization
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'ja-jp'

TIME_ZONE = 'Japan'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

STATIC_URL = "/static/"
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "sui_hei/static"),
]
if os.environ.get('DJANGO_BUILD_ENV') == 'PRODPUSH':
    STATICFILES_DIRS += [
        os.path.join(BASE_DIR, "react-boilerplate/pushbundle"),
    ]
else:
    STATICFILES_DIRS += [
        os.path.join(BASE_DIR, "react-boilerplate/build"),
    ]
STATIC_ROOT = os.path.join(BASE_DIR, "collected_static")

# Don't append `_id` to foreign keys
FK_AUTO_ID = ''

# Locale path

LOCALE_PATHS = [
    os.path.join(BASE_DIR, 'locale'),
]

LANGUAGES = [
    ('ja', _('Japanese')),
]

# Authentiation
AUTH_USER_MODEL = 'sui_hei.User'
LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/'
LOGIN_URL = '/'
APPEND_SLASH = False

# Webpack Loader
if DEBUG:
    DLL_STATS_FILE = os.path.join(
        BASE_DIR, "./react-boilerplate/build/webpack-stats.dll.json")
    DEFAULT_STATS_FILE = os.path.join(
        BASE_DIR, "react-boilerplate/build/webpack-stats.json")
else:
    DLL_STATS_FILE = os.path.join(BASE_DIR,
                                  "collected_static/webpack-stats.dll.json")
    DEFAULT_STATS_FILE = os.path.join(BASE_DIR,
                                      "collected_static/webpack-stats.json")

WEBPACK_LOADER = {
    "DLL": {
        "BUNDLE_DIR_NAME": "",
        "STATS_FILE": DLL_STATS_FILE
    },
    "DEFAULT": {
        "BUNDLE_DIR_NAME": "",
        "STATS_FILE": DEFAULT_STATS_FILE
    }
} # yapf: disable

# Graphene Settings
GRAPHENE = {
    'SCHEMA': 'schema.schema',
    'SCHEMA_OUTPUT': 'react-boilerplate/schema.json'
}

CHANNELS_WS_PROTOCOLS = [
    "graphql-ws",
]

ASGI_APPLICATION = "sui_hei.routing.application"
