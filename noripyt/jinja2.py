from django.conf import settings
from django.contrib.staticfiles.storage import staticfiles_storage
from django.core.urlresolvers import reverse
from django.utils import translation
from jinja2 import Environment


def environment(**options):
    env = Environment(**options)
    env.globals.update({
        'static': staticfiles_storage.url,
        'url': reverse,
        'LANGUAGES': settings.LANGUAGES,
        'translation': translation,
    })
    env.install_gettext_translations(translation)
    return env
