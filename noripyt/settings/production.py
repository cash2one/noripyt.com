from .base import *


DEBUG = False

ALLOWED_HOSTS = ['noripyt.com', 'dev.noripyt.com']

try:
    from .local import *
except ImportError:
    pass
