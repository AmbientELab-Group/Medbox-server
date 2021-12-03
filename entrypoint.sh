#!/bin/sh

python manage.py makemigrations API
python manage.py migrate --no-input
python manage.py collectstatic --noinput

gunicorn API.wsgi:application --workers=3 --bind 0.0.0.0:8000 
