from .base import *


DEBUG = False

ALLOWED_HOSTS = ['noripyt.com', 'dev.noripyt.com']

SERVER_HOST = 'ssl0.ovh.net'
SERVER_PORT = 587
DEFAULT_FROM_EMAIL = 'noreply@noripyt.com'
SERVER_EMAIL = DEFAULT_FROM_EMAIL
EMAIL_SUBJECT_PREFIX = '[Noripyt.com] '
EMAIL_TIMEOUT = 5

try:
    from .local import *
except ImportError:
    pass
