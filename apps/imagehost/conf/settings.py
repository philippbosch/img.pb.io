import os.path

from django.core.exceptions import ImproperlyConfigured
from django.conf import settings


UPLOAD_DIR_URL = getattr(settings, 'IMAGEHOST_UPLOAD_DIR_URL', settings.MEDIA_URL + 'uploads/')
UPLOAD_DIR_PATH = getattr(settings, 'IMAGEHOST_UPLOAD_DIR_PATH', 'uploads/')
