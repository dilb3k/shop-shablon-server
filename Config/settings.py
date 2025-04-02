"""
Django settings for Config project.

Generated by 'django-admin startproject' using Django 4.2.19.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-&^ly@ww$wuk!^0q4%*r!69^v613g$z5=k$ido2ye&zbd$f@g5g'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["*"]

# ✅ CORS sozlamalari uchun kutubxonani qo'shish
INSTALLED_APPS = [
    'corsheaders',  # CORS middleware ishlashi uchun kerak
    'jazzmin',  # Admin interfeysi
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'rest_framework',  # DRF
    'drf_spectacular',  # API schema
    'drf_spectacular_sidecar',
    'channels',  # WebSocket va kanal qo'llab-quvvatlash

    'rest_framework_simplejwt',  # JWT autentifikatsiya

    # Custom apps
    'CategoryApp',
    'Usersapp',
    'Promotion',
    'Order',
    'Admin',
    'Blog',
    'Cart',
    'Review',
    'Like',
    'ProductApp',
    'Massage',
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',  # ✅ CORS middleware-ni eng tepaga qo‘yish kerak
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

# Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
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

# ✅ CORS SOZLAMALARI
CORS_ALLOW_ALL_ORIGINS = True  # Barcha domenlarga ruxsat berish (test uchun)

# Agar faqat ma'lum domenlarga ruxsat bermoqchi bo‘lsangiz, quyidagilarni ishlating:
# CORS_ALLOWED_ORIGINS = [
#     "http://localhost:3000",  # React yoki boshqa frontend domeni
#     "https://yourfrontend.com",
# ]

CORS_ALLOW_CREDENTIALS = True  # Cookie va auth headerlarni yuborish uchun
CORS_ALLOW_METHODS = ["GET", "POST", "PUT", "DELETE", "OPTIONS"]  # Ruxsat berilgan metodlar
CORS_ALLOW_HEADERS = ["*"]  # Barcha headerlarga ruxsat berish
CORS_ALLOWED_ORIGINS = [
    "http://localhost:5173",
    "ws://localhost:5173",
]
# Internationalization
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# Static files (CSS, JavaScript, Images)
STATIC_URL = 'static/'
MEDIA_URL = 'media/'
MEDIA_ROOT = BASE_DIR / 'media'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

REST_FRAMEWORK = {
    'DEFAULT_SCHEMA_CLASS': 'drf_spectacular.openapi.AutoSchema',
    
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    )
}

from datetime import timedelta

SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(days=1),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=7),
    'ROTATE_REFRESH_TOKENS': True,
    'BLACKLIST_AFTER_ROTATION': True,
}
AUTH_USER_MODEL = "Usersapp.UserModel"




ASGI_APPLICATION = 'Config.asgi.application'

CHANNEL_LAYERS = {
    'default': {
        'BACKEND': 'channels_redis.core.RedisChannelLayer',
        'CONFIG': {
            "hosts": [("127.0.0.1", 6379)],
        },
    },
}

SPECTACULAR_SETTINGS = {
    'TITLE': 'OLX API',
    'DESCRIPTION': 'OLX uchun API endpointlar',
    'VERSION': '1.0.0',
    'SERVE_INCLUDE_SCHEMA': False,
    'SWAGGER_UI_DIST': 'SIDECAR',
    'SWAGGER_UI_FAVICON_HREF': 'SIDECAR',
    'REDOC_DIST': 'SIDECAR',
}
