from settings import *
import dj_database_url

DEBUG = False

ALLOWED_HOSTS = ['']

CSRF_TRUSTED_ORIGINS = ["https://" + host for host in ALLOWED_HOSTS]

DATABASES = {
    "default": dj_database_url.parse(
        config("DB_URL", ""),
        conn_max_age=600,
    )
}

DEFAULT_FILE_STORAGE = "cloudinary_storage.storage.MediaCloudinaryStorage"

CLOUDINARY_STORAGE = {
    "CLOUD_NAME": config("CLOUDINARY_CLOUD_NAME"),
    "API_KEY": config("CLOUDINARY_API_KEY"),
    "API_SECRET": config("CLOUDINARY_API_SECRET"),
}

EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"

EMAIL_HOST = config("EMAIL_HOST")

EMAIL_USE_TLS = True

EMAIL_HOST_USER = config("EMAIL_HOST_USER")

DEFAULT_FROM_EMAIL = config("EMAIL_HOST_USER")

EMAIL_HOST_PASSWORD = config("EMAIL_HOST_PASSWORD")

EMAIL_PORT = 587