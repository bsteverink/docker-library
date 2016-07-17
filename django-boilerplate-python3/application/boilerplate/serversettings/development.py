import os

from boilerplate.settings import *

###############################################################################
# DEVELOPMENT SETTINGS
###############################################################################

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

###############################################################################
# DATABASE
# https://docs.djangoproject.com/en/1.9/ref/settings/#databases
###############################################################################

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",
        "NAME": os.environ.get("DATABASE_NAME"),
        "USER": os.environ.get("DATABASE_USER"),
        "PASSWORD": os.environ.get("DATABASE_PASS"),
        "CONN_MAX_AGE": 60,
        "HOST": os.environ.get("DATABASE_HOST") or ""
    },
    "admin": {
        "ENGINE": "django.db.backends.mysql",
        "NAME": os.environ.get("DATABASE_NAME"),
        "USER": os.environ.get("DATABASE_ADMIN_USER"),
        "PASSWORD": os.environ.get("DATABASE_ADMIN_PASS"),
        "CONN_MAX_AGE": 60,
        "HOST": os.environ.get("DATABASE_HOST") or ""
    }
}

###############################################################################
# EMAIL SETTINGS
###############################################################################

EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"
