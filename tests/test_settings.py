SECRET_KEY = "fake-key"
INSTALLED_APPS = [
    "products_core",
    "tests",
]
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
    }
}
