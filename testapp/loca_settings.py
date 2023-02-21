ALLOWED_HOSTS = []
DEBUG = True


# DATABASE CONFIGURATION
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "testapp",
        "USER": "testapp",
        "PASSWORD": "testapp",
        "HOST": "127.0.0.1",
        "PORT": "5432",
        "ATOMIC_REQUESTS": True,
    }
}
