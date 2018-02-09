from fe_eb_site.settings.common import *

DATABASES = {
    'default': {
        # 'ENGINE': 'sql_server.pyodbc',
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': os.environ['RDS_DB_NAME'],
        'USER': os.environ['RDS_USERNAME'],
        'PASSWORD': os.environ['RDS_PASSWORD'],
        'HOST': os.environ['RDS_HOSTNAME'],
        'PORT': os.environ['RDS_PORT'],
    }
}


DATABASES = {    
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'ebdb',
        'USER' : 'ebroot',
        'PASSWORD' : 'Dimsum123!',
        'HOST' : 'defaultdb.cicw2foyeumk.us-east-1.rds.amazonaws.com',
        'PORT' : '5432',
    }
}

INSTALLED_APPS += ('storages',)
AWS_STORAGE_BUCKET_NAME = "fe-dpm-django"
STATICFILES_STORAGE = 'storages.backends.s3boto.S3BotoStorage'
S3_URL = 'http://%s.s3.amazonaws.com/' % AWS_STORAGE_BUCKET_NAME
STATIC_URL = S3_URL