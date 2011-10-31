"""
  Permabank settings for local development
"""
from __future__ import absolute_import
from .base import *


# turn on debug mode
DEBUG = True
TEMPLATE_DEBUG = DEBUG

# use sqlite as data store
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': PROJECT_DIR.child('permabank.db'),
    }
}

# use redis as cache backend
CACHES = {
    'default': {
        'BACKEND': 'redis_cache.RedisCache',
        'LOCATION': 'localhost:6379',
    },
}