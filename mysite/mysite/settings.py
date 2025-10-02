# mysite/settings.py (Final Version)

import os
from pathlib import Path
import dj_database_url
from dotenv import load_dotenv
from decouple import config

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Load environment variables from .env file for local development
load_dotenv(os.path.join(BASE_DIR, '.env'))


# --- Security Settings ---
# It is recommended to set SECRET_KEY in your environment variables for production
SECRET_KEY = config('SECRET_KEY', default='django-insecure-a-default-key-for-local-dev')

# DEBUG will be False on Render, and True locally
DEBUG = 'RENDER' not in os.environ

ALLOWED_HOSTS = []

# Add Render's hostname to allowed hosts
RENDER_EXTERNAL_HOSTNAME = os.environ.get('RENDER_EXTERNAL_HOSTNAME')
if RENDER_EXTERNAL_HOSTNAME:
    ALLOWED_HOSTS.append(RENDER_EXTERNAL_HOSTNAME)

# Add hosts for local development
ALLOWED_HOSTS.extend(['127.0.0.1', 'localhost'])


# --- Application Definitions ---
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'cloudinary_storage',         # Must be before 'django.contrib.staticfiles'
    'django.contrib.staticfiles',
    'cloudinary',
    'profile_app',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware', # For serving static files efficiently
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'mysite.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'mysite.wsgi.application'


# --- Database Configuration ---
if 'RENDER' in os.environ:
    # Production database configuration (Render)
    DATABASES = {
        'default': dj_database_url.config(
            default=config('DATABASE_URL')
        )
    }
else:
    # Local database configuration
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
        }
    }


# --- Password Validation ---
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]


# --- Internationalization ---
LANGUAGE_CODE = 'ja'
TIME_ZONE = 'Asia/Tokyo'
USE_I18N = True
USE_TZ = True


# --- Static and Media File Configuration (Unified for Cloudinary) ---

# URL to use when referring to static files located in STATIC_ROOT
STATIC_URL = '/static/'
# Directory where 'collectstatic' will collect files for deployment
STATIC_ROOT = BASE_DIR / 'staticfiles'
# Directories where Django will look for static files in addition to each app's 'static' directory
STATICFILES_DIRS = [
    BASE_DIR / 'static',
]

# URL for media files
MEDIA_URL = '/media/'
# Directory for storing media files locally (for development)
MEDIA_ROOT = BASE_DIR / 'media'

# Configure Cloudinary as the storage for both static and media files
# This allows 'collectstatic' to upload files from your local machine to Cloudinary
DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'
STATICFILES_STORAGE = 'cloudinary_storage.storage.StaticHashedCloudinaryStorage'

# Cloudinary credentials (read from environment variables)
CLOUDINARY_STORAGE = {
    'CLOUD_NAME': config('CLOUDINARY_CLOUD_NAME'),
    'API_KEY': config('CLOUDINARY_API_KEY'),
    'API_SECRET': config('CLOUDINARY_API_SECRET'),
}


# --- Default Primary Key ---
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'