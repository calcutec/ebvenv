from fe_eb_site.settings.common import *

# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'ebdb',
        'HOST': 'localhost',
        'USER': 'ebroot',
        'PASSWORD': 'Dimsum123!',
        'PORT': '5432'
    },
}

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.0/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, "www", "static")
