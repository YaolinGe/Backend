# Notes for Djando Framework

## Introduction
- `django-admin startproject mysite` # Create a new Django project
- `python manage.py startapp polls` # Create a new Django app
- `python manage.py makemigrations` # Create migrations for changes in models
- `python manage.py migrate` # Apply changes to the database
- `python manage.py runserver` # Start the development server
- `python manage.py shell` # Start the Django shell
- low port number is reserved for system services, so use port number greater than 1024

- `python manage.py startapp <app_name>` # Create a new app
- `python -m django startapp <app_name>` # Create a new app
- `django-admin startapp <app_name>` # Create a new app

## Web frameworks and MVT
- `three-tier architecture`: presentation tier, application tier, data tier
- `MVT`: Model, View, Template
- `data-logic-display`: Model, View, Template
