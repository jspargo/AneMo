#!/bin/sh
# Script to activate the correct python virtualenv and 
# run the anemoController

source django/bin/activate
python manage.py runserver 0.0.0.0:8000
