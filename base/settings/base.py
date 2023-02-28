
import mimetypes
import os
from ast import literal_eval
from pathlib import Path

from decouple import config

from .logging import *

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent.parent.parent

SECRET_KEY = config("SECRET_KEY")

DEBUG = config("DEBUG", cast=bool)
APPEND_SLASH = config("ADD_SLASH", cast=bool)
ALLOWED_HOSTS = literal_eval(config("ALLOWED_HOSTS"))

DJANGO_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    "django.contrib.sites",
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

THIRD_PARTY_APPS = [
    "whitenoise",
    "rest_framework",
    "django_filters",
    "corsheaders"
]

CUSTOM_APPS = [
]


INSTALLED_APPS = DJANGO_APPS+THIRD_PARTY_APPS+CUSTOM_APPS

MIDDLEWARE = [
    "corsheaders.middleware.CorsMiddleware",
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'base.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, "templates")],
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

WSGI_APPLICATION = 'base.wsgi.application'


# AUTHENTICATION_BACKENDS = [
#     'django.contrib.auth.backends.ModelBackend',
#     'allauth.account.auth_backends.AuthenticationBackend',
# ]
# AUTH_USER_MODEL = "accounts.User"

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


LANGUAGE_CODE = 'en-us'

TIME_ZONE = config("TIMEZONE")

USE_I18N = True

USE_L10N = True

USE_TZ = True

STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static")
]


mimetypes.add_type("text/css", ".css", True)
mimetypes.add_type("js/application", ".js", True)
mimetypes.add_type("script", ".js", True)


WHITENOISE_MIMETYPES = {".js": "application/javascript", ".css": "text/css"}

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


if DEBUG:
    from .dev import *
else:
    from .prod import *


CORS_ALLOWED_ORIGINS = [
    "https://stable.candybitsocial.com"

]
if DEBUG:
    CORS_ALLOWED_ORIGINS = CORS_ALLOWED_ORIGINS+["http://localhost:3000",
                                                 "http://127.0.0.1:3000",
                                                 "http://127.0.0.1:8000",
                                                 "http://localhost:8000"]
# CORS_ORIGIN_ALLOW_ALL = True
CORS_ALLOW_CREDENTIALS = True
# Cookies
# CSRF_COOKIE_NAME = 'XSRF-TOKEN'
# CSRF_HEADER_NAME = 'HTTP_X_XSRF_TOKEN'

# Session
if not DEBUG:
    SESSION_COOKIE_DOMAIN = "stable.candybitsocial.com"
    SESSION_COOKIE_SAMESITE = "None"
    SESSION_COOKIE_SECURE = True


# LOGIN_URL = "accounts/login"
# LOGIN_REDIRECT = "candybit_gpt"
# Allauth configurations
# SOCIALACCOUNT_LOGIN_ON_GET = True
# ACCOUNT_USERNAME_REQUIRED = False
# ACCOUNT_AUTHENTICATION_METHOD = "email"
# SITE_ID = 1
# ACCOUNT_EMAIL_VERIFICATION = False
# LOGIN_REDIRECT_URL = "/candy_bit_gpt"
# ACCOUNT_LOGOUT_ON_GET = True
# SITE_ID = 1
# SOCIALACCOUNT_AUTO_SIGNUP = True
# ACCOUNT_EMAIL_REQUIRED = True
# SOCIALACCOUNT_ADAPTER = "base.adapters.OrganizationSocialAccountAdapter"

# SOCIALACCOUNT_PROVIDERS = {
#     'google': {
#         'SCOPE': [
#             'profile',
#             'email',
#         ],
#         'AUTH_PARAMS': {
#             'access_type': 'online',
#         },
#         'OAUTH_PKCE_ENABLED': True,
#     }
# }


REST_FRAMEWORK = {
    'DEFAULT_FILTER_BACKENDS': ['django_filters.rest_framework.DjangoFilterBackend', 'rest_framework.filters.SearchFilter'],
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.SessionAuthentication',
    ],

}


if not DEBUG:
    REST_FRAMEWORK['DEFAULT_PERMISSION_CLASSES'] = [
        'rest_framework.permissions.IsAuthenticated',
    ]
    REST_FRAMEWORK['DEFAULT_RENDERER_CLASSES'] = [
        'rest_framework.renderers.JSONRenderer',]
