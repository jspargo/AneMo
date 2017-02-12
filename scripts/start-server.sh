#!/bin/sh
# Script to activate the correct python virtualenv and
# run the anemoController

source django/bin/activate
pip install -r requirements.txt
cd anemoController
python manage.py makemigrations
python manage.py migrate
python manage.py runserver 0.0.0.0:8000
