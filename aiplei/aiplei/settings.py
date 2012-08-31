# -*- coding: utf-8 -*-

import os
import sys

os.environ['LANG'] = 'en_US.UTF-8'

PROJECT_DIR = os.path.abspath(os.path.dirname(__file__))

for d in ['plugins', 'apps', 'lib']:
    sys.path.insert(0, os.path.join(PROJECT_DIR, '../' + d))

gettext = lambda s: s

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    ('Gustavo Lima', 'gustavo.coelho.lima@gmail.pt'),
)

MANAGERS = ADMINS
DATABASES = {
    'default': {
        'ENGINE': '',  # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': '',                      # Or path to database file if using sqlite3.
        'USER': '',                      # Not used with sqlite3.
        'PASSWORD': '',                  # Not used with sqlite3.
        'HOST': '',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
    }
}

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# In a Windows environment this must be set to your system time zone.
TIME_ZONE = 'Europe/Lisbon'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'pt'
LANGUAGES = (('pt', 'Português'),)

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale.
USE_L10N = True

# If you set this to False, Django will not use timezone-aware datetimes.
USE_TZ = False

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/home/media/media.lawrence.com/media/"
MEDIA_ROOT = os.path.join(PROJECT_DIR, '../..', 'media/')

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://media.lawrence.com/media/", "http://example.com/media/"
MEDIA_URL = '/media/'

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/home/media/media.lawrence.com/static/"
STATIC_ROOT = os.path.join(PROJECT_DIR, '../..', 'static')

# URL prefix for static files.
# Example: "http://media.lawrence.com/static/"
STATIC_URL = '/static/'
ADMIN_MEDIA_PREFIX = STATIC_URL + 'admin/'
CMS_MEDIA_URL = STATIC_URL + 'cms/'
FILER_STATICMEDIA_PREFIX = STATIC_URL + 'filer/'

# Additional locations of static files
STATICFILES_DIRS = (
    ('site', os.path.join(PROJECT_DIR, 'static/')),
)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
    'aiplei.finders.AppMediaDirectoriesFinder',
)

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'fl0r97c*eq6q6vhmtw37oe$n-p3*a3a1@&amp;gcd%8pvj11y2*an#'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    # Uncomment the next line for simple clickjacking protection:
    # 'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'cms.middleware.page.CurrentPageMiddleware',
    'cms.middleware.user.CurrentUserMiddleware',
)

ROOT_URLCONF = 'aiplei.urls'

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'aiplei.wsgi.application'

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.core.context_processors.i18n',
    'django.core.context_processors.request',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
    'django.contrib.auth.context_processors.auth',
    'django.contrib.messages.context_processors.messages',
    'cms.context_processors.media',
    'sekizai.context_processors.sekizai',
)

TEMPLATE_DIRS = (
    os.path.join(PROJECT_DIR, 'templates'),
)

INSTALLED_APPS = (
    'admin_tools',
    'admin_tools.theming',
    'admin_tools.menu',
    'admin_tools.dashboard',

    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'django.contrib.admin',

    # lib
    'south',
    'menus',
    'mptt',
    'cms',
    'sekizai',
    'filer',
    'easy_thumbnails',
    'registration',
    'social_auth',
    'invitation',
    'notification',
    'messages',
    'mailer',

    #apps
    'beta',
    'profiles',
)

# Uncomment if using django-cms and/or django-filer
CMS_SOFTROOT = False
CMS_MODERATOR = False
CMS_PERMISSION = False
CMS_REDIRECTS = True
CMS_SEO_FIELDS = True
CMS_MENU_TITLE_OVERWRITE = True
CMS_PAGE_MEDIA_PATH = 'cms/'
CMS_CONTENT_CACHE_DURATION = 60
CMS_USE_TINYMCE = False

CMS_LANGUAGES = LANGUAGES

# Uncomment if using django-cms and/or django-filer
CMS_TEMPLATES = (
    ('index.html', gettext('index')),
)

# Uncomment if using django-cms and/or django-filer
CMS_PLACEHOLDER_CONF = {
#    'map': {
#        'plugins': ('GoogleMapPlugin',),
#        'name': gettext('Map'),
#        'limits': {
#            'global': 1,
#        },
#    },
}

# Django-filer settings
THUMBNAIL_PROCESSORS = (
    'easy_thumbnails.processors.colorspace',
    'easy_thumbnails.processors.autocrop',
    #'easy_thumbnails.processors.scale_and_crop',
    'filer.thumbnail_processors.scale_and_crop_with_subject_location',
    'easy_thumbnails.processors.filters',
)

# Admin tools configuration
ADMIN_TOOLS_INDEX_DASHBOARD = 'aiplei.dashboard.QueoIndexDashboard'
ADMIN_TOOLS_THEMING_CSS = 'site/css/theming.css'
ADMIN_TOOLS_MENU = 'aiplei.menu.QueoMenu'


DEFAULT_FROM_EMAIL = 'gustavo@queo.pt'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'gustavo@queo.pt'
EMAIL_HOST_PASSWORD = 'Cartesian41'
EMAIL_PORT = 587
EMAIL_USE_TLS = True

# Email settings for django-mailer
#DEFAULT_FROM_EMAIL = ''
#EMAIL_HOST = ''
#EMAIL_HOST_USER = ''
#EMAIL_HOST_PASSWORD = ''
#EMAIL_PORT = 587
#EMAIL_USE_TLS = True

#Registration configuration
ACCOUNT_ACTIVATION_DAYS = 7

#Invitations configuration
ACCOUNT_INVITATION_DAYS = 10
INVITATIONS_PER_USER = 3
INVITE_MODE = True

#Social authentication
AUTHENTICATION_BACKENDS = (
    'social_auth.backends.twitter.TwitterBackend',
    'social_auth.backends.facebook.FacebookBackend',
    'social_auth.backends.google.GoogleOAuthBackend',
    #'social_auth.backends.google.GoogleOAuth2Backend',
    'social_auth.backends.google.GoogleBackend',
    #'social_auth.backends.yahoo.YahooBackend',
    #'social_auth.backends.browserid.BrowserIDBackend',
    #'social_auth.backends.contrib.linkedin.LinkedinBackend',
    #'social_auth.backends.contrib.livejournal.LiveJournalBackend',
    #'social_auth.backends.contrib.orkut.OrkutBackend',
    #'social_auth.backends.contrib.foursquare.FoursquareBackend',
    #'social_auth.backends.contrib.github.GithubBackend',
    #'social_auth.backends.contrib.vkontakte.VKontakteBackend',
    #'social_auth.backends.contrib.live.LiveBackend',
    #'social_auth.backends.contrib.skyrock.SkyrockBackend',
    #'social_auth.backends.contrib.yahoo.YahooOAuthBackend',
    #'social_auth.backends.OpenIDBackend',
    'django.contrib.auth.backends.ModelBackend',
)

TWITTER_CONSUMER_KEY = 'Krmvsp6G8dCcZcyTRbhmQ'
TWITTER_CONSUMER_SECRET = 'AE1TH88qV4EHKqhfGASOjFtCNKsZN5VFv6ehntg3aGg'
FACEBOOK_APP_ID = '356624277751837'
FACEBOOK_API_SECRET = '7ba61bcb24d5db5e867ad083fba26558'
GOOGLE_OAUTH2_CLIENT_ID = ''
GOOGLE_OAUTH2_CLIENT_SECRET = ''
GOOGLE_CONSUMER_KEY = 'anonymous'
GOOGLE_CONSUMER_SECRET = 'anonymous'

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}

try:
    from local_settings import *
except ImportError:
    pass
