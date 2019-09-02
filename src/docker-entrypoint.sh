#!/usr/bin/env bash

python /code/manage.py makemigrations --settings=monolith.settings.production
python /code/manage.py migrate --settings=monolith.settings.production            # Apply database migrations
python /code/manage.py collectstatic --noinput --settings=monolith.settings.production  # Collect static files
#python /code/manage.py loaddata /code/fixtures/auth.json --settings=monolith.settings.production
#python /code/manage.py loaddata /code/fixtures/users.json --settings=monolith.settings.production

#rm /code/celeryev.pid

#Prepare log files and start outputting logs to stdout
touch /logs/gunicorn.log
touch /logs/access.log
tail -n 0 -f /logs/*.log &

cd code

# Start Gunicorn processes
echo Starting Gunicorn.


exec gunicorn monolith.wsgi:application \
    --env DJANGO_SETTINGS_MODULE=monolith.settings.production \
    --bind 0.0.0.0:8000 \
    --workers 3 \
    --timeout 3600 \
    --log-level=info \
    --log-file=/logs/gunicorn.log \
    --access-logfile=/logs/access.log \
"$@"

