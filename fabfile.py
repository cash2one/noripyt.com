from contextlib import contextmanager
from pathlib import Path

from fabric.context_managers import cd, path, shell_env
from fabric.contrib import django
from fabric.decorators import task
from fabric.operations import run, local, sudo
from fabric.state import env


django.project('noripyt')
from django.conf import settings


env.hosts = ['root@noripyt.com']

HOME = Path('/root/')
PROJECT_PATH = HOME / 'noripyt.com'
VIRTUALENV_PATH = HOME / '.virtualenvs/noripyt.com/'
DB_SETTINGS = settings.DATABASES['default']
DB_NAME = DB_SETTINGS['NAME']
DB_USER = DB_SETTINGS['USER']
REMOTE_BACKUP = HOME / 'backups/noripyt.backup'
LOCAL_BACKUP = './backups/noripyt.backup'
REMOTE_MEDIA = PROJECT_PATH / 'media/'
LOCAL_MEDIA = './media/'


@contextmanager
def workon(settings_module='noripyt.settings.production'):
    with cd(str(PROJECT_PATH)):
        with path(str(VIRTUALENV_PATH / 'bin'), behavior='prepend'):
            with shell_env(DJANGO_SETTINGS_MODULE=settings_module):
                yield


@task
def setup_firewall():
    run('ufw disable')
    run('ufw default deny')
    run('ufw allow 80')
    run('ufw allow 22')
    run('ufw allow 443')
    run('ufw enable')


@task
def create_ssl_certificate():
    run('apt install letsencrypt')
    run('systemctl stop nginx')
    try:
        run('letsencrypt certonly --standalone -d noripyt.com')
    finally:
        run('systemctl start nginx')


@task
def renew_ssl_certificate():
    run('letsencrypt renew')


def upgrade_ubuntu():
    sudo('apt-get update')
    sudo('apt-get upgrade')


def pip_install():
    with workon():
        run('pip install -r requirements.txt')


def update_submodules():
    with workon():
        run('git submodule init')
        run('git submodule update')


def migrate_db():
    with workon():
        run('./manage.py migrate')


def collectstatic():
    with workon():
        run('./manage.py collectstatic --noinput')


@task
def restart():
    sudo('supervisorctl restart django')


@task
def update():
    upgrade_ubuntu()

    with workon():
        run('git pull')
        update_submodules()
        run('find . -name "*.pyc" -delete')

    pip_install()
    migrate_db()
    collectstatic()

    restart()


@task
def save_remote_db():
    run('pg_dump -U %s -Fc -b -v -f "%s" %s'
        % (DB_USER, REMOTE_BACKUP, DB_NAME))
    local('rsync "%s":"%s" "%s"' % (env.hosts[0], REMOTE_BACKUP, LOCAL_BACKUP))


@task
def restore_saved_db():
    local('sudo -u postgres dropdb %s' % DB_NAME)
    local('sudo -u postgres createdb %s' % DB_NAME)
    local('pg_restore -U root -e -d %s -j 5 "%s"' % (DB_NAME, LOCAL_BACKUP))


@task
def clone_remote_db():
    save_remote_db()
    restore_saved_db()


@task
def clone_remote_media():
    local('rsync -azv "%s":"%s" "%s"' % (env.hosts[0],
                                         REMOTE_MEDIA, LOCAL_MEDIA))


@task
def clone_remote():
    clone_remote_db()
    clone_remote_media()
