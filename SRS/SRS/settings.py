import os
from pathlib import Path
from dotenv import load_dotenv
# from decouple import Config, Csv, config
# import dj_database_url

load_dotenv()

# # Initialize Config from .env file
# config = Config('.env')

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = str(os.getenv('SECRET_KEY'))

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.getenv('DEBUG')

# ALLOWED_HOSTS = os.getenv('ALLOWED_HOSTS', '*').split(',')
ALLOWED_HOSTS = ['*']

# Application definition
INSTALLED_APPS = [
    'jazzmin',
    'main.apps.MainConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'whitenoise.runserver_nostatic',
    'django.contrib.staticfiles',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'SRS.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
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

WSGI_APPLICATION = 'SRS.wsgi.application'


# Database configuration
# DATABASE_URL = config('DATABASE_URL', default=None)

# if DATABASE_URL:
#     DATABASES = {
#         'default': dj_database_url.parse(DATABASE_URL, conn_max_age=600)
#     }
# else:
#     DATABASES = {
#         'default': {
#             'ENGINE': 'django.db.backends.sqlite3',
#             'NAME': str(Path('F:/Github Projects/Student-Registration-System/SRS/db.sqlite3')),
#         }
#     }

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

STORAGES = {

    "default": {
        "BACKEND": "storages.backends.azure_storage.AzureStorage"
    },
    "staticfiles": {
        "BACKEND": "whitenoise.storage.CompressedStaticFilesStorage",
    },
}

# Password validation
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
        'OPTIONS': {
            'max_similarity': 0.1,
            'user_attributes': ('email',)
        }
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'main.validators.SpecialCharValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
        'OPTIONS': {
            'min_length': 8
        }
    },
    {
        'NAME': 'main.validators.UppercaseValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Internationalization
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'Asia/Kolkata'
USE_I18N = True
USE_TZ = True

LOGIN_URL = 'main:Login'

# Static files (CSS, JavaScript, Images)
STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'static/'

# Azure Storage Account Name and Key
AZURE_ACCOUNT_NAME = str(os.getenv('AZURE_ACCOUNT_NAME'))
AZURE_ACCOUNT_KEY = str(os.getenv('AZURE_ACCOUNT_KEY'))
AZURE_CONTAINER = 'srs079'
AZURE_CUSTOM_DOMAIN = f'{AZURE_ACCOUNT_NAME}.blob.core.windows.net'
AZURE_USE_HTTPS = True


STATIC_URL = '/static/'

STATIC_ROOT = BASE_DIR / 'static/'

MEDIA_URL = 'media/'

MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')

# Default primary key field type
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Email settings
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = str(os.getenv('EMAIL_HOST_USER'))
EMAIL_HOST_PASSWORD = str(os.getenv('EMAIL_HOST_PASSWORD'))
EMAIL_PORT = 587

# Razorpay settings
RAZOR_KEY_ID = str(os.getenv('RAZOR_KEY_ID'))
RAZOR_KEY_SECRET = str(os.getenv('RAZOR_KEY_SECRET'))

# Jazzmin settings
JAZZMIN_SETTINGS = {
    "site_title": "Student Registration System",
    "site_header": "Administration",
    "site_brand": "Site Administration",
    "site_logo": "images/da.jpg",
    "login_logo": "images/dalogo.jpg",
    "site_logo_classes": "img-circle",
    "copyright": "DAIICT",
    "search_model": ["auth.User", "main.Application"],
    "topmenu_links": [
        {"name": "Home", "url": "admin:index", "permissions": ["auth.view_user"]},
        {"app": "main"},
        {"app": "auth"},
    ],
    "usermenu_links": [
        {"model": "auth.user"}
    ],
    "navigation_expanded": False,
    "hide_models": ["auth.group"],
    "order_with_respect_to": ["auth", "main", "main.application", "main.notification", "main.deadline", "main.question", "main.test"],
    "show_ui_builder": True,
}

