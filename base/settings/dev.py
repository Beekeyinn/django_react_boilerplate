import os

from .base import BASE_DIR

# DATABASES = {
#     "default": {
#         "ENGINE": f"django.db.backends.postgresql",
#         "NAME": "candybit_openai",
#         "USER": "postgres",
#         "PASSWORD": "postgres",
#         "PORT": 5432,
#         "HOST": "localhost",
#     }
# }
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": os.path.join(BASE_DIR, "db.sqlite3"),
    }
}

MEDIA_URL = "media/"
MEDIA_ROOT = os.path.join(BASE_DIR, "media")
