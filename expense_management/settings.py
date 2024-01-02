from pathlib import Path
import json

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'django-insecure-83!e=ys6$y5d_yje)w&2=vq%0wo7d2u8iy$zx2enrnsen2u-^$'

DEBUG = True

ALLOWED_HOSTS = ['*']

SITE_ID=1

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    #'expense_management.accounts',
    'expense_management.expenses',
    "django.contrib.sites",
    # 'allauth',
    # 'allauth.account',
    # 'allauth.socialaccount',
    # 'allauth.socialaccount.providers.google',
    # 'allauth.socialaccount.providers.facebook',
]

# SOCIALACCOUNT_PROVIDERS = {
#     "google": {
#         "SCOPE": [
#             "profile",
#             "email"
#         ],
#         "AUTH_PARAMS": {"access_type": "online"},
#         "redirect_uri": "http://127.0.0.1:8000/admin/google/login/callback/",
#         "access_type": "online",
#     }
# }

ACCOUNT_DEFAULT_HTTP_PROTOCOL = "http"

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    "django.contrib.sessions.middleware.SessionMiddleware",
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    #"allauth.account.middleware.AccountMiddleware",
]

ROOT_URLCONF = 'expense_management.urls'

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
                'django.template.context_processors.request',
            ],
        },
    },
]

AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
    #'allauth.account.auth_backends.AuthenticationBackend',
]

WSGI_APPLICATION = 'expense_management.wsgi.application'

STATIC_ROOT = 'static'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

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

#AUTH_USER_MODEL = 'accounts.User'

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

STATIC_URL = '/static/'

STATIC_ROOT = BASE_DIR / 'staticfiles'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

try:
    from expense_management.local_settings import *
except ImportError:
    pass