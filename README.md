# Django Pics

Django Pics is a simple instagram clone. The main goal of this project - try **django-allauth** library (great lib for auth with 3rd party (social) account authentication support), try loading images into CDN service directly (**Upload Care**) and try to make config for deploying (**docker-compose**).

------------

For obvious reasons, deployment config's are not in repository. See examples of deploying configs bellow.

First of all, near default django settings file (`settings.py`) create `settings_prod.py` with similar content (i use django-anymail and mailgun for sending mails):

```python
from .settings import *

# Keep this file in secret!

SECRET_KEY = '9~zWN-O2kTX)nIo?^^.79"c/<3dB_Z}fgh2'

DEBUG = True
ALLOWED_HOSTS = [
    '127.0.0.1',
    '0.0.0.0',
	# Digital Ocean VPS IP, for example...
]

ANYMAIL = {
    'MAILGUN_API_KEY': '123blablabla',
    'MAILGUN_SENDER_DOMAIN': '999blablabla'
}

EMAIL_BACKEND = 'anymail.backends.mailgun.EmailBackend'
DEFAULT_FROM_EMAIL = 'postmaster@sandbox999blablalba.mailgun.org'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'db_pics_prodpass',
        'USER': 'db_username_prodpass',
        'PASSWORD': 'db_password_prodpass',
        'HOST': 'postgres',
        'PORT': '5432',
    }
}

```

Near `docker-compose.dev.yml` file create `docker-compose.prod.yml` with similar content:

```yaml
# Don't forget about logs! Look for Sentry, for example.

version: '2'

services:

  nginx:
    image: nginx:latest
    ports:
      - '80:80'
      - '443:443'
    volumes:
      - ./nginx/conf.d:/etc/nginx/conf.d
      - ./djangopicsproj/static:/djangopics/djangopicsproj/static
    links:
      - web:web
    depends_on:
      - web

  web:
    build: ./
    command: gunicorn --chdir /djangopics/djangopicsproj/ djangopicsproj.wsgi:application --bind 0.0.0.0:8000
    volumes:
      - ./:/djangopics
    environment:
       DJANGO_SETTINGS_MODULE: djangopicsproj.settings_prod
    links:
      - postgres:postgres
    depends_on:
      - postgres


  postgres:
    image: postgres:9.4
    volumes:
    - ./dockerdataprod/psql-data:/var/lib/postgresql/data
    environment:
      POSTGRES_USER: 'db_username_prodpass'
      POSTGRES_PASSWORD: 'db_password_prodpass'
      POSTGRES_DB: 'db_pics_prodpass'
    ports:
      - '5432:5432'
```

Then try:

`docker-compose -f docker-compose.prod.yml up --build`

Don't forget apply migrations (second terminal):

`docker-compose exec -i -t <web container id>  /bin/bash` 

You can get container id with next command:

`docker ps -a`

... change dir to dir with `manage.py `file and:

`python manage.py migrate`

Enjoy!
