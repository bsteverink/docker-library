import os

from boilerplate.settings import *

###############################################################################
# PRODUCTION SETTINGS
###############################################################################

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

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

SERVER_EMAIL = "application@in2systems.nl"
DEFAULT_FROM_EMAIL = os.environ.get("WEBMASTER_EMAIL_USER")

EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST = "smtp.strato.com"
EMAIL_PORT = 465
EMAIL_HOST_USER = os.environ.get("WEBMASTER_EMAIL_USER")
EMAIL_HOST_PASSWORD = os.environ.get("WEBMASTER_EMAIL_PASS")
EMAIL_USE_TLS = False
EMAIL_USE_SSL = True
EMAIL_TIMEOUT = 60

###############################################################################
# CSRF Protection
###############################################################################

ALLOWED_HOSTS = []

# Sets the domains that have access to the API
CORS_ORIGIN_WHITELIST = []
