import os
from pathlib import Path
from datetime import timedelta
import dj_database_url

# Build paths
BASE_DIR = Path(__file__).resolve().parent.parent

# Security settings - USE ENVIRONMENT VARIABLES IN PRODUCTION!
import os

SECRET_KEY = os.environ.get('SECRET_KEY', 'r0v)27599_k%26v-n+&v3p6!fxhhf6r4ke@ll*x$nvh)f8$z86')
DEBUG = os.environ.get('DEBUG', 'False') == 'True'
ALLOWED_HOSTS = os.environ.get('ALLOWED_HOSTS', '*').split(',')


# Application definition
INSTALLED_APPS = [
    'corsheaders',
    'jazzmin',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'rest_framework',
    'drf_spectacular',
    'drf_spectacular_sidecar',
    'channels',
    'rest_framework_simplejwt',

    # Custom apps
    'CategoryApp',
    'Usersapp',
    'Promotion',
    'Order',
    'Blog',
    'Cart',
    'Review',
    'Like',
    'ProductApp',
    'Massage',
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'Config.urls'

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

WSGI_APPLICATION = 'Config.wsgi.application'
ASGI_APPLICATION = 'Config.asgi.application'

# Database Configuration for Render
DATABASES = {
    'default': dj_database_url.parse(
        'postgresql://shop_servers_user:SO0FQQmd3CJKA897oMBhEWilejF7bgM0@dpg-d0olekeuk2gs738q2kkg-a.oregon-postgres.render.com/shop_servers',
        conn_max_age=600,
        conn_health_checks=True,
    )
}

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

# CORS settings
CORS_ALLOW_ALL_ORIGINS = True
CORS_ALLOW_CREDENTIALS = True
CORS_ALLOW_METHODS = ["GET", "POST", "PUT", "DELETE", "OPTIONS"]
CORS_ALLOW_HEADERS = ["*"]

# Internationalization
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'Asia/Tashkent'
USE_I18N = True
USE_TZ = True

# Static and media files
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# Django rest framework and JWT settings
REST_FRAMEWORK = {
    'DEFAULT_SCHEMA_CLASS': 'drf_spectacular.openapi.AutoSchema',
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    )
}

SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(days=1),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=7),
    'ROTATE_REFRESH_TOKENS': True,
    'BLACKLIST_AFTER_ROTATION': True,
}

AUTH_USER_MODEL = "Usersapp.UserModel"

# Redis configuration
# settings.py faylida Redis sozlamalari

REDIS_URL = os.environ.get('REDIS_URL', 'redis://red-d0olkpmuk2gs738q8ffg:6379')

# To'liq Channel Layers konfiguratsiyasi
CHANNEL_LAYERS = {
    'default': {
        'BACKEND': 'channels_redis.core.RedisChannelLayer',
        'CONFIG': {
            "hosts": [REDIS_URL],
            # Qo'shimcha optimallashtirishlar
            "symmetric_encryption_keys": [SECRET_KEY],  # Xavfsizlik uchun
            "connection_kwargs": {
                "socket_connect_timeout": 5,  # 5 sekund
                "socket_keepalive": True
            },
            "capacity": 1500,  # Default 100
            "expiry": 10,      # Default 60
        },
    },
}

# Spectacular (Swagger) settings
SPECTACULAR_SETTINGS = {
    'TITLE': 'OLX API',
    'DESCRIPTION': 'OLX uchun API endpointlar',
    'VERSION': '1.0.0',
    'SERVE_INCLUDE_SCHEMA': False,
    'SWAGGER_UI_DIST': 'SIDECAR',
    'SWAGGER_UI_FAVICON_HREF': 'SIDECAR',
    'REDOC_DIST': 'SIDECAR',
}

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'