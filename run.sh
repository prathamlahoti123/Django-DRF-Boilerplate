#!/bin/sh

set -e

echo "Collecting static files ..."
python manage.py collectstatic --noinput

echo "Running database migrations ..."
python manage.py migrate

echo "Running the application ..."
python -m gunicorn --bind :8000 main.wsgi
