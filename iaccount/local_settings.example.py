import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SECRET_KEY = '_please_use_some_secret_key'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
ALLOWED_HOSTS = ['*']

# Database
# https://docs.djangoproject.com/en/1.9/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.9/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# oauth settings
# For github oauth:
#MAMA_CAS_OAUTH_GITHUB_CLIENT_ID = ''
#MAMA_CAS_OAUTH_GITHUB_CLIENT_SECRET = ''

# For QQ oauth:
#MAMA_CAS_OAUTH_QQ_APP_ID = ''                                             
#MAMA_CAS_OAUTH_QQ_APP_KEY = ''                     

# For WeiBo oauth:
#MAMA_CAS_OAUTH_WEIBO_APP_KEY = ''                                        
#MAMA_CAS_OAUTH_WEIBO_APP_SECRET = ''

# registration settings
ACCOUNT_ACTIVATION_DAYS = 7
REGISTRATION_EMAIL_SUBJECT_PREFIX = '[iSoft Account Registration]'
SEND_ACTIVATION_EMAIL = True
REGISTRATION_AUTO_LOGIN = False

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
DEFAULT_FROM_EMAIL = ''
EMAIL_HOST_PASSWORD = ''
EMAIL_HOST_USER = DEFAULT_FROM_EMAIL

EMAIL_HOST = 'smtp.qq.com'
EMAIL_PORT = 25
