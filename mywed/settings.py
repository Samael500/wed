"""
Django settings for mywed project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
from os.path import join

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

if __name__ in ['settings', 'mywed.settings']:
    import sys
    sys.path.insert(0, join(BASE_DIR, 'mywed'))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '5#1yw)g=zo9qfft-ynl*if19_s%^7zr_9o!@=bw1a)80umkzft'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False
TEMPLATE_DEBUG = False

ALLOWED_HOSTS = ['olya-maks.ru', ]

LOGIN_URL = 'login'


# Application definition

INSTALLED_APPS = (
    'grappelli',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # custom apps
    'compressor',
    'pure_pagination',
    'django_summernote',
    'sorl.thumbnail',
    # mywed apps
    'guests',
    'index',
    'news',
    'helpers',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
    'django.core.context_processors.tz',
    'django.contrib.messages.context_processors.messages',
    'django.core.context_processors.request'
)

ROOT_URLCONF = 'mywed.urls'

WSGI_APPLICATION = 'mywed.wsgi.application'


# Database connection
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'mywed',
        'USER': 'mywed',
        'PASSWORD': '80umkzft',
        'HOST': '127.0.0.1',
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'ru'
TIME_ZONE = 'Europe/Moscow'

USE_I18N = True
USE_L10N = True
USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = 'mywed/static/'

MEDIA_URL = '/media/'
MEDIA_ROOT = 'media/'

TEST_RUNNER = 'rainbowtests.test.runner.RainbowDiscoverRunner'

TEMPLATE_DIRS = (
    join(BASE_DIR, 'mywed', 'templates'),
)

COMPRESS_ROOT = join(BASE_DIR, 'mywed', 'static')

COMPRESS_ENABLED = True
COMPRESS_OFFLINE = True

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'compressor.finders.CompressorFinder',
)

# paginations
PAGINATE_BY = 10
PAGINATION_SETTINGS = {
    'PAGE_RANGE_DISPLAYED': 1,
    'MARGIN_PAGES_DISPLAYED': 3,
}

# summernote
SUMMERNOTE_CONFIG = {
    'styleWithTags': True,
    # Change editor size
    'width': '100%',
    'height': '480',
    # Use proper language setting automatically (default)
    'lang': 'ru-RU',
    # Customize toolbar buttons
    'toolbar': [
        # ['style', ['style']],
        # ['font', ['bold', 'italic', 'underline', 'clear']],
        # ['fontsize', ['fontsize']],
        # ['color', ['color']],
        # ['para', ['ul', 'ol', 'paragraph']],
        # ['height', ['height']],
        # ['table', ['table']],
        # ['insert', ['link', 'picture', 'video', 'hr']],
        ['view', ['fullscreen', 'codeview']],
        # ['help', ['help']],
    ],
}

try:
    from settings_local import *  # noqa
except ImportError:
    pass

try:
    if 'TRAVIS' in os.environ:
        from settings_travis import *  # noqa
except ImportError:
    pass
