#!/bin/bash
echo "Creating Migrations..."
python manage.py makemigrations blog
echo ====================================

echo "Starting Migrations..."
python manage.py migrate
echo ====================================

echo "Creating superuser..."
python manage.py createsuperuser --noinput

echo "Starting Server..."
python manage.py runserver 0.0.0.0:8000
