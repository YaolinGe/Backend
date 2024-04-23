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
- `urlconf`: URL configuration 
- `class-based views`: Django views that are classes to handle `get` and `post` requests
- `path('', views.index, name='index')`: will map to the / url, so no need to add / in the url, otherwise it will not work. 

## Week 2, Views, Requests and URLs, Creating URLs and Views
- `GET` request: used to request data from a specified resource
- `POST` request: used to submit data to be processed to a specified resource
- `PUT` request: used to update data
- `DELETE` request: used to delete data
- `GET / HTTP/1.1`: GET request to the root URL, `/` is the path where the resource is stored in the web server. 
- `Header`: contains metadata about the request
- `HTTP response`: contains the status code, headers, and the response body
    - `100~199`: Informational responses
    - `200~299`: Success responses
    - `300~399`: Redirection responses
    - `400~499`: Client error responses
    - `500~599`: Server error responses
- `URL`
    - subdomain: `www`
    - domain: `example.com`
    - top-level domain: `com`
    - path: `/path/to/resource`
    - query string: `?key1=value1&key2=value2`
- `QueryString`: `?key1=value1&key2=value2` can be used to pass data to the server instead of using the request body
    - `request.GET['key']`: get the value of the key from the query string
- `reverse` function: used to generate URLs from the URL configuration
    - `reverse('index')`: will return the URL for the index view
- `debug=False` needs to be turned on in production, but then the allowed hosts need to be set in the settings.py file, for example, `ALLOWED_HOSTS = ['*']` will allow all hosts to access the server.
- `class-based views` are used to handle requests in Django
    - `View`: the base class for all views
    - `TemplateView`: used to render a template
    - `ListView`: used to render a list of objects
    - `DetailView`: used to render a detail view of an object
    - `FormView`: used to render a form
    - `CreateView`: used to render a form to create an object
    - `UpdateView`: used to render a form to update an object
    - `DeleteView`: used to render a form to delete an object

## Week 3, Models & migrations, models and forms, admin, database configuration
- `new_user = User(username='john', password='doe')`: create a new user object
- `new_user.save()`: save the user object to the database
- `User.objects.get(username='john')`: get the user object with the username 'john'
- `user = User.objects.get(username='john')`: get the user object with the username 'john', and then `user.last_name = 'doe'` to update the user object and then `user.save()` to save the changes to the database
- `User.objects.filter(username='john')`: get all the user objects with the username 'john'
- `User.objects.filter(username='john').delete()`: delete all the user objects with the username 'john'
- `python manage.py shell` to start the Django shell
- `python manage.py makesmigrations` to create the migration files
- `python manage.py migrate` to apply the migrations to the database
- `python manage.py showmigration` to show the migration files
- `python manage.py migrate menuapp 0002_menuitem_price` to apply the migration with the name 0002_menuitem_price while fall back to the previous migration
- `python manage.py sqlmigrate menuapp 0002` to show the SQL code for the migration with the name 0002
- `from menuapp.models import MenuItem` to import the MenuItem model
- `MenuItem.objects.all()` to get all the menu items
- `MenuItem.objects.filter(price__gt=10)` to get all the menu items with the price greater than 10
- `MenuItem.objects.filter(price__lt=10)` to get all the menu items with the price less than 10
