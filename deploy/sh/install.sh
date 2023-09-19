#!/bin/bash
# constants
DJANGO_DIR=$(dirname $(dirname $(cd `dirname $0` && pwd)))
VENV_DIR=$DJANGO_DIR/venv
DB_DIR=$DJANGO_DIR/db.sqlite3
MEDIA_DIR=$DJANGO_DIR/media
DJANGO_SETTINGS_MODULE=config.settings
cd $DJANGO_DIR
echo 'Deleting database db.sqlite3'
if [ -f $DB_DIR ];
then
  sudo rm -r $DB_DIR
fi
echo 'Deleting folder media'
if [ -f $MEDIA_DIR ];
then
  sudo rm -r $MEDIA_DIR
fi
#echo 'Deleting virtual environment'
#if [ -d $VENV_DIR ];
#then
#  deacivate
#  sudo rm -r $VENV_DIR
#fi
#echo 'Creating virtual environment'
#virtualenv $VENV_DIR -ppython3
echo 'Activating virtual environment'
source $VENV_DIR/bin/activate
export DJANGO_SETTINGS_MODULE=$DJANGO_SETTINGS_MODULE
echo 'Installing the requirements in the virtual environment'
pip install -r $DJANGO_DIR/deploy/txt/requirements.txt
# remove migrations
echo 'Deleting current migrations'
find . -path "*/migrations/*.py" -not -name "__init__.py" ! -path */venv/* -delete
# create migrations and insert data initial
echo 'Generating migrations and installing initial data'
python manage.py makemigrations && python manage.py migrate && python manage.py shell --command='from core.init import *' && python manage.py shell --command='from core.utils import *'
echo 'Finished process'
