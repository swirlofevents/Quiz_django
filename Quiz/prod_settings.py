import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

DEBUG = False


# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.mysql',
#         'NAME': 'quizz',
#         'USER': 'root',
#         'PASSWORD': '123qwe',
#         'HOST': 'localhost',
#         'PORT': '5432'
#     }
# }

STATIC_DIR = os.path.join(BASE_DIR, 'static')
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

STATIC_URL = '/static/'
