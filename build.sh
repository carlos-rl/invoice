#!/usr/bin/env bash
# exit on error
set -o errexit

#poetry install
pip install -r deploy/txt/requirements.txt
pip install -r requirements.txt

python manage.py collectstatic --no-input
python manage.py makemigrations
python manage.py migrate
python manage.py shell --command='from core.init import *'