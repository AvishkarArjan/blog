# To use Neon with Django, you have to create a Project on Neon and specify the project connection settings in your settings.py in the same way as for standalone Postgres.
from dotenv import load_dotenv, dotenv_values
import os
load_dotenv()

DATABASES = {
  'default': {
    'ENGINE': 'django.db.backends.postgresql',
    'NAME': os.getenv("DB_NAME"),
    'USER': os.getenv("DB_USER"),
    'PASSWORD': os.getenv("DB_PASS"),
    'HOST': os.getenv("DB_HOST"),
    'PORT': os.getenv("DB_PORT"),
    'OPTIONS': {'sslmode': 'require'},
  }
}