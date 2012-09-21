# Django settings for djangogtd project.
import os
import sys
import urlparse


# running on stckato?
STACKATO = 'VCAP_APPLICATION' in os.environ

DATABASES = {}
if 'DATABASE_URL' in os.environ:
    url = urlparse.urlparse(os.environ['DATABASE_URL'])
    DATABASES['default'] = {
        'NAME': url.path[1:],
        'USER': url.username,
        'PASSWORD': url.password,
        'HOST': url.hostname,
        'PORT': url.port,
        }
    if url.scheme == 'postgres':
        DATABASES['default']['ENGINE'] = 'django.db.backends.postgresql_psycopg2'
    elif url.scheme == 'mysql':
        DATABASES['default']['ENGINE'] = 'django.db.backends.mysql'
else:
    DATABASES['default'] = {
        'ENGINE': 'django.db.backends.sqlite3', # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'dev.db', # Or path to database file if using sqlite3.
        'USER': '', # Not used with sqlite3.
        'PASSWORD': '', # Not used with sqlite3.
        'HOST': '', # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '', # Set to empty string for default. Not used with sqlite3.
        }

SECRET_KEY = ''

# Set PRODUCTION to True so we don't show stackdumps on errors
PRODUCTION = False

# The instance is the group of servers correspond to a C2G stack.  Some good 
# values for this are:
#    "your_name" if you want to stay isolated (thi is the default if missing)
#    "dev" to use the stable dev network util server
#    "stage" or "prod" for something in produciton -- are you sure you want to do that?
INSTANCE="dev"

# Put your name and email address here, so Django serious errors can come to you
# the trailing comma after the list is important so Python correctly interprets 
# this as a list of lists
ADMINS = (
        ('admin', "YOURNAME@stanford.edu"),
        )

# For using S3 Storage, specify these with real settings
# AWS_ACCESS_KEY_ID = 'AAAAAAAAAAAAAAAAAAAA'
# AWS_SECRET_ACCESS_KEY = 'BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB'
# AWS_STORAGE_BUCKET_NAME = 'dev-c2g'

# To use Local Storage.  You still need to define these three all to 'local'
# and specify where you want those local files written
AWS_ACCESS_KEY_ID = 'local'
AWS_SECRET_ACCESS_KEY = 'local'
AWS_STORAGE_BUCKET_NAME = 'local'

if 'STACKATO_FILESYSTEM' in os.environ:
    MEDIA_ROOT = os.environ["STACKATO_FILESYSTEM"] 
else:
    MEDIA_ROOT = '/opt/class2go/uploads'

# This is if you want to change to a different logging directory than the default,
# which is '/var/log/django/'
# Please keep the trailing '/'
LOGGING_DIR = '/app/logs/'

PIAZZA_ENDPOINT = "https://piazza.com/basic_lti"
PIAZZA_KEY = "class2go"
PIAZZA_SECRET = "piazza_xxxxxxx"

# SMTP INFO for SES -- Amazon Simple Email Service $1 per 10K recipients
SES_SMTP_USER = "USER"
SES_SMTP_PASSWD = "PWD"
