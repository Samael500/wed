# Local settings

# Turn debug mode on
DEBUG = True
TEMPLATE_DEBUG = True
COMPRESS_OFFLINE = False

# Database connection
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'mywed.sqlite3',
    }
}
