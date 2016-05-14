# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

GDAL_LIBRARY_PATH = "/Applications/Postgres.app/Contents/Versions/9.4/lib/libgdal.dylib"
GEOS_LIBRARY_PATH = "/Applications/Postgres.app/Contents/Versions/9.4/lib/libgeos_c.dylib"


DATABASES = {
    'default': {
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'NAME': 'tor_nodes_map',
        'USER': '',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
    }
}

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
