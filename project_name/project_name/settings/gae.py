#!/usr/bin/env python
import os

# Load production settings when running on GAE or SETTINGS_MODE is prod
# else, load local settings
if (os.getenv('SERVER_SOFTWARE', '').startswith('Google App Engine') or os.getenv('SETTINGS_MODE') == 'prod'):
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project_name.settings.production")
    from production import *
else:
    from local import *


########## STORAGE CONFIGURATION
# See: https://github.com/ckopanos/django-google-cloud-storage
DEFAULT_FILE_STORAGE = 'backend.gae.storage.googleCloud.GoogleCloudStorage'

GOOGLE_CLOUD_STORAGE_BUCKET = '/name-of-your-bucket-here' # the name of the bucket you have created from the google cloud storage console
GOOGLE_CLOUD_STORAGE_URL = 'http://storage.googleapis.com/bucket' #whatever the url for accessing your cloud storgage bucket
GOOGLE_CLOUD_STORAGE_DEFAULT_CACHE_CONTROL = 'public, max-age: 7200' # default cache control headers for your files
########## END STORAGE CONFIGURATION