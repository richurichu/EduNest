"""
Django settings for edunest project.

Generated by 'django-admin startproject' using Django 4.2.6.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

from pathlib import Path
import os
from datetime import timedelta
from decouple import config

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-d9kz1xxr(rc0^asx1di1rmv^!$eerir%7slenr8xzbtki)#w#g'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['www.edunestonline.site','edunestonline.site','0.0.0.0','127.0.0.1','16.170.210.19', 'localhost']

AUTH_USER_MODEL = 'authentification.CustomUser'
# Application definition


INSTALLED_APPS = [
    'daphne',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'authentification',
    'Courses',
    'Notes',
    'Comments',
    'Testseries',
    'Family',
    'channels',
    'rest_framework',
    'corsheaders',
    'rest_framework_simplejwt.token_blacklist',
    


]



MIDDLEWARE = [
    
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    
]

ROOT_URLCONF = 'edunest.urls'


CHANNEL_LAYERS = {
    'default': {
        'BACKEND': 'channels.layers.InMemoryChannelLayer',
    },
}

ASGI_APPLICATION = 'edunest.asgi.application'


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

WSGI_APPLICATION = 'edunest.wsgi.application'
CORS_ALLOW_ALL_ORIGINS = True
CORS_ALLOW_CREDENTIALS = True

# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'Edunest',   
        'USER': 'postgresss',
        'PASSWORD': '123',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}


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

REST_FRAMEWORK = {
     'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework_simplejwt.authentication.JWTAuthentication',
      ],
}

SIMPLE_JWT = {
     'ACCESS_TOKEN_LIFETIME': timedelta(days=1),
     'REFRESH_TOKEN_LIFETIME': timedelta(days=5),
     'ROTATE_REFRESH_TOKENS': True,
     'BLACKLIST_AFTER_ROTATION': True
}

CSRF_TRUSTED_ORIGINS = ['http://edunestonline.site', 'https://edunestonline.site','http://16.170.210.19']


PAYPAL_MODE = 'sandbox'  # or 'live' for production
PAYPAL_CLIENT_ID = config('PAYPAL_CLIENT_ID')
PAYPAL_SECRET = config('PAYPAL_SECRET')

# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/



LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = 'static/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')
# MEDIA_URL = '/media/'
# MEDIA_URL = 'https://edunestmedia.s3.amazonaws.com/'
MEDIA_URL = 'https://edunestmedia.s3.ap-south-1.amazonaws.com/'
DATA_UPLOAD_MAX_MEMORY_SIZE = 100 * 1024 * 1024 




AWS_ACCESS_KEY_ID = config('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = config('AWS_SECRET_ACCESS_KEY')
AWS_STORAGE_BUCKET_NAME = config('AWS_STORAGE_BUCKET_NAME')
AWS_S3_REGION_NAME = config('AWS_S3_REGION_NAME')
DEFAULT_FILE_STORAGE = config('DEFAULT_FILE_STORAGE')

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = config('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = config('EMAIL_HOST_PASSWORD')

EMAIL_USE_TLS = True
# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
