
DEBUG = True

# Make these unique, and don't share it with anybody.
SECRET_KEY = "96742258-8d4c-4ccd-ac53-943ed222b49f67237cd3-87c4-41e9-9668-3523aeb466a60881dbbe-de48-43e8-916e-e12d7d25f8a8"
NEVERCACHE_KEY = "877e6ea1-f0f8-480d-a54e-5296e3ad003f4ef394a7-f3ff-4291-9191-cd20818d33f17ec69824-f8d0-47aa-9f68-152fdd9d2cc9"

DATABASES = {
    "default": {
        # Ends with "postgresql_psycopg2", "mysql", "sqlite3" or "oracle".
        "ENGINE": "django.db.backends.sqlite3",
        # DB name or path to database file if using sqlite3.
        "NAME": "dev.db",
        # Not used with sqlite3.
        "USER": "",
        # Not used with sqlite3.
        "PASSWORD": "",
        # Set to empty string for localhost. Not used with sqlite3.
        "HOST": "",
        # Set to empty string for default. Not used with sqlite3.
        "PORT": "",
    }
}
