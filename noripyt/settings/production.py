from .base import *


DEBUG = False

ALLOWED_HOSTS = ['.noripyt.com']

EMAIL_HOST = 'mail.gandi.net'
EMAIL_HOST_USER = 'noreply@noripyt.com'
EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASSWORD', '')
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER
SERVER_EMAIL = DEFAULT_FROM_EMAIL
EMAIL_SUBJECT_PREFIX = '[NoriPyt.com] '
EMAIL_TIMEOUT = 5

try:
    from .local import *
except ImportError:
    pass
