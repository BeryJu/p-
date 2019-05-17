"""
Django settings for p2 project.

Generated by 'django-admin startproject' using Django 1.11.1.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

import datetime
import logging
import os
import sys

from sentry_sdk import init as sentry_init
from sentry_sdk.integrations.celery import CeleryIntegration
from sentry_sdk.integrations.django import DjangoIntegration

from p2 import __version__
from p2.lib.config import CONFIG
from p2.lib.sentry import before_send

LOGGER = logging.getLogger(__name__)


SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = CONFIG.get('secret_key',
                        '48e9z8tw=_z0e#m*x70&)u%cgo8#=16uzdze&i8q=*#**)@cp&')  # noqa Debug

DEBUG = CONFIG.get('debug')
CORS_ORIGIN_ALLOW_ALL = DEBUG

ALLOWED_HOSTS = ['*']

INTERNAL_IPS = ['127.0.0.1']

# API -JWT Configurations
JWT_AUTH = {
    'JWT_ALLOW_REFRESH': True,
    'JWT_EXPIRATION_DELTA': datetime.timedelta(seconds=300),
    'JWT_REFRESH_EXPIRATION_DELTA': datetime.timedelta(days=7),
}

# API - Swagger
SWAGGER_SETTINGS = {
    'DEFAULT_INFO': 'p2.api.urls.INFO',
    'SECURITY_DEFINITIONS': {
        'JWT': {
            'type': 'apiKey',
            'name': 'Authorization',
            'in': 'header'
        }
    }
}

# API - REST
REST_FRAMEWORK = {
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.LimitOffsetPagination',
    'PAGE_SIZE': 100,
    'DEFAULT_FILTER_BACKENDS': [
        'rest_framework_guardian.filters.DjangoObjectPermissionsFilter',
        'django_filters.rest_framework.DjangoFilterBackend',
        'rest_framework.filters.OrderingFilter',
        'rest_framework.filters.SearchFilter',
    ],
    'DEFAULT_PERMISSION_CLASSES': (
        'p2.api.permissions.CustomObjectPermissions',
    ),
    # 'DEFAULT_AUTHENTICATION_CLASSES': (
    #     'rest_framework_jwt.authentication.JSONWebTokenAuthentication',
    # ),
}


# Allauth settings
ACCOUNT_ADAPTER = 'p2.root.accounts.NoNewUsersAccountAdapter'
AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
    'guardian.backends.ObjectPermissionBackend',
]
ACCOUNT_EMAIL_VERIFICATION = 'none'

# Redis settings
CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://%s" % CONFIG.get('redis'),
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        }
    }
}
DJANGO_REDIS_IGNORE_EXCEPTIONS = True
DJANGO_REDIS_LOG_IGNORED_EXCEPTIONS = True
SESSION_CACHE_ALIAS = "default"

# Celery settings
# Add a 10 minute timeout to all Celery tasks.
CELERY_TASK_SOFT_TIME_LIMIT = 600
CELERY_BEAT_SCHEDULE = {}
CELERY_CREATE_MISSING_QUEUES = True
CELERY_TASK_DEFAULT_QUEUE = 'p2'
CELERY_BROKER_URL = 'amqp://%s' % CONFIG.get('rabbitmq')
CELERY_RESULT_BACKEND = 'rpc://'
CELERY_IMPORTS = (
    'p2.core.tasks',
    'p2.log.tasks',
)

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'django.contrib.postgres',
    'guardian',
    # Authentication
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth_passbook',
    # p2 - Core Components
    'p2.core.apps.P2CoreConfig',
    'p2.api.apps.P2APIConfig',
    'p2.s3.apps.P2S3Config',
    'p2.serve.apps.P2ServeConfig',
    'p2.log.apps.P2LogConfig',
    'p2.ui.apps.P2UIConfig',
    # p2 - Components
    'p2.components.quota.apps.P2QuotaComponentConfig',
    'p2.components.image.apps.P2ImageComponentConfig',
    'p2.components.public_access.apps.P2PublicAccessComponentConfig',
    # p2 - Storage
    'p2.storage.local.apps.P2LocalStorageConfig',
    # API Frameworks
    'rest_framework',
    'drf_yasg',
    'django_filters',
    # UI Helpers
    'crispy_forms',
]

LOGIN_URL = 'account_login'
LOGIN_REDIRECT_URL = 'p2_ui:index'

CRISPY_TEMPLATE_PACK = 'bootstrap4'

MIDDLEWARE = [
    'p2.core.middleware.HealthCheckMiddleware',
    'p2.log.middleware.StartRequestMiddleware',
    'p2.s3.middleware.S3RoutingMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'p2.log.middleware.EndRequestMiddleware',
]

ROOT_URLCONF = 'p2.root.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'p2/ui/templates/'),
            # os.path.join(BASE_DIR, 'p2/templates')
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'p2.ui.context_processors.version',
            ],
        },
    },
]

VERSION = __version__

WSGI_APPLICATION = 'p2.root.wsgi.application'

DATA_UPLOAD_MAX_MEMORY_SIZE = 536870912

# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {}
for db_alias, db_config in CONFIG.get('databases').items():
    DATABASES[db_alias] = {
        'ENGINE': db_config.get('engine'),
        'HOST': db_config.get('host'),
        'NAME': db_config.get('name'),
        'USER': db_config.get('user'),
        'PASSWORD': db_config.get('password'),
        'OPTIONS': db_config.get('options', {}),
    }

# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True
SITE_ID = 1

# Sentry integration

if not DEBUG:
    sentry_init(
        dsn="https://9041d56f69bd496ea4edfa6420eac665@sentry.services.beryju.org/9",
        integrations=[
            DjangoIntegration(transaction_style="function_name"),
            CeleryIntegration(),
        ],
        before_send=before_send,
        release='p2@%s' % __version__
    )


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

STATIC_URL = '/static/'

with CONFIG.cd('log'):
    LOGGING_HANDLER_MAP = {
        'p2': 'DEBUG',
        'allauth': 'DEBUG',
        'cherrypy': 'DEBUG',
        'django': 'INFO',
        'celery': 'WARNING',
        'botocore': 'DEBUG',
        'werkzeug': 'DEBUG',
    }
    LOGGING = {
        'version': 1,
        'disable_existing_loggers': True,
        'formatters': {
            'default': {
                'format': ('%(asctime)s %(levelname)-8s %(name)-55s '
                           '%(funcName)-20s %(message)s'),
            },
            'colored': {
                '()': 'colorlog.ColoredFormatter',
                'format': ('%(log_color)s%(asctime)s %(levelname)-8s %(name)-55s '
                           '%(funcName)-20s %(message)s'),
            }
        },
        'handlers': {
            'console': {
                'level': 'DEBUG',
                'class': 'logging.StreamHandler',
                'formatter': 'colored',
            },
        },
        'loggers': {
        }
    }
    for handler_name, level in LOGGING_HANDLER_MAP.items():
        LOGGING['loggers'][handler_name] = {
            'handlers': ['console'],
            'level': level,
            'propagate': True,
        }


TEST = any('test' in arg for arg in sys.argv)
TEST_RUNNER = 'xmlrunner.extra.djangotestrunner.XMLTestRunner'
TEST_OUTPUT_VERBOSE = 2

TEST_OUTPUT_FILE_NAME = 'unittest.xml'

STATIC_ROOT = os.path.join(BASE_DIR, 'static/')

if TEST:
    LOGGING = {
        'version': 1,
        'disable_existing_loggers': True,
    }
    CELERY_TASK_ALWAYS_EAGER = True

if DEBUG is True:
    INSTALLED_APPS += [
        'debug_toolbar',
        'django_extensions',
    ]
    MIDDLEWARE.append('debug_toolbar.middleware.DebugToolbarMiddleware')
