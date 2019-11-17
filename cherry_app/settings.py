"""
Django settings for cherry_app project.

Generated by 'django-admin startproject' using Django 2.2.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '!d67*_@lrsx1o*@mp=1hstoi7kej*_o$ag2a+e-cgiw16$*p2r'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["*"]

# Application definition

INSTALLED_APPS = [
    'jet.dashboard',
    'jet',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',

    'books',
    'widget_tweaks',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'invitations',
    'django_select2',
    'django_otp',
    'django_otp.plugins.otp_static',
    'django_otp.plugins.otp_totp',
    'two_factor',
    'otp_yubikey',
    'todo',
    'sendemail.apps.SendemailConfig',
    'uploaded_books',
    'ckeditor',
]

SITE_ID = 4
ACCOUNT_ADAPTER = 'invitations.models.InvitationsAdapter'

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django_otp.middleware.OTPMiddleware',
    'two_factor.middleware.threadlocals.ThreadLocals',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'cherry_app.urls'

AUTHENTICATION_BACKENDS = (
    # Needed to login by username in Django admin, regardless of `allauth`
    'django.contrib.auth.backends.ModelBackend',

    # `allauth` specific authentication methods, such as login by e-mail
    'allauth.account.auth_backends.AuthenticationBackend',
)

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, "templates")],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'todo.context_processors.add_variable_to_context',
            ],
        },
    },
]

WSGI_APPLICATION = 'cherry_app.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Europe/Berlin'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATIC_URL = '/static/'

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'cherry_app/media')

# login/logout redirect URLs
LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/'
LOGIN_URL = 'two_factor:login'
# LOGIN_REDIRECT_URL = 'two_factor:profile'

# invitations and allauth
INVITATIONS_EMAIL_SUBJECT_PREFIX = 'Come and join us! '
# the site is invite only, so it's impossible to register/signup without an invitation
INVITATIONS_INVITATION_ONLY = True

# the login method to use – whether the user logs in by entering their username, e-mail address, or either one of both
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_AUTHENTICATION_METHOD = "username_email"
# the e-mail verification method during signup.When set to “mandatory” the user is blocked from logging in until the email address is verified.
ACCOUNT_EMAIL_VERIFICATION = "optional"
# whether or not the user is automatically logged out after changing or setting their password.
ACCOUNT_LOGOUT_ON_PASSWORD_CHANGE = True
# controls the life time of the session. Default is to ask the user "Remember me?", False to not remember, and True to always remember
# ACCOUNT_SESSION_REMEMBER = False

# emailing
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
# testing contact us form - it prints the content in console
# EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = '587'
EMAIL_HOST_USER = 'cherryfinanceapp@gmail.com'
EMAIL_HOST_PASSWORD = 'cherrycherry'
EMAIL_USE_TLS = True


JET_DEFAULT_THEME = 'light-blue'

JET_THEMES = [
    {
        'theme': 'default',  # theme folder name
        'color': '#47bac1',  # color of the theme's button in user menu
        'title': 'Default'  # theme title
    },
    {
        'theme': 'green',
        'color': '#44b78b',
        'title': 'Green'
    },
    {
        'theme': 'light-green',
        'color': '#2faa60',
        'title': 'Light Green'
    },
    {
        'theme': 'light-violet',
        'color': '#a464c4',
        'title': 'Light Violet'
    },
    {
        'theme': 'light-blue',
        'color': '#5EADDE',
        'title': 'Light Blue'
    },
    {
        'theme': 'light-gray',
        'color': '#222',
        'title': 'Light Gray'
    }
]

JET_SIDE_MENU_ITEMS = [
    {'app_label': 'auth', 'items': [
        {'name': 'group'},
        {'name': 'user'},
    ]},
    {'app_label': 'books', 'items': [
        {'name': 'author'},
        {'name': 'book'},
    ]},
]

# sending real texts and making real calls using Twilio
TWILIO_ACCOUNT_SID = 'ACc6c51b7569730a3f43fb79c33f15fda0'
TWILIO_AUTH_TOKEN = '6808173965b907bf4e939473a8723eef'
TWILIO_CALLER_ID = '+12055510466'

# TWO_FACTOR_SMS_GATEWAY = 'two_factor.gateways.twilio.gateway.Twilio'
# TWO_FACTOR_CALL_GATEWAY = 'two_factor.gateways.twilio.gateway.Twilio'

# fake gateway - use only for development
TWO_FACTOR_SMS_GATEWAY = 'two_factor.gateways.fake.Fake'
TWO_FACTOR_CALL_GATEWAY = 'two_factor.gateways.fake.Fake'

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
        },
    },
    'loggers': {
        'two_factor': {
            'handlers': ['console'],
            'level': 'INFO',
        }
    }
}
DATE_INPUT_FORMATS = ['%m-%d-%Y']

# To-Do System - user doesn't need to have "is stuff" permission to access his tasks/task lists
TODO_STAFF_ONLY = False
