#!/bin/bash

set -e

# Prepare log files and start outputting logs to stdout
touch /var/log/gunicorn/gunicorn.log
touch /var/log/gunicorn/access.log
tail -n 0 -f /var/log/gunicorn/*.log &

args=("$@")

case $1 in
    superuser)
        exec python manage.py createsuperuser
        ;;
    makemigrations)
        exec python manage.py makemigrations ${args[@]:1}
        ;;
    manage)
        exec python manage.py ${args[@]:1}
        ;;
    run)
        python manage.py migrate                  # Apply database migrations
        python manage.py collectstatic --noinput  # Collect static files

        # Start Gunicorn processes
        echo Starting Gunicorn.
        exec gunicorn boilerplate.wsgi \
            --config boilerplate/settings/gunicorn.py
        ;;

    runserver)
        exec python manage.py runserver 0.0.0.0:8000
        ;;
    *)
        if [ -f ./entrypoint-extras.sh ]; then
            ./entrypoint-extras.sh ${args[@]}
        else
            exec "$@"
        fi
        ;;
esac
