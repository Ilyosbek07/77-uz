from pathlib import Path
import environ

BASE_DIR = Path(__file__).resolve().parent.parent.parent

# READING ENV
env = environ.Env()
env.read_env(BASE_DIR / '.env')
# END READING ENV

SECRET_KEY = env.str('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# APPS
DJANGO_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

CUSTOM_APPS = [
    'src.users',
    'src.base',
    'src.common',
]

THIRD_PART_APPS = [
    'django_extensions',  # https://pypi.org/project/django-extensions/
    'debug_toolbar',  # https://django-debug-toolbar.readthedocs.io/
    'corsheaders',  # https://pypi.org/project/django-cors-headers/
    'drf_yasg',  # https://drf-yasg.readthedocs.io/en/stable/readme.html
    'rest_framework',
]

INSTALLED_APPS = DJANGO_APPS + CUSTOM_APPS + THIRD_PART_APPS
# END APPS


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware',
    'django.middleware.locale.LocaleMiddleware',
]

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'src.base.context_processors.project_languages'
            ],
        },
    },
]

WSGI_APPLICATION = 'config.wsgi.application'

# AUTH USER
AUTH_USER_MODEL = 'users.User'

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]
# END AUTH USER

LANGUAGE_CODE = 'en'

# LANGUAGES = (
#     ('ru', 'Russian'),
#     ('en', 'English'),
# )

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


STATIC_URL = 'static/'
STATIC_ROOT = BASE_DIR / 'static'
STATICFILES_DIRS = (
    BASE_DIR / 'staticfiles',
)

MEDIA_URL = 'media/'
MEDIA_ROOT = BASE_DIR / 'media'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# DEBUG TOOLBAR
INTERNAL_IPS = [
    "127.0.0.1",
]
# END DEBUG TOOLBAR

# CORS
CORS_ALLOW_METHODS = ['*']
CORS_ALLOW_HEADERS = ['*']
CORS_ALLOW_CREDENTIALS = True
CORS_ORIGIN_ALLOW_ALL = True
# END CORS
