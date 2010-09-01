# -*- coding: utf-8 -*-

import os.path

_ = lambda s: s

PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))
PROJECT_NAME = os.path.split(PROJECT_ROOT)[-1]

# DEBUGGING
INTERNAL_IPS = ('127.0.0.1', )

# CACHE
CACHE_MIDDLEWARE_KEY_PREFIX = '%s_' % PROJECT_NAME

# EMAIL / ERROR NOTIFY
SERVER_EMAIL = 'hello@pb.io'
ADMINS = (
    ('Philipp Bosch', SERVER_EMAIL),
)
MANAGERS = ADMINS

# DATABASE
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(PROJECT_ROOT, "%s.sqlite3" % PROJECT_NAME),
        'USER': 'root',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
    }
}

# I18N/L10N
TIME_ZONE = 'Europe/Berlin'
LANGUAGE_CODE = 'en'
LANGUAGES = (
    ('en', 'English'),
)
USE_I18N = True
USE_L10N = True

# URLS
SITE_ID = 1
MEDIA_ROOT = os.path.join(PROJECT_ROOT, 'media')
MEDIA_URL = '/media/'
ADMIN_MEDIA_PREFIX = '/admin-media/'
ROOT_URLCONF = '%s.urls' % PROJECT_NAME

# APPS, MIDDLEWARES, CONTEXT PROCESSORS
INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.admin',
    'south',
    'compressor',
    'easy_thumbnails',
    
    'imagehost',
)
MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.middleware.common.CommonMiddleware',
)
TEMPLATE_CONTEXT_PROCESSORS = (
    'django.core.context_processors.request',
    'django.core.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
)

# TEMPLATE LOADING
TEMPLATE_DIRS = (
    os.path.join(PROJECT_ROOT, 'templates'),
)

# SECRET
try:
    SECRET_KEY
except NameError:
    SECRET_FILE = os.path.join(PROJECT_ROOT, 'secret.txt')
    try:
        SECRET_KEY = open(SECRET_FILE).read().strip()
    except IOError:
        try:
            from random import choice
            SECRET_KEY = ''.join([choice('abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(-_=+)') for i in range(50)])
            secret = file(SECRET_FILE, 'w')
            secret.write(SECRET_KEY)
            secret.close()
        except IOError:
            Exception('Please create a %s file with random characters to generate your secret key!' % SECRET_FILE)

# DJANGO-CSS
COMPRESS = True
COMPILER_FORMATS = {
    '.scss': {
        'binary_path': 'sass --scss --style compressed',
        'arguments': '*.scss *.css',
    }
}
COMPRESS_OUTPUT_DIR = 'compressed'

# IMAGEHOST
IMAGEHOST_UPLOAD_DIR_URL = MEDIA_URL + 'uploads/'
IMAGEHOST_UPLOAD_DIR_PATH = 'uploads/'
THUMBNAIL_DEBUG = True
THUMBNAIL_EXTENSION = 'png'

# LOCAL SETTINGS
try:
    execfile(os.path.join(os.path.dirname(__file__), "settings_local.py"))
except IOError:
    pass
