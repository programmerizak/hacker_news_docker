
import os
from pathlib import Path
from decouple import config, Csv


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config("SECRET_KEY")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = config("DEBUG", default=False, cast=bool)

ALLOWED_HOSTS = config("ALLOWED_HOSTS", cast=Csv())


# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    ##########################
    'django.contrib.sites',
    ## For Flatpages ###
    'django.contrib.flatpages',
    ## Sitemap
    'django.contrib.sitemaps',
    ## ALL AUTH APPS 
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    ##########################
    'celery',
    #################
    'crispy_forms',
    'easy_thumbnails',
    'items',
    'api',
    'users',
    ###### DOCUMENTATION #####
    'drf_yasg',
    ###### API###########
    'rest_framework',
    'corsheaders',

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

ROOT_URLCONF = 'website.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / '../templates'],
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


AUTHENTICATION_BACKENDS = (

    # Needed to login by username in Django admin, regardless of `allauth`
    'django.contrib.auth.backends.ModelBackend',

    # `allauth` specific authentication methods, such as login by e-mail
    'allauth.account.auth_backends.AuthenticationBackend',

)


WSGI_APPLICATION = 'website.wsgi.application'



DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": config("DB_NAME"),
        "USER": config("DB_USERNAME"),
        "PASSWORD": config("DB_PASSWORD"),
        "HOST": config("DB_HOSTNAME"),
        "PORT": config("DB_PORT", cast=int),
    }
}


AUTH_USER_MODEL = 'users.User'

SITE_ID = 1


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

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



LOGIN_REDIRECT_URL = 'user:dashboard'
LOGOUT_REDIRECT_URL = 'pages:home'
ACCOUNT_AUTHENTICATION_METHOD = "username_email"
LOGIN_URL = 'account_login'
ACCOUNT_EMAIL_CONFIRMATION_EXPIRE_DAYS = 1
ACCOUNT_LOGIN_ATTEMPTS_LIMIT = 3
ACCOUNT_LOGIN_ATTEMPTS_TIMEOUT = 500
ACCOUNT_LOGOUT_ON_PASSWORD_CHANGE = True
ACCOUNT_USERNAME_BLACKLIST = ['admin', 'admin1', 'admin2', ]
ACCOUNT_LOGOUT_ON_GET = True
USE_THOUSAND_SEPARATOR = True
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_UNIQUE_EMAIL = True


LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Africa/Lagos'

USE_I18N = True

USE_TZ = True

USE_L10N = True



DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'



SITE_NAME = 'Hacker News V2.0'
SITE_TAGLINE = "Where hackers lives"
META_KEYWORDS = '''Python, Django, News, hackers, hackers news,

'''

META_DESCRIPTION = '''
Hacker News is a good platform

'''
AUTHOR = "Isaac Imafidon"


#########################################################################
########################### CELERY ######################################
# Celery
CELERY_BROKER_URL = config("CELERY_BROKER_URL")
CELERY_RESULT_BACKEND = config("REDIS_BACKEND")




from celery.schedules import crontab
import items.tasks

CELERY_BEAT_SCHEDULE = {

    "task_name_1": {
        "task": "items.tasks.checking_tasks",
        "schedule": crontab(minute="*/2"),
    },


    "task_name_2": {
        "task": "items.tasks.update_our_model",
        "schedule": crontab(minute="*/5"),
    },

}
