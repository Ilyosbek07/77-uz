from .base import env

ALLOWED_HOSTS = ['*']

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': 'db.sqlite3',
#     }
# }

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': env.str('POSTGRES_DB'),
        'USER': env.str('POSTGRES_USER'),
        'PASSWORD': env.str('POSTGRES_PASSWORD'),
        'HOST': env.str('POSTGRES_HOST'),
        'PORT': env.int('POSTGRES_PORT')
    }
}


RECAPTCHA_PUBLIC_KEY = '6Lfw_dYnAAAAAG9beUGYn9tCJbIHPrT8LJkYT7pu'
RECAPTCHA_PRIVATE_KEY = '6Lfw_dYnAAAAAFYYq6gnb7iMGZwshPW_nC3XsfQo'
