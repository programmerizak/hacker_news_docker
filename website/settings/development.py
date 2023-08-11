from .base import *

EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"


#Specifying to django where to look for the static files
STATICFILES_DIRS = [
    (BASE_DIR / 'static')
]

#url to access your static files 
STATIC_URL = '/static/'

#where to save the static files to, when we run collectstatics 
STATIC_ROOT = (BASE_DIR / '../static')

#Directory where our media files will be saved to
MEDIA_ROOT = (BASE_DIR /'../media')

#Url in which we can access our media files
MEDIA_URL = '/media/'