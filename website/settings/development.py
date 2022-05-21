from .base import *

# Debug Control
DEBUG = env("DEBUG")

ALLOWED_HOSTS = env("ALLOWED_HOSTS").split(" ")

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env("SECRET_KEY")

# Install 3rd Party Apps
THIRD_PARTY_APPS = [
    'PIL',
    'widget_tweaks',
    'mathfilters'
]

# Django Apps
INSTALLED_APPS += THIRD_PARTY_APPS
