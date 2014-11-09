from __future__ import unicode_literals

SECRET_KEY = "96742258-8d4c-4ccd-ac53-943ed222b49f67237cd3-87c4-41e9-9668-3523aeb466a60881dbbe-de48-43e8-916e-e12d7d25f8a8"
NEVERCACHE_KEY = "877e6ea1-f0f8-480d-a54e-5296e3ad003f4ef394a7-f3ff-4291-9191-cd20818d33f17ec69824-f8d0-47aa-9f68-152fdd9d2cc9"
#ALLOWED_HOSTS = ['107.170.5.233', '107.170.5.233.']
ADMIN_THUMB_SIZE = '200x200'
DEBUG = False 

ALLOWED_HOSTS = [
        '107.170.142.6',
        'http://catalyst4success.org',
        'http://catalyst4success.org.',
	'*',
        ]

DATABASES = {
    "default": {
        # Ends with "postgresql_psycopg2", "mysql", "sqlite3" or "oracle".
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        # DB name or path to database file if using sqlite3.
        "NAME": "catalystcms",
        # Not used with sqlite3.
        "USER": "catalystcms",
        # Not used with sqlite3.
        "PASSWORD": "Westv!ewC4S",
        # Set to empty string for localhost. Not used with sqlite3.
        "HOST": "127.0.0.1",
        # Set to empty string for default. Not used with sqlite3.
        "PORT": "",
    }
}

SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTOCOL", "https")

CACHE_MIDDLEWARE_SECONDS = 60

CACHE_MIDDLEWARE_KEY_PREFIX = "catalystcms"

CACHES = {
    "default": {
        "BACKEND": "django.core.cache.backends.memcached.MemcachedCache",
        "LOCATION": "127.0.0.1:11211",
    }
}

SESSION_ENGINE = "django.contrib.sessions.backends.cache"
