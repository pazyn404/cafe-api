#!/bin/sh

python manage.py makemigrations
python manage.py migrate
python manage.py create_print_rendered_checks_crontab
python manage.py create_default_printers
python manage.py runserver 0.0.0.0:8000
