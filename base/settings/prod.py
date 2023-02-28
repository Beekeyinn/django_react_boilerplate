import os
from pathlib import Path
from decouple import config


BASE_DIR = Path(__file__).resolve().parent.parent.parent
# DATABASES = {
#     "default": {
#         "ENGINE": f"django.db.backends.postgresql",
#         "NAME": config("DATABASE_NAME"),
#         "USER": config("DATABASE_USERNAME"),
#         "PASSWORD": config("DATABASE_PASSWORD"),
#         "PORT": config("DATABASE_PORT"),
#         "HOST": config("DATABASE_HOST"),
#     }
# }
STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")
STATICFILES_STORAGE = "whitenoise.storage.CompressedStaticFilesStorage"
