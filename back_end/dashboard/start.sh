#!/bin/bash

echo "starting djnago"
python manage.py migrate
python manage.py collectstatic --noinput
# python manage.py runserver 0.0.0.0:8000
uwsgi --http :8000 --module dashboard.wsgi
